import streamlit as st
import time
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# おかずリスト
red_list = ["ミニトマト", "カニカマ", "赤パプリカ", "ラディッシュ", "赤ウインナー", "梅干し", "揚げミニトマト", "しば漬け", "明太子", "タコさんウィンナー"]
green_list = ["ブロッコリー", "枝豆", "アスパラガス", "ほうれん草のナムル", "ピーマンの炒め物", "きゅうりの浅漬け", "スナップエンドウ", "インゲンの胡麻和え", "小松菜のおひたし", "オクラ"]
yellow_list = ["卵焼き", "コーンバター", "うずらの煮卵", "さつまいもの甘露煮", "カレー炒り卵", "パプリカソテー", "さつまいもチップス", "チーズウインナー", "カボチャの煮物", "厚焼き玉子"]

st.title("🍱 Bento Vision")

# 状態管理
if 'proposal' not in st.session_state:
    st.session_state.proposal = None
if 'locks' not in st.session_state:
    st.session_state.locks = {"red": False, "green": False, "yellow": False}

uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    # 提案ボタン
    if st.session_state.proposal is None:
        if st.button("✨ 今日のお弁当プランを提案"):
            st.session_state.proposal = {
                "red": random.choice(red_list),
                "green": random.choice(green_list),
                "yellow": random.choice(yellow_list)
            }
            st.rerun()
    else:
        p = st.session_state.proposal
        st.success("提案が完成しました！")
        
        # 固定（ロック）機能付きの表示
        st.markdown("### 今日のプラン（固定したい項目にチェック）")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.session_state.locks["red"] = st.checkbox(f"🔴 赤: {p['red']}", value=st.session_state.locks["red"])
        with col2:
            st.session_state.locks["green"] = st.checkbox(f"🟢 緑: {p['green']}", value=st.session_state.locks["green"])
        with col3:
            st.session_state.locks["yellow"] = st.checkbox(f"🟡 黄: {p['yellow']}", value=st.session_state.locks["yellow"])
        
        st.write("")
        if st.button("🔄 ロックしていないおかずを再検討"):
            # ロックされていないものだけ更新
            if not st.session_state.locks["red"]:
                st.session_state.proposal["red"] = random.choice(red_list)
            if not st.session_state.locks["green"]:
                st.session_state.proposal["green"] = random.choice(green_list)
            if not st.session_state.locks["yellow"]:
                st.session_state.proposal["yellow"] = random.choice(yellow_list)
            st.rerun()

        # リセットボタン（全部やり直したい時用）
        if st.button("❌ 全部リセットして最初から"):
            st.session_state.proposal = None
            st.session_state.locks = {"red": False, "green": False, "yellow": False}
            st.rerun()

st.caption("Bento Vision - Lock & Re-roll Version")
