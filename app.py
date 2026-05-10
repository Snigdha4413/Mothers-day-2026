from streamlit.components.v1 import html as st_html
import streamlit as st

st.set_page_config(
    page_title="A Fairytale Mother's Day Book",
    page_icon="🌙",
    layout="centered",
)

st.markdown("""
<style>
body, .stApp { background: #1a0d2e !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

BOOK_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"/>
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,600&family=Dancing+Script:wght@400;700&family=IM+Fell+English:ital@0;1&display=swap');

* { margin:0; padding:0; box-sizing:border-box; }
:root {
  --rose:#c8506a; --gold:#b8882a; --parchment:#f9f1e2;
  --ink:#2d1a0e; --sage:#5a7a52; --lavender:#7a68a8; --midnight:#1a0d2e;
}
html,body { background:#1a0d2e; margin:0; padding:0; overflow:hidden; }

#book-shell {
  width:100%; height:100vh; background:#1a0d2e;
  overflow:hidden; position:relative;
  font-family:'IM Fell English',serif;
}
#strip-wrap { width:100%; height:calc(100vh - 56px); overflow:hidden; position:relative; }
#strip {
  display:flex; flex-direction:row; height:100%;
  transition:transform 0.6s cubic-bezier(0.77,0,0.18,1); will-change:transform;
}
.page {
  flex:0 0 100%; width:100%; height:100%;
  overflow-y:auto; overflow-x:hidden; position:relative;
  display:flex; flex-direction:column; align-items:center;
  -webkit-overflow-scrolling:touch;
}
.page::-webkit-scrollbar { display:none; }
.page { -ms-overflow-style:none; scrollbar-width:none; }

/* PAGE THEMES */
.pg-cover { background:radial-gradient(ellipse at 50% 55%,#2d1050 0%,#1a0d2e 65%,#0d0618 100%); }
.pg-p1    { background:linear-gradient(170deg,#1f0a30 0%,#3d1850 45%,#1a0d2e 100%); }
.pg-p2    { background:linear-gradient(160deg,#0d2010 0%,#1a4025 50%,#0d2010 100%); }
.pg-p3    { background:linear-gradient(165deg,#1a1030 0%,#2e1848 50%,#1a0820 100%); }
.pg-p4    { background:linear-gradient(160deg,#0d1a28 0%,#1a3048 50%,#0d1520 100%); }
.pg-final { background:radial-gradient(ellipse at 50% 40%,#2d1050 0%,#1a0d2e 70%); }

/* COVER */
.cover-frame {
  position:absolute; inset:12px; border:1px solid rgba(184,136,42,0.4);
  border-radius:10px; pointer-events:none;
  animation:glimmer 4s ease-in-out infinite alternate;
}
@keyframes glimmer {
  from { border-color:rgba(184,136,42,0.2); box-shadow:inset 0 0 40px rgba(184,136,42,0.03); }
  to   { border-color:rgba(184,136,42,0.6); box-shadow:inset 0 0 80px rgba(184,136,42,0.07); }
}
.cover-content {
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  min-height:100%; width:100%; padding:40px 28px 70px;
  text-align:center; gap:10px; position:relative; z-index:2;
}
.cover-eye {
  font-size:56px; animation:breathe 3s ease-in-out infinite;
  filter:drop-shadow(0 0 18px rgba(200,160,60,0.5));
}
@keyframes breathe { 0%,100%{transform:scale(1);} 50%{transform:scale(1.08);} }
.cover-subtitle {
  font-family:'Dancing Script',cursive; font-size:15px; letter-spacing:4px;
  text-transform:uppercase; color:rgba(240,210,140,0.75);
}
.cover-name-display {
  font-family:'Dancing Script',cursive; font-size:26px; color:#f5dfa0;
}
.cover-title {
  font-family:'Playfair Display',serif; font-size:clamp(30px,7vw,50px);
  font-style:italic; font-weight:700; color:#f9f1e2; line-height:1.1;
  text-shadow:0 0 40px rgba(200,100,130,0.4);
}
.cover-title em { color:#e0807a; font-style:normal; }
.cover-rule {
  width:80px; height:1px;
  background:linear-gradient(90deg,transparent,rgba(184,136,42,0.8),transparent);
}
.cover-tagline {
  font-family:'IM Fell English',serif; font-style:italic; font-size:14px;
  color:rgba(240,210,160,0.7); max-width:280px; line-height:1.8;
}
.turn-hint {
  position:absolute; bottom:64px; right:22px;
  font-family:'Dancing Script',cursive; font-size:13px;
  color:rgba(240,210,140,0.5); display:flex; align-items:center; gap:6px;
  animation:nudge 2s ease-in-out infinite;
}
@keyframes nudge { 0%,100%{transform:translateX(0);} 50%{transform:translateX(4px);} }

/* INNER PAGES */
.page-inner {
  max-width:480px; width:100%; display:flex; flex-direction:column;
  align-items:center; gap:16px; text-align:center; padding:36px 22px 80px;
  opacity:0; transform:translateY(24px); transition:opacity 0.7s ease,transform 0.7s ease;
}
.page-inner.vis { opacity:1; transform:translateY(0); }
.pg-label   { font-family:'Dancing Script',cursive; font-size:13px; color:rgba(240,210,140,0.45); letter-spacing:3px; }
.pg-chapter { font-family:'Dancing Script',cursive; font-size:22px; color:#d4836a; letter-spacing:1px; }
.pg-heading { font-family:'Playfair Display',serif; font-size:clamp(20px,4vw,28px); font-style:italic; font-weight:400; color:#f0ddb8; line-height:1.25; }
.pg-heading em { color:#d4836a; font-style:normal; }
.ornament   { font-size:14px; color:rgba(184,136,42,0.7); letter-spacing:8px; }
.pg-text    { font-family:'IM Fell English',serif; font-size:15px; font-style:italic; line-height:1.9; color:rgba(240,220,180,0.82); font-weight:400; }
.pg-text strong { color:#e0a060; font-style:normal; }

/* STORY CARD */
.story-card {
  background:rgba(240,230,200,0.07); border:1px solid rgba(184,136,42,0.25);
  border-radius:10px; padding:20px 22px; width:100%; position:relative;
}
.story-card::before {
  content:'"'; position:absolute; top:-6px; left:14px;
  font-family:'Playfair Display',serif; font-size:48px;
  color:rgba(200,80,106,0.18); line-height:1;
}

/* PARCHMENT LETTER */
.letter {
  background:rgba(249,241,226,0.08); border:1px solid rgba(184,136,42,0.3);
  border-radius:4px; padding:24px 22px; width:100%;
  font-family:'IM Fell English',serif; font-style:italic; font-size:15px;
  line-height:1.95; color:rgba(240,220,180,0.85);
}
.letter::after { content:'❧'; display:block; text-align:right; font-size:16px; color:#c8506a; margin-top:10px; }
.letter strong { color:#e0a060; font-style:normal; }

/* SVG SCENE */
.scene { width:100%; max-width:400px; border-radius:14px; overflow:hidden; box-shadow:0 4px 28px rgba(0,0,0,0.5); cursor:default; flex-shrink:0; }
.scene svg { display:block; width:100%; height:auto; }
.tap-label { font-family:'Dancing Script',cursive; font-size:12px; color:rgba(240,210,140,0.4); letter-spacing:1px; margin-top:-8px; }

/* TAP ANIMATIONS */
.sparkle { animation:sparkleAnim 0.6s ease forwards; }
@keyframes sparkleAnim {
  0%  { transform:scale(1) rotate(0deg); }
  30% { transform:scale(1.5) rotate(15deg); filter:brightness(2); }
  70% { transform:scale(0.9) rotate(-8deg); filter:brightness(1.5); }
  100%{ transform:scale(1) rotate(0deg); filter:brightness(1); }
}
.bloom { animation:bloomAnim 0.7s ease forwards; }
@keyframes bloomAnim {
  0%  { transform:scale(0.4) rotate(-30deg); opacity:0.3; }
  55% { transform:scale(1.25) rotate(8deg); opacity:1; }
  100%{ transform:scale(1) rotate(0deg); opacity:1; }
}
.float-up { animation:floatUpAnim 0.9s ease forwards; }
@keyframes floatUpAnim {
  0%  { transform:translateY(0) rotate(0deg); opacity:1; }
  100%{ transform:translateY(-36px) rotate(25deg); opacity:0; }
}
.wiggle { animation:wiggleAnim 0.5s ease forwards; }
@keyframes wiggleAnim {
  0%  { transform:rotate(0deg); }
  25% { transform:rotate(-12deg) scale(1.1); }
  50% { transform:rotate(12deg) scale(1.15); }
  75% { transform:rotate(-6deg) scale(1.05); }
  100%{ transform:rotate(0deg) scale(1); }
}
.pulse { animation:pulseAnim 0.5s ease forwards; }
@keyframes pulseAnim {
  0%  { transform:scale(1); }
  40% { transform:scale(1.35); filter:brightness(1.6) drop-shadow(0 0 8px gold); }
  100%{ transform:scale(1); filter:brightness(1); }
}

/* ATTRIBS */
.attribs { display:flex; flex-wrap:wrap; gap:8px; justify-content:center; list-style:none; }
.attribs li {
  background:rgba(240,230,200,0.1); border:1px solid rgba(184,136,42,0.3);
  border-radius:30px; padding:5px 14px;
  font-family:'IM Fell English',serif; font-size:13px; font-style:italic;
  color:rgba(240,220,180,0.8);
}

/* FINAL PAGE */
.final-heading { font-family:'Playfair Display',serif; font-size:clamp(22px,5vw,34px); font-style:italic; color:#f9f1e2; line-height:1.2; }
.final-heading .mum-name { color:#e0807a; }
.big-heart {
  font-size:72px; animation:heartbeat 1.5s ease-in-out infinite;
  filter:drop-shadow(0 0 24px rgba(200,80,100,0.7));
}
@keyframes heartbeat { 0%,100%{transform:scale(1);} 15%{transform:scale(1.12);} 30%{transform:scale(1);} 45%{transform:scale(1.06);} }
.signature { font-family:'Dancing Script',cursive; font-size:26px; color:#b8882a; margin-top:4px; }
.sparkle-row { display:flex; gap:10px; justify-content:center; font-size:22px; }

/* STARS */
#stars { position:absolute; inset:0; pointer-events:none; z-index:0; overflow:hidden; }
.star { position:absolute; border-radius:50%; animation:twinkle ease-in-out infinite; }
@keyframes twinkle { 0%,100%{opacity:0.1;transform:scale(1);} 50%{opacity:0.9;transform:scale(1.4);} }

/* NAV */
#nav {
  display:flex; align-items:center; justify-content:center; gap:14px;
  height:56px; padding:0 16px;
  background:linear-gradient(to top,rgba(10,4,20,0.98),rgba(10,4,20,0.6));
  position:relative; z-index:20;
}
.nav-btn {
  background:rgba(255,255,255,0.08); border:1px solid rgba(184,136,42,0.4);
  border-radius:50%; width:40px; height:40px;
  display:flex; align-items:center; justify-content:center;
  font-size:20px; cursor:pointer; color:#f5dfa0;
  transition:background 0.2s,transform 0.15s,opacity 0.3s; user-select:none;
}
.nav-btn:hover  { background:rgba(184,136,42,0.18); transform:scale(1.1); }
.nav-btn:active { transform:scale(0.92); }
.nav-btn[disabled] { opacity:0.2; pointer-events:none; }
.dots { display:flex; gap:7px; align-items:center; }
.dot { width:6px; height:6px; border-radius:50%; background:rgba(255,255,255,0.25); transition:background 0.3s,transform 0.3s; cursor:pointer; }
.dot.on { background:#b8882a; transform:scale(1.4); }
</style>
</head>
<body>

<div id="book-shell">
  <div id="stars"></div>
  <div id="strip-wrap">
  <div id="strip">

  <!-- PAGE 0: COVER -->
  <div class="page pg-cover">
    <div class="cover-frame"></div>
    <div class="cover-content">
      <div class="cover-eye" onclick="tap(this,'pulse')" style="cursor:pointer">🌙</div>
      <div class="cover-subtitle">A Fairytale For</div>
      <div class="cover-name-display">✦ Mummy ✦</div>
      <h1 class="cover-title">Happy<br/><em>Mother's</em> Day</h1>
      <div class="cover-rule"></div>
      <p class="cover-tagline">Once upon a time, a mother made the whole world magical.</p>
      <div class="turn-hint">turn the page ›</div>
    </div>
  </div>

  <!-- PAGE 1: The Enchanted Garden -->
  <div class="page pg-p1">
    <div class="page-inner" data-pi>
      <div class="pg-label">~ Page One ~</div>
      <div class="pg-chapter">The Enchanted Garden</div>
      <h2 class="pg-heading">Where Every Flower<br/>Knew Your <em>Name</em></h2>
      <div class="ornament">❧ ✦ ❧</div>
      <div class="scene">
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
          <g style="cursor:pointer" onclick="tapSvg(this,'pulse')">
            <circle cx="340" cy="45" r="22" fill="#f5d080" opacity="0.92"/>
            <circle cx="352" cy="38" r="17" fill="#2a1050"/>
            <circle cx="344" cy="52" r="3" fill="#f5d080" opacity="0.4"/>
          </g>
          <ellipse cx="80" cy="230" rx="160" ry="90" fill="#2a0e4a" opacity="0.9"/>
          <ellipse cx="320" cy="235" rx="180" ry="95" fill="#220b40" opacity="0.8"/>
          <ellipse cx="200" cy="245" rx="250" ry="100" fill="#1a0830"/>
          <rect x="0" y="178" width="400" height="42" fill="#1a0830"/>
          <rect x="0" y="175" width="400" height="8" fill="#2d1060" opacity="0.6" rx="2"/>
          <rect x="185" y="90" width="14" height="90" fill="#5a3010" rx="3"/>
          <g style="cursor:pointer;transform-origin:193px 65px" onclick="tapSvg(this,'sparkle')">
            <circle cx="193" cy="68" r="42" fill="#3a1870" opacity="0.9"/>
            <circle cx="168" cy="82" r="26" fill="#2e1460" opacity="0.8"/>
            <circle cx="218" cy="80" r="24" fill="#2e1460" opacity="0.7"/>
            <circle cx="178" cy="58" r="5" fill="#ffb040" opacity="0.9"/>
            <circle cx="200" cy="46" r="4" fill="#80d0ff" opacity="0.8"/>
            <circle cx="215" cy="65" r="4.5" fill="#ff8080" opacity="0.8"/>
            <circle cx="185" cy="82" r="3.5" fill="#a0ff80" opacity="0.7"/>
            <circle cx="205" cy="78" r="3" fill="#ffd580" opacity="0.8"/>
          </g>
          <g style="cursor:pointer;transform-origin:60px 178px" onclick="tapSvg(this,'bloom')">
            <rect x="58" y="155" width="4" height="28" fill="#3a6030" rx="1"/>
            <circle cx="60" cy="152" r="11" fill="#c8506a"/>
            <circle cx="60" cy="152" r="6" fill="#ffd580" opacity="0.9"/>
            <circle cx="54" cy="146" r="5" fill="#c8506a" opacity="0.7"/>
            <circle cx="66" cy="146" r="5" fill="#c8506a" opacity="0.7"/>
            <circle cx="54" cy="158" r="5" fill="#c8506a" opacity="0.7"/>
            <circle cx="66" cy="158" r="5" fill="#c8506a" opacity="0.7"/>
          </g>
          <g style="cursor:pointer;transform-origin:100px 178px" onclick="tapSvg(this,'bloom')">
            <rect x="98" y="158" width="4" height="24" fill="#3a6030" rx="1"/>
            <circle cx="100" cy="155" r="9" fill="#7a68a8"/>
            <circle cx="100" cy="155" r="5" fill="#ffd580" opacity="0.9"/>
            <circle cx="95" cy="150" r="4.5" fill="#7a68a8" opacity="0.7"/>
            <circle cx="105" cy="150" r="4.5" fill="#7a68a8" opacity="0.7"/>
            <circle cx="95" cy="160" r="4.5" fill="#7a68a8" opacity="0.7"/>
            <circle cx="105" cy="160" r="4.5" fill="#7a68a8" opacity="0.7"/>
          </g>
          <g style="cursor:pointer;transform-origin:270px 178px" onclick="tapSvg(this,'bloom')">
            <rect x="268" y="156" width="4" height="26" fill="#3a6030" rx="1"/>
            <circle cx="270" cy="153" r="10" fill="#4a9060"/>
            <circle cx="270" cy="153" r="5" fill="#ffd580" opacity="0.9"/>
            <circle cx="264" cy="147" r="5" fill="#4a9060" opacity="0.7"/>
            <circle cx="276" cy="147" r="5" fill="#4a9060" opacity="0.7"/>
            <circle cx="264" cy="159" r="5" fill="#4a9060" opacity="0.7"/>
            <circle cx="276" cy="159" r="5" fill="#4a9060" opacity="0.7"/>
          </g>
          <g style="cursor:pointer;transform-origin:320px 178px" onclick="tapSvg(this,'bloom')">
            <rect x="318" y="160" width="4" height="22" fill="#3a6030" rx="1"/>
            <circle cx="320" cy="157" r="9" fill="#d08030"/>
            <circle cx="320" cy="157" r="5" fill="#ffd580" opacity="0.9"/>
            <circle cx="315" cy="152" r="4.5" fill="#d08030" opacity="0.7"/>
            <circle cx="325" cy="152" r="4.5" fill="#d08030" opacity="0.7"/>
            <circle cx="315" cy="162" r="4.5" fill="#d08030" opacity="0.7"/>
            <circle cx="325" cy="162" r="4.5" fill="#d08030" opacity="0.7"/>
          </g>
          <g style="cursor:pointer;transform-origin:130px 140px" onclick="tapSvg(this,'float-up')">
            <circle cx="130" cy="140" r="3" fill="#a0ff80" opacity="0.9"/>
            <circle cx="130" cy="140" r="6" fill="#a0ff80" opacity="0.2"/>
          </g>
          <g style="cursor:pointer;transform-origin:360px 150px" onclick="tapSvg(this,'float-up')">
            <circle cx="360" cy="150" r="2.5" fill="#80e0ff" opacity="0.9"/>
            <circle cx="360" cy="150" r="5" fill="#80e0ff" opacity="0.2"/>
          </g>
          <g style="cursor:pointer;transform-origin:42px 160px" onclick="tapSvg(this,'float-up')">
            <circle cx="42" cy="160" r="2.5" fill="#ffd580" opacity="0.85"/>
            <circle cx="42" cy="160" r="5" fill="#ffd580" opacity="0.2"/>
          </g>
          <path d="M0,200 Q100,185 200,195 Q300,205 400,190" stroke="#7a68a8" stroke-width="1.5" fill="none" opacity="0.35" stroke-dasharray="6,4"/>
        </svg>
      </div>
      <p class="tap-label">✦ tap the flowers, fireflies &amp; moon ✦</p>
      <div class="story-card">
        <p class="pg-text">
          In a garden where the flowers glowed at midnight,
          there lived a mother whose kindness was older than the stars.
          Every bloom knew her name — and leaned toward her voice
          the way all living things lean toward the light.
        </p>
      </div>
    </div>
  </div>

  <!-- PAGE 2: The Forest of Memories -->
  <div class="page pg-p2">
    <div class="page-inner" data-pi>
      <div class="pg-label">~ Page Two ~</div>
      <div class="pg-chapter">The Forest of Memories</div>
      <h2 class="pg-heading">Where Every Tree<br/>Held a <em>Story</em></h2>
      <div class="ornament">❧ ✦ ❧</div>
      <div class="scene">
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
          <ellipse cx="340" cy="200" rx="100" ry="28" fill="#1a4025" opacity="0.3"/>
          <rect x="55" y="80" width="18" height="130" fill="#2a1808" rx="4"/>
          <g style="cursor:pointer;transform-origin:64px 52px" onclick="tapSvg(this,'sparkle')">
            <ellipse cx="64" cy="56" rx="50" ry="40" fill="#1a4820" opacity="0.95"/>
            <ellipse cx="40" cy="72" rx="30" ry="24" fill="#153d18" opacity="0.8"/>
            <ellipse cx="88" cy="70" rx="28" ry="22" fill="#153d18" opacity="0.75"/>
            <circle cx="50" cy="50" r="4" fill="#40ff80" opacity="0.6"/>
            <circle cx="72" cy="38" r="3" fill="#80ffd0" opacity="0.55"/>
            <circle cx="82" cy="60" r="3.5" fill="#40ff80" opacity="0.5"/>
            <circle cx="58" cy="68" r="3" fill="#c0ffb0" opacity="0.6"/>
          </g>
          <rect x="148" y="70" width="16" height="140" fill="#2a1808" rx="3"/>
          <g style="cursor:pointer;transform-origin:156px 42px" onclick="tapSvg(this,'sparkle')">
            <ellipse cx="156" cy="46" rx="55" ry="44" fill="#1c5224" opacity="0.95"/>
            <ellipse cx="128" cy="64" rx="32" ry="26" fill="#163d1a" opacity="0.8"/>
            <ellipse cx="184" cy="62" rx="30" ry="24" fill="#163d1a" opacity="0.75"/>
            <circle cx="140" cy="40" r="4.5" fill="#ffd580" opacity="0.6"/>
            <circle cx="165" cy="30" r="3.5" fill="#a0ffb0" opacity="0.6"/>
            <circle cx="176" cy="52" r="3" fill="#ffd580" opacity="0.5"/>
            <circle cx="148" cy="60" r="3.5" fill="#80ffd0" opacity="0.6"/>
            <circle cx="170" cy="66" r="3" fill="#a0ffb0" opacity="0.55"/>
          </g>
          <rect x="290" y="85" width="15" height="125" fill="#2a1808" rx="3"/>
          <g style="cursor:pointer;transform-origin:298px 55px" onclick="tapSvg(this,'sparkle')">
            <ellipse cx="298" cy="58" rx="48" ry="38" fill="#1a4820" opacity="0.95"/>
            <ellipse cx="275" cy="74" rx="28" ry="22" fill="#153d18" opacity="0.8"/>
            <ellipse cx="320" cy="72" rx="26" ry="20" fill="#153d18" opacity="0.75"/>
            <circle cx="285" cy="52" r="4" fill="#40ff80" opacity="0.6"/>
            <circle cx="306" cy="42" r="3" fill="#c0ffb0" opacity="0.55"/>
            <circle cx="315" cy="60" r="3.5" fill="#40ff80" opacity="0.5"/>
          </g>
          <g style="cursor:pointer;transform-origin:110px 195px" onclick="tapSvg(this,'bloom')">
            <ellipse cx="110" cy="198" rx="16" ry="5" fill="#ff8060" opacity="0.7"/>
            <path d="M103,198 Q110,175 117,198" fill="#ff6040" opacity="0.9"/>
            <circle cx="107" cy="188" r="2.5" fill="white" opacity="0.6"/>
            <circle cx="114" cy="182" r="2" fill="white" opacity="0.5"/>
          </g>
          <g style="cursor:pointer;transform-origin:240px 198px" onclick="tapSvg(this,'bloom')">
            <ellipse cx="240" cy="201" rx="12" ry="4" fill="#ff8060" opacity="0.7"/>
            <path d="M234,201 Q240,183 246,201" fill="#ff6040" opacity="0.9"/>
            <circle cx="238" cy="192" r="2" fill="white" opacity="0.5"/>
          </g>
          <g style="cursor:pointer;transform-origin:360px 200px" onclick="tapSvg(this,'bloom')">
            <ellipse cx="360" cy="203" rx="10" ry="3.5" fill="#b060ff" opacity="0.7"/>
            <path d="M354,203 Q360,187 366,203" fill="#9040e0" opacity="0.9"/>
            <circle cx="358" cy="194" r="1.8" fill="white" opacity="0.5"/>
          </g>
          <g style="cursor:pointer;transform-origin:348px 120px" onclick="tapSvg(this,'wiggle')">
            <ellipse cx="348" cy="128" rx="14" ry="18" fill="#5a3a10"/>
            <circle cx="342" cy="120" r="8" fill="#7a5a20"/>
            <circle cx="354" cy="120" r="8" fill="#7a5a20"/>
            <circle cx="342" cy="120" r="5" fill="#1a0820"/>
            <circle cx="354" cy="120" r="5" fill="#1a0820"/>
            <circle cx="343" cy="119" r="2" fill="white"/>
            <circle cx="355" cy="119" r="2" fill="white"/>
            <polygon points="348,124 345,128 351,128" fill="#c8803a"/>
            <path d="M334,128 Q320,138 330,148 Q338,138 348,133" fill="#4a2a08" opacity="0.8"/>
            <path d="M362,128 Q376,138 366,148 Q358,138 348,133" fill="#4a2a08" opacity="0.8"/>
          </g>
          <line x1="55" y1="110" x2="155" y2="100" stroke="#3a6030" stroke-width="1.5" opacity="0.5"/>
          <circle cx="75" cy="108" r="3" fill="#ffd580" opacity="0.8"/>
          <circle cx="95" cy="104" r="3" fill="#ff8080" opacity="0.8"/>
          <circle cx="115" cy="103" r="3" fill="#80d0ff" opacity="0.8"/>
          <circle cx="135" cy="101" r="3" fill="#a0ff80" opacity="0.8"/>
          <circle cx="200" cy="18" r="18" fill="#f5e0a0" opacity="0.85"/>
          <circle cx="200" cy="18" r="12" fill="#f9f0c0"/>
        </svg>
      </div>
      <p class="tap-label">✦ tap the trees, mushrooms &amp; owl ✦</p>
      <p class="pg-text">
        Deep in the Forest of Memories, every tree was a story she had told.
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
  </div>

  <!-- PAGE 3: The Starweaver -->
  <div class="page pg-p3">
    <div class="page-inner" data-pi>
      <div class="pg-label">~ Page Three ~</div>
      <div class="pg-chapter">The Starweaver</div>
      <h2 class="pg-heading">She Stitched the Sky<br/>With <em>Care</em></h2>
      <div class="ornament">❧ ✦ ❧</div>
      <div class="scene">
        <svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="mg3" cx="50%" cy="40%" r="65%">
              <stop offset="0%" stop-color="#1a0838"/>
              <stop offset="100%" stop-color="#08040e"/>
            </radialGradient>
          </defs>
          <rect width="400" height="220" fill="url(#mg3)"/>
          <line x1="80" y1="50" x2="140" y2="80" stroke="rgba(180,160,220,0.25)" stroke-width="1"/>
          <line x1="140" y1="80" x2="200" y2="60" stroke="rgba(180,160,220,0.25)" stroke-width="1"/>
          <line x1="200" y1="60" x2="260" y2="90" stroke="rgba(180,160,220,0.25)" stroke-width="1"/>
          <line x1="260" y1="90" x2="320" y2="55" stroke="rgba(180,160,220,0.25)" stroke-width="1"/>
          <line x1="140" y1="80" x2="160" y2="120" stroke="rgba(180,160,220,0.2)" stroke-width="1"/>
          <line x1="200" y1="60" x2="220" y2="110" stroke="rgba(180,160,220,0.2)" stroke-width="1"/>
          <g style="cursor:pointer;transform-origin:80px 50px" onclick="tapSvg(this,'pulse')">
            <circle cx="80" cy="50" r="5" fill="#ffd580" opacity="0.95"/>
            <circle cx="80" cy="50" r="9" fill="#ffd580" opacity="0.2"/>
          </g>
          <g style="cursor:pointer;transform-origin:140px 80px" onclick="tapSvg(this,'pulse')">
            <circle cx="140" cy="80" r="6" fill="#c9b8e8" opacity="0.95"/>
            <circle cx="140" cy="80" r="11" fill="#c9b8e8" opacity="0.18"/>
          </g>
          <g style="cursor:pointer;transform-origin:200px 60px" onclick="tapSvg(this,'pulse')">
            <circle cx="200" cy="60" r="7" fill="#f5d080" opacity="0.95"/>
            <circle cx="200" cy="60" r="13" fill="#f5d080" opacity="0.2"/>
          </g>
          <g style="cursor:pointer;transform-origin:260px 90px" onclick="tapSvg(this,'pulse')">
            <circle cx="260" cy="90" r="5" fill="#80d0ff" opacity="0.95"/>
            <circle cx="260" cy="90" r="9" fill="#80d0ff" opacity="0.18"/>
          </g>
          <g style="cursor:pointer;transform-origin:320px 55px" onclick="tapSvg(this,'pulse')">
            <circle cx="320" cy="55" r="5.5" fill="#ffd580" opacity="0.9"/>
            <circle cx="320" cy="55" r="10" fill="#ffd580" opacity="0.18"/>
          </g>
          <g style="cursor:pointer;transform-origin:160px 120px" onclick="tapSvg(this,'pulse')">
            <circle cx="160" cy="120" r="4" fill="#ff9080" opacity="0.9"/>
            <circle cx="160" cy="120" r="7" fill="#ff9080" opacity="0.18"/>
          </g>
          <g style="cursor:pointer;transform-origin:220px 110px" onclick="tapSvg(this,'pulse')">
            <circle cx="220" cy="110" r="4.5" fill="#a0ff80" opacity="0.9"/>
            <circle cx="220" cy="110" r="8" fill="#a0ff80" opacity="0.18"/>
          </g>
          <ellipse cx="200" cy="195" rx="52" ry="18" fill="#2a1050" opacity="0.95"/>
          <path d="M170,165 Q200,140 230,165 L240,210 Q200,218 160,210 Z" fill="#3a1870"/>
          <path d="M178,155 Q200,145 222,155 L225,175 Q200,180 175,175 Z" fill="#4a2090"/>
          <circle cx="200" cy="145" r="15" fill="#5a3a20"/>
          <circle cx="193" cy="132" r="3" fill="#ffd580" opacity="0.9"/>
          <circle cx="200" cy="129" r="3.5" fill="#f5d080" opacity="0.95"/>
          <circle cx="207" cy="132" r="3" fill="#ffd580" opacity="0.9"/>
          <path d="M178,158 Q155,135 140,80" stroke="#5a3a20" stroke-width="7" fill="none" stroke-linecap="round"/>
          <path d="M222,158 Q245,135 260,90" stroke="#5a3a20" stroke-width="7" fill="none" stroke-linecap="round"/>
          <path d="M140,80 Q170,68 200,60 Q230,52 260,90" stroke="rgba(200,180,255,0.5)" stroke-width="1" fill="none" stroke-dasharray="3,3"/>
          <g style="cursor:pointer;transform-origin:340px 140px" onclick="tapSvg(this,'float-up')">
            <line x1="340" y1="140" x2="375" y2="115" stroke="#ffd580" stroke-width="2" opacity="0.8"/>
            <circle cx="340" cy="140" r="4" fill="#ffd580" opacity="0.95"/>
            <circle cx="340" cy="140" r="7" fill="#ffd580" opacity="0.2"/>
          </g>
          <path d="M0,190 Q100,175 200,185 Q300,195 400,180" stroke="#4a90c0" stroke-width="12" fill="none" opacity="0.1"/>
          <path d="M0,195 Q100,180 200,192 Q300,204 400,186" stroke="#7a68a8" stroke-width="8" fill="none" opacity="0.12"/>
        </svg>
      </div>
      <p class="tap-label">✦ tap the stars &amp; shooting star ✦</p>
      <div class="letter">
        They say there is a woman who weaves the stars each night —
        who decides which ones shine brighter, and which ones fall
        so that someone, somewhere, can make a wish.<br/><br/>
        We always believed it was <strong>Mummy</strong>.
        Because everything good in our sky has your handwriting on it.
      </div>
    </div>
  </div>

  <!-- PAGE 4: The Sea of Dreams -->
  <div class="page pg-p4">
    <div class="page-inner" data-pi>
      <div class="pg-label">~ Page Four ~</div>
      <div class="pg-chapter">The Sea of Dreams</div>
      <h2 class="pg-heading">She Lit the Lighthouse<br/>Every <em>Night</em></h2>
      <div class="ornament">❧ ✦ ❧</div>
      <div class="scene">
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
          <ellipse cx="200" cy="210" rx="30" ry="8" fill="#f5e080" opacity="0.15"/>
          <rect x="196" y="155" width="8" height="55" fill="#f5e080" opacity="0.08"/>
          <g style="cursor:pointer" onclick="tapSvg(this,'wiggle')">
            <path d="M0,165 Q50,155 100,165 Q150,175 200,165 Q250,155 300,165 Q350,175 400,165" stroke="#1a4080" stroke-width="3" fill="none" opacity="0.7"/>
            <path d="M0,178 Q50,168 100,178 Q150,188 200,178 Q250,168 300,178 Q350,188 400,178" stroke="#1a3060" stroke-width="3" fill="none" opacity="0.8"/>
            <rect x="0" y="175" width="400" height="45" fill="#0d2040" opacity="0.9"/>
            <path d="M0,175 Q50,165 100,175 Q150,185 200,175 Q250,165 300,175 Q350,185 400,175" fill="#0d2040" opacity="0.8"/>
          </g>
          <circle cx="30" cy="20" r="1.5" fill="#ffd580" opacity="0.8"/>
          <circle cx="70" cy="40" r="1" fill="white" opacity="0.6"/>
          <circle cx="120" cy="15" r="1.5" fill="#c9b8e8" opacity="0.7"/>
          <circle cx="280" cy="25" r="1.5" fill="#ffd580" opacity="0.7"/>
          <circle cx="380" cy="20" r="1.5" fill="#c9b8e8" opacity="0.7"/>
          <g style="cursor:pointer;transform-origin:200px 40px" onclick="tapSvg(this,'pulse')">
            <circle cx="200" cy="40" r="28" fill="#f5e090" opacity="0.95"/>
            <circle cx="200" cy="40" r="40" fill="#f5e090" opacity="0.1"/>
            <circle cx="213" cy="32" r="20" fill="#0a1830"/>
            <circle cx="205" cy="48" r="4" fill="#f5e090" opacity="0.25"/>
            <circle cx="192" cy="36" r="3" fill="#f5e090" opacity="0.2"/>
          </g>
          <ellipse cx="88" cy="178" rx="40" ry="14" fill="#1a2a3a"/>
          <ellipse cx="88" cy="175" rx="32" ry="10" fill="#243444"/>
          <rect x="78" y="80" width="22" height="96" fill="#e8e0d0" rx="4"/>
          <rect x="80" y="80" width="18" height="96" fill="#d4ccc0" rx="3"/>
          <rect x="78" y="100" width="22" height="14" fill="#c8506a"/>
          <rect x="78" y="130" width="22" height="14" fill="#c8506a"/>
          <rect x="78" y="160" width="22" height="14" fill="#c8506a"/>
          <rect x="72" y="70" width="34" height="14" fill="#a89888" rx="2"/>
          <rect x="76" y="74" width="26" height="8" fill="#c9b8e8" opacity="0.6" rx="2"/>
          <g style="cursor:pointer;transform-origin:89px 56px" onclick="tapSvg(this,'pulse')">
            <ellipse cx="89" cy="56" rx="30" ry="20" fill="url(#lglow)"/>
            <circle cx="89" cy="62" r="10" fill="#ffd580" opacity="0.9"/>
            <circle cx="89" cy="62" r="7" fill="white" opacity="0.7"/>
          </g>
          <path d="M95,62 L340,130" stroke="#ffd580" stroke-width="1.5" opacity="0.12"/>
          <path d="M95,64 L340,160" stroke="#ffd580" stroke-width="1.5" opacity="0.1"/>
          <g style="cursor:pointer;transform-origin:300px 162px" onclick="tapSvg(this,'wiggle')">
            <path d="M268,170 Q300,178 332,170 L325,160 Q300,163 275,160 Z" fill="#5a3a20"/>
            <rect x="298" y="120" width="4" height="42" fill="#7a5a30"/>
            <path d="M302,124 Q330,138 302,158" fill="white" opacity="0.85"/>
            <path d="M298,126 Q272,140 298,158" fill="#e8e0d0" opacity="0.8"/>
            <polygon points="302,120 316,126 302,132" fill="#c8506a" opacity="0.9"/>
          </g>
          <g style="cursor:pointer;transform-origin:150px 195px" onclick="tapSvg(this,'bloom')">
            <circle cx="150" cy="195" r="4" fill="#40d0c0" opacity="0.7"/>
            <circle cx="150" cy="195" r="8" fill="#40d0c0" opacity="0.15"/>
          </g>
          <g style="cursor:pointer;transform-origin:360px 200px" onclick="tapSvg(this,'bloom')">
            <circle cx="360" cy="200" r="3.5" fill="#80a0ff" opacity="0.7"/>
            <circle cx="360" cy="200" r="7" fill="#80a0ff" opacity="0.15"/>
          </g>
        </svg>
      </div>
      <p class="tap-label">✦ tap the moon, lighthouse, boat &amp; sea ✦</p>
      <div class="story-card">
        <p class="pg-text">
          On every stormy night at sea, the sailors looked for one light.
          Not the brightest — the steadiest.<br/><br/>
          That's what <strong>Mummy</strong> has always been.
          <strong>The light that never goes out</strong>.
          The one we navigate home by, no matter how far we've sailed.
        </p>
      </div>
    </div>
  </div>

  <!-- FINAL PAGE -->
  <div class="page pg-final">
    <div class="page-inner final-content" data-pi>
      <div class="pg-label">~ The End ~</div>
      <div class="big-heart" style="cursor:pointer" onclick="tap(this,'pulse')">💗</div>
      <h2 class="final-heading">Happy Mother's Day,<br/><span class="mum-name">Mummy</span></h2>
      <div class="ornament" style="color:rgba(184,136,42,0.8)">✦ ✦ ✦</div>
      <p class="pg-text" style="color:rgba(240,220,180,0.75)">
        And they all lived, loved, and were grateful —
        because <span class="mum-name">Mummy</span> made every chapter worth reading.
      </p>
      <div class="sparkle-row">🌙 ⭐ 🌸 ✨ 🌺</div>
      <p class="signature">With all our love ♡</p>
      <div class="scene" style="margin-top:8px">
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
            font-family="'IM Fell English', serif" font-style="italic" font-size="16"
            fill="rgba(240,220,180,0.55)">once upon a time, and always ✦</text>
        </svg>
      </div>
    </div>
  </div>

  </div><!-- end strip -->
  </div><!-- end strip-wrap -->

  <!-- NAV -->
  <div id="nav">
    <button class="nav-btn" id="prevBtn" onclick="navigate(-1)">&#8249;</button>
    <div class="dots" id="dots"></div>
    <button class="nav-btn" id="nextBtn" onclick="navigate(1)">&#8250;</button>
  </div>
</div>

<script>
const TOTAL = 6;
let cur = 0;
const strip   = document.getElementById('strip');
const dotsEl  = document.getElementById('dots');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

for (let i = 0; i < TOTAL; i++) {
  const d = document.createElement('div');
  d.className = 'dot' + (i === 0 ? ' on' : '');
  d.onclick = () => goTo(i);
  dotsEl.appendChild(d);
}

function goTo(n) {
  cur = Math.max(0, Math.min(TOTAL - 1, n));
  strip.style.transform = 'translateX(' + (-cur * 100) + '%)';
  prevBtn.disabled = cur === 0;
  nextBtn.disabled = cur === TOTAL - 1;
  dotsEl.querySelectorAll('.dot').forEach(function(d, i) { d.classList.toggle('on', i === cur); });
  const page = strip.children[cur];
  if (page) page.scrollTop = 0;
  const inner = page && page.querySelector('[data-pi]');
  if (inner) {
    inner.classList.remove('vis');
    requestAnimationFrame(function() { requestAnimationFrame(function() { inner.classList.add('vis'); }); });
  }
}
window.navigate = function(dir) { goTo(cur + dir); };

// swipe support
let sx = 0, sy = 0;
const wrap = document.getElementById('strip-wrap');
wrap.addEventListener('touchstart', function(e) { sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, {passive:true});
wrap.addEventListener('touchend', function(e) {
  const dx = e.changedTouches[0].clientX - sx;
  const dy = e.changedTouches[0].clientY - sy;
  if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 38) navigate(dx < 0 ? 1 : -1);
}, {passive:true});
document.addEventListener('keydown', function(e) {
  if (e.key === 'ArrowRight') navigate(1);
  if (e.key === 'ArrowLeft')  navigate(-1);
});

goTo(0);

// tap animations
window.tap = function(el, type) {
  el.classList.remove('sparkle','bloom','float-up','wiggle','pulse');
  void el.offsetWidth;
  el.classList.add(type);
  el.addEventListener('animationend', function() { el.classList.remove(type); }, {once:true});
};
window.tapSvg = window.tap;

// twinkling stars
(function() {
  const s = document.getElementById('stars');
  for (let i = 0; i < 40; i++) {
    const el = document.createElement('div');
    el.className = 'star';
    const size = Math.random() * 2.5 + 1;
    const colors = ['#ffd580','white','#c9b8e8','#80d0ff'];
    el.style.cssText =
      'left:' + (Math.random()*100) + '%;top:' + (Math.random()*100) + '%;' +
      'width:' + size + 'px;height:' + size + 'px;' +
      'background:' + colors[Math.floor(Math.random()*colors.length)] + ';' +
      'animation-duration:' + (Math.random()*4+2) + 's;' +
      'animation-delay:' + (Math.random()*5) + 's;';
    s.appendChild(el);
  }
})();
</script>
</body>
</html>"""

st_html(BOOK_HTML, height=700, scrolling=False)
