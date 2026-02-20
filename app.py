import streamlit as st
import random
import re

# [CRITICAL] Must be the very first Streamlit command
st.set_page_config(page_title="JSON RITUAL v6.5", layout="wide")

# ==========================================================
#  PROJECT JSON RITUAL v6.5 [PROFESSIONAL STABLE]
# ==========================================================

STYLE_DB = {
    "moods": {
        "Awakening": {
            "label": "각성 [Awakening]",
            "bpm_default": (100, 160),
            "atmosphere": "Sacred Avant-Garde, Enlightenment",
        },
        "Destruction": {
            "label": "파괴 [Destruction]",
            "bpm_default": (160, 220),
            "atmosphere": "Explosive, High-Gain Ritual",
        },
        "Han": {
            "label": "한 [Han]",
            "bpm_default": (60, 120),
            "atmosphere": "Melancholic, Deep Sorrow",
        },
    },
    "korean_instruments": {
        "Gayageum":     {"label": "가야금 [Gayageum]", "suno_tag": "gayageum"},
        "Haegeum":      {"label": "해금 [Haegeum]", "suno_tag": "haegeum fiddle"},
        "Daegeum":      {"label": "대금 [Daegeum]", "suno_tag": "daegeum flute"},
        "Janggu":       {"label": "장구 [Janggu]", "suno_tag": "janggu drum"},
        "Daebuk":       {"label": "대북 [Daebuk]", "suno_tag": "taiko drum"},
    },
    "western_instruments": {
        "Elec_Guitar":   {"label": "Electric Guitar", "suno_tag": "electric guitar, distortion"},
        "Rock_Drums":    {"label": "Rock Drums", "suno_tag": "rock drums"},
        "Synth":         {"label": "Synthesizer", "suno_tag": "synthesizer lead"},
        "Piano":         {"label": "Grand Piano", "suno_tag": "grand piano"},
    },
    "western_rhythms": {
        "Rock": {"label": "록 [Rock]", "suno_prompt": "classic rock, power chords"},
        "Metal": {"label": "메탈 [Metal]", "suno_prompt": "heavy metal, double bass drum"},
        "Jazz": {"label": "재즈 [Jazz]", "suno_prompt": "jazz, swing rhythm"},
        "EDM": {"label": "EDM", "suno_prompt": "EDM, dance music drop"},
        "Blues": {"label": "블루스 [Blues]", "suno_prompt": "slow blues shuffle"},
    },
    "song_structures": {
        "ritual_4_verses": ["INTRO", "VERSE1", "VERSE2", "VERSE3", "VERSE4", "OUTRO"],
        "minimal": ["INTRO", "VERSE1", "CHORUS", "VERSE2", "OUTRO"],
    },
    "vocal_types": {
        "male_rock": {"label": "남성 - 록", "suno_tag": "male vocal, raspy rock"},
        "male_deep": {"label": "남성 - 저음", "suno_tag": "male vocal, deep baritone"},
        "female_clear": {"label": "여성 - 청아한", "suno_tag": "female vocal, clear soprano"},
        "pansori": {"label": "판소리", "suno_tag": "pansori vocal, traditional Korean singing"},
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

def generate_lyrics(title, vn):
    core = clean_text(title) or "진리"
    verses = {
        1: f"태초의 정적이 터져 나오던 그 날\n{josa(core, 1)} 하늘에 가득했네\n잃어버린 시원의 기억을 다시 깨운다",
        2: f"낡은 시스템이 붕괴하는 소리\n거대한 물결이 몰려온다\n{core} 우리의 심장을 두드린다",
        3: f"디지털과 영성의 경계에 서서\n우리는 무엇을 보는가\n{core} 울려 퍼지는 이 공간",
        4: f"이제 하나로 연결되는 시간\n우주의 마지막 코절\n{core} 영원히 울려 퍼지리라",
    }
    return verses.get(vn, verses[1])

def build_section(key, title, ki, wi, vn=1):
    ki_tags = [STYLE_DB["korean_instruments"].get(k, {}).get("suno_tag", k) for k in ki]
    wi_tags = [STYLE_DB["western_instruments"].get(w, {}).get("suno_tag", w) for w in wi]
    if key == "INTRO":
        return f"[Intro]\n[Professional Instrumental Session - Pure Expertise]\n[Instruments: {', '.join(ki_tags + wi_tags)}]\n[High-quality Studio Recording - No Vocals]"
    lyr = generate_lyrics(title, vn)
    return f"[{key}]\n{lyr}"

def build_full_song(title, struct_key, k_sel, w_sel):
    struct = STYLE_DB["song_structures"].get(struct_key, ["INTRO", "VERSE1", "VERSE2", "OUTRO"])
    result = {}
    vn = 1
    for key in struct:
        result[key] = build_section(key, title, k_sel, w_sel, vn)
        if "VERSE" in key: vn += 1
    return result

def build_suno_prompt(s, ki_tags, wi_tags):
    base_philosophy = "fluxus ritual, avant-garde music, shamanic spirit, deconstructed, "
    genre_part = STYLE_DB["western_rhythms"].get(s["rhythm_key"], {}).get("suno_prompt", "")
    inst_part = ", ".join(ki_tags + wi_tags)
    vocal_part = STYLE_DB["vocal_types"].get(s["vocal_key"], {}).get("suno_tag", "male vocal")
    prompt = f"{base_philosophy}{genre_part}, {inst_part}, {vocal_part}, {s['b_min']}-{s['b_max']} BPM, Korean lyrics, no auto-tune"
    return prompt[:1000]

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@200;400;700&display=swap');
    :root { --accent: #FFE800; --bg: #000; }
    .stApp { background-color: #000; color: #fff !important; font-family: 'Outfit', sans-serif; }
    p, span, div, li, label, .stMarkdown { color: #E0E0E0 !important; }
    h1, h2, h3 { color: #FFFFFF !important; }
    .stCode { background-color: #111 !important; color: #FFE800 !important; border: 1px solid #444 !important; }
    .app-title { font-family: 'Bebas Neue'; font-size: 3.5rem; color: var(--accent) !important; text-align: center; letter-spacing: 10px; margin-top: 20px; }
    .stButton > button { width: 100% !important; background: transparent !important; border: 2px solid var(--accent) !important; color: var(--accent) !important; font-family: 'Bebas Neue' !important; font-size: 1.8rem !important; height: 60px !important; transition: 0.3s; }
    .stButton > button:hover { background: var(--accent) !important; color: #000 !important; box-shadow: 0 0 20px var(--accent); }
    div[data-baseweb="popover"] div, div[data-baseweb="menu"] div, ul[data-baseweb="menu"] li { background-color: #1A1A1A !important; color: #FFFFFF !important; }
    li[role="option"]:hover { background-color: #333333 !important; color: var(--accent) !important; }
    </style>
    """, unsafe_allow_html=True)

def main():
    inject_css()
    st.markdown('<h1 class="app-title">PROJECT JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<div style="color:#FFE800; text-align:center; letter-spacing:5px; margin-bottom:30px;">[ MASTER FUSION v6.5 ]</div>', unsafe_allow_html=True)
    t1, t2, t3 = st.tabs(["SETUP", "STUDIO", "OUTPUT"])
    with t1:
        title = st.text_input("TITLE", "개벽의 소리")
        context = st.text_area("PHILOSOPHY", "사상을 입력하세요...", height=150)
        struct_key = st.selectbox("STRUCTURE", list(STYLE_DB["song_structures"].keys()))
        b_min = st.number_input("BPM Min", 40, 240, 100)
        b_max = st.number_input("BPM Max", 40, 240, 140)
    with t2:
        k_sel = st.multiselect("KOREAN INSTRUMENTS", list(STYLE_DB["korean_instruments"].keys()), ["Janggu"])
        w_sel = st.multiselect("WESTERN INSTRUMENTS", list(STYLE_DB["western_instruments"].keys()), ["Elec_Guitar"])
        r_key = st.selectbox("GENRE", list(STYLE_DB["western_rhythms"].keys()))
        v_key = st.selectbox("VOCAL", list(STYLE_DB["vocal_types"].keys()))
    with t3:
        if st.button("GENERATE RITUAL"):
            ki_t = [STYLE_DB["korean_instruments"][k]["suno_tag"] for k in k_sel]
            wi_t = [STYLE_DB["western_instruments"][w]["suno_tag"] for w in w_sel]
            s_set = {"rhythm_key": r_key, "vocal_key": v_key, "b_min": b_min, "b_max": b_max}
            st.session_state["p_box"] = build_suno_prompt(s_set, ki_t, wi_t)
            st.session_state["s_data"] = build_full_song(title, struct_key, k_sel, w_sel)
        if "p_box" in st.session_state:
            st.code(st.session_state["p_box"], language="text")
            full_text = "\n\n".join(st.session_state["s_data"].values())
            st.code(full_text, language="text")

if __name__ == "__main__":
    main()
