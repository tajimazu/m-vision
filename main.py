import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 1. レシピ付きメニューリスト
rice_list = ["白ご飯", "わかめご飯", "炊き込みご飯", "鮭フレークご飯", "炒飯", "塩昆布おにぎり"]
red_list = ["ミニトマト", "カニカマ", "赤パプリカ", "梅干し", "タコさんウィンナー"]
green_list = ["ブロッコリー", "枝豆", "アスパラガス", "ほうれん草のナムル", "ピーマンの炒め物"]
yellow_list = ["卵焼き", "コーンバター", "うずらの煮卵", "厚焼き玉子", "カボチャの煮物"]

free_list = [
    {"name": "鶏の唐揚げ", "url": "https://www.kurashiru.com/recipes/53066d95-e2a2-466d-8874-884988775f0a"},
    {"name": "ハンバーグ", "url": "https://www.kurashiru.com/recipes/d61e6950-653a-441c-b710-bb2a4a796e63"},
    {"name": "焼き鮭", "url": "https://www.kurashiru.com/recipes/209c18d9-cf6a-466f-b25c-02cf4c3b53c1"},
    {"name": "豚肉の生姜焼き", "url": "https://www.kurashiru.com/recipes/a2327797-40b4-4e20-8025-5f99166f2868"},
    {"name": "ちくわの磯辺揚げ", "url": "https://www.kurashiru.com/recipes/10609341-9447-414e-b962-d99f4d38e217"}
]

# セッション初期化
if 'proposal' not in st.session_state:
    st.session_state.proposal = None
if 'locks' not in st.session_state:
    st.session_state.locks = {"rice": False, "s1": False, "s2": False, "s3": False, "s4": False, "s5": False}

st.title("🍱 Bento Vision")

# CSSでセンター寄せ設定
st.markdown("""
<style>
.center-box { display: flex; justify-content: center; text-align: center; }
pre { display: inline-block; text-align: left; background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# 写真アップロード
uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)

    # 提案ロジック
    if st.session_state.proposal is None:
        if st.button("✨ 今日のお弁当プランを提案"):
            st.session_state.proposal = {
                "rice": random.choice(rice_list),
                "s1": random.choice(red_list), "s2": random.choice(green_list),
                "s3": random.choice(yellow_list), "s4": random.choice(free_list),
                "s5": random.choice(free_list)
            }
            st.rerun()
    else:
        p = st.session_state.proposal
        st.success("献立が決まりました！")

        # 配置図の表示（中央寄せ）
        st.markdown("### 📍 配置ガイド")
        st.markdown('<div class="center-box">', unsafe_allow_html=True)
        st.code("""
    【配置イメージ】
    +-----------------------+
    |           |    ①     |
    |   ご飯    |-----------|
    |           |    ②     |
    |-----------+-----------|
    |     ⑤     | ④ |  ③  |
    +-----------------------+
    """, language="text")
        st.markdown('</div>', unsafe_allow_html=True)

        # 献立リストとロック機能
        st.markdown("### 📝 今日の献立")
        st.session_state.locks["rice"] = st.checkbox(f"🍚 ご飯: {p['rice']}", value=st.session_state.locks["rice"])
        st.session_state.locks["s1"] = st.checkbox(f"🔴 おかず1: {p['s1']}", value=st.session_state.locks["s1"])
        st.session_state.locks["s2"] = st.checkbox(f"🟢 おかず2: {p['s2']}", value=st.session_state.locks["s2"])
        st.session_state.locks["s3"] = st.checkbox(f"🟡 おかず3: {p['s3']}", value=st.session_state.locks["s3"])
        
        for i in [4, 5]:
            key = f"s{i}"
            item = p[key]
            st.session_state.locks[key] = st.checkbox(f"🥢 おかず{i}: {item['name']}", value=st.session_state.locks[key])
            st.markdown(f"　 └ [作り方レシピを開く]({item['url']})")

        # 操作ボタン
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 未チェックを再検討"):
                if not st.session_state.locks["rice"]: st.session_state.proposal["rice"] = random.choice(rice_list)
                if not st.session_state.locks["s1"]: st.session_state.proposal["s1"] = random.choice(red_list)
                if not st.session_state.locks["s2"]: st.session_state.proposal["s2"] = random.choice(green_list)
                if not st.session_state.locks["s3"]: st.session_state.proposal["s3"] = random.choice(yellow_list)
                if not st.session_state.locks["s4"]: st.session_state.proposal["s4"] = random.choice(free_list)
                if not st.session_state.locks["s5"]: st.session_state.proposal["s5"] = random.choice(free_list)
                st.rerun()
        with col2:
            if st.button("❌ 全部リセット"):
                st.session_state.proposal = None
                st.session_state.locks = {k: False for k in st.session_state.locks}
                st.rerun()

st.caption("Bento Vision - Full Managed Version")
