import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# --- リスト定義 ---
rice_list = ["白ご飯（梅干し添え）", "わかめご飯", "炊き込みご飯", "鮭フレークご飯", "玄米ご飯", "雑穀米", "ゆかりご飯", "炒飯", "塩昆布おにぎり", "ツナマヨご飯", "高菜ご飯", "菜飯（なめし）", "カリカリ梅ご飯", "鰹節おかかご飯", "五目ちらし寿司", "とろろ昆布ご飯", "オムライス風ご飯", "豆ごはん", "そぼろご飯", "カレーピラフ"]
red_list = ["ミニトマト", "カニカマ", "赤パプリカ", "ラディッシュ", "赤ウインナー", "梅干し", "揚げミニトマト", "明太子", "タコさんウィンナー", "しば漬け", "パプリカのマリネ", "赤かぶの甘酢漬け", "イチゴ", "さくらんぼ", "赤パプリカの素揚げ", "ビーツのサラダ", "トマトのマリネ", "赤いハム巻き", "カニカマのマヨ和え", "冷凍ラズベリー", "赤ピーマンの炒め物", "紅しょうが"]
green_list = ["ブロッコリー", "枝豆", "アスパラガス", "ほうれん草のナムル", "ピーマンの炒め物", "きゅうりの浅漬け", "スナップエンドウ", "インゲンの胡麻和え", "小松菜のおひたし", "オクラ", "ピーマンの肉詰め", "ほうれん草のバターソテー", "枝豆ピック", "大葉の卵巻き"]
yellow_list = ["卵焼き", "コーンバター", "うずらの煮卵", "さつまいもの甘露煮", "カレー炒り卵", "パプリカソテー", "厚焼き玉子", "チーズウインナー", "カボチャの煮物", "コーンの素揚げ", "炒り卵", "さつまいものレモン煮", "たくあん", "スイートコーン"]
free_list = ["鶏の唐揚げ", "ハンバーグ", "焼き鮭", "豚肉の生姜焼き", "ちくわの磯辺揚げ", "コロッケ", "鯖の塩焼き", "肉団子", "エビフライ", "トンカツ", "鶏の照り焼き", "ブリの照り焼き", "厚揚げの煮物", "シュウマイ", "餃子", "アスパラのベーコン巻き", "白身魚のフライ", "鶏むね肉のピカタ", "豚の角煮", "揚げ出し豆腐"]

st.title("🍱 Bento Vision")

# セッション初期化
if 'proposal' not in st.session_state:
    st.session_state.proposal = None
if 'locks' not in st.session_state:
    st.session_state.locks = {"rice": False, "s1": False, "s2": False, "s3": False, "s4": False, "s5": False}

# 1. 写真アップロード
uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    col_img, col_layout = st.columns([1, 1])
    
    with col_img:
        st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    with col_layout:
        st.subheader("🗺 配置パターンの選択")
        layout_type = st.radio("お弁当箱の形に合わせて選んでください:", ["スタンダード（横分け）", "対角線分け", "センターご飯（日の丸風）"])

    # --- 提案ロジック ---
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
        st.success("メニューが決まりました！次は配置を確認しましょう。")

        # --- 配置マップの表示 ---
        st.markdown("### 📍 配置ガイド（分布図）")
        
        if layout_type == "スタンダード（横分け）":
            st.code(f"""
            |---------------------------|
            |           ご飯            |
            |      ({p['rice']})       |
            |---------------------------|
            |  🔴1  |  🟢2  |  🟡3  |
            |  🥢4  |  🥢5  | 仕切 |
            |---------------------------|
            """, language="text")
        elif layout_type == "対角線分け":
            st.code(f"""
            |---------------------------|
            | ご飯 ({p['rice']})   / 🥢4 |
            |                   /  🥢5 |
            |------------------/  🟡3  |
            |  🔴1  /  🟢2  /---------|
            |---------------------------|
            """, language="text")
        else: # センターご飯
            st.code(f"""
            |---------------------------|
            |  🔴1  |   ご飯    |  🟢2  |
            |  🟡3  | ({p['rice']}) |  🥢4  |
            |  仕切 |           |  🥢5  |
            |---------------------------|
            """, language="text")

        st.info("💡 詰めるコツ：大きい「ご飯」と「おかず4・5（フリー）」から詰めると崩れません！")

        # --- メニュー表示とロック ---
        st.markdown("---")
        st.markdown("### 📝 献立リスト（ロック機能）")
        st.session_state.locks["rice"] = st.checkbox(f"🍚 ご飯: {p['rice']}", value=st.session_state.locks["rice"])
        
        keys = ["s1", "s2", "s3", "s4", "s5"]
        labels = ["🔴 おかず 1", "🟢 おかず 2", "🟡 おかず 3", "🥢 おかず 4", "🥢 おかず 5"]
        
        for i, key in enumerate(keys):
            st.session_state.locks[key] = st.checkbox(f"{labels[i]}: {p[key]}", value=st.session_state.locks[key])
        
        # 再検討・リセット
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🔄 未ロックを再検討"):
                if not st.session_state.locks["rice"]: st.session_state.proposal["rice"] = random.choice(rice_list)
                if not st.session_state.locks["s1"]: st.session_state.proposal["s1"] = random.choice(red_list)
                if not st.session_state.locks["s2"]: st.session_state.proposal["s2"] = random.choice(green_list)
                if not st.session_state.locks["s3"]: st.session_state.proposal["s3"] = random.choice(yellow_list)
                if not st.session_state.locks["s4"]: st.session_state.proposal["s4"] = random.choice(free_list)
                if not st.session_state.locks["s5"]: st.session_state.proposal["s5"] = random.choice(free_list)
                st.rerun()
        with col_btn2:
            if st.button("❌ 全部リセット"):
                st.session_state.proposal = None
                st.session_state.locks = {k: False for k in st.session_state.locks}
                st.rerun()

st.caption("Bento Vision - Visual Layout Guide Version")
