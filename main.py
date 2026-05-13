import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- アプリ設定 ---
st.set_page_config(page_title="M-Vision AI", layout="centered")
st.title("🀄 M-Vision AI点数計算")

# --- AIの設定 ---
if "GEMINI_API_KEY" not in st.secrets:
    st.error("APIキーが設定されていません。")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
# 高速な1.5-flashモデルを使用
model = genai.GenerativeModel('gemini-1.5-flash')

# --- カメラ入力 ---
st.subheader("📸 牌を撮影")
img_file = st.camera_input("手牌を撮影してください")

if img_file:
    # 画像を極限まで軽量化（300pxまで縮小）
    img = Image.open(img_file)
    img.thumbnail((300, 300)) 
    
    st.image(img, caption="この画像をAIに送ります")
    
    if st.button("AI判定をリトライする", type="primary"):
        with st.spinner("通信中..."):
            try:
                # 命令（プロンプト）
                prompt = "麻雀の画像です。成立している役、ドラの数、符を教えて。"
                
                # AIに送信
                response = model.generate_content([prompt, img])
                
                if response.text:
                    st.success("AIが回答しました！")
                    st.write(response.text)
                else:
                    st.warning("AIから返答が空でした。もう一度お試しください。")
                    
            except Exception as e:
                st.error(f"接続エラー: {e}")
