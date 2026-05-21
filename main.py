import streamlit as st
import time

# ページ設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

st.title("🍱 Bento Vision")
st.write("お弁当箱を撮影してレシピを生成")

# カメラ起動
uploaded_file = st.camera_input("カメラを起動")

# 写真が撮れたあとの処理
if uploaded_file is not None:
    st.image(uploaded_file, caption="撮影したお弁当箱", use_container_width=True)
    
    if st.button("✨ おすすめ弁当レシピを表示"):
        # 解析演出
        with st.status("分析中...", expanded=True) as status:
            time.sleep(2)
            status.update(label="解析完了！", state="complete")
        
        # レシピ表示
        st.subheader("🌟 おすすめ弁当レシピ")
        st.info("今日の詰め方提案")
        st.write("1. **メイン：**焼き鮭のほぐし身（中央に配置）")
        st.write("2. **副菜：**ブロッコリーの胡麻和え（隙間埋めに最適）")
        st.write("3. **彩り：**だし巻き卵（黄色を添えてバランスアップ）")
        
        st.balloons()
