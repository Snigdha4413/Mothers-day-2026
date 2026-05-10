import streamlit as st

st.set_page_config(
    page_title="A Fairytale Mother's Day Book",
    page_icon="🌙",
    layout="centered",
)

# ── Fonts & global styles ────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,600&family=Dancing+Script:wght@400;700&family=IM+Fell+English:ital@0;1&display=swap" rel="stylesheet"/>
<style>
:root {
  --rose: #c8506a; --gold: #b8882a; --parchment: #f9f1e2;
  --ink: #2d1a0e;  --sage: #5a7a52; --lavender: #7a68a8;
  --midnight: #1a0d2e;
}
body, .stApp { background: #1a0d2e !important; }
.stApp { font-family: 'IM Fell English', serif; }

/* hide default streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem !important; }

/* ── book shell ── */
.book-shell {
  background: #1a0d2e;
  border-radius: 16px;
  max-width: 660px;
  margin: 0 auto;
  font-family: 'IM Fell English', serif;
}

/* ── cover ── */
.cover-frame {
  border: 1px solid rgba(184,136,42,0.4);
  border-radius: 10px;
  padding: 40px 28px 50px;
  text-align: center;
  background: radial-gradient(ellipse at 50% 55%, #2d1050 0%, #1a0d2e 65%, #0d0618 100%);
  animation: glimmer 4s ease-in-out infinite alternate;
}
@keyframes glimmer {
  from { border-color: rgba(184,136,42,0.2); box-shadow: inset 0 0 40px rgba(184,136,42,0.03); }
  to   { border-color: rgba(184,136,42,0.6); box-shadow: inset 0 0 80px rgba(184,136,42,0.07); }
}
.cover-eye   { font-size: 56px; animation: breathe 3s ease-in-out infinite; filter: drop-shadow(0 0 18px rgba(200,160,60,0.5)); display:block; margin-bottom:14px; }
@keyframes breathe { 0%,100%{transform:scale(1);} 50%{transform:scale(1.08);} }
.cover-subtitle {
  font-family:'Dancing Script',cursive; font-size:15px; letter-spacing:4px;
  text-transform:uppercase; color:rgba(240,210,140,0.75); margin-bottom:8px;
}
.cover-title {
  font-family:'Playfair Display',serif; font-size:clamp(32px,7vw,52px);
  font-style:italic; font-weight:700; color:#f9f1e2; line-height:1.1;
  text-shadow:0 0 40px rgba(200,100,130,0.4); margin:10px 0;
}
.cover-title em { color:#e0807a; font-style:normal; }
.cover-rule { width:80px; height:1px; background:linear-gradient(90deg,transparent,rgba(184,136,42,0.8),transparent); margin:12px auto; }
.cover-tagline {
  font-family:'IM Fell English',serif; font-style:italic; font-size:14px;
  color:rgba(240,210,160,0.7); max-width:280px; line-height:1.8; margin:0 auto;
}

/* ── inner pages ── */
.page-inner {
  text-align:center; padding:30px 22px 16px;
}
.pg-label  { font-family:'Dancing Script',cursive; font-size:13px; color:rgba(240,210,140,0.45); letter-spacing:3px; margin-bottom:4px; }
.pg-chapter{ font-family:'Dancing Script',cursive; font-size:22px; color:#d4836a; letter-spacing:1px; margin-bottom:4px; }
.pg-heading{ font-family:'Playfair Display',serif; font-size:clamp(20px,4vw,28px); font-style:italic; font-weight:400; color:#f0ddb8; line-height:1.25; margin-bottom:4px; }
.pg-heading em { color:#d4836a; font-style:normal; }
.ornament  { font-size:14px; color:rgba(184,136,42,0.7); letter-spacing:8px; margin:6px 0; }
.pg-text   { font-family:'IM Fell English',serif; font-size:15px; font-style:italic; line-height:1.9; color:rgba(240,220,180,0.82); }
.pg-text strong { color:#e0a060; font-style:normal; }

/* ── story card ── */
.story-card {
  background:rgba(240,230,200,0.07); border:1px solid rgba(184,136,42,0.25);
  border-radius:10px; padding:20px 22px; margin-top:14px; position:relative;
}
.story-card::before {
  content:'"'; position:absolute; top:-6px; left:14px;
  font-family:'Playfair Display',serif; font-size:48px;
  color:rgba(200,80,106,0.18); line-height:1;
}

/* ── parchment letter ── */
.letter {
  background:rgba(249,241,226,0.08); border:1px solid rgba(184,136,42,0.3);
  border-radius:4px; padding:24px 22px; margin-top:14px;
  font-family:'IM Fell English',serif; font-style:italic; font-size:15px;
  line-height:1.95; color:rgba(240,220,180,0.85);
}
.letter strong { color:#e0a060; font-style:normal; }

/* ── attribs ── */
.attribs { display:flex; flex-wrap:wrap; gap:8px; justify-content:center; list-style:none; padding:0; margin-top:12px; }
.attribs li {
  background:rgba(240,230,200,0.1); border:1px solid rgba(184,136,42,0.3);
  border-radius:30px; padding:5px 14px;
  font-family:'IM Fell English',serif; font-size:13px;
  font-style:italic; color:rgba(240,220,180,0.8);
}

/* ── final page ── */
.final-heading {
  font-family:'Playfair Display',serif; font-size:clamp(22px,5vw,34px);
  font-style:italic; color:#f9f1e2; line-height:1.2; margin:10px 0;
}
.final-heading .mum-name { color:#e0807a; }
.big-heart  { font-size:72px; animation:heartbeat 1.5s ease-in-out infinite; filter:drop-shadow(0 0 24px rgba(200,80,100,0.7)); display:block; margin:10px auto; }
@keyframes heartbeat { 0%,100%{transform:scale(1);} 15%{transform:scale(1.12);} 30%{transform:scale(1);} 45%{transform:scale(1.06);} }
.signature  { font-family:'Dancing Script',cursive; font-size:26px; color:#b8882a; margin-top:4px; }
.sparkle-row{ display:flex; gap:10px; justify-content:center; font-size:22px; margin:8px 0; }

/* ── scene container ── */
.scene { width:100%; max-width:420px; margin:14px auto 2px; border-radius:14px; overflow:hidden; box-shadow:0 4px 28px rgba(0,0,0,0.5); }
.scene svg { display:block; width:100%; height:auto; }
.tap-label  { font-family:'Dancing Script',cursive; font-size:12px; color:rgba(240,210,140,0.4); letter-spacing:1px; text-align:center; margin-top:2px; }

/* ── page backgrounds ── */
.bg-cover  { background:radial-gradient(ellipse at 50% 55%,#2d1050 0%,#1a0d2e 65%,#0d0618 100%); }
.bg-p1     { background:linear-gradient(170deg,#1f0a30 0%,#3d1850 45%,#1a0d2e 100%); }
.bg-p2     { background:linear-gradient(160deg,#0d2010 0%,#1a4025 50%,#0d2010 100%); }
.bg-p3     { background:linear-gradient(165deg,#1a1030 0%,#2e1848 50%,#1a0820 100%); }
.bg-p4     { background:linear-gradient(160deg,#0d1a28 0%,#1a3048 50%,#0d1520 100%); }
.bg-final  { background:radial-gradient(ellipse at 50% 40%,#2d1050 0%,#1a0d2e 70%); }

/* tap animations */
.sparkle-anim { animation:sparkleAnim 0.6s ease forwards; }
@keyframes sparkleAnim {
  0%   { transform:scale(1) rotate(0deg); }
  30%  { transform:scale(1.5) rotate(15deg); filter:brightness(2); }
  70%  { transform:scale(0.9) rotate(-8deg); filter:brightness(1.5); }
  100% { transform:scale(1) rotate(0deg); filter:brightness(1); }
}

/* stButton overrides for nav */
div[data-testid="stHorizontalBlock"] .stButton > button {
  background:rgba(255,255,255,0.08) !important;
  border:1px solid rgba(184,136,42,0.4) !important;
  border-radius:50% !important;
  width:44px !important; height:44px !important;
  color:#f5dfa0 !important;
  font-size:20px !important;
  padding:0 !important;
  transition:background 0.2s,transform 0.15s;
}
div[data-testid="stHorizontalBlock"] .stButton > button:hover {
  background:rgba(184,136,42,0.18) !important;
  transform:scale(1.1);
}

/* name input */
.stTextInput > div > div > input {
  background:rgba(255,255,255,0.08) !important;
  border:1px solid rgba(184,136,42,0.5) !important;
  border-radius:30px !important;
  font-family:'Dancing Script',cursive !important;
  font-size:18px !important;
  color:#f5dfa0 !important;
  text-align:center !important;
}

/* page-number indicator */
.page-counter {
  font-family:'Dancing Script',cursive; font-size:13px;
  color:rgba(240,210,140,0.5); text-align:center; margin-top:8px;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = 0

TOTAL_PAGES = 5  # 0=cover, 1-4=story pages, but we also have a final (5 visible)

# ── Name input ────────────────────────────────────────────────────────────────
mum_name = st.text_input("", placeholder="her name…", max_chars=20, label_visibility="collapsed")
display_name = mum_name.strip() if mum_name.strip() else "Mum"

# ── Page SVGs ─────────────────────────────────────────────────────────────────
SVG_GARDEN = """
<svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="mg1" cx="50%" cy="30%" r="55%">
      <stop offset="0%" stop-color="#4a1a70"/>
      <stop offset="100%" stop-color="#1a0830"/>
    </radialGradient>
  </defs>
  <rect width="400" height="220" fill="url(#mg1)"/>
  <circle cx="30" cy="20" r="1.5" fill="#ffd580" opacity="0.9"/>
  <circle cx="80" cy="12" r="1" fill="white" opacity="0.7"/>
  <circle cx="140" cy="25" r="1.5" fill="#c9b8e8" opacity="0.8"/>
  <circle cx="200" cy="10" r="1" fill="white"/>
  <circle cx="260" cy="22" r="1.5" fill="#ffd580" opacity="0.8"/>
  <circle cx="330" cy="16" r="1" fill="white" opacity="0.7"/>
  <circle cx="375" cy="30" r="1.5" fill="#c9b8e8"/>
  <!-- crescent moon -->
  <circle cx="340" cy="45" r="22" fill="#f5d080" opacity="0.92"/>
  <circle cx="352" cy="38" r="17" fill="#2a1050"/>
  <!-- rolling hills -->
  <ellipse cx="80" cy="230" rx="160" ry="90" fill="#2a0e4a" opacity="0.9"/>
  <ellipse cx="320" cy="235" rx="180" ry="95" fill="#220b40" opacity="0.8"/>
  <ellipse cx="200" cy="245" rx="250" ry="100" fill="#1a0830"/>
  <rect x="0" y="178" width="400" height="42" fill="#1a0830"/>
  <!-- tree trunk -->
  <rect x="185" y="90" width="14" height="90" fill="#5a3010" rx="3"/>
  <!-- tree canopy -->
  <circle cx="193" cy="68" r="42" fill="#3a1870" opacity="0.9"/>
  <circle cx="168" cy="82" r="26" fill="#2e1460" opacity="0.8"/>
  <circle cx="218" cy="80" r="24" fill="#2e1460" opacity="0.7"/>
  <circle cx="178" cy="58" r="5" fill="#ffb040" opacity="0.9"/>
  <circle cx="200" cy="46" r="4" fill="#80d0ff" opacity="0.8"/>
  <circle cx="215" cy="65" r="4.5" fill="#ff8080" opacity="0.8"/>
  <circle cx="185" cy="82" r="3.5" fill="#a0ff80" opacity="0.7"/>
  <circle cx="205" cy="78" r="3" fill="#ffd580" opacity="0.8"/>
  <!-- flowers -->
  <rect x="58" y="155" width="4" height="28" fill="#3a6030" rx="1"/>
  <circle cx="60" cy="152" r="11" fill="#c8506a"/>
  <circle cx="60" cy="152" r="6" fill="#ffd580" opacity="0.9"/>
  <circle cx="54" cy="146" r="5" fill="#c8506a" opacity="0.7"/>
  <circle cx="66" cy="146" r="5" fill="#c8506a" opacity="0.7"/>
  <circle cx="54" cy="158" r="5" fill="#c8506a" opacity="0.7"/>
  <circle cx="66" cy="158" r="5" fill="#c8506a" opacity="0.7"/>
  <rect x="98" y="158" width="4" height="24" fill="#3a6030" rx="1"/>
  <circle cx="100" cy="155" r="9" fill="#7a68a8"/>
  <circle cx="100" cy="155" r="5" fill="#ffd580" opacity="0.9"/>
  <rect x="268" y="156" width="4" height="26" fill="#3a6030" rx="1"/>
  <circle cx="270" cy="153" r="10" fill="#4a9060"/>
  <circle cx="270" cy="153" r="5" fill="#ffd580" opacity="0.9"/>
  <rect x="318" y="160" width="4" height="22" fill="#3a6030" rx="1"/>
  <circle cx="320" cy="157" r="9" fill="#d08030"/>
  <circle cx="320" cy="157" r="5" fill="#ffd580" opacity="0.9"/>
  <!-- fireflies -->
  <circle cx="130" cy="140" r="3" fill="#a0ff80" opacity="0.9"/>
  <circle cx="130" cy="140" r="6" fill="#a0ff80" opacity="0.2"/>
  <circle cx="360" cy="150" r="2.5" fill="#80e0ff" opacity="0.9"/>
  <circle cx="42" cy="160" r="2.5" fill="#ffd580" opacity="0.85"/>
  <path d="M0,200 Q100,185 200,195 Q300,205 400,190" stroke="#7a68a8" stroke-width="1.5" fill="none" opacity="0.35" stroke-dasharray="6,4"/>
</svg>"""

SVG_FOREST = """
<svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="mg2" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#0d2818"/>
      <stop offset="100%" stop-color="#060e08"/>
    </radialGradient>
  </defs>
  <rect width="400" height="220" fill="url(#mg2)"/>
  <ellipse cx="200" cy="195" rx="240" ry="40" fill="#1a4025" opacity="0.6"/>
  <ellipse cx="80" cy="190" rx="120" ry="30" fill="#1a4025" opacity="0.4"/>
  <!-- trees -->
  <rect x="55" y="80" width="18" height="130" fill="#2a1808" rx="4"/>
  <ellipse cx="64" cy="56" rx="50" ry="40" fill="#1a4820" opacity="0.95"/>
  <ellipse cx="40" cy="72" rx="30" ry="24" fill="#153d18" opacity="0.8"/>
  <ellipse cx="88" cy="70" rx="28" ry="22" fill="#153d18" opacity="0.75"/>
  <circle cx="50" cy="50" r="4" fill="#40ff80" opacity="0.6"/>
  <circle cx="72" cy="38" r="3" fill="#80ffd0" opacity="0.55"/>
  <circle cx="82" cy="60" r="3.5" fill="#40ff80" opacity="0.5"/>
  <rect x="148" y="70" width="16" height="140" fill="#2a1808" rx="3"/>
  <ellipse cx="156" cy="46" rx="55" ry="44" fill="#1c5224" opacity="0.95"/>
  <circle cx="140" cy="40" r="4.5" fill="#ffd580" opacity="0.6"/>
  <circle cx="165" cy="30" r="3.5" fill="#a0ffb0" opacity="0.6"/>
  <circle cx="148" cy="60" r="3.5" fill="#80ffd0" opacity="0.6"/>
  <rect x="290" y="85" width="15" height="125" fill="#2a1808" rx="3"/>
  <ellipse cx="298" cy="58" rx="48" ry="38" fill="#1a4820" opacity="0.95"/>
  <circle cx="285" cy="52" r="4" fill="#40ff80" opacity="0.6"/>
  <circle cx="306" cy="42" r="3" fill="#c0ffb0" opacity="0.55"/>
  <!-- mushrooms -->
  <ellipse cx="110" cy="198" rx="16" ry="5" fill="#ff8060" opacity="0.7"/>
  <path d="M103,198 Q110,175 117,198" fill="#ff6040" opacity="0.9"/>
  <circle cx="107" cy="188" r="2.5" fill="white" opacity="0.6"/>
  <ellipse cx="240" cy="201" rx="12" ry="4" fill="#ff8060" opacity="0.7"/>
  <path d="M234,201 Q240,183 246,201" fill="#ff6040" opacity="0.9"/>
  <!-- owl -->
  <ellipse cx="348" cy="128" rx="14" ry="18" fill="#5a3a10"/>
  <circle cx="342" cy="120" r="8" fill="#7a5a20"/>
  <circle cx="354" cy="120" r="8" fill="#7a5a20"/>
  <circle cx="342" cy="120" r="5" fill="#1a0820"/>
  <circle cx="354" cy="120" r="5" fill="#1a0820"/>
  <circle cx="343" cy="119" r="2" fill="white"/>
  <circle cx="355" cy="119" r="2" fill="white"/>
  <polygon points="348,124 345,128 351,128" fill="#c8803a"/>
  <!-- fairy lights -->
  <line x1="55" y1="110" x2="155" y2="100" stroke="#3a6030" stroke-width="1.5" opacity="0.5"/>
  <circle cx="75" cy="108" r="3" fill="#ffd580" opacity="0.8"/>
  <circle cx="95" cy="104" r="3" fill="#ff8080" opacity="0.8"/>
  <circle cx="115" cy="103" r="3" fill="#80d0ff" opacity="0.8"/>
  <circle cx="135" cy="101" r="3" fill="#a0ff80" opacity="0.8"/>
  <!-- moon -->
  <circle cx="200" cy="18" r="18" fill="#f5e0a0" opacity="0.85"/>
  <circle cx="200" cy="18" r="12" fill="#f9f0c0"/>
</svg>"""

SVG_STARWEAVER = """
<svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="mg3" cx="50%" cy="40%" r="65%">
      <stop offset="0%" stop-color="#1a0838"/>
      <stop offset="100%" stop-color="#08040e"/>
    </radialGradient>
  </defs>
  <rect width="400" height="220" fill="url(#mg3)"/>
  <!-- constellation lines -->
  <line x1="80" y1="50" x2="140" y2="80" stroke="rgba(180,160,220,0.25)" stroke-width="1"/>
  <line x1="140" y1="80" x2="200" y2="60" stroke="rgba(180,160,220,0.25)" stroke-width="1"/>
  <line x1="200" y1="60" x2="260" y2="90" stroke="rgba(180,160,220,0.25)" stroke-width="1"/>
  <line x1="260" y1="90" x2="320" y2="55" stroke="rgba(180,160,220,0.25)" stroke-width="1"/>
  <!-- stars -->
  <circle cx="80" cy="50" r="5" fill="#ffd580" opacity="0.95"/>
  <circle cx="80" cy="50" r="9" fill="#ffd580" opacity="0.2"/>
  <circle cx="140" cy="80" r="6" fill="#c9b8e8" opacity="0.95"/>
  <circle cx="200" cy="60" r="7" fill="#f5d080" opacity="0.95"/>
  <circle cx="260" cy="90" r="5" fill="#80d0ff" opacity="0.95"/>
  <circle cx="320" cy="55" r="5.5" fill="#ffd580" opacity="0.9"/>
  <circle cx="160" cy="120" r="4" fill="#ff9080" opacity="0.9"/>
  <circle cx="220" cy="110" r="4.5" fill="#a0ff80" opacity="0.9"/>
  <circle cx="35" cy="30" r="1.5" fill="white" opacity="0.5"/>
  <circle cx="355" cy="25" r="1.5" fill="white" opacity="0.6"/>
  <!-- mother silhouette -->
  <ellipse cx="200" cy="195" rx="52" ry="18" fill="#2a1050" opacity="0.95"/>
  <path d="M170,165 Q200,140 230,165 L240,210 Q200,218 160,210 Z" fill="#3a1870"/>
  <path d="M178,155 Q200,145 222,155 L225,175 Q200,180 175,175 Z" fill="#4a2090"/>
  <circle cx="200" cy="145" r="15" fill="#5a3a20"/>
  <!-- star crown -->
  <circle cx="193" cy="132" r="3" fill="#ffd580" opacity="0.9"/>
  <circle cx="200" cy="129" r="3.5" fill="#f5d080" opacity="0.95"/>
  <circle cx="207" cy="132" r="3" fill="#ffd580" opacity="0.9"/>
  <!-- arms -->
  <path d="M178,158 Q155,135 140,80" stroke="#5a3a20" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M222,158 Q245,135 260,90" stroke="#5a3a20" stroke-width="7" fill="none" stroke-linecap="round"/>
  <!-- thread -->
  <path d="M140,80 Q170,68 200,60 Q230,52 260,90" stroke="rgba(200,180,255,0.5)" stroke-width="1" fill="none" stroke-dasharray="3,3"/>
  <!-- shooting star -->
  <line x1="340" y1="140" x2="375" y2="115" stroke="#ffd580" stroke-width="2" opacity="0.8"/>
  <circle cx="340" cy="140" r="4" fill="#ffd580" opacity="0.95"/>
  <!-- aurora -->
  <path d="M0,190 Q100,175 200,185 Q300,195 400,180" stroke="#4a90c0" stroke-width="12" fill="none" opacity="0.1"/>
  <path d="M0,195 Q100,180 200,192 Q300,204 400,186" stroke="#7a68a8" stroke-width="8" fill="none" opacity="0.12"/>
</svg>"""

SVG_SEA = """
<svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="mg4" cx="50%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#0a1830"/>
      <stop offset="100%" stop-color="#060c1a"/>
    </radialGradient>
    <radialGradient id="lglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffd580" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#ffd580" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="400" height="220" fill="url(#mg4)"/>
  <!-- moon reflection -->
  <ellipse cx="200" cy="210" rx="30" ry="8" fill="#f5e080" opacity="0.15"/>
  <rect x="196" y="155" width="8" height="55" fill="#f5e080" opacity="0.08"/>
  <!-- waves -->
  <path d="M0,165 Q50,155 100,165 Q150,175 200,165 Q250,155 300,165 Q350,175 400,165" stroke="#1a4080" stroke-width="3" fill="none" opacity="0.7"/>
  <path d="M0,178 Q50,168 100,178 Q150,188 200,178 Q250,168 300,178 Q350,188 400,178" stroke="#1a3060" stroke-width="3" fill="none" opacity="0.8"/>
  <rect x="0" y="175" width="400" height="45" fill="#0d2040" opacity="0.9"/>
  <!-- sky stars -->
  <circle cx="30" cy="20" r="1.5" fill="#ffd580" opacity="0.8"/>
  <circle cx="70" cy="40" r="1" fill="white" opacity="0.6"/>
  <circle cx="120" cy="15" r="1.5" fill="#c9b8e8" opacity="0.7"/>
  <circle cx="280" cy="25" r="1.5" fill="#ffd580" opacity="0.7"/>
  <circle cx="380" cy="20" r="1.5" fill="#c9b8e8" opacity="0.7"/>
  <!-- moon -->
  <circle cx="200" cy="40" r="28" fill="#f5e090" opacity="0.95"/>
  <circle cx="213" cy="32" r="20" fill="#0a1830"/>
  <!-- lighthouse -->
  <ellipse cx="88" cy="178" rx="40" ry="14" fill="#1a2a3a"/>
  <rect x="78" y="80" width="22" height="96" fill="#e8e0d0" rx="4"/>
  <rect x="78" y="100" width="22" height="14" fill="#c8506a" rx="0"/>
  <rect x="78" y="130" width="22" height="14" fill="#c8506a" rx="0"/>
  <rect x="78" y="160" width="22" height="14" fill="#c8506a" rx="0"/>
  <rect x="72" y="70" width="34" height="14" fill="#a89888" rx="2"/>
  <!-- lantern glow -->
  <ellipse cx="89" cy="56" rx="30" ry="20" fill="url(#lglow)"/>
  <circle cx="89" cy="62" r="10" fill="#ffd580" opacity="0.9"/>
  <circle cx="89" cy="62" r="7" fill="white" opacity="0.7"/>
  <!-- light beam -->
  <path d="M95,62 L340,130" stroke="#ffd580" stroke-width="1.5" opacity="0.12"/>
  <path d="M95,64 L340,160" stroke="#ffd580" stroke-width="1.5" opacity="0.1"/>
  <!-- sailboat -->
  <path d="M268,170 Q300,178 332,170 L325,160 Q300,163 275,160 Z" fill="#5a3a20"/>
  <rect x="298" y="120" width="4" height="42" fill="#7a5a30"/>
  <path d="M302,124 Q330,138 302,158" fill="white" opacity="0.85"/>
  <path d="M298,126 Q272,140 298,158" fill="#e8e0d0" opacity="0.8"/>
  <polygon points="302,120 316,126 302,132" fill="#c8506a" opacity="0.9"/>
  <!-- sea creatures -->
  <circle cx="150" cy="195" r="4" fill="#40d0c0" opacity="0.7"/>
  <circle cx="150" cy="195" r="8" fill="#40d0c0" opacity="0.15"/>
  <circle cx="360" cy="200" r="3.5" fill="#80a0ff" opacity="0.7"/>
</svg>"""

SVG_FINAL = """
<svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="100" fill="#120828"/>
  <circle cx="40" cy="50" r="2" fill="#ffd580" opacity="0.85"/>
  <circle cx="80" cy="30" r="1.5" fill="white" opacity="0.7"/>
  <circle cx="120" cy="55" r="1.5" fill="#c9b8e8" opacity="0.8"/>
  <circle cx="160" cy="25" r="2" fill="#ffd580" opacity="0.75"/>
  <circle cx="200" cy="60" r="1.5" fill="white" opacity="0.6"/>
  <circle cx="240" cy="30" r="2" fill="#80d0ff" opacity="0.8"/>
  <circle cx="280" cy="55" r="1.5" fill="#c9b8e8" opacity="0.75"/>
  <circle cx="320" cy="20" r="2" fill="#ffd580" opacity="0.8"/>
  <circle cx="360" cy="50" r="1.5" fill="white" opacity="0.65"/>
  <text x="200" y="74" text-anchor="middle"
    font-family="'IM Fell English', serif"
    font-style="italic" font-size="16"
    fill="rgba(240,220,180,0.55)">once upon a time, and always ✦</text>
</svg>"""

# ── Page content renderer ─────────────────────────────────────────────────────
def render_page(page_idx, name):
    if page_idx == 0:
        # COVER
        st.markdown(f"""
        <div class="cover-frame">
          <span class="cover-eye">🌙</span>
          <div class="cover-subtitle">A Fairytale For</div>
          <div style="font-family:'Dancing Script',cursive;font-size:22px;color:#f5dfa0;margin:6px 0;">
            ✦ {name} ✦
          </div>
          <h1 class="cover-title">Happy<br/><em>Mother's</em> Day</h1>
          <div class="cover-rule"></div>
          <p class="cover-tagline">Once upon a time, a mother made the whole world magical.</p>
        </div>
        """, unsafe_allow_html=True)

    elif page_idx == 1:
        # THE ENCHANTED GARDEN
        st.markdown(f"""
        <div class="page-inner" style="background:linear-gradient(170deg,#1f0a30 0%,#3d1850 45%,#1a0d2e 100%);border-radius:12px;padding:28px 20px;">
          <div class="pg-label">~ Page One ~</div>
          <div class="pg-chapter">The Enchanted Garden</div>
          <h2 class="pg-heading">Where Every Flower<br/>Knew Your <em>Name</em></h2>
          <div class="ornament">❧ ✦ ❧</div>
          <div class="scene">{SVG_GARDEN}</div>
          <p class="tap-label">✦ tap flowers &amp; fireflies ✦</p>
          <div class="story-card">
            <p class="pg-text">
              In a garden where the flowers glowed at midnight,
              there lived a mother whose kindness was older than the stars.
              Every bloom knew her name — and leaned toward her voice
              the way all living things lean toward the light.
            </p>
          </div>
        </div>
        """, unsafe_allow_html=True)

    elif page_idx == 2:
        # THE FOREST OF MEMORIES
        st.markdown(f"""
        <div class="page-inner" style="background:linear-gradient(160deg,#0d2010 0%,#1a4025 50%,#0d2010 100%);border-radius:12px;padding:28px 20px;">
          <div class="pg-label">~ Page Two ~</div>
          <div class="pg-chapter">The Forest of Memories</div>
          <h2 class="pg-heading">Where Every Tree<br/>Held a <em>Story</em></h2>
          <div class="ornament">❧ ✦ ❧</div>
          <div class="scene">{SVG_FOREST}</div>
          <p class="tap-label">✦ tap the trees, mushrooms &amp; owl ✦</p>
          <p class="pg-text">
            Deep in the Forest of Memories, every tree was a story she had told.<br/>
            The tallest ones were the brave days.
            The ones with the most light were the days she laughed until she cried.<br/><br/>
            <strong>The owl kept watch over all of it</strong> —
            because nothing is ever truly forgotten when a mother loves you.
          </p>
          <ul class="attribs">
            <li>🌙 Keeper of stories</li>
            <li>🌿 Rooted and strong</li>
            <li>✨ Bringer of light</li>
            <li>🦉 Wise beyond measure</li>
            <li>🔮 A little bit magic</li>
            <li>🌸 Endlessly warm</li>
          </ul>
        </div>
        """, unsafe_allow_html=True)

    elif page_idx == 3:
        # THE STARWEAVER
        st.markdown(f"""
        <div class="page-inner" style="background:linear-gradient(165deg,#1a1030 0%,#2e1848 50%,#1a0820 100%);border-radius:12px;padding:28px 20px;">
          <div class="pg-label">~ Page Three ~</div>
          <div class="pg-chapter">The Starweaver</div>
          <h2 class="pg-heading">She Stitched the Sky<br/>With <em>Care</em></h2>
          <div class="ornament">❧ ✦ ❧</div>
          <div class="scene">{SVG_STARWEAVER}</div>
          <p class="tap-label">✦ tap the stars &amp; shooting star ✦</p>
          <div class="letter">
            They say there is a woman who weaves the stars each night —
            who decides which ones shine brighter, and which ones fall
            so that someone, somewhere, can make a wish.<br/><br/>
            We always believed it was <strong>{name}</strong>.
            Because everything good in our sky has your handwriting on it.
          </div>
        </div>
        """, unsafe_allow_html=True)

    elif page_idx == 4:
        # THE SEA OF DREAMS
        st.markdown(f"""
        <div class="page-inner" style="background:linear-gradient(160deg,#0d1a28 0%,#1a3048 50%,#0d1520 100%);border-radius:12px;padding:28px 20px;">
          <div class="pg-label">~ Page Four ~</div>
          <div class="pg-chapter">The Sea of Dreams</div>
          <h2 class="pg-heading">She Lit the Lighthouse<br/>Every <em>Night</em></h2>
          <div class="ornament">❧ ✦ ❧</div>
          <div class="scene">{SVG_SEA}</div>
          <p class="tap-label">✦ tap the moon, lighthouse, boat &amp; sea ✦</p>
          <div class="story-card">
            <p class="pg-text">
              On every stormy night at sea, the sailors looked for one light.
              Not the brightest — the steadiest.<br/><br/>
              That's what <strong>{name}</strong> has always been.
              <strong>The light that never goes out</strong>.
              The one we navigate home by, no matter how far we've sailed.
            </p>
          </div>
        </div>
        """, unsafe_allow_html=True)

    elif page_idx == 5:
        # FINAL PAGE
        st.markdown(f"""
        <div class="page-inner" style="background:radial-gradient(ellipse at 50% 40%,#2d1050 0%,#1a0d2e 70%);border-radius:12px;padding:28px 20px;">
          <div class="pg-label">~ The End ~</div>
          <span class="big-heart">💗</span>
          <h2 class="final-heading">Happy Mother's Day,<br/><span class="mum-name">{name}</span></h2>
          <div class="ornament" style="color:rgba(184,136,42,0.8)">✦ ✦ ✦</div>
          <p class="pg-text" style="color:rgba(240,220,180,0.75);">
            And they all lived, loved, and were grateful —
            because <em>{name}</em> made every chapter worth reading.
          </p>
          <div class="sparkle-row">🌙 ⭐ 🌸 ✨ 🌺</div>
          <p class="signature">With all our love ♡</p>
          <div class="scene">{SVG_FINAL}</div>
        </div>
        """, unsafe_allow_html=True)


# ── Main layout ───────────────────────────────────────────────────────────────
st.markdown('<div class="book-shell">', unsafe_allow_html=True)

render_page(st.session_state.page, display_name)

# Navigation
TOTAL = 6  # pages 0–5
col_prev, col_mid, col_next = st.columns([1, 4, 1])

with col_prev:
    if st.button("‹", disabled=(st.session_state.page == 0), key="prev"):
        st.session_state.page -= 1
        st.rerun()

with col_mid:
    labels = ["Cover", "I · Garden", "II · Forest", "III · Stars", "IV · Sea", "The End"]
    st.markdown(
        f'<p class="page-counter">{labels[st.session_state.page]} &nbsp;·&nbsp; {st.session_state.page + 1} / {TOTAL}</p>',
        unsafe_allow_html=True
    )

with col_next:
    if st.button("›", disabled=(st.session_state.page == TOTAL - 1), key="next"):
        st.session_state.page += 1
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
