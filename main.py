import streamlit as st
from PIL import Image
import random

# 🎨 Streamlit 페이지 설정
st.set_page_config(
    page_title="✨MBTI 진로 추천기✨",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 🖼️ 헤더 이미지 또는 이모지 타이틀
st.markdown("<h1 style='text-align: center; color: #ff66c4;'>🌈 MBTI로 알아보는 나의 직업 추천 💼</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>당신의 성격 유형에 딱 맞는 진로를 찾아보세요! 🧭</h3>", unsafe_allow_html=True)
st.markdown("---")

# 🌟 MBTI 유형 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 💼 MBTI별 직업 추천 데이터
job_recommendations = {
    "ISTJ": ["👮 경찰", "📊 회계사", "🏛️ 행정직 공무원"],
    "ISFJ": ["🩺 간호사", "👩‍🏫 초등학교 교사", "🧾 사회복지사"],
    "INFJ": ["🎨 심리상담가", "✍️ 작가", "📚 인문학자"],
    "INTJ": ["🧠 전략 컨설턴트", "💻 데이터 과학자", "🧪 연구원"],
    "ISTP": ["🛠️ 기계공학자", "🚗 자동차 정비사", "🔧 기술 분석가"],
    "ISFP": ["🎨 디자이너", "🎭 예술가", "📸 포토그래퍼"],
    "INFP": ["📖 시인", "🎬 영화감독", "🧘 명상 전문가"],
    "INTP": ["💻 개발자", "🧪 물리학자", "🤖 AI 엔지니어"],
    "ESTP": ["📈 세일즈 매니저", "🎤 방송인", "🎯 기업가"],
    "ESFP": ["🎤 가수", "🎭 배우", "🎉 이벤트 플래너"],
    "ENFP": ["💡 브랜드 디자이너", "🧑‍🏫 교육자", "🌍 NGO 활동가"],
    "ENTP": ["🚀 스타트업 창업자", "📣 마케터", "🎤 토론가"],
    "ESTJ": ["🧑‍💼 관리자", "💼 경영 컨설턴트", "🧾 감사원"],
    "ESFJ": ["🧑‍🍳 요리사", "🏫 학교 교사", "🎗️ 자원봉사 코디네이터"],
    "ENFJ": ["🧑‍⚕️ 심리 치료사", "🗣️ 스피치 강사", "🎓 진로 코치"],
    "ENTJ": ["💼 CEO", "📊 투자분석가", "🎯 전략 기획자"]
}

# 🎯 사용자 MBTI 선택
selected_mbti = st.selectbox("🧠 당신의 MBTI 유형을 선택하세요!", mbti_types, index=mbti_types.index("INFP"))

if selected_mbti:
    st.markdown(f"## 🧬 <span style='color:#ffafcc'>{selected_mbti}</span> 유형의 추천 직업은?", unsafe_allow_html=True)
    
    jobs = job_recommendations.get(selected_mbti, ["🤷‍♀️ 추천 직업이 없어요!"])
    selected_color = random.choice(["#ff66c4", "#a6e3e9", "#ffc75f", "#9d4edd", "#00b4d8"])

    for job in jobs:
        st.markdown(f"<div style='font-size: 24px; padding: 10px; background-color: {selected_color}; border-radius: 10px; margin: 10px 0; color: white; text-align: center;'>{job}</div>", unsafe_allow_html=True)

# 📝 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by ChatGPT | 교육용 프로젝트</p>", unsafe_allow_html=True)
