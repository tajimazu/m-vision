import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

st.set_page_config(page_title="M-Vision AI")
st.title("🀄 M-Vision AI点数計算")

# キー設定
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # モデル名を最新の指定方法に変更
    model = genai.GenerativeModel('gemini-pro-vision')
else:
    st.error("APIキーが見つかりません")
    st.stop()

img_file = st.camera_input("手牌を撮影")

if img_file:
    img = Image.open(img_file)
    img.thumbnail((400, 400))
    st.image(img, caption="解析中...")
    
    if st.button("AIで役を判定する", type="primary"):
        with st.spinner("AIが解析しています..."):
            try:
                # 画像データをAIが読み取れる形式に変換
                buf = io.BytesIO()
                img.save(buf, format='JPEG')
                
                # AIへの問い合わせ（画像データを直接渡す）
                response = model.generate_content([
                    "この麻雀牌の画像から、成立している役（大三元など）、ドラ、符、点数を短く教えてください。",
                    {"mime_type": "image/jpeg", "data": buf.getvalue()}
                ])
                
                if response.text:
                    st.success("判定完了！")
                    st.write(response.text)
                else:
                    st.warning("AIからの回答が空でした。もう一度お試しください。")
            except Exception as e:
                # エラーの詳細を表示
                st.error(f"エラーが発生しました: {e}")
