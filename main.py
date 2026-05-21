import streamlit as st
import time
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 提案メニュー
menu_options = [
    {"red": "ミニトマト", "green": "ブロッコリー", "yellow": "卵焼き", "tip": "定番の赤・緑・黄で、まずは基本を抑えましょう！"},
    {"red": "カニカマ", "green": "枝豆", "yellow": "コーンバター", "tip": "枝豆はピックに刺すと可愛いです。"},
    {"red": "赤パプリカ", "green": "アスパラガス", "yellow": "うずらの煮卵", "tip": "アスパラは縦に詰めると隙間にフィット！"},
    {"red": "ラディッシュ", "green": "ナムル", "yellow": "さつまいも", "tip": "和風でまとめたい時に。"}
]

st.title("🍱 Bento Vision")

# 状態管理
if 'proposal' not in st.session_state:
    st.session_state.proposal = None

uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    # 提案がまだなら「提案ボタン」、既にあるなら「もう一品ボタン」を表示する仕組み
    if st.session_state.proposal is None:
        if st.button("✨ 隙間埋めレシピを提案！"):
            with st.status("分析中...", expanded=True) as status:
                time.sleep(1.5)
                status.update(label="完了！", state="complete")
            st.session_state.proposal = random.choice(menu_options)
            st.rerun()
    else:
        # 結果表示
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
        
        # 提案が出ている時だけ「もう一品」を表示
        if st.button("🔄 もう一品提案して！"):
            st.session_state.proposal = random.choice(menu_options)
            st.rerun()
