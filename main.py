import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- アプリ設定 ---
st.set_page_config(page_title="M-Vision AI", layout="centered")
st.title("🀄 M-Vision AI点数計算")

# --- AIの設定 (Secretsからキーを取得) ---
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("APIキーが設定されていません。StreamlitのSecretsを確認してください。")

# --- カメラ入力 ---
st.subheader("📸 牌を撮影してAI解析")
img_file = st.camera_input("手牌を撮影してください")

if img_file:
    img = Image.open(img_file)
    st.image(img, caption="解析中...")
    
    with st.spinner("AIが役を読み取っています..."):
        # AIへの指示（プロンプト）
        prompt = """
        この麻雀の牌の画像から、成立している「役」と「ドラの数」、「符」を推測して教えてください。
        回答は以下の形式で短く出力してください。
        【判定結果】
        役: 
        ドラ: 
        符: 
        """
        try:
            response = model.generate_content([prompt, img])
            st.success("AIの解析が完了しました！")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI解析中にエラーが発生しました: {e}")

st.divider()
st.info("※AIの判定は100%ではありません。必要に応じて下のボタンで修正してください。")

# --- 手動計算機能 (これまでの機能を維持) ---
st.sidebar.header("📋 手動調整")
# ... (必要に応じてここに以前のUIを追加)
