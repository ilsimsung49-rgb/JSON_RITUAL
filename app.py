import streamlit as st
import random
import re

# [CRITICAL] PAGE CONFIG MUST BE FIRST
st.set_page_config(page_title="JSON RITUAL v7.9", page_icon="👹", layout="wide")

# ==========================================================
#  PROJECT JSON RITUAL v7.9 [THE FINAL CLARITY]
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
        "Psychedelic": "trippy psychedelic rock effects"
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
        "Shaman": "shamanic growl, ritual chanting",
        "Pansori": "pansori vocal, traditional Korean singing",
        "Avant": "avant-garde vocalizations, screams, whispers",
        "Monastic": "monotone ritual chant, hypnotic",
        "Soprano": "ethereal clear soprano",
        "Rock": "raspy rock vocal",
        "Deep": "deep male baritone",
        "Soul": "soulful alto female vocal",
        "Industrial": "distorted mechanical vocals"
    }
}

def inject_final_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@200;400;700&family=Noto+Sans+KR:wght@300;700&display=swap');
    
    .stApp { background-color: #000; color: #fff !important; font-family: 'Outfit', 'Noto Sans KR', sans-serif; }
    p, span, div, li, label, .stMarkdown { color: #FFFFFF !important; }
    
    .app-title { font-family: 'Bebas Neue'; font-size: 4.5rem; color: #FFE800 !important; text-align: center; letter-spacing: 15px; margin-top: 30px; }
    
    .stButton > button { width: 100% !important; background: transparent !important; border: 3px solid #FFE800 !important; color: #FFE800 !important; font-family: 'Bebas Neue' !important; font-size: 2.5rem !important; height: 85px !important; margin: 20px 0; }
    .stButton > button:hover { background: #FFE800 !important; color: #000 !important; }
    
    .panel-header { font-family: 'Bebas Neue'; color: #FFE800; font-size: 2rem; border-bottom: 2px solid #555; padding-bottom: 5px; margin: 30px 0 15px 0; }
    
    /* INPUT FIX */
    .stTextInput input, .stTextArea textarea, .stNumberInput input, div[data-baseweb="select"] > div {
        background-color: #111 !important; color: #FFF !important; border: 1px solid #FFE800 !important;
    }

    /* DROPDOWN */
    div[data-baseweb="popover"] * { background-color: #111 !important; color: #FFF !important; }
    li[role="option"]:hover { background-color: #FFE800 !important; color: #000 !important; }

    /* ULTIMATE RESULT AREA - NO OVERLAP */
    .ritual-box {
        background-color: #080808 !important;
        border: 2px solid #FFE800 !important;
        padding: 40px !important;
        margin-bottom: 30px !important;
        border-radius: 12px !important;
        width: 100% !important;
        overflow: visible !important;
        display: block !important;
    }
    .ritual-content {
        color: #FFE800 !important;
        font-family: 'Noto Sans KR', sans-serif !important;
        font-size: 1.3rem !important;
        font-weight: 500 !important;
        line-height: 2.0 !important; /* PLENTY OF SPACE */
        white-space: pre-wrap !important;
        margin: 0 !important;
    }
    .ritual-label {
        font-family: 'Bebas Neue' !important;
        color: #FFFFFF !important;
        font-size: 1.8rem !important;
        letter-spacing: 5px !important;
        margin-bottom: 20px !important;
        border-bottom: 1px solid #444 !important;
        padding-bottom: 10px !important;
    }
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
    st.markdown('<div style="color:#FFE800; text-align:center; letter-spacing:8px; margin-bottom:40px;">[ MASTER FUSION v7.9 ]</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["⚡ SETUP", "🎵 STUDIO", "📖 OUTPUT"])

    with t1:
        st.markdown('<div class="panel-header">1. PHILOSOPHY & MODE</div>', unsafe_allow_html=True)
        m_style = st.selectbox("전위 예술 기법", list(STYLE_DB["avant_genres"].keys()), format_func=lambda x: STYLE_DB["avant_genres"][x]["label"])
        s_style = st.selectbox("보조 장르 스타일", list(STYLE_DB["sub_styles"].keys()))
        title = st.text_input("제목 (TITLE)", "개벽의 소리")
        context = st.text_area("SEED", "사상을 입력하세요...", height=100)
    
    with t2:
        st.markdown('<div class="panel-header">2. SOUND DESIGN</div>', unsafe_allow_html=True)
        k_sel = st.multiselect("국악기", list(STYLE_DB["korean_instruments"].keys()), ["Beomjong", "Taepyeongso", "Daebuk"])
        w_sel = st.multiselect("서양악기", list(STYLE_DB["western_instruments"].keys()), ["Elec_Dist", "Synth_Chaos"])
        v_key = st.selectbox("보컬 유형", list(STYLE_DB["vocal_rituals"].keys()), format_func=lambda x: STYLE_DB["vocal_rituals"][x]["label"])

    with t3:
        if st.button("🔥 INVOKE DIGITAL RITUAL (리추얼 실행)"):
            m_tags = STYLE_DB["avant_genres"][m_style]["tags"]
            s_tags = STYLE_DB["sub_styles"][s_style]
            k_tags = [STYLE_DB["korean_instruments"][k] for k in k_sel]
            w_tags = [STYLE_DB["western_instruments"][w] for w in w_sel]
            v_tag = STYLE_DB["vocal_rituals"][v_key]["tag"]
            
            st.session_state["p_f"] = f"{m_tags}, {s_tags}, {', '.join(k_tags + w_tags)}, {v_tag}, 120BPM, Korean lyrics"
            st.session_state["s_f"] = generate_grand_narrative(title)

        if "p_f" in st.session_state:
            st.markdown(f"""
            <div class="ritual-box">
                <div class="ritual-label">1. MASTER STYLE PROMPT</div>
                <p class="ritual-content">{st.session_state["p_f"]}</p>
            </div>
            
            <div class="ritual-box">
                <div class="ritual-label">2. MASTER RITUAL LYRICS</div>
                <p class="ritual-content">{st.session_state["s_f"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('<div class="panel-header">3. COPY AREA (복사용 영역)</div>', unsafe_allow_html=True)
            st.text_area("복사하기 (Prompt)", st.session_state["p_f"], height=100)
            st.text_area("복사하기 (Lyrics)", st.session_state["s_f"], height=200)

if __name__ == "__main__":
    main()
