import streamlit as st

st.title("🍱 Bento Vision")

# APIキーの入力欄
api_key = st.text_input("Gemini API Keyを入力してください", type="password")

# キーが空でないか確認するボタン
if st.button("設定を保存"):
    if api_key:
        st.success("APIキーが入力されました！")
    else:
        st.error("キーを入力してください。")
