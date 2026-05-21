import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 1. 充実の全20項目リスト
rice_list = [
    {"name": f"{n}ご飯", "url": "https://www.kurashiru.com/search?query=ご飯"} for n in 
    ["白", "わかめ", "炊き込み", "鮭フレーク", "玄米", "雑穀", "ゆかり", "炒飯", "塩昆布", "梅干し", "高菜", "菜飯", "カリカリ梅", "おかか", "ちらし寿司", "とろろ昆布", "オムライス風", "豆", "そぼろ", "カレーピラフ"]
]
red_list = [
    {"name": n, "url": "https://www.kurashiru.com/search?query=赤おかず"} for n in 
    ["ミニトマト", "カニカマ", "赤パプリカ", "ラディッシュ", "赤ウインナー", "揚げミニトマト", "明太子", "タコさんウィンナー", "しば漬け", "パプリカマリネ", "赤かぶ漬け", "イチゴ", "さくらんぼ", "赤パプリカ素揚げ", "ビーツサラダ", "トマトマリネ", "赤ハム巻き", "カニカママヨ", "冷凍ラズベリー", "紅しょうが"]
]
green_list = [
    {"name": n, "url": "https://www.kurashiru.com/search?query=緑おかず"} for n in 
    ["ブロッコリー", "枝豆", "アスパラお浸し", "ほうれん草ナムル", "ピーマン炒め", "きゅうり浅漬け", "スナップエンドウ", "インゲン胡麻和え", "小松菜おひたし", "オクラ", "ピーマン肉詰め", "ほうれん草ソテー", "枝豆ピック", "大葉卵巻き", "アスパラベーコン", "ブロッコリー素揚げ", "ピーマンマリネ", "きゅうりナムル", "枝豆塩昆布", "菜の花"]
]
yellow_list = [
    {"name": n, "url": "https://www.kurashiru.com/search?query=黄おかず"} for n in 
    ["卵焼き", "コーンバター", "うずら煮卵", "さつまいも甘露煮", "カレー炒り卵", "パプリカソテー", "厚焼き玉子", "チーズウインナー", "カボチャ煮物", "コーン素揚げ", "炒り卵", "さつまいもレモン煮", "たくあん", "スイートコーン", "伊達巻", "さつまいも素揚げ", "コーンマヨ", "うずらベーコン", "カボチャ素揚げ", "味付け卵"]
]
free_list = [
    {"name": n, "url": "https://www.kurashiru.com/search?query=メインおかず"} for n in 
    ["鶏の唐揚げ", "ハンバーグ", "焼き鮭", "生姜焼き", "磯辺揚げ", "コロッケ", "鯖塩焼き", "肉団子", "エビフライ", "トンカツ", "鶏照り焼き", "鯖味噌煮", "メンチカツ", "豚の角煮", "鶏つくね", "アジフライ", "カニクリームコロッケ", "回鍋肉", "酢豚", "鶏塩焼き"]
]

# セッション初期化
if 'proposal' not in st.session_state: st.session_state.proposal = None
if 'last_ids' not in st.session_state: st.session_state.last_ids = None
if 'locks' not in st.session_state: st.session_state.locks = {"rice": False, "s1": False, "s2": False, "s3": False, "s4": False, "s5": False}

st.title("🍱 Bento Vision")

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

uploaded_file = st.file_uploader("お弁当箱の写真をアップロード（任意）", type=["jpg", "jpeg", "png"])

if st.button("✨ 今日のお弁当プランを提案"):
    st.session_state.proposal = get_random_proposal()
    st.session_state.locks = {k: False for k in st.session_state.locks}

if st.session_state.proposal:
    p = st.session_state.proposal
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

    if st.button("🔄 未チェックを再検討"):
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
