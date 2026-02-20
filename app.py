import streamlit as st
import random
import re

# [CRITICAL] STREAMLIT PAGE CONFIG
st.set_page_config(page_title="JSON RITUAL v6.9", page_icon="👹", layout="wide")

# ==========================================================
#  PROJECT JSON RITUAL v6.9 [THE FLUXUS SPIRIT RESTORED]
# ==========================================================

STYLE_DB = {
    "korean_instruments": {
        "Gayageum": {"label": "가야금 [Gayageum]", "suno_tag": "gayageum"},
        "Geomungo": {"label": "거문고 [Geomungo]", "suno_tag": "geomungo"},
        "Haegeum": {"label": "해금 [Haegeum]", "suno_tag": "haegeum fiddle"},
        "Daegeum": {"label": "대금 [Daegeum]", "suno_tag": "daegeum flute"},
        "Piri": {"label": "피리 [Piri]", "suno_tag": "piri oboe"},
        "Taepyeongso": {"label": "태평소 [Taepyeongso]", "suno_tag": "taepyeongso shawm"},
        "Beomjong": {"label": "범종 [Temple Bell]", "suno_tag": "temple bell"},
        "Daebuk": {"label": "대북 [Daebuk Drum]", "suno_tag": "taiko drum"},
        "Janggu": {"label": "장구 [Janggu]", "suno_tag": "janggu drum"},
        "Kkwaenggwari": {"label": "꽱과리 [Gong]", "suno_tag": "kkwaenggwari gong"},
        "Jing": {"label": "징 [Jing]", "suno_tag": "jing large gong"},
    },
    "western_instruments": {
        "Elec_Guitar_Dist": {"label": "Elec Guitar [Distortion]", "suno_tag": "electric guitar, distortion"},
        "Lead_Guitar": {"label": "Lead Guitar [Solo]", "suno_tag": "lead guitar solo"},
        "Rhythm_Guitar": {"label": "Rhythm Guitar [Crunch]", "suno_tag": "rhythm guitar"},
        "Acous_Guitar": {"label": "Acoustic Guitar", "suno_tag": "acoustic guitar"},
        "Bass_Gtr": {"label": "Heavy Bass Guitar", "suno_tag": "heavy bass guitar"},
        "Rock_Drums": {"label": "Rock Drums", "suno_tag": "rock drums"},
        "Double_Bass": {"label": "Double Bass Drum [Metal]", "suno_tag": "double bass drum"},
        "Synth_Lead": {"label": "Synthesizer Lead", "suno_tag": "synthesizer lead"},
        "Synth_Pad": {"label": "Synth Pad [Ambient]", "suno_tag": "synth pad"},
        "Sub_Bass": {"label": "808 Sub-Bass", "suno_tag": "808 sub-bass"},
        "Drum_Machine": {"label": "Drum Machine [808]", "suno_tag": "drum machine"},
        "Sequencer": {"label": "Analog Sequencer", "suno_tag": "analog sequencer"},
        "Harmonica": {"label": "Harmonica", "suno_tag": "harmonica"},
        "Piano": {"label": "Grand Piano", "suno_tag": "grand piano"},
        "Electric_Piano": {"label": "Electric Piano", "suno_tag": "electric piano"},
        "Organ": {"label": "Hammond Organ", "suno_tag": "hammond organ"},
        "Violin": {"label": "Solo Violin", "suno_tag": "solo violin"},
        "Strings": {"label": "Orchestral Strings", "suno_tag": "orchestral strings"},
        "Choir": {"label": "Epic Choir", "suno_tag": "choir"},
        "Trumpet": {"label": "Trumpet", "suno_tag": "trumpet"},
    },
    "western_rhythms": {
        "Rock": {"label": "록 [Rock]", "suno_prompt": "classic rock, power chords"},
        "Metal": {"label": "메탈 [Metal]", "suno_prompt": "heavy metal, distorted riffs"},
        "Blues": {"label": "블루스 [Blues]", "suno_prompt": "slow blues shuffle"},
        "EDM": {"label": "EDM / Electronic", "suno_prompt": "EDM, dance music"},
        "Jazz": {"label": "재즈 [Jazz]", "suno_prompt": "jazz, swing rhythm"},
        "Folk": {"label": "포크 [Folk]", "suno_prompt": "acoustic folk"},
        "Progressive": {"label": "프로그레시브", "suno_prompt": "progressive arrangement"},
    },
}

def clean_t(txt): return re.sub(r'[\u4e00-\u9fff\(\)]+', '', txt).strip() if txt else ""

def generate_grand_lyrics(title):
    core = clean_t(title) or "진리"
    ritual = f"[INTRO]\n[Professional Instrumental Session - Shamanic Fusion Ritual]\n[Pure expertise, high-quality, NO VOCALS]\n\n"
    ritual += f"[VERSE 1 - THE AWAKENING]\n태초의 정적이 터져 나오던 그 날\n{core} 하늘에 가득했네\n잃어버린 시원의 기억을 다시 깨운다\n\n"
    ritual += f"[VERSE 2 - THE DECONSTRUCTION]\n낡은 시스템이 붕괴하는 소리\n거대한 물결이 몰려온다\n{core} 우리의 심장을 두드린다\n\n"
    ritual += f"[VERSE 3 - THE SINGULARITY]\n디지털과 영성의 경계에 서서\n우리는 무엇을 보는가\n{core} 울려 퍼지는 이 전위적 공간\n\n"
    ritual += f"[OUTRO - THE REBIRTH]\n이제 하나로 연결되는 시간\n우주의 마지막 코드이자 첫 소절\n{core} 영원히 울려 퍼지리라"
    return ritual

def inject_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@200;400;700&display=swap');
    .stApp { background-color: #000; color: #fff !important; font-family: 'Outfit', sans-serif; }
    p, span, div, li, label { color: #E0E0E0 !important; }
    .app-title { font-family: 'Bebas Neue'; font-size: 4rem; color: #FFE800 !important; text-align: center; letter-spacing: 12px; margin: 30px 0; }
    .stButton > button { width: 100% !important; background: transparent !important; border: 2px solid #FFE800 !important; color: #FFE800 !important; font-family: 'Bebas Neue' !important; font-size: 2.22rem !important; height: 77px !important; transition: 0.3s; }
    .stButton > button:hover { background: #FFE800 !important; color: #000 !important; box-shadow: 0 0 33px #FFE800; }
    .stTextInput input, .stTextArea textarea, .stNumberInput input, .stSelectbox div[data-baseweb="select"] > div, .stMultiSelect div[data-baseweb="select"] > div {
        background-color: #1A1A1A !important; color: #FFFFFF !important; border: 1px solid #FFE800 !important;
    }
    div[data-baseweb="popover"] div, div[data-baseweb="menu"] div { background-color: #1A1A1A !important; color: #FFFFFF !important; }
    li[role="option"]:hover { background-color: #333333 !important; color: #FFE800 !important; }
    span[data-baseweb="tag"] { background-color: #FFE800 !important; color: #000 !important; }
    </style>
    """, unsafe_allow_html=True)

def main():
    inject_style()
    st.markdown('<h1 class="app-title">PROJECT JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<div style="color:#FFE800; text-align:center; letter-spacing:8px; margin-bottom:40px;">[ MASTER FUSION v6.9 - FLUXUS RITUAL ]</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["⚡ SETUP", "🎵 STUDIO", "📖 OUTPUT"])

    with t1:
        title = st.text_input("SONG TITLE", "개벽의 소리")
        context = st.text_area("PHILOSOPHY SEED", "사상을 입력하세요...", height=150)
        b_min = st.number_input("BPM Min", 40, 240, 100)
        b_max = st.number_input("BPM Max", 40, 240, 140)

    with t2:
        st.markdown("### SOUND DESIGN")
        k_sel = st.multiselect("KOREAN INSTRUMENTS", list(STYLE_DB["korean_instruments"].keys()), ["Janggu", "Gayageum", "Taepyeongso"])
        w_sel = st.multiselect("WESTERN INSTRUMENTS", list(STYLE_DB["western_instruments"].keys()), ["Elec_Guitar_Dist", "Double_Bass", "Synth_Lead"])
        r_key = st.selectbox("BASE GENRE", list(STYLE_DB["western_rhythms"].keys()))
        v_key = st.selectbox("VOCAL", ["male powerful", "male deep", "female clear soprano", "pansori", "ritual chant"])

    with t3:
        if st.button("🔥 GENERATE MASTER RITUAL"):
            ki_t = [STYLE_DB["korean_instruments"][k]["suno_tag"] for k in k_sel]
            wi_t = [STYLE_DB["western_instruments"][k]["suno_tag"] for k in w_sel]
            # THE CORE FLUXUS PROMPT LOGIC
            base = "fluxus ritual, avant-garde music, shamanic spirit, experimental deconstruction, "
            genre_p = STYLE_DB["western_rhythms"][r_key]["suno_prompt"]
            st.session_state["p_box"] = f"{base}{genre_p}, {', '.join(ki_t + wi_t)}, {v_key}, {b_min}-{b_max} BPM, Korean lyrics, no auto-tune"
            st.session_state["lyrics"] = generate_grand_lyrics(title)

        if "p_box" in st.session_state:
            st.markdown("### 1. SUNO STYLE BOX")
            st.code(st.session_state["p_box"], language="text")
            st.markdown("### 2. MASTER LYRICS & FLOW")
            st.code(st.session_state["lyrics"], language="text")

if __name__ == "__main__":
    main()
