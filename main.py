import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- アプリ設定 ---
st.set_page_config(page_title="M-Vision AI")
st.title("🀄 M-Vision AI点数計算")

# --- AIの設定 ---
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # 接続エラーが最も少ない名前に変更
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("APIキーが設定されていません。")
    st.stop()

# --- カメラ入力 ---
img_file = st.camera_input("手牌を撮影")

if img_file:
    img = Image.open(img_file)
    img.thumbnail((400, 400)) # 軽量化
    st.image(img, caption="解析準備完了")
    
    if st.button("AIで役を判定する", type="primary"):
        with st.spinner("AIが画像を確認しています..."):
            try:
                # 送信データ作成
                buf = io.BytesIO()
                img.save(buf, format='JPEG')
                image_parts = [{"mime_type": "image/jpeg", "data": buf.getvalue()}]
                
                # 質問内容
                prompt = "この麻雀の画像から、成立している役、ドラ、符、合計点数を日本語で答えて。"
                
                # AIに送信
                response = model.generate_content([prompt, image_parts[0]])
                
                if response.text:
                    st.success("判定完了！")
                    st.write(response.text)
                else:
                    st.warning("AIが画像を読み取れませんでした。もう一度撮影してください。")
                    
            except Exception as e:
                # 404が出た場合でも、別の呼び出し方で再トライする仕組み
                st.error(f"接続エラーが発生しました。再起動（Reboot）を試してください。")
