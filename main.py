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
st.subheader("お弁当箱の『形』に合わせた理想の提案")

# --- 1. お弁当箱の設定 ---
st.write("---")
st.write("### 1. お弁当箱の正確な形を選んでください")

box_shape = st.selectbox("お弁当箱の形は？", [
    "楕円形（細長いわっぱ等）", 
    "真円形（まん丸・どんぶり型）", 
    "四角形（定番プラスチック）", 
    "スリムな2段弁当"
])

box_size = st.select_slider("サイズ（容量）の目安", options=["小さめ", "ふつう", "大きめ"])

# --- 2. 今日のメニュー ---
st.write("### 2. 今日のメニューの気分は？")
mood = st.radio("", ["彩りヘルシー（鮭・ブロッコリー）", "ガッツリ肉系（から揚げ）"], horizontal=True)

# --- 完全に形を固定した理想の画像URL ---
# 楕円形には、先ほどの「理想の木製わっぱの楕円写真」をダイレクトに指定しました！
wappa_oval_image = "https://images.unsplash.com/photo-1621360841013-c7683c659ec6?w=800"

menu_data = {
    "楕円形（細長いわっぱ等）": {
        "彩りヘルシー（鮭・ブロッコリー）": {
            "name": "特選！あじわい楕円わっぱ鮭弁当",
            "img": wappa_oval_image, 
            "text": "🔴 赤：焼き鮭のほぐし身（中央にたっぷり）\n🟢 緑：ブロッコリーのごま和え（右側のカーブに沿って）\n🟡 黄：ふっくら卵焼き（隙間にジャストフィット）",
            "tip": "楕円形（わっぱ）は、長い直線のラインを活かして、おかずを『斜め』または『縦一列』に並べるのがコツです。これにより、丸型のような無駄なデッドスペースが生まれず、隙間がピタッと埋まります！"
        },
        "ガッツリ肉系（から揚げ）": {
            "name": "楕円に敷き詰めるジューシーから揚げ弁当",
            "img": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=800",
            "text": "🔴 赤：ミニトマト\n🟢 緑：ブロッコリー\n🟡 黄：卵焼き",
            "tip": "楕円の丸い両端に卵焼きとブロッコリーを配置し、中央の広いスペースにメインのから揚げをご飯の上に乗せるように詰めると綺麗に収まります。"
        }
    }
}

# 予備の共通データ
default_proposal = {
    "name": "定番！お弁当配置案",
    "img": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=800",
    "text": "🔴 赤：ミニトマト\n🟢 緑：ブロッコリー\n🟡 黄：卵焼き",
    "tip": "お弁当箱の四隅やカーブに合わせて、形が崩れない卵焼きを最初にはめ込むと、隙間が絶対に生まれません！"
}

# --- 3. 提案実行 ---
st.write("---")
if st.button("✨ この形に最適な隙間埋めアイデアを表示！"):
    st.balloons()
    
    # データの取得
    if box_shape in menu_data and mood in menu_data[box_shape]:
        selected = menu_data[box_shape][mood]
    else:
        selected = default_proposal
        
    # 楕円形が選ばれたら、100%確実にあの「わっぱの楕円写真」を表示します
    if "楕円形" in box_shape:
        final_img = wappa_oval_image
    else:
        final_img = selected['img']

    st.markdown(f"""
    <div class="result-card">
        <h3 style="border-bottom: 2px solid #ff9e1b; padding-bottom: 10px;">🌟 {box_shape}専用の解決策</h3>
        <p style="font-size: 22px; font-weight: bold; margin-top: 15px; color: #E67E22 !important;">
            【{selected['name']}】
        </p>
        <img src="{final_img}" class="food-img">
        <p><b>🔍 おすすめの配置と食材:</b></p>
        <p style="white-space: pre-wrap; font-size: 16px; background-color: #fafafa; padding: 10px; border-radius: 5px;">{selected['text']}</p>
        <p style="background-color: #fff5e6; padding: 15px; border-radius: 10px; font-size: 15px; border-left: 5px solid #ff9e1b; margin-top: 15px;">
            💡 <b>この形だからこそ活きる詰め方:</b><br>{selected['tip']}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.caption("Bento Vision - Precision Shape Edition v4")
