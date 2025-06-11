import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="💫 아이돌 멤버 소속 그룹 찾기",
    page_icon="🌟",
    layout="centered"
)

# 🎀 타이틀
st.markdown("<h1 style='text-align:center; color:#ff66c4;'>🌈 아이돌 멤버 → 소속 그룹 찾기 🎶</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#5f0f40;'>멤버 이름을 입력하면 소속된 그룹을 알려드려요! ✨</h4>", unsafe_allow_html=True)
st.markdown("---")

# 멤버-그룹 매핑
idol_members = {
    # BTS
    "정국": ["BTS"],
    "뷔": ["BTS"],
    "지민": ["BTS"],
    "RM": ["BTS"],
    "진": ["BTS"],
    "슈가": ["BTS"],
    "제이홉": ["BTS"],
    
    # BLACKPINK
    "제니": ["BLACKPINK"],
    "지수": ["BLACKPINK"],
    "로제": ["BLACKPINK"],
    "리사": ["BLACKPINK"],

    # TWICE
    "나연": ["TWICE"],
    "정연": ["TWICE"],
    "모모": ["TWICE"],
    "사나": ["TWICE"],
    "지효": ["TWICE"],
    "미나": ["TWICE"],
    "다현": ["TWICE"],
    "채영": ["TWICE"],
    "쯔위": ["TWICE"],

    # IVE
    "장원영": ["IVE"],
    "안유진": ["IVE"],
    "레이": ["IVE"],
    "가을": ["IVE"],
    "리즈": ["IVE"],
    "이서": ["IVE"],

    # NEWJEANS
    "민지": ["NEWJEANS"],
    "하니": ["NEWJEANS"],
    "다니엘": ["NEWJEANS"],
    "해린": ["NEWJEANS"],
    "혜인": ["NEWJEANS"],

    # LE SSERAFIM
    "사쿠라": ["LE SSERAFIM", "IZ*ONE"],
    "김채원": ["LE SSERAFIM", "IZ*ONE"],
    "허윤진": ["LE SSERAFIM"],
    "카즈하": ["LE SSERAFIM"],
    "홍은채": ["LE SSERAFIM"],

    # BOYNEXTDOOR (보넥)
    "성호": ["BOYNEXTDOOR"],
    "리우": ["BOYNEXTDOOR"],
    "재현": ["BOYNEXTDOOR"],
    "태산": ["BOYNEXTDOOR"],
    "이한": ["BOYNEXTDOOR"],
    "운학": ["BOYNEXTDOOR"]
}

# 사용자 입력
member_input = st.text_input("🧑‍🎤 아이돌 멤버 이름을 입력해 보세요!", placeholder="예: 정국, 장원영, 성호")

# 색상 팔레트
color_palette = ["#ffafcc", "#a2d2ff", "#cdb4db", "#ffc8dd", "#fbc4ab", "#b5ead7", "#d0f4de"]

# 결과 출력
if member_input:
    name = member_input.strip()
    if name in idol_members:
        groups = idol_members[name]
        st.markdown(f"<h2 style='color:#f72585;'>💖 {name}님의 소속 그룹은?</h2>", unsafe_allow_html=True)

        for group in groups:
            color = random.choice(color_palette)
            st.markdown(
                f"<div style='background-color:{color}; padding:15px; border-radius:12px; text-align:center; color:white; font-size:24px; margin:10px 0;'>🎤 {group}</div>",
                unsafe_allow_html=True
            )
    else:
        st.warning("😥 죄송해요! 해당 멤버 정보를 찾을 수 없어요. 정확히 입력해 주세요.")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Made with 💜 for K-POP Fans by ChatGPT</p>", unsafe_allow_html=True)

