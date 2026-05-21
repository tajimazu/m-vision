import streamlit as st
import random

# （リストは省略していますが、前回のものがそのまま使えます）
# ... (前回の rice_list, red_list, green_list, yellow_list, free_list をここに配置)

st.title("🍱 Bento Vision - カスタム配置モード")

# 提案データをセッションに保持
if 'proposal' not in st.session_state:
    st.session_state.proposal = None

if st.button("✨ 今日のお弁当プランを生成"):
    st.session_state.proposal = {
        "rice": "ご飯",
        "s1": "赤：おかず1", "s2": "緑：おかず2", "s3": "黄：おかず3", "s4": "フリー4", "s5": "フリー5"
    }

if st.session_state.proposal:
    p = st.session_state.proposal
    
    # 田島さんの写真に合わせたレイアウトを表示
    st.markdown("### 🍱 あなたのお弁当箱への配置ガイド")
    
    # 視覚的な配置マップの描画
    st.code(f"""
    【お弁当箱 配置イメージ】
    +-----------------------------+
    |           |       ①        |
    |   ご飯    |---------------|
    |           |       ②        |
    |-----------+---------------|
    |     ⑤     |   ④  |   ③   |
    +-----------------------------+
    """, language="text")
    
    st.write(f"1. **🔴 おかず1**: {p['s1']}")
    st.write(f"2. **🟢 おかず2**: {p['s2']}")
    st.write(f"3. **🟡 おかず3**: {p['s3']}")
    st.write(f"4. **🥢 おかず4**: {p['s4']}")
    st.write(f"5. **🥢 おかず5**: {p['s5']}")
    
    st.info("💡 写真の仕切りに合わせて、この順番で詰めてみてください！")
