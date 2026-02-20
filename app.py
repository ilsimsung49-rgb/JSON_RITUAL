import streamlit as st
import random
import re

# [CRITICAL] MUST BE FIRST
st.set_page_config(page_title="JSON RITUAL v6.7", page_icon="👹", layout="wide")

# ==========================================================
#  PROJECT JSON RITUAL v6.7 [MASTER FUSION FINAL]
# ==========================================================

STYLE_DB = {
    "moods": {
        "Awakening": {"label": "각성 [Awakening]", "color": "#FFD700", "bpm": (100, 160), "atmosphere": "Sacred, Enlightenment"},
        "Destruction": {"label": "파괴 [Destruction]", "color": "#FF2D2D", "bpm": (160, 220), "atmosphere": "Explosive, High-Gain"},
        "Han": {"label": "한 [Han]", "color": "#4A7CFF", "bpm": (60, 120), "atmosphere": "Melancholic, Deep Sorrow"},
        "Void": {"label": "허공 [Void]", "color": "#00E5A0", "bpm": (40, 80), "atmosphere": "Transcendent, Cosmic"},
        "Madness": {"label": "광기 [Madness]", "color": "#FF4500", "bpm": (130, 200), "atmosphere": "Chaotic, Liberation"},
    },
    "korean_instruments": {
        "Gayageum": {"label": "가야금 [Gayageum]", "suno_tag": "gayageum"},
        "Haegeum": {"label": "해금 [Haegeum]", "suno_tag": "haegeum fiddle"},
        "Daegeum": {"label": "대금 [Daegeum]", "suno_tag": "daegeum flute"},
        "Piri": {"label": "피리 [Piri]", "suno_tag": "piri oboe"},
        "Beomjong": {"label": "범종 [Temple Bell]", "suno_tag": "temple bell"},
        "Daebuk": {"label": "대북 [Daebuk Drum]", "suno_tag": "taiko drum"},
        "Janggu": {"label": "장구 [Janggu]", "suno_tag": "janggu drum"},
        "Kkwaenggwari": {"label": "꽱과리 [Gong]", "suno_tag": "kkwaenggwari gong"},
        "Jing": {"label": "징 [Jing]", "suno_tag": "jing large gong"},
    },
    "western_instruments": {
        "Elec_Guitar": {"label": "Electric Guitar", "suno_tag": "electric guitar, distortion"},
        "Rock_Drums": {"label": "Rock Drums", "suno_tag": "rock drums"},
        "Synth_Lead": {"label": "Synthesizer Lead", "suno_tag": "synthesizer lead"},
        "Synth_Pad": {"label": "Synth Pad", "suno_tag": "synth pad, ambient"},
        "Piano": {"label": "Grand Piano", "suno_tag": "grand piano"},
        "Violin": {"label": "Solo Violin", "suno_tag": "solo violin"},
        "Strings": {"label": "Orchestral Strings", "suno_tag": "orchestral strings"},
        "Choir": {"label": "Epic Choir", "suno_tag": "choir, epic vocals"},
        "Bass_Gtr": {"label": "Heavy Bass Guitar", "suno_tag": "heavy bass guitar"},
    },
    "western_rhythms": {
        "Rock": {"label": "록 [Rock]", "suno_prompt": "classic rock, power chords"},
        "Metal": {"label": "메탈 [Metal]", "suno_prompt": "heavy metal, double bass drum"},
        "Jazz": {"label": "재즈 [Jazz]", "suno_prompt": "jazz, swing rhythm"},
        "EDM": {"label": "EDM", "suno_prompt": "EDM, dance music drop"},
        "Blues": {"label": "블루스 [Blues]", "suno_prompt": "slow blues shuffle"},
        "Folk": {"label": "포크 [Folk]", "suno_prompt": "acoustic folk"},
        "Progressive": {"label": "프로그레시브", "suno_prompt": "progressive rock"},
    },
    "song_structures": {
        "ritual_4_verses": ["INTRO", "VERSE1", "PRE_CHORUS", "CHORUS1", "VERSE2", "BRIDGE", "VERSE3", "CHORUS2", "VERSE4", "OUTRO"],
        "minimal": ["INTRO", "VERSE1", "CHORUS", "VERSE2", "OUTRO"],
    },
    "vocal_types": {
        "male_rock": {"label": "남성 - 록", "suno_tag": "male vocal, raspy rock"},
        "male_deep": {"label": "남성 - 저음", "suno_tag": "male vocal, deep baritone"},
        "female_clear": {"label": "여성 - 청아한", "suno_tag": "female vocal, clear soprano"},
        "pansori": {"label": "판소리 창", "suno_tag": "pansori vocal, traditional Korean singing"},
        "chant": {"label": "주문/챈트", "suno_tag": "ritual chant, monotone"},
    },
}

def clean_text(text):
    if not text: return ""
    return re.sub(r'[\u4e00-\u9fff\(\)]+', '', text).strip()

def josa(word, j_type):
    if not word: return ""
    last_char = word[-1]
    if not (0xAC00 <= ord(last_char) <= 0xD7A3): return word
    has_batchim = (ord(last_char) - 0xAC00) % 28 > 0
    if j_type == 1: return word + ("은" if has_batchim else "는")
    return word

def generate_full_lyrics(title, context, vn):
    core = clean_text(title) or "진리"
    verses = {
        1: f"태초의 정적이 터져 나오던 그 날\n{josa(core, 1)} 하늘에 가득했네\n잃어버린 시원의 기억을 다시 깨운다",
        2: f"낡은 시스템이 붕괴하는 소리\n거대한 물결이 몰려온다\n{core} 우리의 심장을 두드린다",
        3: f"디지털과 영성의 경계에 서서\n우리는 무엇을 보는가\n{core} 울려 퍼지는 이 공간",
        4: f"이제 하나로 연결되는 시간\n우주의 마지막 코드이자 첫 소절\n{core} 영원히 울려 퍼지리라",
    }
    return verses.get(vn, verses[1])

def build_section(key, title, context, ki, wi, vn=1):
    ki_t = [STYLE_DB["korean_instruments"].get(k, {}).get("suno_tag", k) for k in ki]
    wi_t = [STYLE_DB["western_instruments"].get(w, {}).get("suno_tag", w) for w in wi]
    if key == "INTRO":
        return f"[Intro]\n[Professional Instrumental Session - Shamanic Fusion]\n[Instruments: {', '.join(ki_t + wi_t)}]\n[High-quality Studio Recording - No Vocals]"
    lyr = generate_full_lyrics(title, context, vn)
    return f"[{key}]\n{lyr}"

def build_full_song(title, context, struct_key, k_sel, w_sel):
    struct = STYLE_DB["song_structures"].get(struct_key, ["INTRO", "VERSE1", "VERSE2", "OUTRO"])
    result = {}
    vn = 1
    for key in struct:
        result[key] = build_section(key, title, context, k_sel, w_sel, vn)
        if "VERSE" in key: vn += 1
    return result

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@200;400;700&family=Noto+Sans+KR:wght@300;700&display=swap');
    :root { --accent: #FFE800; --bg: #000; }
    .stApp { background-color: #000; color: #fff !important; font-family: 'Outfit', 'Noto Sans KR', sans-serif; }
    p, span, div, li, label, .stMarkdown { color: #E0E0E0 !important; }
    h1, h2, h3 { color: #FFFFFF !important; }
    .stCode { background-color: #111 !important; color: #FFE800 !important; border: 1px solid #444 !important; }
    .app-title { font-family: 'Bebas Neue'; font-size: 4rem; color: var(--accent) !important; text-align: center; letter-spacing: 12px; margin-top: 20px; }
    .stButton > button { width: 100% !important; background: transparent !important; border: 2px solid var(--accent) !important; color: var(--accent) !important; font-family: 'Bebas Neue' !important; font-size: 2.2rem !important; height: 75px !important; transition: 0.3s; }
    .stButton > button:hover { background: var(--accent) !important; color: #000 !important; box-shadow: 0 0 30px var(--accent); }
    
    .stTextInput input, .stTextArea textarea, .stNumberInput input, 
    .stSelectbox div[data-baseweb="select"] > div,
    .stMultiSelect div[data-baseweb="select"] > div {
        background-color: #1A1A1A !important; color: #FFFFFF !important; border: 1px solid var(--accent) !important;
    }
    div[data-baseweb="popover"] div, div[data-baseweb="menu"] div { background-color: #1A1A1A !important; color: #FFFFFF !important; }
    li[role="option"]:hover { background-color: #333333 !important; color: var(--accent) !important; }
    </style>
    """, unsafe_allow_html=True)

def main():
    inject_css()
    st.markdown('<h1 class="app-title">PROJECT JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<div style="color:#FFE800; text-align:center; letter-spacing:8px; margin-bottom:40px;">[ MASTER FUSION v6.7 ]</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["⚡ SETUP", "🎵 STUDIO", "📖 OUTPUT"])

    with t1:
        title = st.text_input("SONG TITLE", "개벽의 소리")
        context = st.text_area("PHILOSOPHY SEED", "사상을 입력하세요...", height=150)
        struct_key = st.selectbox("STRUCTURE", list(STYLE_DB["song_structures"].keys()))
        b_min = st.number_input("BPM Min", 40, 240, 100)
        b_max = st.number_input("BPM Max", 40, 240, 140)

    with t2:
        k_sel = st.multiselect("KOREAN INSTRUMENTS", list(STYLE_DB["korean_instruments"].keys()), ["Janggu", "Gayageum"])
        w_sel = st.multiselect("WESTERN INSTRUMENTS", list(STYLE_DB["western_instruments"].keys()), ["Elec_Guitar", "Rock_Drums"])
        r_key = st.selectbox("MAIN GENRE", list(STYLE_DB["western_rhythms"].keys()))
        v_key = st.selectbox("VOCAL RITUAL", list(STYLE_DB["vocal_types"].keys()))
        v_tone = st.text_input("VOCAL TONE DETAIL", "Professional and powerful")

    with t3:
        if st.button("🔥 GENERATE MASTER RITUAL"):
            ki_t = [STYLE_DB["korean_instruments"][k]["suno_tag"] for k in k_sel]
            wi_t = [STYLE_DB["western_instruments"][k]["suno_tag"] for k in w_sel]
            base_prompt = "fluxus ritual, avant-garde music, shamanic spirit, "
            genre_p = STYLE_DB["western_rhythms"][r_key]["suno_prompt"]
            vocal_p = STYLE_DB["vocal_types"][v_key]["suno_tag"]
            st.session_state["p_box"] = f"{base_prompt}{genre_p}, {', '.join(ki_t + wi_t)}, {vocal_p}, {v_tone}, {b_min}-{b_max} BPM, Korean lyrics"
            st.session_state["s_data"] = build_full_song(title, context, struct_key, k_sel, w_sel)

        if "p_box" in st.session_state:
            st.markdown("### 1. SUNO STYLE BOX")
            st.code(st.session_state["p_box"], language="text")
            st.markdown("### 2. MASTER LYRICS & FLOW")
            full_text = "\n\n".join(st.session_state["s_data"].values())
            st.code(full_text, language="text")

if __name__ == "__main__":
    main()
