import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# おかずのパーツリスト（ここを増やせば増やすほど組み合わせが無限になります！）
red_list = ["ミニトマト", "カニカマ", "赤パプリカ", "ラディッシュ", "赤ウインナー", "梅干し", "揚げミニトマト"]
green_list = ["ブロッコリー", "枝豆", "アスパラガス", "ほうれん草のナムル", "ピーマンの炒め物", "きゅうりの浅漬け", "スナップエンドウ"]
yellow_list = ["卵焼き", "コーンバター", "うずらの煮卵", "さつまいもの甘露煮", "カレー炒り卵", "パプリカソテー", "さつまいもチップス"]

st.title("🍱 Bento Vision")

# 状態管理
if 'proposal' not in st.session_state:
    st.session_state.proposal = None

uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    # 提案ボタン
    if st.session_state.proposal is None:
        if st.button("✨ 今日のおかずを組み合わせる"):
            # 各色から1つずつ選ぶ
            st.session_state.proposal = {
                "red": random.choice(red_list),
                "green": random.choice(green_list),
                "yellow": random.choice(yellow_list)
            }
            st.rerun()
    else:
        # 結果表示
        p = st.session_state.proposal
        st.success("提案が完成しました！")
        
        st.markdown(f"""
        <div style="background-color: white; padding: 25px; border-radius: 15px; border-left: 10px solid #ff9e1b; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            <h2 style="color: #ff9e1b; margin-top: 0;">今日のおすすめ隙間埋め</h2>
            <hr>
            <div style="font-size: 20px; line-height: 2;">
                🔴 赤のおかず：<b style="color: black;">{p['red']}</b><br>
                🟢 緑のおかず：<b style="color: black;">{p['green']}</b><br>
                🟡 黄のおかず：<b style="color: black;">{p['yellow']}</b>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("🔄 もう一回組み合わせる"):
            st.session_state.proposal = {
                "red": random.choice(red_list),
                "green": random.choice(green_list),
                "yellow": random.choice(yellow_list)
            }
            st.rerun()
