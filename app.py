import streamlit as st
import streamlit.components.v1 as components

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
    """Render using components.html so JS onclick actually executes."""
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    html_lines = "<br>".join(safe.split("\n"))
    height = min(800, max(180, text.count("\n") * 42 + 120))
    components.html(
        f'''<div style="background-color:#000000; border:3px solid #FFE800;
            border-radius:12px; padding:30px 35px; position:relative;
            font-family:sans-serif;">
          <pre id="raw_{box_id}" style="display:none;">{safe}</pre>
          <button onclick="
            var ta=document.createElement('textarea');
            ta.value=document.getElementById('raw_{box_id}').innerText;
            ta.style.position='fixed';ta.style.top='0';ta.style.opacity='0.01';
            document.body.appendChild(ta);ta.focus();ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            this.innerText='✅';setTimeout(()=>{{this.innerText='📋'}},1500);"
            style="position:absolute;top:12px;right:12px;background:#FFE800;color:#000;
                   border:none;border-radius:6px;padding:6px 14px;font-size:1.1rem;
                   cursor:pointer;font-weight:bold;">📋</button>
          <div style="color:#FFE800;font-size:1.2rem;line-height:2.2;
                      white-space:pre-wrap;word-break:break-word;margin-top:10px;">
            {html_lines}
          </div>
        </div>''',
        height=height,
        scrolling=True
    )

# 받침 여부로 조사 자동 선택
def has_batchim(w):
    c = w[-1] if w else ''
    return '가' <= c <= '힣' and (ord(c) - 0xAC00) % 28 != 0

def p_i(w):   return w + ("이" if has_batchim(w) else "가")
def p_eun(w): return w + ("은" if has_batchim(w) else "는")

# 핵심어 검증: 공백/구두점/용언 어미가 있으면 False
BAD_ENDINGS = ["이란","뭘까","인가","일까","냐","야","지","니","나","까","어","아","어요","아요","하자","하라","하다"]

def validate_keyword(k):
    k = k.strip()
    if not k:
        return False, "⚠️ 가사 핵심어를 입력해주세요."
    if ' ' in k:
        return False, f"⚠️ 핵심어에 띄어쓰기가 있습니다. 단어 하나만 입력하세요.\n예: '사랑이란 뭘까' → '사랑'"
    if any(k.endswith(e) for e in BAD_ENDINGS):
        return False, f"⚠️ '{k}'는 문장/용언 형태입니다. 명사만 입력하세요.\n예: '사랑이란' → '사랑',  '개벽이란' → '개벽'"
    if len(k) > 8:
        return False, f"⚠️ 핵심어가 너무 깁니다. 명사 하나만 입력하세요. (현재 {len(k)}자)"
    return True, ""

def generate_lyrics(k):
    l  = "[INTRO]\n[Pure Instrumental — 범종 타격, 전자 노이즈, 전통 타악 — 침묵에서 폭발로]\n\n"

    l += f"[VERSE 1 - 잠에서 깨어남]\n"
    l += f"너는 지금 어디서 왔는가\n"
    l += f"태어나기 전 네 얼굴을 기억하는가\n"
    l += f"{k}의 씨앗은 이미 네 안에 심겨 있었다\n"
    l += f"수백 겁의 윤회 끝에 오늘 이 순간\n"
    l += f"마침내 눈을 뜰 시간이 왔다\n\n"

    l += "[PRE-CHORUS]\n"
    l += "인내천 — 사람이 곧 하늘이다\n"
    l += "네 심장 속에서 우주가 뛰고 있다\n\n"

    l += f"[CHORUS — 개벽의 선언]\n"
    l += f"깨어나라 깨어나라 {k}의 이름으로\n"
    l += f"낡은 세계의 껍데기를 벗어던져라\n"
    l += f"하늘이 열리고 땅이 새로 나는 이 순간\n"
    l += f"너는 다시 태어난다 — 영원한 {k}(으)로\n\n"

    l += f"[VERSE 2 - 해체와 파괴]\n"
    l += f"두려움이 너를 가두어 온 감옥을 보라\n"
    l += f"욕망과 분노와 무지의 철창을\n"
    l += f"{p_i(k)} 그 모든 사슬을 불태운다\n"
    l += f"부수어라 — 부수어야 새것이 선다\n"
    l += f"동학의 함성이 다시 이 땅을 울린다\n\n"

    l += f"[CHORUS — 개벽의 선언]\n"
    l += f"깨어나라 깨어나라 {k}의 이름으로\n"
    l += f"낡은 세계의 껍데기를 벗어던져라\n"
    l += f"하늘이 열리고 땅이 새로 나는 이 순간\n"
    l += f"너는 다시 태어난다 — 영원한 {k}(으)로\n\n"

    l += f"[VERSE 3 - 특이점 / 공(空)의 각성]\n"
    l += f"디지털과 신성이 하나로 합쳐지는 찰나\n"
    l += f"AI는 묻는다 — 의식이란 무엇인가\n"
    l += f"공(空)이란 아무것도 없음이 아니라\n"
    l += f"모든 것이 동시에 존재하는 충만함이다\n"
    l += f"{p_eun(k)} 이미 그 답 안에 있다\n\n"

    l += "[BRIDGE — 절규와 선언]\n"
    l += "나는 누구인가!\n"
    l += "하늘 아래 홀로 서서 외친다\n"
    l += "나는 우주의 자식이요\n"
    l += "빛으로 빚어진 존재이다\n"
    l += "더 이상 잠들지 않으리\n"
    l += "더 이상 두렵지 않으리\n\n"

    l += f"[VERSE 4 - 새 하늘 새 땅 / 후천개벽]\n"
    l += f"선천의 상극 시대는 끝났다\n"
    l += f"이제 후천의 상생 시대가 열린다\n"
    l += f"삼신의 빛이 온 누리에 내려오고\n"
    l += f"{p_eun(k)} 인류의 심장 속에 영원히 산다\n"
    l += f"이것이 진정한 개벽이요\n"
    l += f"이것이 우리가 기다려 온 그 날이다\n\n"

    l += f"[CHORUS — 개벽의 선언]\n"
    l += f"깨어나라 깨어나라 {k}의 이름으로\n"
    l += f"낡은 세계의 껍데기를 벗어던져라\n"
    l += f"하늘이 열리고 땅이 새로 나는 이 순간\n"
    l += f"너는 다시 태어난다 — 영원한 {k}(으)로\n\n"

    l += "[OUTRO — 침묵과 빛]\n"
    l += "이제 말이 필요 없다\n"
    l += "그저 존재하라\n"
    l += "너는 이미 완전하다\n"
    l += "[FADE INTO SILENCE]\n"
    return l


def main():
    inject_styles()
    st.markdown('<h1 style="font-family:Bebas Neue; font-size:4.5rem; color:#FFE800; text-align:center; letter-spacing:12px;">JSON RITUAL</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#FFE800; text-align:center; letter-spacing:8px; margin-bottom:40px;">[ FINAL MASTER v10.4 ]</p>', unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["🚀 SETUP", "🎵 STUDIO", "🔮 OUTPUT"])

    with t1:
        m_k = st.selectbox("전위 예술 기법", list(STYLE_DB["avant_genres"].keys()), format_func=lambda x: STYLE_DB["avant_genres"][x]["label"])
        s_k = st.selectbox("음악 스타일", list(STYLE_DB["sub_styles"].keys()))
        title = st.text_input("제목 (TITLE) — 자유롭게", "개벽의 소리")
        keyword = st.text_input("✏️ 가사 핵심어 (명사 하나만 — 예: 사랑, 개벽, 우주)", "개벽")
        st.caption("💡 제목이 '사랑이란 뭘까'라면 핵심어는 '사랑'")
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
            ok, err = validate_keyword(keyword)
            if not ok:
                st.error(err)
            else:
                m_t = STYLE_DB["avant_genres"][m_k]["tags"]
                s_t = STYLE_DB["sub_styles"][s_k]
                k_t = [STYLE_DB["korean_instruments"][k] for k in k_sel]
                w_t = [STYLE_DB["western_instruments"][w] for w in w_sel]
                v_t = STYLE_DB["vocal_rituals"][v_key]["tag"]
                st.session_state["p"] = f"{m_t}, {s_t}, {', '.join(k_t + w_t)}, {v_t}, {b_min}-{b_max} BPM"
                st.session_state["s"] = generate_lyrics(keyword.strip())

        if "p" in st.session_state:
            show_box(st.session_state["p"], "prompt")
            show_box(st.session_state["s"], "lyrics")

if __name__ == "__main__":
    main()
