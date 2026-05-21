import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 1. メニューリスト（レシピリンク付き）
rice_list = [
    {"name": "梅干しご飯", "url": "https://www.kurashiru.com/recipes/e89c0d12-3456-4789-a0b1-c2d3e4f56789"},
    {"name": "白ご飯", "url": "https://www.kurashiru.com/recipes/5c3577d6-3e4b-4b2e-a4b5-4b5745778844"},
    {"name": "わかめご飯", "url": "https://www.kurashiru.com/recipes/d337d121-657d-4171-85f2-53b05f69e6b4"},
    {"name": "炊き込みご飯", "url": "https://www.kurashiru.com/recipes/7b2e95a9-e85d-4f11-9252-012586b5b546"},
    {"name": "鮭フレークご飯", "url": "https://www.kurashiru.com/recipes/6e2b10a2-23c5-4d76-8f37-1845f34177b9"}
]
red_list = [
    {"name": "ミニトマト", "url": "https://www.kurashiru.com/recipes/a1b2c3d4-e5f6-4g7h-8i9j-k0l1m2n3o4p5"},
    {"name": "カニカマ", "url": "https://www.kurashiru.com/recipes/b2c3d4e5-f6g7-4h8i-9j0k-l1m2n3o4p5q6"},
    {"name": "タコさんウィンナー", "url": "https://www.kurashiru.com/recipes/d4e5f6g7-h8i9-4j0k-1l2m-n3o4p5q6r7s8"}
]
green_list = [
    {"name": "ブロッコリーの胡麻和え", "url": "https://www.kurashiru.com/recipes/f6g7h8i9-j0k1-4l2m-3n4o-p5q6r7s8t9u0"},
    {"name": "ほうれん草のナムル", "url": "https://www.kurashiru.com/recipes/i9j0k1l2-m3n4-4o5p-6q7r-s8t9u0v1w2x3"}
]
yellow_list = [
    {"name": "卵焼き", "url": "https://www.kurashiru.com/recipes/k1l2m3n4-o5p6-4q7r-8s9t-u0v1w2x3y4z5"},
    {"name": "カボチャの煮物", "url": "https://www.kurashiru.com/recipes/l2m3n4o5-p6q7-4r8s-9t0u-v1w2x3y4z5a6"}
]
free_list = [
    {"name": "鶏の唐揚げ", "url": "https://www.kurashiru.com/recipes/53066d95-e2a2-466d-8874-884988775f0a"},
    {"name": "ハンバーグ", "url": "https://www.kurashiru.com/recipes/d61e6950-653a-441c-b710-bb2a4a796e63"},
    {"name": "焼き鮭", "url": "https://www.kurashiru.com/recipes/209c18d9-cf6a-466f-b25c-02cf4c3b53c1"},
    {"name": "ちくわの磯辺揚げ", "url": "https://www.kurashiru.com/recipes/10609341-9447-414e-b962-d99f4d38e217"}
]

# セッション初期化
if 'proposal' not in st.session_state: st.session_state.proposal = None
if 'locks' not in st.session_state: st.session_state.locks = {"rice": False, "s1": False, "s2": False, "s3": False, "s4": False, "s5": False}

st.title("🍱 Bento Vision")

# 写真アップロード
uploaded_file = st.file_uploader("お弁当箱の写真をアップロード（任意）", type=["jpg", "jpeg", "png"])

# 提案ボタン
if st.button("✨ 今日のお弁当プランを提案"):
    st.session_state.proposal = {
        "rice": random.choice(rice_list), "s1": random.choice(red_list), 
        "s2": random.choice(green_list), "s3": random.choice(yellow_list), 
        "s4": random.choice(free_list), "s5": random.choice(free_list)
    }

# メイン表示
if st.session_state.proposal:
    p = st.session_state.proposal
    
    if uploaded_file:
        st.markdown("### 📍 配置ガイド")
        st.image(uploaded_file, caption="この写真を参考に詰めてください", use_container_width=True)

    st.markdown("### 📝 今日の献立とレシピ")
    st.info("固定したいおかずはチェックを入れてください")
    
    st.session_state.locks["rice"] = st.checkbox(f"🍚 ご飯: {p['rice']['name']}", value=st.session_state.locks["rice"])
    st.markdown(f"　 └ [作り方レシピ]({p['rice']['url']})")
    st.session_state.locks["s1"] = st.checkbox(f"🔴 赤: {p['s1']['name']}", value=st.session_state.locks["s1"])
    st.markdown(f"　 └ [作り方レシピ]({p['s1']['url']})")
    st.session_state.locks["s2"] = st.checkbox(f"🟢 緑: {p['s2']['name']}", value=st.session_state.locks["s2"])
    st.markdown(f"　 └ [作り方レシピ]({p['s2']['url']})")
    st.session_state.locks["s3"] = st.checkbox(f"🟡 黄: {p['s3']['name']}", value=st.session_state.locks["s3"])
    st.markdown(f"　 └ [作り方レシピ]({p['s3']['url']})")
    st.session_state.locks["s4"] = st.checkbox(f"🥢 おかず4: {p['s4']['name']}", value=st.session_state.locks["s4"])
    st.markdown(f"　 └ [作り方レシピ]({p['s4']['url']})")
    st.session_state.locks["s5"] = st.checkbox(f"🥢 おかず5: {p['s5']['name']}", value=st.session_state.locks["s5"])
    st.markdown(f"　 └ [作り方レシピ]({p['s5']['url']})")

    # 再検討ロジック
    if st.button("🔄 未チェックを再検討"):
        if not st.session_state.locks["rice"]: st.session_state.proposal["rice"] = random.choice(rice_list)
        if not st.session_state.locks["s1"]: st.session_state.proposal["s1"] = random.choice(red_list)
        if not st.session_state.locks["s2"]: st.session_state.proposal["s2"] = random.choice(green_list)
        if not st.session_state.locks["s3"]: st.session_state.proposal["s3"] = random.choice(yellow_list)
        if not st.session_state.locks["s4"]: st.session_state.proposal["s4"] = random.choice(free_list)
        if not st.session_state.locks["s5"]: st.session_state.proposal["s5"] = random.choice(free_list)
        st.rerun()
