import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Bento Vision", page_icon="🍱")
st.title("🍱 Bento Vision")

# APIキーの入力欄
api_key = st.text_input("Gemini API Key", type="password")

# カメラ機能
uploaded_file = st.camera_input("お弁当箱を撮影")

# 画像が撮影された後の処理
if uploaded_file is not None and api_key:
    st.image(uploaded_file, caption="撮影したお弁当箱")
    
    if st.button("✨ AIでレシピを提案"):
        with st.spinner("AIが箱の形を分析中..."):
            try:
                # APIの設定
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # 画像の準備
                img = Image.open(uploaded_file)
                
                # AIへの命令
                response = model.generate_content([
                    "このお弁当箱の写真を見て、隙間を埋めるための栄養バランスの良いおかずの組み合わせと、その詰め方のコツを教えてください。", 
                    img
                ])
                
                # 結果表示
                st.write("---")
                st.subheader("🌟 AIからのレシピ提案")
                st.write(response.text)
                st.balloons()
                
            except Exception as e:
                st.error(f"エラー発生: {e}")
elif uploaded_file is not None and not api_key:
    st.warning("先にGemini API Keyを入力してください！")
