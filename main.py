import streamlit as st
import time

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# デザイン
st.markdown("""
    <style>
    .main { background-color: #fff9f0; }
    .result-box { background-color: white; padding: 20px; border-radius: 15px; border-left: 10px solid #ff9e1b; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍱 Bento Vision")
st.subheader("カメラ撮影＆お弁当分析")

# カメラ撮影
uploaded_file = st.camera_input("カメラを起動して撮影", camera_facing="environment")

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    if st.button("✨ 隙間埋めレシピを提案！"):
        
        # 演出
        with st.status("分析中...", expanded=True) as status:
            time.sleep(1.0)
            st.write("お弁当箱の形状を解析...")
            time.sleep(1.0)
            st.write("最適な食材を選定中...")
            time.sleep(1.0)
            status.update(label="完了！", state="complete")
        
        # 結果の提示（メニューを明記）
        st.success("提案が完成しました！")
        st.markdown("""
        <div class="result-box">
            <h3 style="color: #2c3e50;">💡 本日のおすすめの隙間埋め</h3>
            <p>🔴 <b>赤：ミニトマト</b>（彩りに最適！）</p>
            <p>🟢 <b>緑：ブロッコリー</b>（隙間のボリュームアップに。）</p>
            <p>🟡 <b>黄：卵焼き</b>（どんな隙間にもフィットする万能選手！）</p>
            <p><i>※今後はここにお弁当箱の形に合わせた、より具体的なレシピを表示します！</i></p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.caption("Bento Vision - Stable Version 2.0")
