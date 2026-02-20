import streamlit as st
import random
import re

# 1. MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="JSON RITUAL v6.4", layout="wide")

# ==========================================================
#  PROJECT JSON RITUAL v6.4.3 [ULTRA-STABLE]
# ==========================================================

STYLE_DB = {
    "moods": {
        "Awakening": {
            "label": "각성 [Awakening]",
            "bpm_default": (100, 160),
            "atmosphere": "Sacred, Enlightenment",
        },
    },
    "korean_instruments": {
        "Gayageum":     {"label": "가야금 [Gayageum]", "suno_tag": "gayageum"},
        "Janggu":       {"label": "장구 [Janggu]", "suno_tag": "janggu drum"},
    },
    "western_instruments": {
        "Elec_Guitar":   {"label": "Electric Guitar", "suno_tag": "electric guitar, distortion"},
        "Rock_Drums":    {"label": "Rock Drum Kit", "suno_tag": "rock drums"},
    },
    "western_rhythms": {
        "Rock": {"label": "록 [Rock]", "suno_prompt": "classic rock, power chords"},
        "Jazz": {"label": "재즈 [Jazz]", "suno_prompt": "jazz, swing rhythm"},
        "EDM": {"label": "EDM", "suno_prompt": "EDM, dance music"},
        "Folk": {"label": "포크 [Folk]", "suno_prompt": "acoustic folk"},
    },
    "song_structures": {
        "ritual_4_verses": ["INTRO", "VERSE1", "VERSE2", "VERSE3", "VERSE4", "OUTRO"],
    },
    "vocal_types": {
        "male": {"label": "남성 보컬", "suno_tag": "male vocal"},
        "female": {"label": "여성 보컬", "suno_tag": "female vocal"},
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
        1: f"태초의 빛이 내리는 이곳\n{josa(core, 1)} 하늘에 가득하네\n우리의 길을 찾아 나선다",
        2: f"닫힌 문이 열리는 소리\n거대한 물결이 몰려온다\n{core} 노래하며 나아가리",
        3: f"현실과 이상의 경계에서\n우리는 무엇을 보는가\n{core} 울려 퍼지는 이 공간",
        4: f"이제 하나로 연결되는 시간\n우주의 마지막 소절\n{core} 영원히 기억되리",
    }
    return verses.get(vn, verses[1])

def build_section(key, title, ki, wi, vn=1):
    ki_tags = [STYLE_DB["korean_instruments"].get(k, {}).get("suno_tag", k) for k in ki]
    wi_tags = [STYLE_DB["western_instruments"].get(w, {}).get("suno_tag", w) for w in wi]
    if key == "INTRO":
        return f"[Intro]\n[Instrumental Session: {', '.join(ki_tags + wi_tags)}]\n[Pure expertise, no vocals]"
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
    base = "fluxus ritual, avant-garde music, shamanic spirit, "
    genre = STYLE_DB["western_rhythms"].get(s["rhythm_key"], {}).get("suno_prompt", "")
    inst = ", ".join(ki_tags + wi_tags)
    vocal = STYLE_DB["vocal_types"].get(s["vocal_key"], {}).get("suno_tag", "")
    return f"{base}{genre}, {inst}, {vocal}, {s['b_min']}-{s['b_max']} BPM, Korean lyrics"

def inject_css():
    st.markdown("""
    <style>
    :root { --accent: #FFE800; }
    .stApp { background-color: #000; color: #fff; }
    p, span, label, div { color: #E0E0E0 !important; }
    h1, h2, h3 { color: #FFF !important; }
    .stCode { background-color: #111 !important; color: #FFE800 !important; }
    .app-title { color: var(--accent) !important; text-align: center; font-size: 3rem; }
    </style>
    """, unsafe_allow_html=True)

def main():
    inject_css()
    st.markdown('<h1 class="app-title">PROJECT JSON RITUAL</h1>', unsafe_allow_html=True)
    t1, t2, t3 = st.tabs(["SETUP", "STUDIO", "OUTPUT"])
    with t1:
        title = st.text_input("SONG TITLE", "개벽의 소리")
        b_min = st.number_input("BPM Min", 40, 240, 100)
        b_max = st.number_input("BPM Max", 40, 240, 140)
    with t2:
        k_sel = st.multiselect("KOREAN", list(STYLE_DB["korean_instruments"].keys()), ["Janggu"])
        w_sel = st.multiselect("WESTERN", list(STYLE_DB["western_instruments"].keys()), ["Elec_Guitar"])
        r_key = st.selectbox("GENRE", list(STYLE_DB["western_rhythms"].keys()))
        v_key = st.selectbox("VOCAL", list(STYLE_DB["vocal_types"].keys()))
    with t3:
        if st.button("GENERATE"):
            ki_t = [STYLE_DB["korean_instruments"][k]["suno_tag"] for k in k_sel]
            wi_t = [STYLE_DB["western_instruments"][w]["suno_tag"] for w in w_sel]
            s_dict = {"rhythm_key": r_key, "vocal_key": v_key, "b_min": b_min, "b_max": b_max}
            st.session_state["p"] = build_suno_prompt(s_dict, ki_t, wi_t)
            st.session_state["s"] = build_full_song(title, "ritual_4_verses", k_sel, w_sel)
        if "p" in st.session_state:
            st.code(st.session_state["p"])
            lyr = "\n\n".join(st.session_state["s"].values())
            st.code(lyr)

if __name__ == "__main__":
    main()
