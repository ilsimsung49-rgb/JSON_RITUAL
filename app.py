import streamlit as st

st.set_page_config(page_title="JSON RITUAL v10.4", page_icon="👹", layout="wide")

STYLE_DB = {
    "avant_genres": {
        "Fluxus": {"label": "플럭서스 [FLUXUS]", "tags": "fluxus ritual, experimental deconstruction, art-life fusion, chaotic, anti-art"},
        "Avant_Garde": {"label": "아방가르드 [AVANT-GARDE]", "tags": "avant-garde music, experimental, atonal, dissonant, radical breaking of rules"},
        "Industrial_Ritual": {"label": "인더스트리얼 리추얼", "tags": "industrial, mechanical sounds, dark ritual, repetitive noise, steel textures"},
        "Progressive_Fusion": {"label": "프로그레시브 퓨전", "tags": "progressive, complex arrangement, world music fusion, epic structure"},
        "Experimental_Void": {"label": "전위적 허공 [VOID]", "tags": "space drone, ambient, transcendent, experimental atmosphere, minimalistic"}
    },
    "sub_styles": {
        "Rock": "classic rock, 70s rock", "Hard_Rock": "hard rock, aggressive riffs",
        "Heavy_Metal": "heavy metal, distorted guitar", "Death_Metal": "death metal, blast beats, extreme vocals",
        "Blues_Soul": "soulful blues, electric shuffle", "Jazz_Abstract": "abstract jazz, free jazz",
        "Funk_Groove": "funk, slap bass, groovy", "Psychedelic": "psychedelic rock, trippy effects",
        "EDM_Chaos": "EDM, heavy electronic, synthesizer chaos", "Psy_Trance": "psychedelic trance, hypnotic pulse",
        "Techno_Glitch": "techno, glitchy, industrial beat", "Dark_Ambient": "dark ambient, eerie drone",
        "Industrial_Noise": "industrial noise, metallic percussion", "Orchestral_Epic": "grand orchestral, cinematic strings",
        "Tribal": "shamanic ritual, tribal percussion", "Lofi_HipHop": "lo-fi hip hop, dusty beats"
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
        "Piano": "grand piano", "Rhodes": "Rhodes electric piano", "Organ": "hammond organ", "Violin": "solo violin",
        "Cello": "deep cello solo", "Strings": "orchestral strings", "Epic_Choir": "epic cinematic choir",
        "Harmonica": "harmonica", "Pipe_Organ": "pipe organ", "808_Machine": "TR-808 drum machine",
        "Turntable": "turntable scratches, foley noise"
    },
    "vocal_rituals": {
        "Avant_Screams": {"label": "전위적 괴성 [Screams]", "tag": "avant-garde screams, abstract vocalizations"},
        "Shaman_Deep": {"label": "샤먼/주술 거친목소리", "tag": "male shamanic growl, ritualistic deep chanting"},
        "Pansori_Husky": {"label": "허스키한 판소리 도성", "tag": "pansori vocal, traditional Korean, husky"},
        "Clear_Soprano": {"label": "청아한 소프라노", "tag": "clear ethereal soprano, heavenly female voice"},
        "Pure_Children": {"label": "청아한 소년/소녀 합창", "tag": "pure children choir"},
        "Husky_Rock": {"label": "거친 허스키 록 보컬", "tag": "raspy husky male rock vocal"},
        "Deep_Void": {"label": "낮고 깊은 바리톤", "tag": "deep male baritone, resonant"},
        "Monastic_Chant": {"label": "단조로운 주문 [Chant]", "tag": "monotone ritual chant, hypnotic drone"},
        "Soulful_Alto": {"label": "소울풀한 깊은 여성보컬", "tag": "soulful deep alto female vocal"},
        "Hypnotic_Whispers": {"label": "몽환적인 속삭임", "tag": "hypnotic whispers, breathing"},
        "Narration": {"label": "나레이션/대서사 낭독", "tag": "grand spoken word narrative"},
        "Industrial_Vox": {"label": "인더스트리얼 변조 보컬", "tag": "distorted industrial vocals"},
        "AI_Cyber": {"label": "사이버네틱 AI 목소리 [AI Voice]", "tag": "cybernetic artificial voice, synthesized monotone"},
        "Buddhist_Chant": {"label": "전통 범패/염불", "tag": "traditional Buddhist chant"}
    }
}

def inject_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Noto+Sans+KR:wght@300;700&display=swap');
    .stApp { background-color: #000 !important; color: #fff !important; }
    p, span, label, .stMarkdown p { color: #FFFFFF !important; }
    .stTextInput input, .stTextArea textarea, .stNumberInput input, div[data-baseweb="select"] > div {
        background-color: #111 !important; color: #FFF !important; border: 1px solid #FFE800 !important;
    }
    .stButton > button { width:100% !important; background:transparent !important; border:3px solid #FFE800 !important; color:#FFE800 !important; font-family:'Bebas Neue' !important; font-size:2.5rem !important; height:85px !important; margin:20px 0; }
    .stButton > button:hover { background:#FFE800 !important; color:#000 !important; }
    div[data-baseweb="popover"] * { background-color:#111 !important; color:#FFF !important; }
    li[role="option"]:hover { background-color:#FFE800 !important; color:#000 !important; }
    </style>
    """, unsafe_allow_html=True)

def show_box(text, box_id):
    """Render text in a box with INLINE styles + JS copy button."""
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Use a hidden textarea for reliable clipboard copy
    js_text = text.replace("`", "\\`").replace("\\", "\\\\").replace("$", "\\$")
    html_lines = "<br>".join(safe.split("\n"))
    st.markdown(
        f'<div style="background-color:#000000; border:3px solid #FFE800; '
        f'border-radius:12px; padding:30px 35px; margin-bottom:25px; position:relative;">'
        f'<button onclick="navigator.clipboard.writeText(`{js_text}`).then(()=>{{this.innerText=\'✅\';setTimeout(()=>{{this.innerText=\'📋\'}},1500)}})" '
        f'style="position:absolute; top:12px; right:12px; background:#FFE800; color:#000; '
        f'border:none; border-radius:6px; padding:6px 14px; font-size:1.1rem; cursor:pointer; font-weight:bold;">📋</button>'
        f'<div style="color:#FFE800; font-family:Noto Sans KR, sans-serif; font-size:1.3rem; '
        f'line-height:2.3; white-space:pre-wrap; word-break:break-word;">'
        f'{html_lines}</div></div>',
        unsafe_allow_html=True
    )

def generate_lyrics(title):
    core = title or "개벽"
    l  = "[INTRO]\n[Professional Instrumental Session - THE GRAND RITUAL FUSION]\n\n"
    l += f"[VERSE 1 - AWAKENING]\n태초의 정적 속에서 빛이 갈라지던 그 날\n{core} 하늘에 가득히 번져나갔네\n잃어버린 시원의 기억을 다시 깨운다\n\n"
    l += "[PRE-CHORUS]\n경계 위에 서서 우리는 춤춘다\n해체되는 시간의 틈새로 흘러드는 빛\n\n"
    l += f"[CHORUS]\n개벽의 소리가 온 우주를 진동시키고\n해체된 시간 속에서 우리는 다시 태어나리\n예술은 곧 운명이요 삶은 곧 {core}의 실현이다\n\n"
    l += f"[VERSE 2 - DECONSTRUCTION]\n낡은 체제의 질서가 붕괴하는 소리\n거대한 변화의 물결이 몰려온다\n{core} 우리의 심장을 뜨겁게 두드린다\n\n"
    l += f"[CHORUS]\n개벽의 소리가 온 우주를 진동시키고\n해체된 시간 속에서 우리는 다시 태어나리\n예술은 곧 운명이요 삶은 곧 {core}의 실현이다\n\n"
    l += f"[VERSE 3 - SINGULARITY]\n디지털과 영성의 경계가 사라진 찰나\n우리는 무엇을 마주하게 되는가\n{core} 울려 퍼지는 이 전위적인 공간\n\n"
    l += "[BRIDGE]\n터져 나오는 영혼의 외침\n해체하라, 파괴하라, 그리고 다시 세우라\n시원의 에너지가 쿤달리니처럼 솟구친다\n\n"
    l += f"[VERSE 4 - NEW GENESIS]\n이제 하나로 연결되는 영원의 시간\n우주의 마지막 코드이자 첫 소절\n{core} 영원토록 울려 퍼지리라\n\n"
    l += f"[CHORUS]\n개벽의 소리가 온 우주를 진동시키고\n해체된 시간 속에서 우리는 다시 태어나리\n예술은 곧 운명이요 삶은 곧 {core}의 실현이다\n\n"
    l += "[OUTRO]\n시원의 빛으로 돌아가는 길\n이것은 노래가 아니요, 우주의 맥박이다\n[FADE OUT]\n"
    return l

def main():
    inject_styles()
    st.markdown('<h1 style="font-family:Bebas Neue; font-size:4.5rem; color:#FFE800; text-align:center; letter-spacing:12px;">JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#FFE800; text-align:center; letter-spacing:8px; margin-bottom:40px;">[ FINAL MASTER v10.4 ]</p>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["🚀 SETUP", "🎵 STUDIO", "🔮 OUTPUT"])

    with t1:
        m_k = st.selectbox("전위 예술 기법", list(STYLE_DB["avant_genres"].keys()), format_func=lambda x: STYLE_DB["avant_genres"][x]["label"])
        s_k = st.selectbox("음악 스타일", list(STYLE_DB["sub_styles"].keys()))
        title = st.text_input("제목 (TITLE)", "개벽의 소리")
        st.text_area("SEED", "사상을 입력하세요...", height=100)
        col1, col2 = st.columns(2)
        b_min = col1.number_input("BPM Min", 40, 240, 100)
        b_max = col2.number_input("BPM Max", 40, 240, 140)

    with t2:
        k_sel = st.multiselect("국악기", list(STYLE_DB["korean_instruments"].keys()), ["Beomjong", "Daebuk"])
        w_sel = st.multiselect("서양악기", list(STYLE_DB["western_instruments"].keys()), ["Elec_Dist", "Synth_Chaos"])
        v_key = st.selectbox("보컬 유형", list(STYLE_DB["vocal_rituals"].keys()), format_func=lambda x: STYLE_DB["vocal_rituals"][x]["label"])

    with t3:
        if st.button("🔥 INVOKE THE FINAL RITUAL"):
            m_t = STYLE_DB["avant_genres"][m_k]["tags"]
            s_t = STYLE_DB["sub_styles"][s_k]
            k_t = [STYLE_DB["korean_instruments"][k] for k in k_sel]
            w_t = [STYLE_DB["western_instruments"][w] for w in w_sel]
            v_t = STYLE_DB["vocal_rituals"][v_key]["tag"]
            st.session_state["p"] = f"{m_t}, {s_t}, {', '.join(k_t + w_t)}, {v_t}, {b_min}-{b_max} BPM"
            st.session_state["s"] = generate_lyrics(title)

        if "p" in st.session_state:
            # INLINE HTML - BROWSER CANNOT OVERRIDE THIS
            show_box(st.session_state["p"], "prompt")
            show_box(st.session_state["s"], "lyrics")

if __name__ == "__main__":
    main()
