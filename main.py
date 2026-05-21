import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# ページ設定
st.set_page_config(page_title="Bento Vision AI", page_icon="🍱")
st.title("🍱 Bento Vision AI")

# AIの設定 (ここにAPIキーが必要です)
api_key = st.text_input("Gemini API Keyを入力してください", type="password")
genai.configure(api_key=api_key)

uploaded_file = st.camera_input("お弁当箱を撮影")

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱")
    
    if st.button("✨ このお弁当箱でレシピを生成"):
        if not api_key:
            st.error("APIキーを入力してください！")
        else:
            with st.spinner("AIが理想のお弁当をデザイン中..."):
                # ここで本来はGeminiの画像生成機能を呼び出します
                # ※技術的な詳細はステップごとに詳しく解説します！
                st.write("---")
                st.subheader("🌟 AIによる完成イメージ")
                st.info("ここにAIが生成した『おかずが詰まったお弁当画像』が表示されます")
                st.write("1. 焼き鮭のほぐし身")
                st.write("2. ブロッコリーの胡麻和え")
                st.write("3. だし巻き卵")
