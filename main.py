import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Bento Vision", page_icon="🍱")
st.title("🍱 Bento Vision")

# APIキーをここに直接埋め込むとコードが流出した際に危険なので、
# 画面で入力したキーをプログラム内で使います。
api_key = st.text_input("Gemini API Keyを入力してください", type="password")

uploaded_file = st.camera_input("お弁当箱を撮影")

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱")
    
    if st.button("✨ AIでレシピを提案"):
        if not api_key:
            st.error("APIキーを入力してください！")
        else:
            try:
                # Geminiの設定
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # 画像の読み込み
                img = Image.open(uploaded_file)
                
                with st.spinner("AIが箱の形を分析中..."):
                    # 画像を送ってレシピを生成
                    response = model.generate_content([
                        "このお弁当箱の写真を見て、隙間を埋めるための栄養バランスの良いおかずの組み合わせと、その詰め方のコツを教えてください。", 
                        img
                    ])
                    
                    st.write("---")
                    st.subheader("🌟 AIからのレシピ提案")
                    st.write(response.text)
                    st.balloons()
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
