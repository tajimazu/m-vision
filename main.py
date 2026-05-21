import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision Prototype", page_icon="🍱")

# デザイン（CSS）
st.markdown("""
    <style>
    .main { background-color: #fff9f0; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff9e1b; color: white; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #e68a00; border: none; }
    .result-card { background-color: white; padding: 20px; border-radius: 15px; border-left: 10px solid #ff9e1b; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    /* 文字の色を黒に固定 */
    .result-card h3, .result-card p, .result-card li { color: black !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍱 Bento Vision")
st.subheader("お弁当箱の隙間、AIが解決します")

# --- ステップ1: 弁当箱の設定 ---
st.write("---")
st.write("### 1. お弁当箱を選んでください")
col1, col2 = st.columns(2)
with col1:
    box_shape = st.selectbox("形は？", ["四角（定番）", "丸・楕円（わっぱ等）", "スリムな2段", "丼タイプ"])
with col2:
    box_size = st.select_slider("サイズは？", options=["小さめ", "ふつう", "大きめ"])

# --- ステップ2: 今日の気分 ---
st.write("### 2. 今日の気分は？")
mood = st.radio("", ["ガッツリ食べたい！", "ヘルシーにまとめたい", "とにかく時短（3分以内！）"], horizontal=True)

# --- おかずデータの準備（Phase 1用） ---
side_dishes = {
    "red": ["ミニトマト", "カニカマ", "赤パプリカのマリネ", "ラディッシュ"],
    "green": ["ブロッコリー", "枝豆ピック", "ほうれん草のナムル", "アスパラ"],
    "yellow": ["卵焼き", "コーンバター", "さつまいもの甘露煮", "うずら卵"],
    "tips": {
        "四角（定番）": "角の隙間には形が崩れにくい「卵焼き」や「ちくわ」がおすすめ！",
        "丸・楕円（わっぱ等）": "中心から放射状におかずを並べると、プロ級の仕上がりに。",
        "スリムな2段": "深さを活かして、縦長のおかず（アスパラやスティック野菜）を立てて詰めましょう。",
        "丼タイプ": "ご飯の上にドカッとメインを乗せて、周りに彩りを散らして！"
    }
}

# --- ステップ3: 提案実行 ---
st.write("---")
if st.button("✨ ピッタリな隙間埋め案を表示！"):
    st.balloons()
    
    # 提案ロジック
    dish_red = random.choice(side_dishes["red"])
    dish_green = random.choice(side_dishes["green"])
    dish_yellow = random.choice(side_dishes["yellow"])
    tip = side_dishes["tips"][box_shape]
    
    # 巨大化したアイコンと文字色の修正
    st.markdown(f"""
    <div class="result-card">
        <div style="text-align: center; margin-bottom: 20px;">
            <p style="font-size: 120px; margin: 0; line-height: 1;">🍱</p>
            <h3>{box_shape}（{box_size}）への提案</h3>
        </div>
        <p><strong>【おすすめの隙間埋め3点セット】</strong></p>
        <ul>
            <li>🔴 <b>{dish_red}</b></li>
            <li>🟢 <b>{dish_green}</b></li>
            <li>🟡 <b>{dish_yellow}</b></li>
        </ul>
        <p style="margin-top:15px; color:#666 !important;">💡 <b>詰め方のコツ:</b><br>{tip}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info(f"💡 {mood}のあなたには、メインのおかずの横に「{dish_green}」を多めに敷き詰めると満足度が上がりますよ！")

st.write("---")
st.caption("Phase 1: Logic Test Version. 次のPhase 2では「写真解析機能」を搭載予定です。")
