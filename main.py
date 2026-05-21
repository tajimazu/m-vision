import streamlit as st
import time

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# デザイン（CSS）
st.markdown("""
    <style>
    .main { background-color: #fff9f0; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3.5em; background-color: #ff9e1b; color: white; border: none; font-weight: bold; font-size: 18px; }
    .stButton>button:hover { background-color: #e68a00; border: none; }
    .result-card { background-color: white !important; padding: 25px; border-radius: 15px; border: 2px solid #ff9e1b; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-top: 20px; }
    .result-card h3, .result-card p, .result-card li { color: #2c3e50 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍱 Bento Vision")
st.subheader("お弁当箱を分析してレシピを提案")

# セッション状態の初期化（結果を消さないための記憶装置）
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False

# --- 1. カメラ撮影 ---
st.write("---")
st.write("### 📸 お弁当箱（空でもOK）を撮影")

# 外カメ(environment)を優先。もし内カメになったらスマホのカメラ切り替えボタンを触ってみてください
uploaded_file = st.camera_input("カメラを起動", camera_facing="environment")

# 写真が撮れたら
if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    # 2. レシピ考案スタートボタン
    if st.button("✨ おすすめ弁当レシピを考案スタート！"):
        
        # 3. 解析・分析の演出
        with st.status("AIによる画像分析中...", expanded=True) as status:
            st.write("箱の形状とサイズを測定しています...")
            time.sleep(1.5)
            st.write("空きスペースに最適な彩りを計算中...")
            time.sleep(1.5)
            st.write("栄養バランスを考慮したレシピを構築中...")
            time.sleep(1.5)
            status.update(label="分析完了！", state="complete", expanded=False)
        
        # 分析完了フラグをオンにする
        st.session_state.analysis_done = True

# 4. 分析結果の表示（フラグがオンの時だけ表示され続ける）
if st.session_state.analysis_done:
    st.success("🍱 あなたにぴったりのレシピが完成しました！")
    
    st.markdown(f"""
    <div class="result-card">
        <h3 style="text-align: center; margin-bottom: 20px;">🌟 おすすめ弁当レシピ 🌟</h3>
        
        <p><b>【メインの構成】</b></p>
        <p>撮影した箱の形に合わせて、以下の3点を配置するのがベストです。</p>
        
        <ul>
            <li>🔴 <b>彩りトマトとパプリカ：</b>右上のコーナーに固めて配置すると、全体が引き締まります。</li>
            <li>🟢 <b>ブロッコリーの胡麻和え：</b>メインおかずの横に敷き詰め、隙間を完全にガード。</li>
            <li>🟡 <b>だし巻き卵（厚切り）：</b>箱の高さに合わせて縦に詰めると、ボリューム感が出ます。</li>
        </ul>
        
        <div style="background-color: #fff5e6; padding: 15px; border-radius: 10px; margin-top: 15px;">
            <p style="margin: 0;"><b>💡 ワンポイントアドバイス:</b><br>
            空きスペースの形から、今日のあなたは「少し柔らかめのおかず」を隙間に詰めると、お昼に開けた時の崩れが防げますよ！</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # リセットボタン（もう一度撮り直したい場合）
    if st.button("🔄 もう一度分析する"):
        st.session_state.analysis_done = False
        st.rerun()
    
    st.balloons()

st.write("---")
st.caption("Bento Vision - Phase 2.3 (Persistent Result Version)")

### 🏃‍♂️ 最後に
GitHubの `main.py` を上書きして保存（Commit）したら、スマホでリロードしてください。
1. カメラを起動して撮影。
2. オレンジ色の「考案スタート！」ボタンを押す。
3. 演出が終わると、その下にドカーンとレシピカードが表示されます。

今度こそ、分析結果が逃げ出さずにしっかり残るはずです！試してみてくださいね。

レシピ提案アプリとしての第一歩が完成しました！いかがでしょうか？
