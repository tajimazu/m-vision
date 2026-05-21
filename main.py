import streamlit as st
import time

st.set_page_config(page_title="Bento Vision", page_icon="🍱")

st.title("🍱 Bento Vision")
st.subheader("お弁当箱を分析して隙間を埋める")

# カメラではなく「画像アップロード」に変更（どんなスマホでも確実です！）
uploaded_file = st.file_uploader("お弁当の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    if st.button("✨ 隙間埋めレシピを提案！"):
        # 分析の演出
        with st.status("分析中...", expanded=True) as status:
            time.sleep(1.0)
            st.write("お弁当箱の形状を解析...")
            time.sleep(1.0)
            st.write("隙間に合う食材を選定中...")
            time.sleep(1.0)
            status.update(label="完了！", state="complete")
        
        # 結果表示
        st.success("提案が完成しました！")
        st.markdown("""
        <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
            <h3 style="color: #333;">💡 おすすめの隙間埋め</h3>
            <p>🔴 <b>ミニトマト：</b>角に3つ置くと安定します。</p>
            <p>🟢 <b>ブロッコリー：</b>隙間のボリュームアップに。</p>
            <p>🟡 <b>卵焼き：</b>形に合わせてカットして詰めると完璧！</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
