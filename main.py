import streamlit as st
import time
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# デザイン（文字色を #2c3e50（濃いグレー）に固定）
st.markdown("""
    <style>
    .main { background-color: #fff9f0; }
    .result-box { 
        background-color: white; 
        padding: 25px; 
        border-radius: 15px; 
        border-left: 10px solid #ff9e1b; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.1); 
        margin-top: 20px;
        color: #2c3e50; 
    }
    h2, h3, p, div { color: #2c3e50 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🍱 Bento Vision")

# 状態管理
if 'proposal' not in st.session_state:
    st.session_state.proposal = None

uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    if st.session_state.proposal is None:
        if st.button("✨ 隙間埋めレシピを提案！"):
            with st.status("分析中...", expanded=True) as status:
                time.sleep(1.0)
                status.update(label="分析完了！", state="complete")
            st.session_state.proposal = random.choice(menu_options)
            st.rerun()
    else:
        # 結果表示
        p = st.session_state.proposal
        st.success("提案が完成しました！")
        
        st.markdown(f"""
        <div class="result-box">
            <h2 style="margin-top: 0;">{p['name']}</h2>
            <hr>
            <div style="font-size: 20px; line-height: 2;">
                🔴 赤のおかず：<b>{p['red']}</b><br>
                🟢 緑のおかず：<b>{p['green']}</b><br>
                🟡 黄のおかず：<b>{p['yellow']}</b>
            </div>
            <div style="background-color: #fff9f0; padding: 15px; border-radius: 10px; margin-top: 20px;">
                <p style="margin: 0;"><b>💡 詰め方のコツ:</b><br>{p['tip']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("🔄 もう一品提案して！"):
            st.session_state.proposal = random.choice(menu_options)
            st.rerun()
