import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🌟 K-pop 멤버 소속 그룹 찾기",
    page_icon="🎤",
    layout="centered"
)

# 제목
st.markdown("<h1 style='text-align:center; color:#ff66c4;'>🌈 아이돌 멤버 → 소속 그룹 찾기 🎶</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#5f0f40;'>멤버 이름을 입력하면 소속 그룹을 알려드려요! ✨</h4>", unsafe_allow_html=True)
st.markdown("---")

# 멤버-그룹 매핑 데이터
idol_members = {
    # BTS
    "정국": ["BTS"], "뷔": ["BTS"], "지민": ["BTS"], "RM": ["BTS"], "진": ["BTS"], "슈가": ["BTS"], "제이홉": ["BTS"],

    # BLACKPINK
    "제니": ["BLACKPINK"], "지수": ["BLACKPINK"], "로제": ["BLACKPINK"], "리사": ["BLACKPINK"],

    # TWICE
    "나연": ["TWICE"], "정연": ["TWICE"], "모모": ["TWICE"], "사나": ["TWICE"], "지효": ["TWICE"],
    "미나": ["TWICE"], "다현": ["TWICE"], "채영": ["TWICE"], "쯔위": ["TWICE"],

    # IVE
    "장원영": ["IVE"], "안유진": ["IVE"], "레이": ["IVE"], "가을": ["IVE"], "리즈": ["IVE"], "이서": ["IVE"],

    # NEWJEANS
    "민지": ["NEWJEANS"], "하니": ["NEWJEANS"], "다니엘": ["NEWJEANS"], "해린": ["NEWJEANS"], "혜인": ["NEWJEANS"],

    # LE SSERAFIM
    "사쿠라": ["LE SSERAFIM", "IZ*ONE"], "김채원": ["LE SSERAFIM", "IZ*ONE"], "허윤진": ["LE SSERAFIM"],
    "카즈하": ["LE SSERAFIM"], "홍은채": ["LE SSERAFIM"],

    # BOYNEXTDOOR
    "성호": ["BOYNEXTDOOR"], "리우": ["BOYNEXTDOOR"], "재현": ["BOYNEXTDOOR"],
    "태산": ["BOYNEXTDOOR"], "이한": ["BOYNEXTDOOR"], "운학": ["BOYNEXTDOOR"],

    # EXO
    "백현": ["EXO"], "찬열": ["EXO"], "디오": ["EXO"], "수호": ["EXO"], "카이": ["EXO"], "세훈": ["EXO"],
    "시우민": ["EXO"], "레이": ["EXO"], "첸": ["EXO"],

    # NCT 127
    "태용": ["NCT 127"], "재현": ["NCT 127", "BOYNEXTDOOR"], "유타": ["NCT 127"], "쟈니": ["NCT 127"],
    "도영": ["NCT 127"], "정우": ["NCT 127"], "해찬": ["NCT 127", "NCT DREAM"], "태일": ["NCT 127"], "마크": ["NCT 127", "NCT DREAM"],

    # NCT DREAM
    "천러": ["NCT DREAM"], "지성": ["NCT DREAM"], "런쥔": ["NCT DREAM"], "제노": ["NCT DREAM"], "재민": ["NCT DREAM"],

    # SEVENTEEN
    "에스쿱스": ["SEVENTEEN"], "정한": ["SEVENTEEN"], "조슈아": ["SEVENTEEN"], "준": ["SEVENTEEN"], "호시": ["SEVENTEEN"],
    "원우": ["SEVENTEEN"], "우지": ["SEVENTEEN"], "디에잇": ["SEVENTEEN"], "민규": ["SEVENTEEN"],
    "도겸": ["SEVENTEEN"], "승관": ["SEVENTEEN"], "버논": ["SEVENTEEN"], "디노": ["SEVENTEEN"],

    # (G)I-DLE
    "소연": ["(G)I-DLE"], "미연": ["(G)I-DLE"], "민니": ["(G)I-DLE"], "우기": ["(G)I-DLE"], "슈화": ["(G)I-DLE"],

    # aespa
    "카리나": ["aespa"], "윈터": ["aespa"], "지젤": ["aespa"], "닝닝": ["aespa"],

    # ITZY
    "예지": ["ITZY"], "리아": ["ITZY"], "류진": ["ITZY"], "채령": ["ITZY"], "유나": ["ITZY"],

    # Stray Kids
    "방찬": ["Stray Kids"], "리노": ["Stray Kids"], "창빈": ["Stray Kids"], "현진": ["Stray Kids"],
    "한": ["Stray Kids"], "필릭스": ["Stray Kids"], "승민": ["Stray Kids"], "아이엔": ["Stray Kids"],

    # TREASURE
    "지훈": ["TREASURE"], "요시": ["TREASURE"], "준규": ["TREASURE"], "마시호": ["TREASURE"], "윤재혁": ["TREASURE"],
    "아사히": ["TREASURE"], "도영": ["TREASURE"], "하루토": ["TREASURE"], "박정우": ["TREASURE"], "소정환": ["TREASURE"],

    # ENHYPEN
    "정원": ["ENHYPEN"], "희승": ["ENHYPEN"], "제이": ["ENHYPEN"], "제이크": ["ENHYPEN"], "성훈": ["ENHYPEN"],
    "선우": ["ENHYPEN"], "니키": ["ENHYPEN"],

    # TXT
    "수빈": ["TXT"], "연준": ["TXT"], "범규": ["TXT"], "태현": ["TXT"], "휴닝카이": ["TXT"],

    # Red Velvet
    "아이린": ["Red Velvet"], "슬기": ["Red Velvet"], "웬디": ["Red Velvet"], "조이": ["Red Velvet"], "예리": ["Red Velvet"],

    # SHINee
    "온유": ["SHINee"], "종현": ["SHINee"], "키": ["SHINee"], "민호": ["SHINee"], "태민": ["SHINee"]
}

# 사용자 입력
member_input = st.text_input("🧑‍🎤 아이돌 멤버 이름을 입력해 보세요!", placeholder="예: 정국, 태연, 성호")

# 컬러 팔레트
color_palette = ["#ffafcc", "#a2d2ff", "#cdb4db", "#ffc8dd", "#fbc4ab", "#d0f4de", "#d9faff", "#b5ead7"]

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
        st.warning("😥 죄송해요! 해당 멤버 정보를 찾을 수 없어요. 다시 확인해 주세요.")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Made with 💜 for K-pop Fans by ChatGPT</p>", unsafe_allow_html=True)

