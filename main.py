import streamlit as st
import google.generativeai as genai
from PIL import Image

st.title("🀄 M-Vision AI 最終テスト")

# キー設定
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

img_file = st.camera_input("テスト撮影")

if img_file:
    img = Image.open(img_file)
    # 判定ボタンをなくして、撮影したら即実行される最もシンプルな形
    with st.spinner("AIに直接問い合わせ中..."):
        try:
            # 画像をそのままAIに投げる（一番標準的な方法）
            response = model.generate_content(["この麻雀牌の役を教えて", img])
            st.write(response.text)
        except Exception as e:
            st.error(f"エラー内容: {e}")
