import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 1. メニュー生成関数
def create_menu(category_name, count):
    return [{"name": f"{category_name}_{i+1}", "url": "https://www.kurashiru.com/search?query=おかず"} for i in range(count)]

# 各カテゴリ30個ずつ作成
rice_list = create_menu("ご飯", 30)
red_list = create_menu("赤おかず", 30)
green_list = create_menu("緑おかず", 30)
yellow_list = create_menu("黄おかず", 30)
free_list = create_menu("メインおかず", 30)

# セッション初期化
if 'proposal' not in st.session_state: st.session_state.proposal = None
if 'last_ids' not in st.session_state: st.session_state.last_ids = None
if 'locks' not in st.session_state: st.session_state.locks = {"rice": False, "s1": False, "s2": False, "s3": False, "s4": False, "s5": False}

st.title("🍱 Bento Vision")

# --- 写真アップロード工程（一番上に配置） ---
uploaded_file = st.file_uploader("1. お弁当箱（番号入り）の写真をアップロードしてください", type=["jpg", "jpeg", "png"])

# ランダム提案ロジック
def get_random_proposal():
    while True:
        new_p = {
            "rice": random.choice(rice_list), "s1": random.choice(red_list), 
            "s2": random.choice(green_list), "s3": random.choice(yellow_list), 
            "s4": random.choice(free_list), "s5": random.choice(free_list)
        }
        if new_p["s4"]["name"] != new_p["s5"]["name"]:
            current_ids = tuple(item['name'] for item in new_p.values())
            if current_ids != st.session_state.last_ids:
                st.session_state.last_ids = current_ids
                return new_p

if st.button("✨ 2. 今日のお弁当プランを提案"):
    st.session_state.proposal = get_random_proposal()
    st.session_state.locks = {k: False for k in st.session_state.locks}

# 表示処理
if st.session_state.proposal:
    p = st.session_state.proposal
    
    # 写真がある場合のみガイドとして表示
    if uploaded_file:
        st.markdown("### 📍 配置ガイド")
        st.image(uploaded_file, use_container_width=True)

    st.markdown("### 📝 今日の献立")
    
    def show_item(label, key, item):
        st.session_state.locks[key] = st.checkbox(f"{label}: {item['name']}", value=st.session_state.locks[key])
        st.markdown(f"　 └ [作り方レシピ]({item['url']})")

    show_item("🍚 ご飯", "rice", p["rice"])
    show_item("🔴 赤", "s1", p["s1"]); show_item("🟢 緑", "s2", p["s2"]); show_item("🟡 黄", "s3", p["s3"])
    show_item("🥢 おかず4", "s4", p["s4"]); show_item("🥢 おかず5", "s5", p["s5"])

    if st.button("🔄 3. 未チェックを再検討"):
        if not st.session_state.locks["rice"]: st.session_state.proposal["rice"] = random.choice(rice_list)
        if not st.session_state.locks["s1"]: st.session_state.proposal["s1"] = random.choice(red_list)
        if not st.session_state.locks["s2"]: st.session_state.proposal["s2"] = random.choice(green_list)
        if not st.session_state.locks["s3"]: st.session_state.proposal["s3"] = random.choice(yellow_list)
        if not st.session_state.locks["s4"]: st.session_state.proposal["s4"] = random.choice(free_list)
        if not st.session_state.locks["s5"]: 
            while True:
                new_s5 = random.choice(free_list)
                if new_s5["name"] != st.session_state.proposal["s4"]["name"]:
                    st.session_state.proposal["s5"] = new_s5
                    break
        st.rerun()
