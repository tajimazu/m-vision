import streamlit as st
import time

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

st.title("🍱 Bento Vision")
st.subheader("お弁当箱を分析して隙間を埋める")

# --- 1. カメラ撮影 ---
st.write("---")
# シンプルに設定し、エラーを減らします
uploaded_file = st.camera_input("カメラを起動して撮影してください")

# --- 2. レシピ考案スタートボタン ---
if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    if st.button("✨ レシピ考案スタート！"):
        
        # --- 3. 解析・分析の演出 ---
        with st.status("解析・分析中...", expanded=True) as status:
            st.write("形状をスキャンしています...")
            time.sleep(1.5)
            st.write("隙間を計算中...")
            time.sleep(1.5)
            status.update(label="完了！", state="complete", expanded=False)

        # --- 4. アイデアの提示 ---
        st.success("提案が完成しました！")
        
        st.markdown("""
        <div style="background-color: #fff9f0; padding: 20px; border-radius: 15px; border: 2px solid #ff9e1b;">
            <h3 style="color: #ff9e1b;">💡 おすすめ隙間埋めメニュー</h3>
            <p>1. <b>ミニトマト</b>（角の隙間に）</p>
            <p>2. <b>ブロッコリー</b>（メインの横に）</p>
            <p>3. <b>卵焼き</b>（空いたスペースにフィット！）</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()

st.write("---")
st.caption("Bento Vision - Simple Camera Version")
