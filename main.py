import streamlit as st
import time
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 提案メニュー
menu_options = [
    {"name": "定番！彩り三色わっぱ弁当", "red": "ミニトマト", "green": "ブロッコリー", "yellow": "卵焼き", "tip": "迷ったらこれ！定番の赤・緑・黄で間違いなしです。"},
    {"name": "おつまみ感覚！彩りおかず弁当", "red": "カニカマ", "green": "枝豆", "yellow": "コーンバター", "tip": "枝豆をピックに刺すと、見た目がグンと可愛くなります。"},
    {"name": "ちょっと贅沢な洋風弁当", "red": "赤パプリカのマリネ", "green": "アスパラガス", "yellow": "うずらの煮卵", "tip": "アスパラを縦に詰めると、隙間にピタッとハマります。"},
    {"name": "ほっこり和風ランチ弁当", "red": "ラディッシュ", "green": "ほうれん草のナムル", "yellow": "さつまいもの甘露煮", "tip": "さつまいもの甘みが和食のいいアクセントになります。"}
]

st.title("🍱 Bento Vision")

# 状態管理
if 'proposal' not in st.session_state:
    st.session_state.proposal = None

uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    # 提案ボタン
    if st.session_state.proposal is None:
        if st.button("✨ 隙間埋めレシピを提案！"):
            with st.status("分析中...", expanded=True) as status:
                time.sleep(1.0)
                status.update(label="分析完了！", state="complete")
            st.session_state.proposal = random.choice(menu_options)
            st.rerun()
    else:
        # 結果表示
        p = st.session_state.proposal
        st.success("提案が完成しました！")
        
        st.markdown(f"""
        <div style="background-color: white; padding: 25px; border-radius: 15px; border-left: 10px solid #ff9e1b; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            <h2 style="color: #ff9e1b; margin-top: 0;">{p['name']}</h2>
            <hr>
            <div style="font-size: 20px; line-height: 2;">
                🔴 赤のおかず：<b>{p['red']}</b><br>
                🟢 緑のおかず：<b>{p['green']}</b><br>
                🟡 黄のおかず：<b>{p['yellow']}</b>
            </div>
            <div style="background-color: #fff9f0; padding: 15px; border-radius: 10px; margin-top: 20px;">
                <p style="margin: 0;"><b>💡 詰め方のコツ:</b><br>{p['tip']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("🔄 もう一品提案して！"):
            st.session_state.proposal = random.choice(menu_options)
            st.rerun()
