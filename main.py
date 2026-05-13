import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- アプリ設定 ---
st.set_page_config(page_title="M-Vision AI", layout="centered")
st.title("🀄 M-Vision AI点数計算")

# --- AIの設定 ---
if "GEMINI_API_KEY" not in st.secrets:
    st.error("APIキーがSecretsに設定されていません。")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# --- カメラ入力 ---
st.subheader("📸 牌を撮影してAI解析")
img_file = st.camera_input("手牌を撮影してください")

if img_file:
    # 画像を読み込んでリサイズ（高速化のため）
    img = Image.open(img_file)
    img.thumbnail((800, 800)) # サイズを小さくする
    
    st.image(img, caption="解析を開始します...")
    
    # 解析実行ボタン（自動実行ではなくボタン式にして安定させる）
    if st.button("AIで役を判定する", type="primary"):
        with st.spinner("AIが考え中... (10秒ほどお待ちください)"):
            prompt = "この画像にある麻雀の役とドラの数、符を教えてください。形式：【役】、ドラ【点】、符【点】"
            
            try:
                # 画像をバイトデータに変換して送信
                buf = io.BytesIO()
                img.save(buf, format='JPEG')
                image_data = buf.getvalue()
                
                response = model.generate_content([
                    prompt,
                    {'mime_type': 'image/jpeg', 'data': image_data}
                ])
                
                st.success("判定完了！")
                st.markdown(f"### 🤖 AIの回答\n{response.text}")
                
            except Exception as e:
                st.error(f"エラーが発生しました。時間を置いて再度お試しください。内容: {e}")

st.divider()
st.info("※判定が遅い場合は、一度アプリを再読み込みしてください。")
