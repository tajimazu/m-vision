import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# デザイン（CSS）で文字色とカードをオシャレに
st.markdown("""
    <style>
    .main { background-color: #fff9f0; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff9e1b; color: white; border: none; font-weight: bold; font-size: 18px; }
    .stButton>button:hover { background-color: #e68a00; border: none; }
    .result-card { background-color: white; padding: 25px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-top: 20px; }
    .result-card h3, .result-card p, .result-card li { color: #2C3E50 !important; }
    .food-img { width: 100%; border-radius: 15px; margin-top: 10px; margin-bottom: 15px; object-fit: cover; height: 200px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍱 Bento Vision")
st.subheader("お弁当箱の隙間を、美味しい写真で解決！")

# --- 1. お弁当箱の設定 ---
st.write("---")
st.write("### 1. お弁当箱のタイプ")
col1, col2 = st.columns(2)
with col1:
    box_shape = st.selectbox("形は？", ["四角（定番）", "丸・楕円（わっぱ等）", "スリムな2段", "丼タイプ"])
with col2:
    box_size = st.select_slider("サイズは？", options=["小さめ", "ふつう", "大きめ"])

# --- 2. 今日の気分 ---
st.write("### 2. 今日の気分は？")
mood = st.radio("", ["ガッツリ肉系！", "ヘルシー野菜多め", "1分で出来る超時短"], horizontal=True)

# --- 写真付きおかずデータの準備 ---
menu_data = {
    "ガッツリ肉系！": {
        "name": "ジューシー鶏のから揚げ ＆ ミニトマト",
        "img": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=600",
        "tip": "お弁当の主役！四角い弁当箱の角に、山を作るように立体的に積み上げると隙間が綺麗に埋まります。"
    },
    "ヘルシー野菜多め": {
        "name": "ブロッコリーと卵のごま和え（彩り満点）",
        "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600",
        "tip": "緑と黄色のグラデーションが最高。楕円形や丸型のお弁当箱なら、緩やかなカーブに沿って敷き詰めると美しいです。"
    },
    "1分で出来る超時短": {
        "name": "ちくわの磯辺焼き風 ＆ ぷちトマト",
        "img": "https://images.unsplash.com/photo-1582450871972-ab5ca641643d?w=600",
        "tip": "切って詰めるだけ！スリムな2段弁当の細長い隙間には、ちくわを縦に並べて入れるとピタッと収まります。"
    }
}

# --- 3. 提案実行 ---
st.write("---")
if st.button("✨ 写真で隙間埋めアイデアを見る！"):
    st.balloons()
    
    # ユーザーの気分に合わせたデータを取得
    selected = menu_data[mood]
    
    # 画面にリッチなカードを表示
    st.markdown(f"""
    <div class="result-card">
        <h3 style="border-bottom: 2px solid #ff9e1b; padding-bottom: 10px;">🌟 {box_shape}（{box_size}）へのおすすめ</h3>
        <p style="font-size: 20px; font-weight: bold; margin-top: 15px; color: #E67E22 !important;">
            ▶︎ {selected['name']}
        </p>
        <img src="{selected['img']}" class="food-img">
        <p style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; font-size: 15px; border-left: 5px solid #27AE60;">
            💡 <b>このお弁当箱への詰め方コツ:</b><br>{selected['tip']}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.caption("Bento Vision - Prototype v2 (Photo Display Version)")
