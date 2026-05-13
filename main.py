import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- 設定 ---
st.set_page_config(page_title="M-Vision AI")
st.title("🀄 M-Vision AI点数計算")

# API設定
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')

    # カメラ入力
    img_file = st.camera_input("手牌を撮影してください")

    if img_file:
        img = Image.open(img_file)
        img.thumbnail((400, 400)) # 軽くする
        
        with st.spinner("AIが解析中..."):
            try:
                # シンプルにAIに聞く
                response = model.generate_content(["この麻雀牌の役、ドラ、符を教えて", img])
                st.success("判定完了！")
                st.write(response.text)
            except Exception as e:
                st.error(f"エラー: {e}")
else:
    st.error("APIキーが見つかりません")
