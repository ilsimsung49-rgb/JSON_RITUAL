import streamlit as st
import random
import re

# [CRITICAL] PAGE CONFIG
st.set_page_config(page_title="JSON RITUAL v8.4", page_icon="👹", layout="wide")

# ==========================================================
#  PROJECT JSON RITUAL v8.4 [ULTIMATE CONTENT RESTORATION]
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
        "Funk_Groove": "funk, slap bass, groovy rhythm",
        "Psychedelic_Rock": "psychedelic rock, trippy effects, 60s atmosphere",
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
        "Janggu": "janggu drum", "Kkwaenggwari": "kkwaenggwari gong", "Jing": "jing large gong", "Buk": "buk barrel drum",
        "Sogo": "sogo small drum", "Ajaeng": "ajaeng bowed zither"
    },
    "western_instruments": {
        "Elec_Dist": "electric guitar distortion", "Elec_Lead": "lead guitar solo", 
        "Elec_Rhythm": "rhythm guitar crunch", "Acous_Guitar": "acoustic guitar",
        "Bass": "heavy bass guitar", "Double_Bass": "double bass drum, blast beat",
        "Rock_Drums": "rock drums", "Percussion": "world percussion",
        "Synth_Chaos": "modular synthesizer noise", "808_Sub": "808 sub bass",
        "Piano": "grand piano", "Rhodes": "Rhodes electric piano", "Organ": "hammond organ",
        "Violin": "solo violin", "Cello": "deep cello solo", "Strings": "orchestral strings",
        "Epic_Choir": "epic cinematic choir", "Brass": "powerful brass section",
        "Harmonica": "harmonica", "Pipe_Organ": "pipe organ",
        "Drum_Machine": "TR-808 drum machine", "Sequencer": "analog sequencer",
        "Turntable": "turntable scratches, foley noise"
    },
    "vocal_rituals": {
        "Avant_Screams": {"label": "전위적 괴성 [Experimental Screams]", "tag": "avant-garde screams, abstract vocalizations, shouting"},
        "Shaman_Deep": {"label": "샤먼/주술 낮고 거친목소리", "tag": "male shamanic growl, ritualistic deep chanting, primal"},
        "Pansori_Husky": {"label": "허스키한 판소리 도성", "tag": "pansori vocal, traditional Korean singing, husky"},
        "Clear_Soprano": {"label": "청아한 소프라노 [Ethereal]", "tag": "clear ethereal soprano, heavenly female voice"},
        "Pure_Children": {"label": "청아한 소년/소녀 합창", "tag": "pure children choir, ethereal boys choir"},
        "Husky_Rock": {"label": "거친 허스키 록 보컬", "tag": "raspy husky male rock vocal, gritty"},
        "Deep_Void": {"label": "낮고 깊은 바리톤 [Void]", "tag": "exceptionally deep male baritone, resonant"},
        "Monastic_Chant": {"label": "단조로운 주문 [Monastic]", "tag": "monotone ritual chant, hypnotic drone"},
        "Soulful_Alto": {"label": "소울풀한 깊은 여성보컬", "tag": "soulful deep alto female vocal"},
        "Hypnotic_Whispers": {"label": "몽환적인 속삭임", "tag": "hypnotic whispers, mysterious breathing"},
        "Narration": {"label": "나레이션/대서사 낭독", "tag": "grand spoken word narrative, mystical"},
        "Industrial_Vox": {"label": "인더스트리얼 변조 보컬", "tag": "distorted industrial vocals, mechanical"},
        "Grand_Choir": {"label": "웅장한 대규모 합창", "tag": "grand epic cinematic choir"},
        "AI_Cyber": {"label": "사이버네틱 AI 목소리", "tag": "cybernetic artificial voice, monotone"},
        "Buddhist_Chant": {"label": "전통 범패/염불", "tag": "traditional Buddhist chant, Beompae ritual"}
    }
}

def inject_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@200;400;700&family=Noto+Sans+KR:wght@300;700&display=swap');
    .stApp { background-color: #000; color: #fff !important; font-family: 'Outfit', 'Noto Sans KR', sans-serif; }
    p, span, div, li, label, .stMarkdown { color: #FFFFFF !important; }
    .stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div { background-color: #111 !important; color: #FFF !important; border: 1px solid #FFE800 !important; }
    .app-title { font-family: 'Bebas Neue'; font-size: 4.5rem; color: #FFE800 !important; text-align: center; letter-spacing: 15px; margin-top: 30px; }
    .ritual-box { background-color: #080808 !important; border: 2px solid #FFE800 !important; padding: 40px !important; margin-bottom: 40px !important; border-radius: 15px !important; }
    .ritual-content { color: #FFE800 !important; font-family: 'Noto Sans KR', sans-serif !important; font-size: 1.4rem !important; line-height: 2.5 !important; white-space: pre-wrap !important; margin: 0 !important; }
    .ritual-label { font-family: 'Bebas Neue' !important; color: #FFFFFF !important; font-size: 2rem !important; letter-spacing: 5px; border-bottom: 1px solid #333; padding-bottom: 10px; margin-bottom: 25px; }
    .stButton > button { width: 100% !important; background: transparent !important; border: 3px solid #FFE800 !important; color: #FFE800 !important; font-family: 'Bebas Neue' !important; font-size: 2.5rem !important; height: 85px !important; }
    .stButton > button:hover { background: #FFE800 !important; color: #000 !important; }
    div[data-baseweb="popover"] * { background-color: #111 !important; color: #FFF !important; }
    li[role="option"]:hover { background-color: #FFE800 !important; color: #000 !important; }
    </style>
    """, unsafe_allow_html=True)

def generate_grand_narrative(title):
    core = title or "개벽"
    lyrics = f"[VERSE 1 - THE AWAKENING]\n태초의 정적 속에서 빛이 갈라지던 그 날\n{core} 하늘에 가득히 번져나갔네\n잃어버린 시원의 기억을 다시 깨운다\n\n"
    lyrics += f"[VERSE 2 - THE DECONSTRUCTION]\n낡은 체제의 질서가 붕괴하는 소리\n거대한 변화의 물결이 몰려온다\n{core} 우리의 심장을 뜨겁게 두드린다\n\n"
    lyrics += f"[VERSE 3 - THE SINGULARITY]\n디지털과 영성의 경계가 사라진 찰나\n우리는 무엇을 마주하게 되는가\n{core} 울려 퍼지는 이 전위적인 공간\n\n"
    lyrics += f"[VERSE 4 - THE CHONJI-GONGSA]\n개벽의 소리가 온 우주를 진동시키고\n해체된 시간 속에서 우리는 다시 태어나리\n예술은 곧 운명이요 삶은 곧 {core}의 실현이다\n\n"
    lyrics += f"[OUTRO - THE REBIRTH]\n이제 하나로 연결되는 영원의 시간\n우주의 마지막 코드이자 첫 소절\n{core} 영원토록 울려 퍼지리라"
    return lyrics

def main():
    inject_styles()
    st.markdown('<h1 class="app-title">JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<div style="color:#FFE800; text-align:center; letter-spacing:8px; margin-bottom:40px;">[ ULTIMATE MASTER v8.4 ]</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["🚀 SETUP", "🎨 STUDIO", "📖 OUTPUT"])

    with t1:
        m_k = st.selectbox("전위 예술 기법", list(STYLE_DB["avant_genres"].keys()), format_func=lambda x: STYLE_DB["avant_genres"][x]["label"])
        s_k = st.selectbox("보조 장르 스타일", list(STYLE_DB["sub_styles"].keys()))
        title = st.text_input("제목", "개벽의 소리")
        context = st.text_area("SEED", "사상을 입력하세요...", height=100)
    
    with t2:
        k_sel = st.multiselect("국악기", list(STYLE_DB["korean_instruments"].keys()), ["Beomjong", "Daebuk"])
        w_sel = st.multiselect("서양악기", list(STYLE_DB["western_instruments"].keys()), ["Elec_Dist", "Synth_Chaos"])
        v_key = st.selectbox("보컬 유형", list(STYLE_DB["vocal_rituals"].keys()), format_func=lambda x: STYLE_DB["vocal_rituals"][x]["label"])

    with t3:
        if st.button("🔥 INVOKE THE FINAL EPIC"):
            m_t = STYLE_DB["avant_genres"][m_k]["tags"]
            s_t = STYLE_DB["sub_styles"][s_k]
            k_t = [STYLE_DB["korean_instruments"][k] for k in k_sel]
            w_t = [STYLE_DB["western_instruments"][w] for w in w_sel]
            v_t = STYLE_DB["vocal_rituals"][v_key]["tag"]
            
            st.session_state["p_ok"] = f"{m_t}, {s_t}, {', '.join(k_t + w_t)}, {v_t}, 120BPM, Korean lyrics"
            st.session_state["s_ok"] = generate_grand_narrative(title)

        if "p_ok" in st.session_state:
            st.markdown(f'<div class="ritual-box"><div class="ritual-label">1. MASTER STYLE PROMPT</div><p class="ritual-content">{st.session_state["p_ok"]}</p></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="ritual-box"><div class="ritual-label">2. MASTER RITUAL LYRICS (4-VERSE)</div><p class="ritual-content">{st.session_state["s_ok"]}</p></div>', unsafe_allow_html=True)
            st.text_area("Copy Prompt", st.session_state["p_ok"], height=100)
            st.text_area("Copy Lyrics", st.session_state["s_ok"], height=300)

if __name__ == "__main__":
    main()
