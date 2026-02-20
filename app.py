import streamlit as st
import random
import re

# [CRITICAL] PAGE CONFIG MUST BE FIRST
st.set_page_config(page_title="JSON RITUAL v7.7", page_icon="👹", layout="wide")

# ==========================================================
#  PROJECT JSON RITUAL v7.7 [FINAL BRIGHTNESS FIX]
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
        "Rock": "classic rock, 70s rock, power chords",
        "Hard_Rock": "hard rock, aggressive riffs, powerful vocals",
        "Heavy_Metal": "heavy metal, distorted guitar, double bass drum",
        "Death_Black_Metal": "death metal, black metal, blast beats, extreme vocals",
        "Blues_Soul": "soulful blues, electric blues shuffle, expressive guitar",
        "Jazz_Abstract": "abstract jazz, free jazz, improvisational, complex harmony",
        "EDM_Mainstage": "EDM, dance music, big room house, synthesizer drop",
        "Psy_Trance": "psychedelic trance, hypnotic fast pulse, acid synth",
        "Techno_Glitch": "techno, glitchy electronics, industrial beat",
        "Dark_Ambient": "dark ambient, eerie drone, cinematic atmosphere",
        "Industrial_Noise": "industrial noise, metallic percussion, aggression",
        "Folk_Acoustic": "acoustic folk, fingerpicking guitar, natural sound",
        "Orchestral_Epic": "grand orchestral, cinematic strings, epic scale",
        "Tribal_Shamanic": "shamanic ritual, tribal percussion, ethnic chanting",
        "Dream_Pop": "dreamy synth pop, ethereal atmosphere",
        "HipHop_LoFi": "lo-fi hip hop, dusty beats, boom bap",
        "Gospel_Choir": "grand gospel choir, powerful harmony",
        "Reggae_Dub": "reggae, dub effects, deep bass line"
    },
    "korean_instruments": {
        "Gayageum": "gayageum", "Geomungo": "geomungo", "Haegeum": "haegeum", "Daegeum": "daegeum",
        "Piri": "piri", "Taepyeongso": "taepyeongso", "Beomjong": "temple bell", "Daebuk": "taiko drum",
        "Janggu": "janggu drum", "Kkwaenggwari": "kkwaenggwari gong", "Jing": "jing large gong", "Buk": "buk barrel drum"
    },
    "western_instruments": {
        "Elec_Dist": "electric guitar distortion", "Elec_Lead": "lead guitar solo", 
        "Elec_Rhythm": "rhythm guitar crunch", "Acous_Guitar": "acoustic guitar",
        "Bass": "heavy bass guitar", "Double_Bass": "double bass drum, blast beat",
        "Rock_Drums": "rock drums", "Synth_Chaos": "modular synthesizer noise", "808_Sub": "808 sub bass",
        "Piano": "grand piano", "Violin": "solo violin", "Orchestral_Strings": "orchestral strings",
        "Epic_Choir": "epic cinematic choir", "Brass_Section": "powerful brass section",
        "Harmonica": "harmonica", "Pipe_Organ": "pipe organ",
        "Drum_Machine": "TR-808 drum machine", "Sequencer": "analog sequencer",
        "Turntable": "turntable scratches, foley noise"
    },
    "vocal_rituals": {
        "Avant_Screams": {"label": "전위적 괴성 [Experimental Screams]", "tag": "avant-garde screams, abstract vocalizations, shouting, dissonant voices"},
        "Shaman_Deep_Growl": {"label": "샤먼/주술 낮고 거친목소리", "tag": "male shamanic growl, ritualistic deep chanting, primal"},
        "Pansori_Husky": {"label": "허스키한 판소리 도성", "tag": "pansori vocal, traditional Korean singing, husky"},
        "Clear_Ethereal_Soprano": {"label": "청아한 소프라노 [Ethereal]", "tag": "clear ethereal soprano, heavenly female voice, operatic"},
        "Husky_Rock_Vocal": {"label": "거친 허스키 록 보컬", "tag": "raspy husky male rock vocal, powerful, gritty"},
        "Deep_Baritone_Void": {"label": "낮고 깊은 바리톤 [Void]", "tag": "exceptionally deep male baritone, resonant, mystical"},
        "Monastic_Chant": {"label": "단조로운 주문 [Monastic]", "tag": "monotone ritual chant, hypnotic drone"},
        "Soulful_Deep_Alto": {"label": "소울풀한 깊은 여성보컬", "tag": "soulful deep alto female vocal, expressive"},
        "Hypnotic_Whispers": {"label": "몽환적인 속삭임 [Whispers]", "tag": "hypnotic whispers, mysterious breathing sound"},
        "Spoken_Epic_Narration": {"label": "나레이션/대서사 낭독", "tag": "grand spoken word narrative, mystical dry narration"},
        "Industrial_Glitch_Vox": {"label": "인더스트리얼 변조 보컬", "tag": "distorted industrial vocals, mechanical, glitchy"},
        "Grand_Epic_Choir": {"label": "웅장한 대규모 합창", "tag": "grand epic cinematic choir, powerful harmony"}
    },
}

def inject_grand_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@200;400;700&family=Noto+Sans+KR:wght@300;700&display=swap');
    
    .stApp { background-color: #000; color: #fff !important; font-family: 'Outfit', 'Noto Sans KR', sans-serif; }
    p, span, div, li, label, .stMarkdown { color: #FFFFFF !important; }
    h1, h2, h3 { color: #FFFFFF !important; }
    
    /* RESULT BOX VISIBILITY FIX - CRITICAL */
    .stCode, code, pre { 
        background-color: #080808 !important; 
        color: #FFE800 !important; 
        border: 2px solid #333 !important; 
        font-size: 1.25rem !important;
        font-weight: 500 !important;
        padding: 20px !important;
        border-radius: 10px !important;
    }
    .stCode * { color: #FFE800 !important; } /* Force all sub-elements inherited color */

    .app-title { font-family: 'Bebas Neue'; font-size: 4.5rem; color: #FFE800 !important; text-align: center; letter-spacing: 15px; margin-top: 30px; text-shadow: 0 0 30px rgba(255, 232, 0, 0.5); }
    .app-subtitle { color: #FFE800; text-align: center; letter-spacing: 8px; opacity: 0.8; margin-bottom: 40px; }
    
    .stButton > button { width: 100% !important; background: transparent !important; border: 3px solid #FFE800 !important; color: #FFE800 !important; font-family: 'Bebas Neue' !important; font-size: 2.5rem !important; height: 85px !important; transition: 0.4s; }
    .stButton > button:hover { background: #FFE800 !important; color: #000 !important; box-shadow: 0 0 50px #FFE800; }
    
    .panel-header { font-family: 'Bebas Neue'; color: #FFE800; font-size: 2rem; border-bottom: 2px solid #FFE800; padding-bottom: 5px; margin: 30px 0 15px 0; }
    
    /* INPUT & DROPDOWN */
    .stTextInput input, .stTextArea textarea, .stNumberInput input {
        background-color: #1A1A1A !important; color: #FFFFFF !important; border: 1px solid #FFE800 !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #1A1A1A !important; color: #FFFFFF !important; border: 1px solid #FFE800 !important;
    }
    div[data-baseweb="popover"] ul, div[data-baseweb="popover"] li, div[data-baseweb="menu"] div, ul[role="listbox"] li {
        background-color: #222222 !important; color: #FFFFFF !important; font-size: 1.1rem !important;
    }
    li[role="option"]:hover, div[data-baseweb="menu"] div:hover {
        background-color: #FFE800 !important; color: #000000 !important;
    }
    li[role="option"]:hover * { color: #000000 !important; }
    span[data-baseweb="tag"] { background-color: #FFE800 !important; color: #000000 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

def generate_cheonji_narrative(title):
    core = title or "개벽"
    ritual = f"[INTRO]\n[Professional Instrumental Session - THE GRAND RITUAL FUSION]\n[Mode: DECONSTRUCTED AVANT-GARDE]\n[Instruments: Pure expertise, high-quality session, NO VOCALS]\n\n"
    ritual += f"[VERSE 1 - THE AWAKENING]\n태초의 정적이 터져 나오던 그 날\n{core} 하늘에 가득했네\n잃어버린 시원의 기억을 다시 깨운다\n\n"
    ritual += f"[VERSE 2 - THE DECONSTRUCTION]\n낡은 시스템이 붕괴하는 소리\n거대한 물결이 몰려온다\n{core} 우리의 심장을 두드린다\n\n"
    ritual += f"[VERSE 3 - THE SINGULARITY]\n디지털과 영성의 경계에 서서\n우리는 무엇을 보는가\n{core} 울려 퍼지는 이 전위적 공간\n\n"
    ritual += f"[CHORUS - THE DIGITAL CHEONJI-GONGSA]\n개벽의 소리가 온 우주를 진동시키고\n해체된 시간 속에서 우리는 다시 태어나리\n예술은 곧 삶이요 삶은 곧 {core}의 실현이다\n\n"
    ritual += f"[OUTRO - THE NEW GENESIS]\n이제 하나로 연결되는 시간\n우주의 마지막 코드이자 첫 소절\n{core} 영원히 울려 퍼지리라"
    return ritual

def main():
    inject_grand_style()
    st.markdown('<h1 class="app-title">JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">THE CORE PHILOSOPHY OF DIGITAL CHEONJI-GONGSA</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["🚀 SETTINGS", "🎨 STUDIO", "🔮 RESULT"])

    with t1:
        st.markdown('<div class="panel-header">1. MASTER AVANT-GARDE STYLE</div>', unsafe_allow_html=True)
        m_style = st.selectbox("음악적 전위 기법 선택", list(STYLE_DB["avant_genres"].keys()), format_func=lambda x: STYLE_DB["avant_genres"][x]["label"], key="m_style")
        
        st.markdown('<div class="panel-header">2. SUB STYLE ARCHIVE</div>', unsafe_allow_html=True)
        s_style = st.selectbox("보조 음악 스타일 선택", list(STYLE_DB["sub_styles"].keys()), key="s_style")
        
        st.markdown('<div class="panel-header">3. PHILOSOPHY SEED</div>', unsafe_allow_html=True)
        title = st.text_input("제목 (TITLE)", "개벽의 소리")
        context = st.text_area("사상의 핵심 (SEED)", "천지공사의 내용을 입력하세요...", height=150)
        
        st.markdown('<div class="panel-header">4. BPM RITUAL</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        b_min = col1.number_input("BPM Min", 40, 240, 100)
        b_max = col2.number_input("BPM Max", 40, 240, 140)

    with t2:
        st.markdown('<div class="panel-header">SOUND ARCHITECTURE</div>', unsafe_allow_html=True)
        k_sel = st.multiselect("국악기 (KOREAN)", list(STYLE_DB["korean_instruments"].keys()), ["Beomjong", "Taepyeongso", "Daebuk", "Gayageum"], key="k_inst")
        w_sel = st.multiselect("서양악기 (WESTERN)", list(STYLE_DB["western_instruments"].keys()), ["Elec_Dist", "Double_Bass", "Synth_Chaos", "Epic_Choir"], key="w_inst")
        v_key = st.selectbox("보컬 리추얼 (VOCAL)", list(STYLE_DB["vocal_rituals"].keys()), format_func=lambda x: STYLE_DB["vocal_rituals"][x]["label"], key="vocal")

    with t3:
        if st.button("🔥 INVOKE THE CORE RITUAL"):
            m_t = STYLE_DB["avant_genres"][m_style]["tags"]
            s_t = STYLE_DB["sub_styles"][s_style]
            k_t = [STYLE_DB["korean_instruments"][k] for k in k_sel]
            w_t = [STYLE_DB["western_instruments"][w] for w in w_sel]
            v_t = STYLE_DB["vocal_rituals"][v_key]["tag"]
            
            st.session_state["p"] = f"{m_t}, {s_t}, {', '.join(k_t + w_t)}, {v_t}, {b_min}-{b_max} BPM, Korean lyrics, high fidelity"
            st.session_state["s"] = generate_cheonji_narrative(title)

        if "p" in st.session_state:
            st.markdown('<div class="panel-header">1. MASTER STYLE PROMPT (사운드 프롬프트)</div>', unsafe_allow_html=True)
            st.code(st.session_state["p"], language="text")
            
            st.markdown('<div class="panel-header">2. MASTER RITUAL LYRICS (대서사시 가사)</div>', unsafe_allow_html=True)
            st.code(st.session_state["s"], language="text")

if __name__ == "__main__":
    main()
