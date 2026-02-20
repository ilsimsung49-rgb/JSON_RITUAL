import streamlit as st
import random
import re

# [CRITICAL] PAGE CONFIG MUST BE FIRST
st.set_page_config(page_title="JSON RITUAL v8.0", page_icon="👹", layout="wide")

# ==========================================================
#  PROJECT JSON RITUAL v8.0 [STABLE & CLARITY FIX]
# ==========================================================

STYLE_DB = {
    "avant_genres": {
        "Fluxus": {"label": "플럭서스 [FLUXUS]", "tags": "fluxus ritual, experimental deconstruction, art-life fusion, chaotic, anti-art"},
        "Avant_Garde": {"label": "아방가르드 [AVANT-GARDE]", "tags": "avant-garde music, experimental, atonal, dissonant, radical breaking of rules"},
        "Industrial_Ritual": {"label": "인더스트리얼 리추얼", "tags": "industrial, mechanical sounds, dark ritual, repetitive noise, steel textures"},
        "Progressive_Fusion": {"label": "프로그레시브 퓨전", "tags": "progressive, complex arrangement, world music fusion, epic structure"},
        "Experimental_Void": {"label": "전위적 허공 [VOID]", "tags": "space drone, ambient, transcendent, experimental atmosphere, minimalistic"}
    },
    "sub_styles": {
        "Rock_Metal": "hard rock, heavy metal, distorted riffs",
        "EDM_Chaos": "glitch electronic, synthesizer chaos",
        "Blues_Jazz": "soulful blues, abstract free jazz",
        "Tribal": "shamanic ritual percussion",
        "Ambient": "deep space drone ambient",
        "Industrial": "harsh mechanical industrial",
        "Psychedelic": "trippy psychedelic rock"
    },
    "korean_instruments": {
        "Gayageum": "gayageum", "Geomungo": "geomungo", "Haegeum": "haegeum", "Daegeum": "daegeum",
        "Piri": "piri", "Taepyeongso": "taepyeongso", "Beomjong": "temple bell", "Daebuk": "taiko drum",
        "Janggu": "janggu drum", "Kkwaenggwari": "kkwaenggwari gong", "Jing": "jing gong", "Buk": "buk drum"
    },
    "western_instruments": {
        "Elec_Dist": "electric guitar distortion", "Elec_Lead": "lead guitar solo", 
        "Bass": "heavy bass guitar", "Rock_Drums": "rock drums",
        "Synth_Chaos": "modular synthesizer noise", "808_Sub": "808 sub bass",
        "Piano": "grand piano", "Violin": "solo violin", "Epic_Choir": "epic choir"
    },
    "vocal_rituals": {
        "Shaman": {"label": "샤먼/주술 보컬", "tag": "male shamanic growl, ritualistic chanting"},
        "Pansori": {"label": "허스키한 판소리 도성", "tag": "pansori vocal, traditional Korean singing, husky"},
        "Avant": {"label": "전위적 발성/괴성", "tag": "avant-garde vocalizations, screams, whispers, deconstructed"},
        "Monastic": {"label": "단조로운 주문/챈트", "tag": "monotone ritual chant, hypnotic drone"},
        "Soprano": {"label": "청아한 소프라노", "tag": "ethereal clear soprano, operatic, heavenly"},
        "Rock": {"label": "허스키한 록 보컬", "tag": "raspy rock vocal, powerful gritty"},
        "Deep": {"label": "낮고 깊은 바리톤", "tag": "deep male baritone, resonant, mystical"},
        "Soul": {"label": "소울풀한 알토", "tag": "soulful alto female vocal, expressive"},
        "Industrial": {"label": "인더스트리얼 변조", "tag": "distorted mechanical vocals, metallic"}
    }
}

def inject_final_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@200;400;700&family=Noto+Sans+KR:wght@300;700&display=swap');
    
    .stApp { background-color: #000; color: #fff !important; font-family: 'Outfit', 'Noto Sans KR', sans-serif; }
    p, span, div, li, label, .stMarkdown { color: #FFFFFF !important; }
    
    .app-title { font-family: 'Bebas Neue'; font-size: 4.5rem; color: #FFE800 !important; text-align: center; letter-spacing: 15px; margin-top: 30px; }
    
    /* Input Styling */
    .stTextInput input, .stTextArea textarea, .stNumberInput input, div[data-baseweb="select"] > div {
        background-color: #111 !important; color: #FFF !important; border: 1px solid #FFE800 !important;
    }
    
    /* Dropdown Clarity */
    div[data-baseweb="popover"] ul, div[data-baseweb="popover"] li {
        background-color: #111 !important; color: #FFF !important;
    }
    li[role="option"]:hover { background-color: #FFE800 !important; color: #000 !important; }
    li[role="option"]:hover * { color: #000 !important; }

    /* ULTIMATE RESULT AREA - ZERO OVERLAP */
    .ritual-box {
        background-color: #050505 !important;
        border: 2px solid #FFE800 !important;
        padding: 40px !important;
        margin-bottom: 40px !important;
        border-radius: 15px !important;
        position: relative !important;
        z-index: 99 !important;
    }
    .ritual-content {
        color: #FFE800 !important;
        font-family: 'Noto Sans KR', sans-serif !important;
        font-size: 1.4rem !important;
        line-height: 2.2 !important; /* ULTRA CLARITY SPACE */
        white-space: pre-wrap !important;
        margin: 0 !important;
        word-break: keep-all !important;
    }
    .ritual-label {
        font-family: 'Bebas Neue' !important;
        color: #FFFFFF !important;
        font-size: 2rem !important;
        letter-spacing: 5px !important;
        margin-bottom: 25px !important;
        border-bottom: 1px solid #333 !important;
        padding-bottom: 10px !important;
    }
    
    .stButton > button { width: 100% !important; background: transparent !important; border: 3px solid #FFE800 !important; color: #FFE800 !important; font-family: 'Bebas Neue' !important; font-size: 2.5rem !important; height: 85px !important; }
    .stButton > button:hover { background: #FFE800 !important; color: #000 !important; }
    </style>
    """, unsafe_allow_html=True)

def generate_grand_narrative(title):
    core = title or "개벽"
    ritual = f"[VERSE 1 - THE AWAKENING]\n태초의 정적이 터져 나오던 그 날\n{core} 하늘에 가득했네\n잃어버린 시원의 기억을 다시 깨운다\n\n"
    ritual += f"[VERSE 2 - THE DECONSTRUCTION]\n낡은 시스템이 붕괴하는 소리\n거대한 물결이 몰려온다\n{core} 우리의 심장을 두드린다\n\n"
    ritual += f"[CHORUS - THE DIGITAL CHEONJI-GONGSA]\n개벽의 소리가 온 우주를 진동시키고\n해체된 시간 속에서 우리는 다시 태어나리\n예술은 곧 삶이요 삶은 곧 {core}의 실현이다\n\n"
    ritual += f"[OUTRO - THE NEW GENESIS]\n이제 하나로 연결되는 시간\n우주의 마지막 코드이자 첫 소절\n{core} 영원히 울려 퍼지리라"
    return ritual

def main():
    inject_final_style()
    st.markdown('<h1 class="app-title">JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<div style="color:#FFE800; text-align:center; letter-spacing:8px; margin-bottom:40px;">[ MASTER FUSION v8.0 ]</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["🚀 SETUP", "🎨 STUDIO", "📖 OUTPUT"])

    with t1:
        m_key = st.selectbox("전위 예술 기법", list(STYLE_DB["avant_genres"].keys()), format_func=lambda x: STYLE_DB["avant_genres"][x]["label"])
        s_key = st.selectbox("보조 장르 스타일", list(STYLE_DB["sub_styles"].keys()))
        title = st.text_input("제목 (TITLE)", "개벽의 소리")
        context = st.text_area("SEED", "사상을 입력하세요...", height=100)
    
    with t2:
        k_sel = st.multiselect("국악기", list(STYLE_DB["korean_instruments"].keys()), ["Beomjong", "Taepyeongso", "Daebuk"])
        w_sel = st.multiselect("서양악기", list(STYLE_DB["western_instruments"].keys()), ["Elec_Dist", "Synth_Chaos"])
        v_key = st.selectbox("보컬 유형", list(STYLE_DB["vocal_rituals"].keys()), format_func=lambda x: STYLE_DB["vocal_rituals"][x]["label"])

    with t3:
        if st.button("🔥 INVOKE DIGITAL RITUAL (리추얼 실행)"):
            m_t = STYLE_DB["avant_genres"][m_key]["tags"]
            s_t = STYLE_DB["sub_styles"][s_key]
            k_t = [STYLE_DB["korean_instruments"][k] for k in k_sel]
            w_t = [STYLE_DB["western_instruments"][w] for w in w_sel]
            v_t = STYLE_DB["vocal_rituals"][v_key]["tag"]
            
            st.session_state["p_stable"] = f"{m_t}, {s_t}, {', '.join(k_t + w_t)}, {v_t}, 120BPM, Korean lyrics"
            st.session_state["s_stable"] = generate_grand_narrative(title)

        if "p_stable" in st.session_state:
            st.markdown(f"""
            <div class="ritual-box">
                <div class="ritual-label">1. MASTER STYLE PROMPT</div>
                <p class="ritual-content">{st.session_state["p_stable"]}</p>
            </div>
            
            <div class="ritual-box">
                <div class="ritual-label">2. MASTER RITUAL LYRICS</div>
                <p class="ritual-content">{st.session_state["s_stable"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.text_area("Prompt Copy Area", st.session_state["p_stable"], height=100)
            st.text_area("Lyrics Copy Area", st.session_state["s_stable"], height=200)

if __name__ == "__main__":
    main()
