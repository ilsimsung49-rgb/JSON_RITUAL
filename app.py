import streamlit as st
import random
import re

# [CRITICAL] MUST BE FIRST
st.set_page_config(page_title="JSON RITUAL v6.8", page_icon="👹", layout="wide")

# ==========================================================
#  PROJECT JSON RITUAL v6.8 [GRAND RITUAL FINAL]
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
        "Elec_Guitar_Dist": {"label": "Electric Guitar [Distortion]", "suno_tag": "electric guitar, distortion"},
        "Elec_Guitar_Lead": {"label": "Electric Guitar [Lead]", "suno_tag": "lead guitar solo"},
        "Elec_Guitar_Rhythm": {"label": "Electric Guitar [Rhythm]", "suno_tag": "rhythm guitar"},
        "Acous_Guitar": {"label": "Acoustic Guitar", "suno_tag": "acoustic guitar"},
        "Bass_Gtr": {"label": "Heavy Bass Guitar", "suno_tag": "heavy bass guitar"},
        "Rock_Drums": {"label": "Rock Drums", "suno_tag": "rock drums"},
        "Double_Bass": {"label": "Double Bass Drum [Metal]", "suno_tag": "double bass drum, blast beat"},
        "Synth_Lead": {"label": "Synthesizer Lead", "suno_tag": "synthesizer lead"},
        "Synth_Pad": {"label": "Synth Pad [Ambient]", "suno_tag": "synth pad, ambient"},
        "Sub_Bass": {"label": "808 Sub-Bass", "suno_tag": "808 sub-bass"},
        "Drum_Machine": {"label": "TR-808 Drum Machine", "suno_tag": "drum machine, 808"},
        "Sequencer": {"label": "Analog Sequencer", "suno_tag": "analog sequencer"},
        "Harmonica": {"label": "Harmonica", "suno_tag": "harmonica"},
        "Piano": {"label": "Grand Piano", "suno_tag": "grand piano"},
        "Electric_Piano": {"label": "Electric Piano [Rhodes]", "suno_tag": "electric piano"},
        "Organ": {"label": "Hammond Organ", "suno_tag": "hammond organ"},
        "Violin": {"label": "Solo Violin", "suno_tag": "solo violin"},
        "Strings": {"label": "Orchestral Strings", "suno_tag": "orchestral strings"},
        "Choir": {"label": "Epic Choir", "suno_tag": "choir, epic vocals"},
        "Trumpet": {"label": "Trumpet [Brass]", "suno_tag": "trumpet"},
    },
    "western_rhythms": {
        "Rock": {"label": "록 [Rock]", "suno_prompt": "classic rock, power chords"},
        "Hard_Rock_Metal": {"label": "하드록 / 메탈 [Metal]", "suno_prompt": "heavy metal, distorted riffs, double bass drum"},
        "Blues": {"label": "블루스 [Blues]", "suno_prompt": "slow blues shuffle, soulful guitar"},
        "EDM": {"label": "EDM / 일렉트로닉", "suno_prompt": "EDM, dance music, synthesizer drop"},
        "Jazz": {"label": "재즈 [Jazz]", "suno_prompt": "jazz, swing rhythm, walking bass"},
        "Folk": {"label": "포크 [Folk]", "suno_prompt": "acoustic folk, fingerpicking"},
        "Progressive": {"label": "프로그레시브", "suno_prompt": "progressive rock, complex arrangement"},
    },
    "vocal_types": {
        "male_rock": {"label": "남성 - 거친 록", "suno_tag": "male vocal, raspy rock"},
        "male_deep": {"label": "남성 - 깊은 저음", "suno_tag": "male vocal, deep baritone"},
        "female_clear": {"label": "여성 - 청아한", "suno_tag": "female vocal, clear soprano"},
        "pansori": {"label": "판소리 창", "suno_tag": "pansori vocal, traditional Korean singing"},
        "chant": {"label": "주문/챈트 [Ritual]", "suno_tag": "ritual chant, monotone hypnotic"},
        "experimental": {"label": "전위적 발성", "suno_tag": "avant-garde vocalizations, abstract"},
    },
}

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@200;400;700&display=swap');
    :root { --accent: #FFE800; }
    .stApp { background-color: #000; color: #fff; font-family: 'Outfit', sans-serif; }
    p, span, div, li, label { color: #E0E0E0 !important; }
    h1, h2, h3 { color: #FFF !important; }
    .app-title { font-family: 'Bebas Neue'; font-size: 4rem; color: var(--accent) !important; text-align: center; letter-spacing: 12px; }
    .stButton > button { background: transparent; border: 2px solid var(--accent); color: var(--accent); font-family: 'Bebas Neue'; font-size: 2rem; height: 70px; }
    .stButton > button:hover { background: var(--accent); color: #000; }
    .stTextInput input, .stTextArea textarea, .stNumberInput input, .stSelectbox div[data-baseweb="select"] > div, .stMultiSelect div[data-baseweb="select"] > div {
        background-color: #1A1A1A !important; color: #FFFFFF !important; border: 1px solid var(--accent) !important;
    }
    div[data-baseweb="popover"] div, div[data-baseweb="menu"] div { background-color: #1A1A1A !important; color: #FFFFFF !important; }
    li[role="option"]:hover { background-color: #333333 !important; color: var(--accent) !important; }
    span[data-baseweb="tag"] { background-color: var(--accent) !important; color: #000 !important; }
    </style>
    """, unsafe_allow_html=True)

def main():
    inject_css()
    st.markdown('<h1 class="app-title">PROJECT JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<div style="color:#FFE800; text-align:center; letter-spacing:8px; margin-bottom:40px;">[ GRAND RITUAL v6.8 ]</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["⚡ SETUP", "🎵 STUDIO", "📖 OUTPUT"])

    with t1:
        title = st.text_input("SONG TITLE", "개벽의 소리")
        context = st.text_area("PHILOSOPHY SEED", "사상을 입력하세요...", height=150)
        b_min = st.number_input("BPM Min", 40, 240, 100)
        b_max = st.number_input("BPM Max", 40, 240, 140)

    with t2:
        k_sel = st.multiselect("KOREAN INSTRUMENTS", list(STYLE_DB["korean_instruments"].keys()), ["Janggu", "Gayageum"])
        w_sel = st.multiselect("WESTERN INSTRUMENTS", list(STYLE_DB["western_instruments"].keys()), ["Elec_Guitar_Dist", "Rock_Drums"])
        r_key = st.selectbox("MAIN GENRE", list(STYLE_DB["western_rhythms"].keys()))
        v_key = st.selectbox("VOCAL", list(STYLE_DB["vocal_types"].keys()))

    with t3:
        if st.button("🔥 GENERATE MASTER RITUAL"):
            ki_t = [STYLE_DB["korean_instruments"][k]["suno_tag"] for k in k_sel]
            wi_t = [STYLE_DB["western_instruments"][k]["suno_tag"] for k in w_sel]
            base = "fluxus ritual, avant-garde music, shamanic spirit, "
            genre_p = STYLE_DB["western_rhythms"][r_key]["suno_prompt"]
            vocal_p = STYLE_DB["vocal_types"][v_key]["suno_tag"]
            st.session_state["p_box"] = f"{base}{genre_p}, {', '.join(ki_t + wi_t)}, {vocal_p}, {b_min}-{b_max} BPM, Korean lyrics"
            st.session_state["lyrics"] = f"[INTRO]\n[Professional Instrumental Session - Shamanic Fusion]\n[Instruments: {', '.join(ki_t + wi_t)}]\n\n[VERSE 1]\n태초의 빛이 갈라지는 소리\n{title} 하늘에 울려 퍼지네\n\n[OUTRO]\n영광의 마침표"

        if "p_box" in st.session_state:
            st.code(st.session_state["p_box"])
            st.code(st.session_state["lyrics"])

if __name__ == "__main__":
    main()
