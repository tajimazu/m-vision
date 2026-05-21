import streamlit as st
import random

# ページの設定
st.set_page_config(page_title="Bento Vision", page_icon="🍱")

# 1. 全メニューリスト（名前とURLのセット）
# ※田島さんの指摘通り、梅干しはご飯リストへ、赤リストからは削除しています
rice_list = [
    {"name": "梅干しご飯", "url": "https://www.kurashiru.com/recipes/e89c0d12-3456-4789-a0b1-c2d3e4f56789"},
    {"name": "白ご飯", "url": "https://www.kurashiru.com/recipes/5c3577d6-3e4b-4b2e-a4b5-4b5745778844"},
    {"name": "わかめご飯", "url": "https://www.kurashiru.com/recipes/d337d121-657d-4171-85f2-53b05f69e6b4"},
    {"name": "炊き込みご飯", "url": "https://www.kurashiru.com/recipes/7b2e95a9-e85d-4f11-9252-012586b5b546"},
    {"name": "鮭フレークご飯", "url": "https://www.kurashiru.com/recipes/6e2b10a2-23c5-4d76-8f37-1845f34177b9"},
    {"name": "玄米ご飯", "url": "https://www.kurashiru.com/recipes/f69a5840-7539-44e2-9c43-159497e29463"},
    {"name": "雑穀米", "url": "https://www.kurashiru.com/recipes/6879e6f2-6b9c-4f1c-99c0-9a29a0b6339a"},
    {"name": "ゆかりご飯", "url": "https://www.kurashiru.com/recipes/c4b8b6a9-8f3d-4c3d-bd88-12c85b3a4a9d"},
    {"name": "炒飯", "url": "https://www.kurashiru.com/recipes/a32490d1-6784-4860-9189-e58f27364b63"},
    {"name": "塩昆布おにぎり", "url": "https://www.kurashiru.com/recipes/7d3a2b1c-9e8d-4c6b-95a4-321f0b987654"}
]

red_list = [
    {"name": "ミニトマト", "url": "https://www.kurashiru.com/recipes/a1b2c3d4-e5f6-4g7h-8i9j-k0l1m2n3o4p5"},
    {"name": "カニカマ", "url": "https://www.kurashiru.com/recipes/b2c3d4e5-f6g7-4h8i-9j0k-l1m2n3o4p5q6"},
    {"name": "タコさんウィンナー", "url": "https://www.kurashiru.com/recipes/d4e5f6g7-h8i9-4j0k-1l2m-n3o4p5q6r7s8"},
    {"name": "赤パプリカのマリネ", "url": "https://www.kurashiru.com/recipes/c3d4e5f6-g7h8-4i9j-0k1l-m2n3o4p5q6r7s8"},
    {"name": "しば漬け", "url": "https://www.kurashiru.com/recipes/e5f6g7h8-i9j0-4k1l-2m3n-o4p5q6r7s8t9"}
]

green_list = [
    {"name": "ブロッコリーの胡麻和え", "url": "https://www.kurashiru.com/recipes/f6g7h8i9-j0k1-4l2m-3n4o-p5q6r7s8t9u0"},
    {"name": "枝豆", "url": "https://www.kurashiru.com/recipes/g7h8i9j0-k1l2-4m3n-4o5p-q6r7s8t9u0v1"},
    {"name": "アスパラガスのお浸し", "url": "https://www.kurashiru.com/recipes/h8i9j0k1-l2m3-4n4o-5p6q-r7s8t9u0v1w2"},
    {"name": "ほうれん草のナムル", "url": "https://www.kurashiru.com/recipes/i9j0k1l2-m3n4-4o5p-6q7r-s8t9u0v1w2x3"},
    {"name": "ピーマンの塩昆布炒め", "url": "https://www.kurashiru.com/recipes/j0k1l2m3-n4o5-4p6q-7r8s-t9u0v1w2x3y4"}
]

yellow_list = [
    {"name": "卵焼き", "url": "https://www.kurashiru.com/recipes/k1l2m3n4-o5p6-4q7r-8s9t-u0v1w2x3y4z5"},
    {"name": "カボチャの煮物", "url": "https://www.kurashiru.com/recipes/l2m3n4o5-p6q7-4r8s-9t0u-v1w2x3y4z5a6"},
    {"name": "コーンバター", "url": "https://www.kurashiru.com/recipes/m3n4o5p6-q7r8-4s9t-0u1v-w2x3y4z5a6b7"},
    {"name": "うずらの煮卵", "url": "https://www.kurashiru.com/recipes/n4o5p6q7-r8s9-4t0u-1v2w-3x4y5z6a7b8c9"},
    {"name": "さつまいもの甘露煮", "url": "https://www.kurashiru.com/recipes/o5p6q7r8-s9t0-4u1v-2w3x-4y5z6a7b8c9d0"}
]

free_list = [
    {"name": "鶏の唐揚げ", "url": "https://www.kurashiru.com/recipes/53066d95-e2a2-466d-8874-884988775f0a"},
    {"name": "ハンバーグ", "url": "https://www.kurashiru.com/recipes/d61e6950-653a-441c-b710-bb2a4a796e63"},
    {"name": "焼き鮭", "url": "https://www.kurashiru.com/recipes/209c18d9-cf6a-466f-b25c-02cf4c3b53c1"},
    {"name": "豚肉の生姜焼き", "url": "https://www.kurashiru.com/recipes/a2327797-40b4-4e20-8025-5f99166f2868"},
    {"name": "ちくわの磯辺揚げ", "url": "https://www.kurashiru.com/recipes/10609341-9447-414e-b962-d99f4d38e217"},
    {"name": "コロッケ", "url": "https://www.kurashiru.com/recipes/7989938b-d79e-4c74-a3f2-140306c4b267"},
    {"name": "鯖の塩焼き", "url": "https://www.kurashiru.com/recipes/9a4891b2-263a-4933-912f-688849c7162b"},
    {"name": "肉団子", "url": "https://www.kurashiru.com/recipes/c735d487-73d6-4447-817e-727c95e1e93c"},
    {"name": "エビフライ", "url": "https://www.kurashiru.com/recipes/3b2c2e08-9642-45e0-9285-f3775f0f3531"},
    {"name": "トンカツ", "url": "https://www.kurashiru.com/recipes/e54e1a06-a94f-4d0f-a492-c43a6d9124
