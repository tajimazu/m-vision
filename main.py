import streamlit as st
import time
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# おかずのパーツリスト（ここを自由に書き換えて、お気に入りのおかずを増やしてください！）
red_list = [
    "ミニトマト", "カニカマ", "赤パプリカ", "ラディッシュ", "赤ウインナー", 
    "梅干し", "揚げミニトマト", "しば漬け", "明太子", "タコさんウィンナー"
]
green_list = [
    "ブロッコリー", "枝豆", "アスパラガス", "ほうれん草のナムル", "ピーマンの炒め物", 
    "きゅうりの浅漬け", "スナップエンドウ", "インゲンの胡麻和え", "小松菜のおひたし", "オクラ"
]
yellow_list = [
    "卵焼き", "コーンバター", "うずらの煮卵", "さつまいもの甘露煮", "カレー炒り卵", 
    "パプリカソテー", "さつまいもチップス", "チーズウインナー", "カボチャの煮物", "厚焼き玉子"
]

st.title("🍱 Bento Vision")

# 状態管理
if 'proposal' not in st.session_state:
    st.session_state.proposal = None

# 写真アップロード
uploaded_file = st.file_uploader("お弁当箱の写真をアップロード", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    # 提案ボタンの制御
    if st.session_state.proposal is None:
        if st.button("✨ 今日のお弁当プランを提案"):
            with st.status("分析中...", expanded=True) as status:
                time.sleep(1.0)
                status.update(label="完了！", state="complete")
            
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
            <h2 style="color: #ff9e1b; margin-top: 0;">今日のお弁当プラン</h2>
            <hr>
            <div style="font-size: 20px; line-height: 2; color: #555;">
                🔴 赤のおかず：<b style="color: black;">{p['red']}</b><br>
                🟢 緑のおかず：<b style="color: black;">{p['green']}</b><br>
                🟡 黄のおかず：<b style="color: black;">{p['yellow']}</b>
            </div>
            <div style="background-color: #fff9f0; padding: 15px; border-radius: 10px; margin-top: 20px; color: #555;">
                <p style="margin: 0;"><b>💡 ワンポイントアドバイス:</b><br>
                彩り豊かな3色のおかずが揃いました！今日のお弁当は完璧な仕上がりになりますよ。</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("🔄 別のプランを考える"):
            st.session_state.proposal = {
                "red": random.choice(red_list),
                "green": random.choice(green_list),
                "yellow": random.choice(yellow_list)
            }
            st.rerun()

st.caption("Bento Vision - Bento Plan Version")
