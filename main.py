import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 1. 20個ずつメニューリストを定義
rice_list = [
    {"name": "白ご飯", "url": "https://www.kurashiru.com/search?query=白ご飯"}, {"name": "わかめご飯", "url": "https://www.kurashiru.com/search?query=わかめご飯"},
    {"name": "炊き込みご飯", "url": "https://www.kurashiru.com/search?query=炊き込みご飯"}, {"name": "鮭フレークご飯", "url": "https://www.kurashiru.com/search?query=鮭フレークご飯"},
    {"name": "玄米ご飯", "url": "https://www.kurashiru.com/search?query=玄米ご飯"}, {"name": "雑穀米", "url": "https://www.kurashiru.com/search?query=雑穀米"},
    {"name": "ゆかりご飯", "url": "https://www.kurashiru.com/search?query=ゆかりご飯"}, {"name": "炒飯", "url": "https://www.kurashiru.com/search?query=炒飯"},
    {"name": "塩昆布おにぎり", "url": "https://www.kurashiru.com/search?query=塩昆布おにぎり"}, {"name": "梅干しご飯", "url": "https://www.kurashiru.com/search?query=梅干しご飯"},
    {"name": "高菜ご飯", "url": "https://www.kurashiru.com/search?query=高菜ご飯"}, {"name": "菜飯", "url": "https://www.kurashiru.com/search?query=菜飯"},
    {"name": "カリカリ梅ご飯", "url": "https://www.kurashiru.com/search?query=カリカリ梅ご飯"}, {"name": "おかかご飯", "url": "https://www.kurashiru.com/search?query=おかかご飯"},
    {"name": "ちらし寿司", "url": "https://www.kurashiru.com/search?query=ちらし寿司"}, {"name": "とろろ昆布ご飯", "url": "https://www.kurashiru.com/search?query=とろろ昆布ご飯"},
    {"name": "オムライス風", "url": "https://www.kurashiru.com/search?query=オムライス風"}, {"name": "豆ご飯", "url": "https://www.kurashiru.com/search?query=豆ご飯"},
    {"name": "そぼろご飯", "url": "https://www.kurashiru.com/search?query=そぼろご飯"}, {"name": "カレーピラフ", "url": "https://www.kurashiru.com/search?query=カレーピラフ"}
]

red_list = [
    {"name": "ミニトマト", "url": "https://www.kurashiru.com/search?query=ミニトマト"}, {"name": "カニカマ", "url": "https://www.kurashiru.com/search?query=カニカマ"},
    {"name": "赤パプリカ", "url": "https://www.kurashiru.com/search?query=赤パプリカ"}, {"name": "ラディッシュ", "url": "https://www.kurashiru.com/search?query=ラディッシュ"},
    {"name": "赤ウインナー", "url": "https://www.kurashiru.com/search?query=赤ウインナー"}, {"name": "揚げミニトマト", "url": "https://www.kurashiru.com/search?query=揚げミニトマト"},
    {"name": "明太子", "url": "https://www.kurashiru.com/search?query=明太子"}, {"name": "タコさんウィンナー", "url": "https://www.kurashiru.com/search?query=タコさんウィンナー"},
    {"name": "しば漬け", "url": "https://www.kurashiru.com/search?query=しば漬け"}, {"name": "赤パプリカマリネ", "url": "https://www.kurashiru.com/search?query=赤パプリカマリネ"},
    {"name": "赤かぶ漬け", "url": "https://www.kurashiru.com/search?query=赤かぶ漬け"}, {"name": "イチゴ", "url": "https://www.kurashiru.com/search?query=イチゴ"},
    {"name": "さくらんぼ", "url": "https://www.kurashiru.com/search?query=さくらんぼ"}, {"name": "赤パプリカ素揚げ", "url": "https://www.kurashiru.com/search?query=赤パプリカ素揚げ"},
    {"name": "ビーツサラダ", "url": "https://www.kurashiru.com/search?query=ビーツサラダ"}, {"name": "トマトマリネ", "url": "https://www.kurashiru.com/search?query=トマトマリネ"},
    {"name": "赤ハム巻き", "url": "https://www.kurashiru.com/search?query=赤ハム巻き"}, {"name": "カニカママヨ", "url": "https://www.kurashiru.com/search?query=カニカママヨ"},
    {"name": "冷凍ラズベリー", "url": "https://www.kurashiru.com/search?query=冷凍ラズベリー"}, {"name": "紅しょうが", "url": "https://www.kurashiru.com/search?query=紅しょうが"}
]

green_list = [
    {"name": "ブロッコリー", "url": "https://www.kurashiru.com/search?query=ブロッコリー"}, {"name": "枝豆", "url": "https://www.kurashiru.com/search?query=枝豆"},
    {"name": "アスパラお浸し", "url": "https://www.kurashiru.com/search?query=アスパラお浸し"}, {"name": "ほうれん草ナムル", "url": "https://www.kurashiru.com/search?query=ほうれん草ナムル"},
    {"name": "ピーマン炒め", "url": "https://www.kurashiru.com/search?query=ピーマン炒め"}, {"name": "きゅうり浅漬け", "url": "https://www.kurashiru.com/search?query=きゅうり浅漬け"},
    {"name": "スナップエンドウ", "url": "https://www.kurashiru.com/search?query=スナップエンドウ"}, {"name": "インゲン胡麻和え", "url": "https://www.kurashiru.com/search?query=インゲン胡麻和え"},
    {"name": "小松菜おひたし", "url": "https://www.kurashiru.com/search?query=小松菜おひたし"}, {"name": "オクラ", "url": "https://www.kurashiru.com/search?query=オクラ"},
    {"name": "ピーマン肉詰め", "url": "https://www.kurashiru.com/search?query=ピーマン肉詰め"}, {"name": "ほうれん草ソテー", "url": "https://www.kurashiru.com/search?query=ほうれん草ソテー"},
    {"name": "枝豆ピック", "url": "https://www.kurashiru.com/search?query=枝豆ピック"}, {"name": "大葉卵巻き", "url": "https://www.kurashiru.com/search?query=大葉卵巻き"},
    {"name": "アスパラベーコン", "url": "https://www.kurashiru.com/search?query=アスパラベーコン"}, {"name": "ブロッコリー素揚げ", "url": "https://www.kurashiru.com/search?query=ブロッコリー素揚げ"},
    {"name": "ピーマンマリネ", "url": "https://www.kurashiru.com/search?query=ピーマンマリネ"}, {"name": "きゅうりナムル", "url": "https://www.kurashiru.com/search?query=きゅうりナムル"},
    {"name": "枝豆塩昆布", "url": "https://www.kurashiru.com/search?query=枝豆塩昆布"}, {"name": "菜の花", "url": "https://www.kurashiru.com/search?query=菜の花"}
]

yellow_list = [
    {"name": "卵焼き", "url": "https://www.kurashiru.com/search?query=卵焼き"}, {"name": "コーンバター", "url": "https://www.kurashiru.com/search?query=コーンバター"},
    {"name": "うずら煮卵", "url": "https://www.kurashiru.com/search?query=うずら煮卵"}, {"name": "さつまいも甘露煮", "url": "https://www.kurashiru.com/search?query=さつまいも甘露煮"},
    {"name": "カレー炒り卵", "url": "https://www.kurashiru.com/search?query=カレー炒り卵"}, {"name": "パプリカソテー", "url": "https://www.kurashiru.com/search?query=パプリカソテー"},
    {"name": "厚焼き玉子", "url": "https://www.kurashiru.com/search?query=厚焼き玉子"}, {"name": "チーズウインナー", "url": "https://www.kurashiru.com/search?query=チーズウインナー"},
    {"name": "カボチャ煮物", "url": "https://www.kurashiru.com/search?query=カボチャ煮物"}, {"name": "コーン素揚げ", "url": "https://www.kurashiru.com/search?query=コーン素揚げ"},
    {"name": "炒り卵", "url": "https://www.kurashiru.com/search?query=炒り卵"}, {"name": "さつまいもレモン煮", "url": "https://www.kurashiru.com/search?query=さつまいもレモン煮"},
    {"name": "たくあん", "url": "https://www.kurashiru.com/search?query=たくあん"}, {"name": "スイートコーン", "url": "https://www.kurashiru.com/search?query=スイートコーン"},
    {"name": "伊達巻", "url": "https://www.kurashiru.com/search?query=伊達巻"}, {"name": "さつまいも素揚げ", "url": "https://www.kurashiru.com/search?query=さつまいも素揚げ"},
    {"name": "コーンマヨ", "url": "https://www.kurashiru.com/search?query=コーンマヨ"}, {"name": "うずらベーコン", "url": "https://www.kurashiru.com/search?query=うずらベーコン"},
    {"name": "カボチャ素揚げ", "url": "https://www.kurashiru.com/search?query=カボチャ素揚げ"}, {"name": "味付け卵", "url": "https://www.kurashiru.com/search?query=味付け卵"}
]

free_list = [
    {"name": "鶏の唐揚げ", "url": "https://www.kurashiru.com/search?query=鶏の唐揚げ"}, {"name": "ハンバーグ", "url": "https://www.kurashiru.com/search?query=ハンバーグ"},
    {"name": "焼き鮭", "url": "https://www.kurashiru.com/search?query=焼き鮭"}, {"name": "生姜焼き", "url": "https://www.kurashiru.com/search?query=生姜焼き"},
    {"name": "磯辺揚げ", "url": "https://www.kurashiru.com/search?query=磯辺揚げ"}, {"name": "コロッケ", "url": "https://www.kurashiru.com/search?query=コロッケ"},
    {"name": "鯖塩焼き", "url": "https://www.kurashiru.com/search?query=鯖塩焼き"}, {"name": "肉団子", "url": "https://www.kurashiru.com/search?query=肉団子"},
    {"name": "エビフライ", "url": "https://www.kurashiru.com/search?query=エビフライ"}, {"name": "トンカツ", "url": "https://www.kurashiru.com/search?query=トンカツ"},
    {"name": "鶏照り焼き", "url": "https://www.kurashiru.com/search?query=鶏照り焼き"}, {"name": "鯖味噌煮", "url": "https://www.kurashiru.com/search?query=鯖味噌煮"},
    {"name": "メンチカツ", "url": "https://www.kurashiru.com/search?query=メンチカツ"}, {"name": "豚の角煮", "url": "https://www.kurashiru.com/search?query=豚の角煮"},
    {"name": "鶏つくね", "url": "https://www.kurashiru.com/search?query=鶏つくね"}, {"name": "アジフライ", "url": "https://www.kurashiru.com/search?query=アジフライ"},
    {"name": "カニクリームコロッケ", "url": "https://www.kurashiru.com/search?query=カニクリームコロッケ"}, {"name": "回鍋肉", "url": "https://www.kurashiru.com/search?query=回鍋肉"},
    {"name": "酢豚", "url": "https://www.kurashiru.com/search?query=酢豚"}, {"name": "鶏塩焼き", "url": "https://www.kurashiru.com/search?query=鶏塩焼き"}
]

# セッション初期化
if 'proposal' not in st.session_state: st.session_state.proposal = None
if 'last_ids' not in st.session_state: st.session_state.last_ids = None
if 'locks' not in st.session_state: st.session_state.locks = {"rice": False, "s1": False, "s2": False, "s3": False, "s4": False, "s5": False}

st.title("🍱 Bento Vision")

# 写真アップロード工程
uploaded_file = st.file_uploader("1. お弁当箱の写真をアップロードしてください", type=["jpg", "jpeg", "png"])

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
