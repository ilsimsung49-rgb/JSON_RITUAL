import streamlit as st
import random
import re

# ==========================================================
#  [PROJECT JSON RITUAL v6.4 - FLEXIBLE GENRE SYSTEM]
#  Genre Flexibility & Professional Intro Logic
# ==========================================================

STYLE_DB = {
    "moods": {
        "Destruction": {
            "label": "파괴 [Destruction]",
            "color": "#FF2D2D",
            "bpm_default": (160, 220),
            "rhythm": "Blast Beat Metal",
            "keywords": ["분노", "파괴", "혁명", "폭발", "전쟁"],
            "atmosphere": "Explosive, High-Gain",
            "icon": "💥",
        },
        "Han": {
            "label": "한 [Han]",
            "color": "#4A7CFF",
            "bpm_default": (60, 140),
            "rhythm": "Slow Jajinmori (12/8)",
            "keywords": ["슬픔", "한", "이별", "고독", "눈물"],
            "atmosphere": "Melancholic, Deep Sorrow",
            "icon": "😢",
        },
        "Void": {
            "label": "허공 [Void]",
            "color": "#00E5A0",
            "bpm_default": (40, 80),
            "rhythm": "Free Tempo Drone",
            "keywords": ["우주", "신비", "철학", "명상", "무극"],
            "atmosphere": "Transcendent, Cosmic",
            "icon": "🌌",
        },
        "Awakening": {
            "label": "각성 [Awakening]",
            "color": "#FFD700",
            "bpm_default": (100, 160),
            "rhythm": "Majestic Grand Whimori",
            "keywords": ["각성", "깨달음", "홍익", "개벽"],
            "atmosphere": "Sacred, Enlightenment",
            "icon": "🙏",
        },
    },

    "korean_instruments": {
        "Gayageum":     {"label": "가야금 [Gayageum]",          "suno_tag": "gayageum"},
        "Haegeum":      {"label": "해금 [Haegeum]",             "suno_tag": "haegeum fiddle"},
        "Daegeum":      {"label": "대금 [Daegeum Flute]",       "suno_tag": "daegeum flute"},
        "Piri":         {"label": "피리 [Piri]",                 "suno_tag": "piri oboe"},
        "Beomjong":     {"label": "범종 [Temple Bell]",          "suno_tag": "temple bell"},
        "Daebuk":       {"label": "대북 [Grand Taiko Drum]",    "suno_tag": "taiko drum"},
        "Janggu":       {"label": "장구 [Janggu]",               "suno_tag": "janggu drum"},
        "Kkwaenggwari": {"label": "꽱과리 [Kkwaenggwari]",       "suno_tag": "kkwaenggwari small gong"},
        "Jing":         {"label": "징 [Jing Gong]",              "suno_tag": "jing large gong"},
        "Buk":          {"label": "북 [Buk Barrel Drum]",       "suno_tag": "buk barrel drum"},
    },

    "western_instruments": {
        "Elec_Guitar":   {"label": "Electric Guitar [Distortion]",    "suno_tag": "electric guitar, distortion"},
        "Lead_Guitar":   {"label": "Lead Guitar [Solo]",              "suno_tag": "lead guitar solo"},
        "Acous_Guitar":  {"label": "Acoustic Guitar [Folk]",          "suno_tag": "acoustic guitar"},
        "Rock_Drums":    {"label": "Rock Drum Kit",                   "suno_tag": "rock drums"},
        "Synth_Lead":    {"label": "Synthesizer Lead",                "suno_tag": "synthesizer lead"},
        "Synth_Pad":     {"label": "Synthesizer Pad [Ambient]",       "suno_tag": "synth pad, ambient"},
        "Piano":         {"label": "Grand Piano",                     "suno_tag": "grand piano"},
        "Violin":        {"label": "Solo Violin",                     "suno_tag": "solo violin"},
        "Strings":       {"label": "Orchestral Strings",              "suno_tag": "orchestral strings"},
        "Choir":         {"label": "Epic Choir",                      "suno_tag": "choir, epic vocals"},
    },

    "western_rhythms": {
        "Rock": {
            "label": "록 [Rock]",
            "suno_prompt": "classic rock, power chords, driving drums",
        },
        "Hard_Rock_Metal": {
            "label": "하드록 / 메탈 [Hard Rock Metal]",
            "suno_prompt": "heavy metal, distorted riffs, double bass drum",
        },
        "Blues": {
            "label": "블루스 [Blues]",
            "suno_prompt": "slow blues shuffle, soulful guitar",
        },
        "EDM": {
            "label": "EDM / 일렉트로닉",
            "suno_prompt": "EDM, dance music, synthesizer lead, 808 bass",
        },
        "Folk": {
            "label": "포크 [Folk]",
            "suno_prompt": "acoustic folk, fingerpicking guitar",
        },
        "Jazz": {
            "label": "재즈 [Jazz]",
            "suno_prompt": "jazz, swing rhythm, walking bass",
        },
        "Progressive": {
            "label": "프로그레시브 [Progressive]",
            "suno_prompt": "progressive rock, complex arrangement, odd time signature",
        },
    },

    "song_structures": {
        "ritual_4_verses": ["INTRO", "VERSE1", "PRE_CHORUS", "CHORUS1", "VERSE2", "BRIDGE", "VERSE3", "CHORUS2", "VERSE4", "OUTRO"],
        "minimal": ["INTRO", "VERSE1", "CHORUS", "VERSE2", "CHORUS", "OUTRO"],
    },

    "vocal_types": {
        "male_deep":     {"label": "남성 - 저음", "suno_tag": "male vocal, deep baritone"},
        "male_raspy":   {"label": "남성 - 거친 록", "suno_tag": "male vocal, raspy rock voice"},
        "female_alto":  {"label": "여성 - 알토", "suno_tag": "female vocal, warm alto"},
        "pansori":      {"label": "판소리 창", "suno_tag": "pansori vocal, traditional Korean singing"},
    },
}

def clean_text(text):
    if not text: return ""
    text = re.sub(r'[\u4e00-\u9fff]+', '', text) 
    text = re.sub(r'\([^)]*[A-Za-z][^)]*\)', '', text) 
    text = text.replace('(', '').replace(')', '') 
    return text.strip()

def josa(word, j_type):
    if not word: return ""
    last_char = word[-1]
    if not (0xAC00 <= ord(last_char) <= 0xD7A3): return word
    has_batchim = (ord(last_char) - 0xAC00) % 28 > 0
    if j_type == 1: return f"{word}은" if has_batchim else f"{word}는"
    elif j_type == 2: return f"{word}이" if has_batchim else f"{word}가"
    elif j_type == 3: return f"{word}을" if has_batchim else f"{word}를"
    return word

def generate_lyrics(title, context, verse_num):
    c_title = clean_text(title) or "진실의 소리"
    core = c_title.split()[0] if c_title.split() else "진리"
    
    verses = {
        1: [f"태초의 정적이 터져 나오던 그 날\n{josa(core, 1)} 하늘에 가득했네\n잃어버린 시원의 기억을 깨우며\n새로운 길을 찾아 나선다"],
        2: [f"낡은 시스템이 붕괴하는 소리\n거대한 물결이 몰려온다\n{josa(core, 2)} 우리의 심장을 두드리고\n닫혀있던 문이 열린다"],
        3: [f"가상과 현실의 경계에 서서\n우리는 무엇을 보는가\n{josa(core, 3)} 노래하며 나아가리\n빛과 어둠이 교차하는 이 공간"],
        4: [f"이제 하나로 연결되는 시간\n우주의 마지막 코드이자 첫 소절\n{josa(core, 1)} 영원히 울려 퍼지리니\n우리는 모두 빛의 자녀들"],
    }
    return random.choice(verses.get(verse_num, verses[1]))

def build_section(key, title, context, ki, wi, rhythm_key, vn=1):
    ki_tags = [STYLE_DB["korean_instruments"].get(k, {}).get("suno_tag", k) for k in ki]
    wi_tags = [STYLE_DB["western_instruments"].get(w, {}).get("suno_tag", w) for w in wi]
    
    if key == "INTRO":
        return (
            f"[Intro]\n"
            f"[Professional Instrumental Session - Pure Expertise]\n"
            f"[Masterful performance involving: {', '.join(ki_tags + wi_tags)}]\n"
            f"[Strong rhythmic fusion of Eastern and Western instruments]\n"
            f"[High-quality Studio Recording - Instrumental Only]\n"
            f"[No Vocals]"
        )

    lyr = generate_lyrics(title, context, vn)
    rhy = STYLE_DB["western_rhythms"].get(rhythm_key, list(STYLE_DB["western_rhythms"].values())[0])
    tag = f"[{rhy['label']} {key}]"
    return f"{tag}\n{lyr}"

def build_full_song(title, context, struct_key, k_sel, w_sel, rhythm_key):
    struct = STYLE_DB["song_structures"].get(struct_key, STYLE_DB["song_structures"]["ritual_4_verses"])
    result = {"Title": clean_text(title)}
    v_cnt = 0
    for key in struct:
        if "VERSE" in key or "CHORUS" in key or "BRIDGE" in key: v_cnt += 1
        result[key] = build_section(key, title, context, k_sel, w_sel, rhythm_key, max(1, v_cnt))
    return result

def build_suno_prompt(s, ki_tags, wi_tags):
    rhy_data = STYLE_DB["western_rhythms"].get(s["rhythm_key"], {})
    vocal_data = STYLE_DB["vocal_types"].get(s["vocal_key"], {})
    
    base_philosophy = "fluxus ritual, avant-garde awakening music, shamanic Korean spirit, deconstructed soundscape, "
    genre_part = f"{rhy_data.get('suno_prompt', '')}, "
    inst_part = f"{', '.join(ki_tags + wi_tags)}, "
    vocal_part = f"{vocal_data.get('suno_tag', '')}, {s['vocal_tone']}, "
    bpm_part = f"{s['b_min']}-{s['b_max']} BPM, "
    
    suno_style = f"{base_philosophy}{genre_part}{inst_part}{vocal_part}{bpm_part}sung in Korean, no auto-tune"
    if len(suno_style) > 1000: suno_style = suno_style[:997] + "..."

    return suno_style

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@200;400;700&family=Share+Tech+Mono&family=Noto+Sans+KR:wght@300;700&display=swap');
    :root { --accent: #FFE800; --bg: #000; }
    .stApp { background-color: #000; color: #fff !important; font-family: 'Outfit', sans-serif; }
    p, span, div, li, label, .stMarkdown { color: #E0E0E0 !important; }
    h1, h2, h3 { color: #FFFFFF !important; }
    .stCode { background-color: #111 !important; color: #FFE800 !important; border: 1px solid #444 !important; }
    .app-title { font-family: 'Bebas Neue'; font-size: 4rem; color: var(--accent) !important; text-align: center; letter-spacing: 12px; margin-top: 20px; text-shadow: 0 0 20px rgba(255, 232, 0, 0.6); }
    .panel-header { font-family: 'Bebas Neue'; color: var(--accent); font-size: 1.3rem; letter-spacing: 3px; border-bottom: 2px solid var(--accent); margin-bottom: 15px; padding-bottom: 5px; }
    .stButton > button { width: 100% !important; background: transparent !important; border: 2px solid var(--accent) !important; color: var(--accent) !important; font-family: 'Bebas Neue' !important; font-size: 2rem !important; height: 70px !important; transition: 0.4s; }
    .stButton > button:hover { background: var(--accent) !important; color: #000 !important; box-shadow: 0 0 30px var(--accent); }
    
    .stTextInput input, .stTextArea textarea, .stNumberInput input, 
    .stSelectbox div[data-baseweb="select"] > div,
    .stMultiSelect div[data-baseweb="select"] > div {
        background-color: #1A1A1A !important; color: #FFFFFF !important; border: 1px solid var(--accent) !important;
    }

    /* 드롭다운 메뉴 아이템 시인성 강화 */
    div[data-baseweb="popover"] div, 
    div[data-baseweb="menu"] div, 
    div[data-baseweb="list-box"] div,
    ul[data-baseweb="menu"] li {
        background-color: #1A1A1A !important; 
        color: #FFFFFF !important;
    }
    
    /* 선택된 항목 및 호버 효과 */
    li[role="option"]:hover, 
    div[data-baseweb="menu"] div:hover {
        background-color: #333333 !important;
        color: var(--accent) !important;
    }
    
    /* 멀티셀렉트 태그 글자색 */
    span[data-baseweb="tag"] {
        background-color: var(--accent) !important;
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="JSON RITUAL v6.4", page_icon="🎵", layout="wide")
    inject_css()
    st.markdown('<h1 class="app-title">PROJECT JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<div style="color:#FFE800; text-align:center; letter-spacing:8px; opacity:0.8; margin-bottom:30px;">[ FLEXIBLE RITUAL v6.4 ]</div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["⚡ SETUP", "🎵 STUDIO", "📖 OUTPUT"])

    with tab1:
        col1, col2 = st.columns(2, gap="large")
        with col1:
            st.markdown('<div class="panel-header">🎼 SEED</div>', unsafe_allow_html=True)
            title = st.text_input("SONG TITLE", placeholder="예: 개벽의 소리")
            context = st.text_area("PHILOSOPHY SEED", placeholder="사상을 입력하세요...", height=250)
        with col2:
            st.markdown('<div class="panel-header">🌀 RITUAL STRUCTURE</div>', unsafe_allow_html=True)
            struct_key = st.radio("STRUCTURE", list(STYLE_DB["song_structures"].keys()), format_func=lambda x: x.replace("_", " ").upper())
            st.markdown('<div class="panel-header">⏱ MANUAL BPM CONTROL</div>', unsafe_allow_html=True)
            b_min = st.number_input("BPM Minimum", 40, 240, 100)
            b_max = st.number_input("BPM Maximum", 40, 240, 140)

    with tab2:
        st.markdown('<div class="panel-header">🎎 SOUND DESIGN</div>', unsafe_allow_html=True)
        col_inst = st.columns(2)
        with col_inst[0]:
            k_sel = st.multiselect("KOREAN INSTRUMENTS", list(STYLE_DB["korean_instruments"].keys()), default=["Janggu"])
        with col_inst[1]:
            w_sel = st.multiselect("WESTERN INSTRUMENTS", list(STYLE_DB["western_instruments"].keys()), default=["Elec_Guitar", "Rock_Drums"])
        
        st.markdown('<div class="panel-header">🎸 MAIN GENRE</div>', unsafe_allow_html=True)
        rhythm_key = st.selectbox("CHOOSE MAIN GENRE", list(STYLE_DB["western_rhythms"].keys()))
        
        v_col1, v_col2 = st.columns(2)
        with v_col1:
            vocal_key = st.selectbox("VOCAL TYPE", list(STYLE_DB["vocal_types"].keys()), index=1)
        with v_col2:
            vocal_tone = st.text_input("VOCAL TONE DETAIL", "Professional and powerful")

    with tab3:
        if st.button("🔥 GENERATE MASTER RITUAL"):
            if not title: st.error("No Title!")
            else:
                ki_tags = [STYLE_DB["korean_instruments"][k]["suno_tag"] for k in k_sel]
                wi_tags = [STYLE_DB["western_instruments"][k]["suno_tag"] for k in w_sel]
                settings = {"rhythm_key": rhythm_key, "vocal_key": vocal_key, "vocal_tone": vocal_tone, "b_min": b_min, "b_max": b_max}
                
                suno_style = build_suno_prompt(settings, ki_tags, wi_tags)
                song_data = build_full_song(title, context, struct_key, k_sel, w_sel, rhythm_key)
                
                st.session_state["suno_style"] = suno_style
                st.session_state["song_data"] = song_data

        if "suno_style" in st.session_state:
            st.markdown("### 1️⃣ SUNO STYLE BOX")
            st.code(st.session_state["suno_style"], language="text")
            st.markdown("### 2️⃣ MASTER LYRICS & INTRO")
            full_lyr = ""
            for k, v in st.session_state["song_data"].items():
                if k != "Title": full_lyr += v + "\n\n"
            st.code(full_lyr.strip(), language="text")

if __name__ == "__main__":
    main()
