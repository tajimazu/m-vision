import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 1. レシピ付きフリー枠メニュー（名前とURLのセット）
free_list = [
    {"name": "鶏の唐揚げ", "url": "https://www.kurashiru.com/recipes/53066d95-e2a2-466d-8874-884988775f0a"},
    {"name": "ハンバーグ", "url": "https://www.kurashiru.com/recipes/d61e6950-653a-441c-b710-bb2a4a796e63"},
    {"name": "焼き鮭", "url": "https://www.kurashiru.com/recipes/209c18d9-cf6a-466f-b25c-02cf4c3b53c1"},
    {"name": "豚肉の生姜焼き", "url": "https://www.kurashiru.com/recipes/a2327797-40b4-4e20-8025-5f99166f2868"},
    {"name": "ちくわの磯辺揚げ", "url": "https://www.kurashiru.com/recipes/10609341-9447-414e-b962-d99f4d38e217"},
    {"name": "コロッケ", "url": "https://www.kurashiru.com/recipes/7989938b-d79e-4c74-a3f2-140306c4b267"},
    {"name": "鯖の塩焼き", "url": "https://www.kurashiru.com/recipes/9a4891b2-263a-4933-912f-688849c7162b"},
    {"name": "肉団子", "url": "https://www.kurashiru.com/recipes/c735d487-73d6-4447-817e-727c95e1e93c"},
    {"name": "エビフライ", "url": "https://www.kurashiru.com/recipes/3b2c2e08-9642-45e0-9285-f3775f0f3531"},
    {"name": "トンカツ", "url": "https://www.kurashiru.com/recipes/e54e1a06-a94f-4d0f-a492-c43a6d912423"}
]

# その他のメニューリスト
rice_list = ["白ご飯", "わかめご飯", "炊き込みご飯", "鮭フレークご飯", "炒飯", "塩昆布おにぎり"]
red_list = ["ミニトマト", "カニカマ", "赤パプリカ", "梅干し", "タコさんウィンナー"]
green_list = ["ブロッコリー", "枝豆", "アスパラガス", "ほうれん草のナムル", "ピーマンの炒め物"]
yellow_list = ["卵焼き", "コーンバター", "うずらの煮卵", "厚焼き玉子", "カボチャの煮物"]

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

# 提案ボタン
if st.button("✨ 今日のお弁当プランを提案"):
    st.session_state.proposal = {
        "rice": random.choice(rice_list),
        "s1": random.choice(red_list), "s2": random.choice(green_list),
        "s3": random.choice(yellow_list), "s4": random.choice(free_list),
        "s5": random.choice(free_list)
    }
    st.rerun()

if st.session_state.proposal:
    p = st.session_state.proposal
    st.success("献立が決まりました！")

    # 配置図の表示（中央寄せ）
    st.markdown("### 🍱 配置ガイド")
    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    st.code(f"""
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
    
    # メニュー表示
    st.markdown("### 📝 今日の献立とレシピ")
    st.write(f"🍚 ご飯: {p['rice']}")
    st.write(f"🔴 おかず1: {p['s1']}")
    st.write(f"🟢 おかず2: {p['s2']}")
    st.write(f"🟡 おかず3: {p['s3']}")
    
    # レシピ付き表示
    for i in [4, 5]:
        item = p[f"s{i}"]
        st.write(f"🥢 おかず{i}: [{item['name']}]({item['url']}) (←レシピ)")

    # 再検討ボタン
    if st.button("🔄 再検討"):
        st.session_state.proposal = None
        st.rerun()

st.caption("Bento Vision - Recipe Edition")
