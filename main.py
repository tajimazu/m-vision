import streamlit as st

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# デザイン（CSS）
st.markdown("""
    <style>
    .main { background-color: #fff9f0; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff9e1b; color: white; border: none; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍱 Bento Vision")
st.subheader("Phase 2: カメラで隙間をパシャリ")

st.write("---")
st.write("### 📸 途中まで作ったお弁当を撮ってください")

# スマホのカメラを起動する魔法の1行
uploaded_file = st.camera_input("ここをタップしてカメラを起動")

if uploaded_file is not None:
    st.success("📸 写真の撮影に成功しました！")
    
    # 撮影された画像を画面に表示
    st.image(uploaded_file, caption="あなたのお弁当", use_container_width=True)
    
    st.write("---")
    st.write("### 🔍 AIが隙間を分析中...")
    
    # ここに将来、自動で隙間を埋めるAIの頭脳を合体させます
    st.info("💡 次のステップで、この画像から『ミニトマト』や『ブロッコリー』の配置案を合成するAI（Gemini）の目を繋ぎ込みます！")

st.write("---")
st.caption("Bento Vision - Phase 2.0 (Camera Test Version)")
