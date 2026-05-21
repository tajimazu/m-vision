import streamlit as st

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# デザイン（CSS）
st.markdown("""
    <style>
    .main { background-color: #fff9f0; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff9e1b; color: white; border: none; font-weight: bold; font-size: 18px; }
    .stButton>button:hover { background-color: #e68a00; border: none; }
    .result-card { background-color: white; padding: 25px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-top: 20px; }
    .result-card h3, .result-card p, .result-card li { color: #2C3E50 !important; }
    .food-img { width: 100%; border-radius: 15px; margin-top: 10px; margin-bottom: 15px; object-fit: cover; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍱 Bento Vision")
st.subheader("お弁当箱の隙間を、理想の写真で解決！")

# --- 1. お弁当箱の設定 ---
st.write("---")
st.write("### 1. お弁当箱のタイプ")
col1, col2 = st.columns(2)
with col1:
    # 選択肢を「楕円形」にきっちり修正！
    box_shape = st.selectbox("形は？", ["楕円形（わっぱ等）", "四角（定番）", "スリムな2段", "丼タイプ"])
with col2:
    box_size = st.select_slider("サイズは？", options=["小さめ", "ふつう", "大きめ"])

# --- 2. 今日の気分 ---
st.write("### 2. 今日の気分は？")
mood = st.radio("", ["彩りヘルシー（鮭・ブロッコリー）", "ガッツリ肉系！", "1分で出来る超時短"], horizontal=True)

# --- 気分に合わせた写真データ ---
menu_data = {
    "彩りヘルシー（鮭・ブロッコリー）": {
        "name": "特選！楕円わっぱの彩り鮭弁当",
        "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800",
        "text": "🔴 赤：焼き鮭のほぐし身\n🟢 緑：ブロッコリーのごま和え\n🟡 黄：ふっくら卵焼き",
        "tip": "楕円形のお弁当箱は、長い方の直線を活かしておかずを「縦一列」に並べるか、ご飯を斜めに敷き詰めてそのカーブに沿わせるように詰めると、隙間がピタッと埋まります！"
    },
    "ガッツリ肉系！": {
        "name": "お弁当のための「鶏のから揚げ弁当」",
        "img": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=800",
        "text": "🔴 赤：ミニトマト\n🟢 緑：えだまめピック\n🟡 黄：コーンバター",
        "tip": "四角いお弁当箱の角（デッドスペース）には、まず形が崩れない卵焼きをハメ込み、空いた中央にから揚げを山型に積み上げると綺麗に埋まります！"
    },
    "1分で出来る超時短": {
        "name": "王道スタミナ！豚の生姜焼き弁当",
        "img": "https://images.unsplash.com/photo-1621360841013-c7683c659ec6?w=800",
        "text": "🔴 赤：梅干し\n🟢 緑：千切りキャベツ\n🟡 黄：ポテトサラダ",
        "tip": "生姜焼きのような汁気のあるおかずは、千切りキャベツをクッションにして乗せると、タレを吸って隙間も埋まり一石二鳥です！"
    }
}

# --- 3. 提案実行 ---
st.write("---")
if st.button("✨ 理想のお弁当アイデアを表示する！"):
    st.balloons()
    
    selected = menu_data[mood]
    
    st.markdown(f"""
    <div class="result-card">
        <h3 style="border-bottom: 2px solid #ff9e1b; padding-bottom: 10px;">🌟 {box_shape}（{box_size}）への提案</h3>
        <p style="font-size: 22px; font-weight: bold; margin-top: 15px; color: #E67E22 !important;">
            【{selected['name']}】
        </p>
        <img src="{selected['img']}" class="food-img">
        <p><b>🔍 おすすめの隙間埋め食材:</b></p>
        <p style="white-space: pre-wrap; font-size: 16px; background-color: #fafafa; padding: 10px; border-radius: 5px;">{selected['text']}</p>
        <p style="background-color: #fff5e6; padding: 15px; border-radius: 10px; font-size: 15px; border-left: 5px solid #ff9e1b; margin-top: 15px;">
            💡 <b>このお弁当箱への詰め方コツ:</b><br>{selected['tip']}
        </p>
    </div>
    """, unsafe_allow_html=True)

st
