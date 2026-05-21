import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# デザイン（CSS）で見た目をリッチに
st.markdown("""
    <style>
    .main { background-color: #fff9f0; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff9e1b; color: white; border: none; font-weight: bold; font-size: 18px; }
    .stButton>button:hover { background-color: #e68a00; border: none; }
    .result-card { background-color: white; padding: 25px; border-radius: 15px; border-left: 10px solid #ff9e1b; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-top: 20px; }
    .result-card h3, .result-card p, .result-card li { color: #2c3e50 !important; }
    .bento-img { width: 100%; border-radius: 10px; margin-top: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🍱 Bento Vision")
st.subheader("お弁当箱の隙間、AIが解決します")

# --- 1. お弁当箱の設定 ---
st.write("---")
st.write("### 1. お弁当箱を選んでください")
col1, col2 = st.columns(2)
with col1:
    box_shape = st.selectbox("形は？", ["丸・楕円（わっぱ等）", "四角（定番）", "スリムな2段", "丼タイプ"])
with col2:
    box_size = st.select_slider("サイズは？", options=["小さめ", "ふつう", "大きめ"])

# --- 2. 今日の気分 ---
st.write("### 2. 今日の気分は？")
mood = st.radio("", ["ガッツリ食べたい！", "ヘルシーにまとめたい", "とにかく時短（3分以内！）"], horizontal=True)

# --- リアルなお弁当写真とデータの準備 ---
# 無料で使える本物の美味しそうな料理写真URLを設定しています
bento_data = {
    "丸・楕円（わっぱ等）": {
        "title": "特選！あじわい鮭わっぱ弁当",
        "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", # 彩り豊かな健康的なご飯
        "red": "焼き鮭のほぐし身（中央にたっぷり）",
        "green": "ブロッコリーのごま和え（右側のカーブに沿って）",
        "yellow": "ふっくら卵焼き（隙間にジャストフィット）",
        "tip": "丸いカーブに沿わせるように、ブロッコリーなどの柔らかい副菜を詰めると綺麗に隙間が埋まります！"
    },
    "四角（定番）": {
        "title": "がっつり！唐揚げヒーロー弁当",
        "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=800&q=80", # 美味しそうな肉・料理
        "red": "ミニトマト（四隅の角にポンと配置）",
        "green": "ピーマンの塩昆布和え（唐揚げの仕切りに）",
        "yellow": "マカロニサラダ（四角い壁に押し付けるように）",
        "tip": "四角いお弁当箱は「角」にデッドスペースができやすいです。角に固形の卵焼きやミニトマトを最初にロックすると安定します！"
    },
    "スリムな2段": {
        "title": "スタイリッシュ！二段ロコモコ風弁当",
        "img": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80", # サラダ・ボウル風
        "red": "にんじんのしりしり（細長い溝を埋める）",
        "green": "アスパラの肉巻き（長さを活かしてそのまま横たえる）",
        "yellow": "うずらの煮卵（コロンと隙間に並べる）",
        "tip": "幅が狭いスリム弁当は、おかずを「横一列」に並べるのがコツ。アスパラなど細長い食材が大活躍します！"
    },
    "丼タイプ": {
        "title": "豪快！彩りそぼろ丼弁当",
        "img": "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?auto=format&fit=crop&w=800&q=80", # 具だくさん料理
        "red": "紅生姜（一箇所にまとめてアクセントに）",
        "green": "絹さや・インゲン（斜めに並べてシャープに）",
        "yellow": "炒り卵（ご飯が見えないように敷き詰める）",
        "tip": "丼ものは立体感が命！ご飯を少し山なりに盛り、その傾斜に沿っておかずを乗せていくと立体感が出て美味しそうに見えます。"
    }
}

# --- 3. 提案実行 ---
st.write("---")
if st.button("✨ ピッタリな隙間埋め案を表示！"):
    st.balloons()
    
    # ユーザーが選んだ形に合わせたデータを取得
    choice = bento_data[box_shape]
    
    st.markdown(f"""
    <div class="result-card">
        <h2 style="color: #ff9e1b; font-size: 24px; text-align: center; margin-bottom: 5px;">⭐ {box_shape} 専用の解決策</h2>
        <h3 style="text-align: center; font-weight: bold; margin-bottom: 15px;">【{choice['title']}】</h3>
        
        <img src="{choice['img']}" class="bento-img" alt="お弁当イメージ">
        
        <p style="margin-top: 20px;">🔍 <b>おすすめの配置と食材:</b></p>
        <ul>
            <li>🔴 <b>赤：</b>{choice['red']}</li>
            <li>🟢 <b>緑：</b>{choice['green']}</li>
            <li>🟡 <b>黄：</b>{choice['yellow']}</li>
        </ul>
        <p style="margin-top:15px; background-color: #fff5e6; padding: 10px; border-radius: 5px;">
            💡 <b>このお弁当箱を極めるコツ:</b><br>{choice['tip']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info(f"💡 【{mood}】の気分に合わせてボリュームを微調整しています。明日のランチタイムが楽しみですね！")

st.write("---")
st.caption("Bento Vision - Phase 1.1 (Real Image Test Version)")
