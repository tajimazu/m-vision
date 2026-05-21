import streamlit as st
import time
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 提案メニューのデータベース
menu_options = [
    {"red": "ミニトマト", "green": "ブロッコリー", "yellow": "卵焼き", "tip": "定番の赤・緑・黄で、まずは基本を抑えましょう！"},
    {"red": "カニカマ", "green": "枝豆", "yellow": "コーンバター", "tip": "お子様も喜ぶ彩り！枝豆はピックに刺すと可愛いです。"},
    {"red": "赤パプリカのマリネ", "green": "アスパラガス", "yellow": "うずらの煮卵", "tip": "ちょっと大人な彩り。アスパラは縦に詰めると隙間にフィットします。"},
    {"red": "ラディッシュ", "green": "ほうれん草のナムル", "yellow": "さつまいもの甘露煮", "tip": "和風でまとめたい時に。さつまいもの黄色がアクセントになります。"}
]

st.title("🍱 Bento Vision")
st.subheader("アップロードして隙間埋めレシピを提案")

# 写真アップロード
uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    # セッション状態を使って、提案を保持する（ボタンを押しても消えないようにする）
    if 'proposal' not in st.session_state:
        st.session_state.proposal = None

    if st.button("✨ 隙間埋めレシピを提案！") or st.button("🔄 もう一品考えて！"):
        # ランダムにメニューを一つ選ぶ
        st.session_state.proposal = random.choice(menu_options)
        
        # 演出
        with st.status("分析中...", expanded=True) as status:
            time.sleep(1.0)
            st.write("お弁当箱の形状を解析...")
            time.sleep(0.8)
            st.write("最適な食材を選定中...")
            time.sleep(0.8)
            status.update(label="完了！", state="complete")
            
        st.balloons()

    # 提案を表示
    if st.session_state.proposal:
        p = st.session_state.proposal
        st.success("提案が完成しました！")
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 15px; border-left: 10px solid #ff9e1b; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: #2c3e50;">💡 本日のおすすめの隙間埋め</h3>
            <p>🔴 <b>赤：{p['red']}</b></p>
            <p>🟢 <b>緑：{p['green']}</b></p>
            <p>🟡 <b>黄：{p['yellow']}</b></p>
            <p><i>💡 詰め方のコツ: {p['tip']}</i></p>
        </div>
        """, unsafe_allow_html=True)

st.caption("Bento Vision - Recipe Randomizer Version")
