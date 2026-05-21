import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# リストの拡張
rice_list = ["白ご飯（梅干し添え）", "わかめご飯", "炊き込みご飯", "鮭フレークご飯", "玄米ご飯", "雑穀米", "ゆかりご飯", "炒飯"]
side_list = [
    "ミニトマト", "カニカマ", "赤パプリカ", "ラディッシュ", "赤ウインナー", "梅干し", "揚げミニトマト", "しば漬け", "明太子", "タコさんウィンナー",
    "ブロッコリー", "枝豆", "アスパラガス", "ほうれん草のナムル", "ピーマンの炒め物", "きゅうりの浅漬け", "スナップエンドウ", "インゲンの胡麻和え", "小松菜のおひたし", "オクラ",
    "卵焼き", "コーンバター", "うずらの煮卵", "さつまいもの甘露煮", "カレー炒り卵", "パプリカソテー", "さつまいもチップス", "チーズウインナー", "カボチャの煮物", "厚焼き玉子"
]

st.title("🍱 Bento Vision")

# セッション初期化
if 'proposal' not in st.session_state:
    st.session_state.proposal = None
if 'locks' not in st.session_state:
    st.session_state.locks = {"rice": False, "s1": False, "s2": False, "s3": False, "s4": False, "s5": False}

uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    if st.session_state.proposal is None:
        if st.button("✨ 今日のお弁当プランを提案"):
            st.session_state.proposal = {
                "rice": random.choice(rice_list),
                "s1": random.choice(side_list), "s2": random.choice(side_list),
                "s3": random.choice(side_list), "s4": random.choice(side_list),
                "s5": random.choice(side_list)
            }
            st.rerun()
    else:
        p = st.session_state.proposal
        st.success("提案が完成しました！")
        
        st.markdown("### 🍱 今日の献立（固定したいものにチェック）")
        
        # ご飯のロック
        st.session_state.locks["rice"] = st.checkbox(f"🍚 ご飯: {p['rice']}", value=st.session_state.locks["rice"])
        
        # おかずのロック（2列に分ける）
        col1, col2 = st.columns(2)
        keys = ["s1", "s2", "s3", "s4", "s5"]
        for i, key in enumerate(keys):
            if i % 2 == 0:
                with col1:
                    st.session_state.locks[key] = st.checkbox(f"🥢 おかず{i+1}: {p[key]}", value=st.session_state.locks[key])
            else:
                with col2:
                    st.session_state.locks[key] = st.checkbox(f"🥢 おかず{i+1}: {p[key]}", value=st.session_state.locks[key])
        
        st.write("")
        if st.button("🔄 ロックしていないものを再検討"):
            if not st.session_state.locks["rice"]: st.session_state.proposal["rice"] = random.choice(rice_list)
            for key in keys:
                if not st.session_state.locks[key]: st.session_state.proposal[key] = random.choice(side_list)
            st.rerun()

        if st.button("❌ 全部リセット"):
            st.session_state.proposal = None
            st.session_state.locks = {k: False for k in st.session_state.locks}
            st.rerun()

st.caption("Bento Vision - Deluxe Plan Version")
