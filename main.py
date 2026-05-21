import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 1. 充実のメニューリスト定義
rice_list = [
    "白ご飯（梅干し添え）", "わかめご飯", "炊き込みご飯", "鮭フレークご飯", "玄米ご飯", 
    "雑穀米", "ゆかりご飯", "炒飯", "塩昆布おにぎり", "ツナマヨご飯", 
    "高菜ご飯", "菜飯（なめし）", "カリカリ梅ご飯", "鰹節おかかご飯", "五目ちらし寿司", 
    "とろろ昆布ご飯", "オムライス風ご飯", "豆ごはん", "そぼろご飯", "カレーピラフ"
]

red_list = [
    "ミニトマト", "カニカマ", "赤パプリカ", "ラディッシュ", "赤ウインナー", "梅干し", 
    "揚げミニトマト", "明太子", "タコさんウィンナー", "しば漬け", "パプリカのマリネ", 
    "赤かぶの甘酢漬け", "イチゴ", "さくらんぼ", "赤パプリカの素揚げ", "ビーツのサラダ", 
    "トマトのマリネ", "赤いハム巻き", "カニカマのマヨ和え", "冷凍ラズベリー", "赤ピーマンの炒め物", "紅しょうが"
]

green_list = [
    "ブロッコリー", "枝豆", "アスパラガス", "ほうれん草のナムル", "ピーマンの炒め物", 
    "きゅうりの浅漬け", "スナップエンドウ", "インゲンの胡麻和え", "小松菜のおひたし", "オクラ",
    "ピーマンの肉詰め", "ほうれん草のバターソテー", "枝豆ピック", "大葉の卵巻き"
]

yellow_list = [
    "卵焼き", "コーンバター", "うずらの煮卵", "さつまいもの甘露煮", "カレー炒り卵", 
    "パプリカソテー", "厚焼き玉子", "チーズウインナー", "カボチャの煮物", "コーンの素揚げ",
    "炒り卵", "さつまいものレモン煮", "たくあん", "スイートコーン"
]

# フリー枠（レシピリンク付き）
free_list = [
    {"name": "鶏の唐揚げ", "url": "https://www.kurashiru.com/recipes/4dbf823e-598f-4fc0-b609-8f6fff8028b6"},
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

# 1. 写真アップロード（復活！）
uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)

    # 2. 提案ボタン
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

        # 3. 配置ガイド（分布図）の表示
        st.markdown("### 📍 配置ガイド")
        st.markdown('<div class="center-box">', unsafe_allow_html=True)
        st.code(f"""
    +-----------------------+
    |           |    ①     |
    |   ご飯    |-----------|
    |           |    ②     |
    |-----------+-----------|
    |     ⑤     | ④ |  ③  |
    +-----------------------+
    """, language="text")
        st.markdown('</div>', unsafe_allow_html=True)

        # 4. ロック機能付き献立リスト
        st.markdown("### 📝 今日の献立（固定するものにチェック）")
        
        st.session_state.locks["rice"] = st.checkbox(f"🍚 ご飯: {p['rice']}", value=st.session_state.locks["rice"])
        st.session_state.locks["s1"] = st.checkbox(f"🔴 おかず1: {p['s1']}", value=st.session_state.locks["s1"])
        st.session_state.locks["s2"] = st.checkbox(f"🟢 おかず2: {p['s2']}", value=st.session_state.locks["s2"])
        st.session_state.locks["s3"] = st.checkbox(f"🟡 おかず3: {p['s3']}", value=st.session_state.locks["s3"])
        
        # フリー枠は名前とレシピリンクを表示しつつロック
        for i in [4, 5]:
            key = f"s{i}"
            item = p[key]
            label = f"🥢 おかず{i}: {item['name']}"
            st.session_state.locks[key] = st.checkbox(label, value=st.session_state.locks[key])
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

st.caption("Bento Vision - Visual & Recipe Edition")
