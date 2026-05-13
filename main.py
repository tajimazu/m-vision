import streamlit as st

# アプリのタイトル
st.title("🀄 M-Vision 点数計算")

# --- サイドバー：基本設定 ---
st.sidebar.header("基本設定")
is_parent = st.sidebar.radio("あなたの立場", ["子", "親"]) == "親"
win_type = st.sidebar.radio("アガリ方", ["ロン", "ツモ", "流局"])
naki = st.sidebar.checkbox("鳴き（副露）あり")

# --- メイン画面：役とドラの選択 ---
st.subheader("1. 役とドラを選択")
dora = st.number_input("ドラ・赤ドラ合計", min_value=0, max_value=13, value=0)

yaku_list = [
    '立直', '一発', '門前清自模和', '断幺九', '平和', '一盃口', '役牌', '七対子', 
    '三色同順', '一気通貫', '混一色', '清一色', '国士無双', '大三元', '四暗刻'
]
selected_yaku = st.multiselect("成立した役を選んでください", yaku_list)

# --- 2. 符と本場の設定 ---
st.subheader("2. 詳細設定")
col1, col2 = st.columns(2)
with col1:
    fu = st.selectbox("符", [20, 25, 30, 40, 50, 60, 70], index=2)
with col2:
    honba = st.number_input("本場", min_value=0, value=0)

# --- 3. 計算実行 ---
if st.button("点数を計算する", type="primary"):
    # ※ここにこれまでの計算ロジックを入れる
    # 計算結果を表示
    st.divider()
    st.header(f"💰 合計： 12600 点")
    st.info(f"内訳： {' + '.join(selected_yaku)} + ドラ({dora})")
