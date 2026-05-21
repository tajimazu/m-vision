import streamlit as st
import time

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

st.title("🍱 Bento Vision")
st.subheader("カメラを向けてお弁当箱を分析")

# --- 1. カメラ撮影（外向きカメラを強制指定） ---
st.write("---")
st.write("### 📸 お弁当箱を撮影してください")

# 'environment' を指定することで、背面カメラを優先的に起動します
uploaded_file = st.camera_input("ここをタップして外向きカメラを起動", camera_facing="environment")

# --- 2. レシピ考案スタートボタン ---
if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    if st.button("✨ レシピ考案スタート！"):
        
        # --- 3. 解析・分析の演出 ---
        with st.status("解析・分析中...", expanded=True) as status:
            st.write("お弁当箱の形をスキャン中...")
            time.sleep(1.5)
            st.write("隙間の面積を計算中...")
            time.sleep(1.5)
            st.write("彩り豊かな食材とマッチング中...")
            time.sleep(1.5)
            status.update(label="アイデアの提示完了！", state="complete", expanded=False)

        # --- 4. アイデアの提示 ---
        st.success("提案が完成しました！")
        
        st.markdown("""
        <div style="background-color: #fff9f0; padding: 20px; border-radius: 15px; border: 2px solid #ff9e1b;">
            <h3 style="color: #ff9e1b;">💡 今日の「隙間埋め」おすすめメニュー</h3>
            <p><strong>1. 鮮やか彩りミニトマト：</strong>隙間の角に3つ入れると安定します。</p>
            <p><strong>2. 枝豆ピック：</strong>小さい隙間を埋めるのに最適！見た目も華やかに。</p>
            <p><strong>3. ふっくら卵焼き：</strong>箱の形に合わせてカットして詰めるとプロ級の仕上がり。</p>
            <hr>
            <p><i>お弁当箱の形をしっかり認識しました！この配置で最高のお弁当になりますよ。</i></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()

st.write("---")
st.caption("Bento Vision - Phase 2.2 (Back Camera Version)")
