import streamlit as st
import time

st.set_page_config(page_title="Bento Vision", page_icon="🍱")

st.title("🍱 Bento Vision")
st.write("お弁当箱を分析してレシピを提案します")

uploaded_file = st.camera_input("カメラを起動")

if uploaded_file is not None:
    st.image(uploaded_file)
    if st.button("✨ おすすめレシピを表示"):
        with st.status("分析中..."):
            time.sleep(2)
        st.subheader("🌟 おすすめ弁当レシピ")
        st.write("1. 焼き鮭のほぐし身")
        st.write("2. ブロッコリーの胡麻和え")
        st.write("3. だし巻き卵")
