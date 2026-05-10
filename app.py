import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Mother's Day 🌸",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .stApp { background: #1a0a2e; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
#  📸  PASTE YOUR PHOTO URLS HERE
#
#  How to get a direct image URL:
#  • Google Photos  → open photo → share → "Create link" → paste here
#  • WhatsApp saved → upload to imgbb.com (free) → copy "Direct link"
#  • Any photo      → upload to imgur.com → right-click → "Copy image address"
#
#  Leave a value as "" to show a decorative placeholder instead.
# ─────────────────────────────────────────────────────────────────────
PHOTO_1 = ""   # Cover — a portrait of Mum
PHOTO_2 = ""   # Page 2 — a favourite memory
PHOTO_3 = ""   # Page 3 — a together / family photo
PHOTO_4 = ""   # Page 4 — an everyday candid moment
PHOTO_5 = ""   # Final page photo
# ─────────────────────────────────────────────────────────────────────


def photo_slot(url, slot_id, shape="rect", dark=False):
    """
    Returns HTML for a photo slot.
    shape = "circle" | "rect" | "portrait"
    Falls back to an illustrated placeholder if url is empty or broken.
    """
    if shape == "circle":
        css_class = "photo-circle"
    elif shape == "portrait":
        css_class = "photo-portrait"
    else:
        css_class = "photo-rect"

    placeholder_bg = (
        "linear-gradient(135deg,#3d1a5c,#6a2080)"
        if dark
        else "linear-gradient(135deg,#f2b5c3,#d4a0b8)"
    )
    placeholder_txt = (
        "rgba(242,181,195,0.7)" if dark else "rgba(45,27,78,0.45)"
    )

    ph_html = (
        f'<div class="photo-placeholder {css_class}" '
        f'style="background:{placeholder_bg};">'
        f'<span class="ph-icon">📷</span>'
        f'<span class="ph-label" style="color:{placeholder_txt};">Paste your photo URL above</span>'
        f'</div>'
    )

    if url:
        return (
            f'<img id="{slot_id}" src="{url}" alt="photo" class="{css_class}" '
            f'onerror="this.outerHTML=\'{ph_html.replace(chr(39), chr(34))}\'" />'
        )
    return ph_html


STORYBOOK_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no"/>
<title>Happy Mother's Day</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,600&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet"/>
<style>
/* ── RESET ── */
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;}}
:root{{
  --rose:#e8607a;--blush:#f2b5c3;--gold:#d4a853;--cream:#fdf6ec;
  --sage:#7ca982;--lavender:#c9b8e8;--midnight:#1a0a2e;
  --parchment:#f5ead6;--ink:#2d1b4e;
}}
html,body{{
  width:100%;height:100%;overflow:hidden;
  font-family:'Cormorant Garamond',serif;
  background:var(--midnight);color:var(--ink);
  -webkit-font-smoothing:antialiased;
}}

/* ── AMBIENT PARTICLES (fixed, behind everything) ── */
#particles{{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;}}
.particle{{position:absolute;animation:floatUp linear infinite;opacity:0;}}
@keyframes floatUp{{
  0%{{transform:translateY(100vh) rotate(0deg);opacity:0;}}
  10%{{opacity:0.5;}}90%{{opacity:0.2;}}
  100%{{transform:translateY(-10vh) rotate(720deg);opacity:0;}}
}}

/* ── BOOK WRAPPER: horizontal strip ── */
#book{{
  position:fixed;inset:0;
  display:flex;flex-direction:row;
  width:100%;height:100svh;
  overflow:hidden;
  touch-action:pan-y;          /* vertical scroll still works inside cards */
}}

/* ── PAGE STRIP ── */
#strip{{
  display:flex;flex-direction:row;
  height:100%;
  /* width set by JS once we know page count */
  transition:transform 0.55s cubic-bezier(0.77,0,0.175,1);
  will-change:transform;
}}

/* ── INDIVIDUAL PAGES ── */
.page{{
  flex:0 0 100vw;
  width:100vw;
  height:100svh;
  position:relative;
  overflow-y:auto;         /* allow scroll within a tall page on small screens */
  overflow-x:hidden;
  -webkit-overflow-scrolling:touch;
  display:flex;flex-direction:column;
  align-items:center;
  justify-content:flex-start;
  padding:0 0 80px;        /* room for nav bar */
}}

/* page colour themes */
.page-cover  {{background:radial-gradient(ellipse at 50% 60%,#3d1a5c 0%,#1a0a2e 60%,#0d0518 100%);}}
.page-p1     {{background:linear-gradient(160deg,#fdf0f5,#f5dce8 50%,#e8c5d5);}}
.page-p2     {{background:linear-gradient(160deg,#f0f5ed,#d8ead5 50%,#b8d4b5);}}
.page-p3     {{background:linear-gradient(160deg,#fdf6ec,#f5e8c8 50%,#e8d4a0);}}
.page-p4     {{background:linear-gradient(160deg,#ede8f5,#d8ccef 50%,#c0b0e0);}}
.page-p5     {{background:linear-gradient(160deg,#f5edf0,#e8d0d8 50%,#d4b0c0);}}
.page-final  {{background:radial-gradient(ellipse at 50% 40%,#3d1a5c,#1a0a2e 70%);}}

/* ── COVER PAGE ── */
.cover-inner{{
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  min-height:100svh;width:100%;padding:60px 24px 100px;text-align:center;
  position:relative;gap:12px;
}}
.cover-border{{
  position:absolute;inset:14px;
  border:1.5px solid rgba(212,168,83,0.35);border-radius:4px;
  pointer-events:none;animation:borderGlow 3s ease-in-out infinite alternate;
}}
@keyframes borderGlow{{
  from{{border-color:rgba(212,168,83,0.2);}}
  to{{border-color:rgba(212,168,83,0.55);box-shadow:inset 0 0 60px rgba(212,168,83,0.06);}}
}}
.corner{{position:absolute;width:36px;height:36px;border-color:var(--gold);border-style:solid;opacity:0.5;}}
.corner.tl{{top:22px;left:22px;border-width:2px 0 0 2px;}}
.corner.tr{{top:22px;right:22px;border-width:2px 2px 0 0;}}
.corner.bl{{bottom:22px;left:22px;border-width:0 0 2px 2px;}}
.corner.br{{bottom:22px;right:22px;border-width:0 2px 2px 0;}}

.cover-photo-wrap{{
  width:clamp(130px,38vw,190px);height:clamp(130px,38vw,190px);
  border-radius:50%;border:3px solid var(--gold);
  box-shadow:0 0 0 6px rgba(212,168,83,0.15),0 0 40px rgba(232,96,122,0.35);
  overflow:hidden;flex-shrink:0;
  opacity:0;animation:fadeUp 1s ease 0.4s forwards;
}}
.cover-photo-wrap .photo-circle{{width:100%;height:100%;object-fit:cover;display:block;}}
.cover-subtitle{{
  font-family:'Dancing Script',cursive;
  font-size:clamp(0.85rem,3vw,1.15rem);
  color:var(--blush);letter-spacing:4px;text-transform:uppercase;
  opacity:0;animation:fadeUp 1s ease 0.7s forwards;
}}

/* ── NAME PERSONALISER ── */
.name-input-wrap{{
  display:flex;align-items:center;gap:10px;
  opacity:0;animation:fadeUp 1s ease 0.9s forwards;
  margin-top:4px;
}}
.name-input-wrap label{{
  font-family:'Dancing Script',cursive;
  font-size:clamp(0.85rem,3vw,1.1rem);
  color:var(--blush);letter-spacing:1px;
}}
#nameInput{{
  background:rgba(255,255,255,0.10);
  border:1px solid rgba(212,168,83,0.5);
  border-radius:30px;
  padding:6px 16px;
  font-family:'Dancing Script',cursive;
  font-size:clamp(0.95rem,3vw,1.15rem);
  color:var(--cream);
  width:clamp(100px,28vw,160px);
  text-align:center;
  outline:none;
  transition:border-color 0.3s,box-shadow 0.3s;
}}
#nameInput::placeholder{{color:rgba(242,181,195,0.45);}}
#nameInput:focus{{border-color:var(--gold);box-shadow:0 0 12px rgba(212,168,83,0.3);}}

.cover-title{{
  font-family:'Playfair Display',serif;
  font-size:clamp(2.2rem,11vw,5rem);
  font-style:italic;color:var(--cream);line-height:1.1;
  text-shadow:0 0 50px rgba(232,96,122,0.3);
  opacity:0;animation:fadeUp 1s ease 1.1s forwards;
}}
.cover-title span{{color:var(--rose);}}
.cover-divider{{
  width:90px;height:2px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
  opacity:0;animation:fadeUp 1s ease 1.3s forwards;
}}
.cover-tagline{{
  font-size:clamp(0.92rem,3vw,1.1rem);font-style:italic;
  color:var(--blush);max-width:300px;line-height:1.8;
  opacity:0;animation:fadeUp 1s ease 1.5s forwards;
}}

/* Turn-page hint on cover */
.turn-hint{{
  position:absolute;bottom:26px;right:26px;
  display:flex;align-items:center;gap:8px;
  color:rgba(242,181,195,0.6);
  font-family:'Dancing Script',cursive;
  font-size:clamp(0.78rem,2.5vw,0.95rem);
  letter-spacing:1px;
  opacity:0;animation:fadeUp 1s ease 2s forwards;
  pointer-events:none;
}}
.turn-arrow{{font-size:1.3rem;animation:nudgeRight 1.5s ease-in-out infinite;}}
@keyframes nudgeRight{{0%,100%{{transform:translateX(0);}}50%{{transform:translateX(5px);}}}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(18px);}}to{{opacity:1;transform:translateY(0);}}}}

/* ── INNER CONTENT WRAPPER ── */
.page-inner{{
  max-width:460px;width:100%;
  display:flex;flex-direction:column;align-items:center;
  gap:20px;text-align:center;position:relative;z-index:2;
  padding:52px 20px 20px;
  opacity:0;transform:translateY(28px);
  transition:opacity 0.7s ease,transform 0.7s ease;
}}
.page-inner.visible{{opacity:1;transform:translateY(0);}}

/* ── TYPOGRAPHY ── */
.page-number{{font-family:'Dancing Script',cursive;font-size:0.82rem;color:rgba(45,27,78,0.38);letter-spacing:3px;}}
.page-chapter{{font-family:'Dancing Script',cursive;font-size:clamp(1.05rem,4vw,1.45rem);color:var(--rose);letter-spacing:1px;}}
.page-heading{{font-family:'Playfair Display',serif;font-size:clamp(1.45rem,5.5vw,2.3rem);font-style:italic;color:var(--ink);line-height:1.2;}}
.page-heading em{{color:var(--rose);font-style:normal;}}
.ornament{{font-size:1.1rem;color:var(--gold);letter-spacing:8px;opacity:0.7;}}
.page-text{{font-size:clamp(0.96rem,3vw,1.12rem);line-height:1.9;color:#3a2040;font-weight:300;}}
.page-text strong{{font-weight:600;color:var(--rose);font-style:italic;}}
.mum-name{{color:var(--rose);font-style:italic;font-weight:600;}}

/* ── PHOTO ELEMENTS ── */
.photo-circle{{width:100%;height:100%;object-fit:cover;display:block;}}
.photo-rect{{width:100%;height:100%;object-fit:cover;display:block;}}
.photo-portrait{{width:100%;height:100%;object-fit:cover;display:block;}}

.photo-frame{{
  width:100%;max-width:320px;aspect-ratio:4/3;
  border-radius:12px;overflow:hidden;
  border:2px solid rgba(212,168,83,0.5);
  box-shadow:0 8px 30px rgba(0,0,0,0.14),0 0 0 5px rgba(255,255,255,0.35);
  flex-shrink:0;
}}
.photo-frame.portrait{{aspect-ratio:3/4;max-width:230px;}}
.photo-frame img{{width:100%;height:100%;object-fit:cover;display:block;}}
.photo-placeholder{{
  width:100%;height:100%;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;
  color:rgba(45,27,78,0.4);font-family:'Dancing Script',cursive;font-size:0.9rem;
}}
.ph-icon{{font-size:2.2rem;}}
.ph-label{{font-size:0.82rem;text-align:center;padding:0 8px;}}
.photo-caption{{font-family:'Dancing Script',cursive;font-size:0.9rem;color:rgba(45,27,78,0.45);font-style:italic;margin-top:-8px;}}

/* ── STORY CARD ── */
.story-card{{
  background:rgba(255,255,255,0.52);backdrop-filter:blur(10px);
  border:1px solid rgba(255,255,255,0.8);border-radius:14px;
  padding:22px;
  box-shadow:0 6px 28px rgba(0,0,0,0.07),inset 0 1px 0 rgba(255,255,255,0.9);
  width:100%;position:relative;
}}
.story-card::before{{
  content:'"';position:absolute;top:-8px;left:16px;
  font-family:'Playfair Display',serif;font-size:3.5rem;color:var(--rose);opacity:0.11;line-height:1;
}}

/* ── LOVE LETTER ── */
.love-letter{{
  background:var(--parchment);border:1px solid rgba(212,168,83,0.4);
  border-radius:4px;padding:26px 22px;
  font-style:italic;line-height:1.95;
  font-size:clamp(0.93rem,2.8vw,1.08rem);color:#3a2040;
  box-shadow:4px 4px 16px rgba(0,0,0,0.07);width:100%;
}}
.love-letter::after{{content:'❧';display:block;text-align:right;font-size:1.2rem;color:var(--rose);margin-top:12px;}}

/* ── ATTRIBUTES ── */
.attributes{{display:flex;flex-wrap:wrap;gap:9px;justify-content:center;list-style:none;}}
.attributes li{{
  background:rgba(255,255,255,0.68);border:1px solid rgba(212,168,83,0.3);
  border-radius:30px;padding:6px 14px;
  font-size:0.88rem;color:var(--ink);font-style:italic;
}}

/* ── FINAL PAGE ── */
.final-content .page-heading{{color:var(--cream);}}
.final-content .page-text{{color:rgba(242,181,195,0.82);}}
.big-heart{{font-size:clamp(4rem,16vw,7rem);animation:heartbeat 1.5s ease-in-out infinite;filter:drop-shadow(0 0 25px rgba(232,96,122,0.6));line-height:1;}}
@keyframes heartbeat{{0%,100%{{transform:scale(1);}}14%{{transform:scale(1.1);}}28%{{transform:scale(1);}}42%{{transform:scale(1.05);}}70%{{transform:scale(1);}}}}
.signature{{font-family:'Dancing Script',cursive;font-size:clamp(1.25rem,5vw,1.85rem);color:var(--gold);margin-top:4px;}}
.sparkle-row{{display:flex;gap:10px;justify-content:center;font-size:1.5rem;animation:sparkleRow 2s ease-in-out infinite;}}
@keyframes sparkleRow{{0%,100%{{opacity:0.7;transform:scale(1);}}50%{{opacity:1;transform:scale(1.05);}}}}

/* ── FLOATING PETALS ── */
.petal{{position:absolute;pointer-events:none;font-size:clamp(0.8rem,2vw,1.2rem);animation:petalDrift linear infinite;opacity:0;}}
@keyframes petalDrift{{
  0%{{transform:translate(0,-20px) rotate(0deg);opacity:0;}}
  10%{{opacity:0.18;}}
  100%{{transform:translate(var(--dx,30px),110svh) rotate(var(--dr,360deg));opacity:0;}}
}}

/* ── TAP-TO-ANIMATE SCENE OBJECTS ── */
.tap-obj{{cursor:pointer;transition:transform 0.2s;user-select:none;display:inline-block;}}
.tap-obj:active{{transform:scale(0.9);}}
.tap-obj.pop{{animation:popAnim 0.5s ease forwards;}}
@keyframes popAnim{{0%{{transform:scale(1);}}40%{{transform:scale(1.4) rotate(15deg);}}70%{{transform:scale(0.95) rotate(-5deg);}}100%{{transform:scale(1) rotate(0deg);}}}}
.tap-obj.bloom{{animation:bloomAnim 0.7s ease forwards;}}
@keyframes bloomAnim{{0%{{transform:scale(0.5) rotate(-20deg);opacity:0.5;}}60%{{transform:scale(1.3) rotate(5deg);opacity:1;}}100%{{transform:scale(1) rotate(0deg);opacity:1;}}}}
.tap-obj.fly{{animation:flyAnim 0.8s ease forwards;}}
@keyframes flyAnim{{0%{{transform:translateY(0) rotate(0deg);}}100%{{transform:translateY(-30px) rotate(20deg);opacity:0;}}}}
.tap-hint{{
  font-family:'Dancing Script',cursive;
  font-size:0.78rem;color:rgba(45,27,78,0.4);letter-spacing:1px;
  margin-top:-10px;
}}

/* ── SVG SCENE WRAPPER ── */
.scene-wrap{{
  width:100%;max-width:380px;
  border-radius:16px;overflow:hidden;
  box-shadow:0 8px 32px rgba(0,0,0,0.13);
  flex-shrink:0;
}}
.scene-wrap svg{{display:block;width:100%;height:auto;}}

/* ── NAV BAR ── */
#nav{{
  position:fixed;bottom:0;left:0;right:0;
  display:flex;align-items:center;justify-content:center;
  gap:16px;
  padding:12px 16px 16px;
  background:linear-gradient(to top,rgba(26,10,46,0.92),transparent);
  z-index:100;pointer-events:none;
}}
.nav-btn{{
  pointer-events:all;
  background:rgba(255,255,255,0.12);
  border:1px solid rgba(212,168,83,0.4);
  border-radius:50%;width:44px;height:44px;
  display:flex;align-items:center;justify-content:center;
  font-size:1.2rem;cursor:pointer;
  transition:background 0.2s,transform 0.15s,opacity 0.3s;
  color:var(--cream);
  -webkit-tap-highlight-color:transparent;
  user-select:none;
}}
.nav-btn:hover{{background:rgba(212,168,83,0.2);transform:scale(1.08);}}
.nav-btn:active{{transform:scale(0.93);}}
.nav-btn:disabled,.nav-btn[disabled]{{opacity:0.25;pointer-events:none;}}

.page-dots{{
  display:flex;gap:7px;align-items:center;
  pointer-events:all;
}}
.dot{{
  width:7px;height:7px;border-radius:50%;
  background:rgba(255,255,255,0.3);
  transition:background 0.3s,transform 0.3s;
  cursor:pointer;
}}
.dot.active{{background:var(--gold);transform:scale(1.35);}}

/* ── MOBILE TWEAKS ── */
@media(max-width:440px){{
  .love-letter{{padding:20px 16px;}}
  .story-card{{padding:18px 16px;}}
  .photo-frame{{max-width:100%;}}
  .photo-frame.portrait{{max-width:190px;}}
  .attributes li{{font-size:0.82rem;padding:5px 12px;}}
  .cover-inner{{padding:50px 18px 90px;gap:10px;}}
}}
</style>
</head>
<body>

<!-- AMBIENT PARTICLES -->
<div id="particles"></div>

<!-- ═══════════════════════════════════════
     BOOK CONTAINER (horizontal strip)
════════════════════════════════════════ -->
<div id="book">
<div id="strip">

<!-- ═══════════ PAGE 0: COVER ═══════════ -->
<section class="page page-cover">
  <div class="cover-inner">
    <div class="cover-border"></div>
    <div class="corner tl"></div><div class="corner tr"></div>
    <div class="corner bl"></div><div class="corner br"></div>

    <div class="cover-photo-wrap">
      {photo_slot(PHOTO_1, "cover-img", shape="circle", dark=True)}
    </div>

    <div class="cover-subtitle">A storybook for</div>

    <!-- NAME PERSONALISER -->
    <div class="name-input-wrap">
      <label for="nameInput">✦</label>
      <input id="nameInput" type="text" maxlength="24"
             placeholder="Type her name…" autocomplete="off"
             oninput="updateName(this.value)" />
      <label for="nameInput">✦</label>
    </div>

    <h1 class="cover-title">Happy<br/><span>Mother's</span> Day</h1>
    <div class="cover-divider"></div>
    <p class="cover-tagline">A small book of love for <span class="mum-name" id="tagline-name">the woman who gave us everything</span>.</p>

    <div class="turn-hint">
      <span>Turn the page</span>
      <span class="turn-arrow">›</span>
    </div>
  </div>
</section>

<!-- ═══════════ PAGE 1: In the Beginning ═══════════ -->
<section class="page page-p1">
  <span class="petal" style="left:5%;--dx:20px;--dr:200deg;animation-duration:9s;animation-delay:0s;">🌸</span>
  <span class="petal" style="left:82%;--dx:-30px;--dr:300deg;animation-duration:11s;animation-delay:2s;">🌺</span>

  <div class="page-inner" data-page="1">
    <span class="page-number">~ Page One ~</span>
    <p class="page-chapter">Chapter One</p>
    <h2 class="page-heading">In the Beginning,<br/>there was <em>You</em></h2>
    <div class="ornament">❧ ✦ ❧</div>

    <!-- ILLUSTRATED SVG SCENE 1: Sunrise nursery -->
    <div class="scene-wrap">
      <svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg">
        <!-- sky gradient -->
        <defs>
          <linearGradient id="sky1" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#fde8f0"/>
            <stop offset="100%" stop-color="#fcc8da"/>
          </linearGradient>
          <radialGradient id="sunGlow" cx="50%" cy="40%" r="30%">
            <stop offset="0%" stop-color="#ffd580" stop-opacity="0.7"/>
            <stop offset="100%" stop-color="#fcc8da" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="380" height="200" fill="url(#sky1)"/>
        <ellipse cx="190" cy="80" rx="80" ry="80" fill="url(#sunGlow)"/>
        <!-- hills -->
        <ellipse cx="60" cy="210" rx="120" ry="70" fill="#f2b5c3" opacity="0.5"/>
        <ellipse cx="310" cy="215" rx="130" ry="75" fill="#e8a0b5" opacity="0.4"/>
        <ellipse cx="190" cy="220" rx="200" ry="80" fill="#d4869e" opacity="0.3"/>
        <!-- ground -->
        <rect x="0" y="165" width="380" height="35" fill="#c97090" opacity="0.25" rx="4"/>
        <!-- house -->
        <rect x="148" y="120" width="84" height="55" fill="#fdf0f5" rx="4"/>
        <polygon points="136,122 190,82 244,122" fill="#e8607a" opacity="0.85"/>
        <rect x="172" y="143" width="16" height="32" fill="#d4869e" rx="2"/><!-- door -->
        <rect x="154" y="126" width="14" height="14" fill="#c9b8e8" opacity="0.7" rx="2"/><!-- window l -->
        <rect x="212" y="126" width="14" height="14" fill="#c9b8e8" opacity="0.7" rx="2"/><!-- window r -->
        <!-- chimney -->
        <rect x="205" y="90" width="10" height="22" fill="#d4869e"/>
        <!-- smoke puffs (tap-to-animate) -->
        <circle class="tap-obj pop" onclick="tapAnim(this,'pop')" cx="210" cy="84" r="6" fill="rgba(255,255,255,0.65)" title="Tap me!"/>
        <circle class="tap-obj pop" onclick="tapAnim(this,'pop')" cx="216" cy="76" r="4.5" fill="rgba(255,255,255,0.5)"/>
        <!-- sun -->
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="60" cy="38" r="22" fill="#ffd580" opacity="0.9"/>
        <line x1="60" y1="10" x2="60" y2="3" stroke="#ffd580" stroke-width="2"/>
        <line x1="60" y1="66" x2="60" y2="73" stroke="#ffd580" stroke-width="2"/>
        <line x1="32" y1="38" x2="25" y2="38" stroke="#ffd580" stroke-width="2"/>
        <line x1="88" y1="38" x2="95" y2="38" stroke="#ffd580" stroke-width="2"/>
        <line x1="41" y1="19" x2="36" y2="14" stroke="#ffd580" stroke-width="2"/>
        <line x1="79" y1="57" x2="84" y2="62" stroke="#ffd580" stroke-width="2"/>
        <line x1="79" y1="19" x2="84" y2="14" stroke="#ffd580" stroke-width="2"/>
        <line x1="41" y1="57" x2="36" y2="62" stroke="#ffd580" stroke-width="2"/>
        <!-- bird (tap to fly) -->
        <path class="tap-obj fly" onclick="tapAnim(this,'fly')"
              d="M310,55 Q318,48 326,55 Q332,48 340,55" stroke="#c97090" stroke-width="2" fill="none"/>
        <path class="tap-obj fly" onclick="tapAnim(this,'fly')"
              d="M290,62 Q296,56 302,62 Q307,56 313,62" stroke="#c97090" stroke-width="2" fill="none"/>
        <!-- flowers -->
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="128" cy="170" r="8" fill="#e8607a" opacity="0.85"/>
        <rect x="126.5" y="170" width="3" height="12" fill="#7ca982"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="255" cy="168" r="7" fill="#f2b5c3"/>
        <rect x="253.5" y="168" width="3" height="11" fill="#7ca982"/>
      </svg>
    </div>
    <p class="tap-hint">✦ Tap the sun, smoke, birds &amp; flowers ✦</p>

    <div class="story-card">
      <p class="page-text">
        Before there were words, before there were memories —
        there was the warmth of your arms.<br/><br/>
        You were the first voice that felt like home,
        the first laugh that felt like sunlight,
        and the first pair of hands we ever reached for.
      </p>
    </div>
  </div>
</section>

<!-- ═══════════ PAGE 2: Magic You Made Ordinary ═══════════ -->
<section class="page page-p2">
  <span class="petal" style="left:10%;--dx:50px;--dr:400deg;animation-duration:10s;animation-delay:1s;">🍃</span>
  <span class="petal" style="left:72%;--dx:-20px;--dr:260deg;animation-duration:12s;animation-delay:3s;">🌿</span>

  <div class="page-inner" data-page="2">
    <span class="page-number">~ Page Two ~</span>
    <p class="page-chapter">Chapter Two</p>
    <h2 class="page-heading">The Magic You<br/>Made Ordinary</h2>
    <div class="ornament">❧ ✦ ❧</div>

    <!-- SVG SCENE 2: Kitchen garden morning -->
    <div class="scene-wrap">
      <svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="sky2" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#e8f5e0"/>
            <stop offset="100%" stop-color="#c8e8c0"/>
          </linearGradient>
        </defs>
        <rect width="380" height="200" fill="url(#sky2)"/>
        <!-- ground strip -->
        <rect x="0" y="155" width="380" height="45" fill="#a8cc90" rx="0"/>
        <!-- fence -->
        <rect x="20" y="110" width="3" height="48" fill="#d4a853" opacity="0.6" rx="1"/>
        <rect x="36" y="110" width="3" height="48" fill="#d4a853" opacity="0.6" rx="1"/>
        <rect x="52" y="110" width="3" height="48" fill="#d4a853" opacity="0.6" rx="1"/>
        <rect x="68" y="110" width="3" height="48" fill="#d4a853" opacity="0.6" rx="1"/>
        <rect x="84" y="110" width="3" height="48" fill="#d4a853" opacity="0.6" rx="1"/>
        <rect x="18" y="118" width="72" height="4" fill="#d4a853" opacity="0.5" rx="1"/>
        <rect x="18" y="138" width="72" height="4" fill="#d4a853" opacity="0.5" rx="1"/>
        <!-- big tree -->
        <rect x="290" y="95" width="12" height="70" fill="#8B6914" opacity="0.7" rx="2"/>
        <circle class="tap-obj pop" onclick="tapAnim(this,'pop')" cx="296" cy="78" r="38" fill="#7ca982" opacity="0.85"/>
        <circle cx="280" cy="90" r="22" fill="#6ab870" opacity="0.6"/>
        <circle cx="312" cy="88" r="20" fill="#5ea665" opacity="0.5"/>
        <!-- flower bed (tap to bloom) -->
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="118" cy="154" r="9" fill="#e8607a"/>
        <rect x="116" y="154" width="4" height="14" fill="#7ca982"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="140" cy="152" r="8" fill="#f2b5c3"/>
        <rect x="138" y="152" width="4" height="13" fill="#7ca982"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="162" cy="155" r="9" fill="#ffd580"/>
        <rect x="160" y="155" width="4" height="12" fill="#7ca982"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="184" cy="153" r="8" fill="#c9b8e8"/>
        <rect x="182" y="153" width="4" height="13" fill="#7ca982"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="206" cy="154" r="9" fill="#e8607a"/>
        <rect x="204" y="154" width="4" height="14" fill="#7ca982"/>
        <!-- tea cup (tap to pop) -->
        <ellipse class="tap-obj pop" onclick="tapAnim(this,'pop')" cx="240" cy="148" rx="22" ry="14" fill="#fdf6ec" stroke="#d4a853" stroke-width="1.5"/>
        <rect x="218" y="134" width="44" height="14" fill="#fdf6ec" stroke="#d4a853" stroke-width="1.5" rx="4"/>
        <path d="M262,139 Q270,141 268,148 Q265,154 260,151" stroke="#d4a853" stroke-width="1.5" fill="none"/>
        <text x="230" y="144" font-size="9" fill="#c97090" font-style="italic">tea ☕</text>
        <!-- birds -->
        <path class="tap-obj fly" onclick="tapAnim(this,'fly')"
              d="M50,55 Q57,47 64,55 Q70,47 77,55" stroke="#7ca982" stroke-width="2" fill="none"/>
        <path class="tap-obj fly" onclick="tapAnim(this,'fly')"
              d="M30,65 Q36,58 42,65 Q47,58 53,65" stroke="#7ca982" stroke-width="2" fill="none"/>
      </svg>
    </div>
    <p class="tap-hint">✦ Tap the flowers, tea & tree ✦</p>

    <div class="photo-frame">
      {photo_slot(PHOTO_2, "photo2", shape="rect")}
    </div>
    <p class="photo-caption">A favourite memory ✦</p>

    <p class="page-text">
      You turned simple mornings into rituals,
      ordinary dinners into celebrations,
      and hard days into stories that made us stronger.<br/><br/>
      There is a kind of magic only mothers know —
      the kind that hides in <strong>band-aids and bedtime stories</strong>.
    </p>
    <ul class="attributes">
      <li>🤍 Always patient</li><li>🌸 Endlessly warm</li>
      <li>⭐ Quietly brave</li><li>🌿 Rooted and strong</li>
      <li>✨ Fiercely loving</li><li>☀️ Steadily there</li>
    </ul>
  </div>
</section>

<!-- ═══════════ PAGE 3: Lessons ═══════════ -->
<section class="page page-p3">
  <span class="petal" style="left:20%;--dx:30px;--dr:320deg;animation-duration:14s;animation-delay:0s;">🌼</span>
  <span class="petal" style="left:65%;--dx:-40px;--dr:240deg;animation-duration:11s;animation-delay:4s;">✿</span>

  <div class="page-inner" data-page="3">
    <span class="page-number">~ Page Three ~</span>
    <p class="page-chapter">Chapter Three</p>
    <h2 class="page-heading">Everything We Know,<br/>We Learned from <em><span class="mum-name" id="heading-name-3">You</span></em></h2>
    <div class="ornament">❧ ✦ ❧</div>

    <!-- SVG SCENE 3: Autumn reading nook -->
    <div class="scene-wrap">
      <svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="sky3" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#fdf6ec"/>
            <stop offset="100%" stop-color="#f5e8c8"/>
          </linearGradient>
        </defs>
        <rect width="380" height="200" fill="url(#sky3)"/>
        <!-- window frame -->
        <rect x="30" y="20" width="110" height="140" fill="#c9b8e8" opacity="0.3" rx="6" stroke="#d4a853" stroke-width="1.5"/>
        <rect x="83" y="20" width="2" height="140" fill="#d4a853" opacity="0.5"/>
        <rect x="30" y="86" width="110" height="2" fill="#d4a853" opacity="0.5"/>
        <!-- autumn tree outside window -->
        <rect x="74" y="58" width="7" height="80" fill="#8B6914" opacity="0.5" rx="2"/>
        <circle class="tap-obj pop" onclick="tapAnim(this,'pop')" cx="78" cy="44" r="30" fill="#e8a030" opacity="0.55"/>
        <circle cx="60" cy="56" r="18" fill="#d4853a" opacity="0.4"/>
        <circle cx="96" cy="54" r="16" fill="#c97020" opacity="0.4"/>
        <!-- falling leaves (tap) -->
        <text class="tap-obj fly" onclick="tapAnim(this,'fly')" x="44" y="100" font-size="14" opacity="0.7">🍂</text>
        <text class="tap-obj fly" onclick="tapAnim(this,'fly')" x="96" y="110" font-size="12" opacity="0.6">🍁</text>
        <text class="tap-obj fly" onclick="tapAnim(this,'fly')" x="55" y="125" font-size="11" opacity="0.5">🍂</text>
        <!-- armchair -->
        <rect x="185" y="115" width="110" height="55" fill="#c9b8e8" rx="8"/><!-- seat -->
        <rect x="175" y="95" width="20" height="75" fill="#b8a8d8" rx="6"/><!-- left arm -->
        <rect x="285" y="95" width="20" height="75" fill="#b8a8d8" rx="6"/><!-- right arm -->
        <rect x="185" y="80" width="110" height="38" fill="#b8a8d8" rx="8"/><!-- back -->
        <!-- person silhouette in chair -->
        <circle cx="238" cy="88" r="13" fill="#7ca982" opacity="0.7"/><!-- head -->
        <ellipse cx="238" cy="108" rx="22" ry="16" fill="#7ca982" opacity="0.6"/><!-- body -->
        <!-- book -->
        <rect class="tap-obj pop" onclick="tapAnim(this,'pop')" x="220" y="117" width="38" height="28" fill="#e8607a" rx="3" opacity="0.85"/>
        <line x1="239" y1="117" x2="239" y2="145" stroke="#fdf0f5" stroke-width="1.5"/>
        <!-- floor lamp -->
        <rect x="330" y="88" width="4" height="82" fill="#d4a853" opacity="0.6" rx="2"/>
        <ellipse cx="332" cy="88" rx="18" ry="8" fill="#ffd580" opacity="0.5"/>
        <ellipse class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="332" cy="80" rx="14" ry="18" fill="#ffd580" opacity="0.4"/>
        <!-- rug -->
        <ellipse cx="248" cy="172" rx="75" ry="18" fill="#d4a853" opacity="0.25"/>
        <ellipse cx="248" cy="172" rx="55" ry="12" fill="#e8607a" opacity="0.1"/>
      </svg>
    </div>
    <p class="tap-hint">✦ Tap the leaves, book & lamp ✦</p>

    <div class="photo-frame portrait">
      {photo_slot(PHOTO_3, "photo3", shape="portrait")}
    </div>
    <p class="photo-caption">Together ✦</p>

    <div class="love-letter">
      You taught us how to be kind — not just politely, but deeply.<br/>
      You showed us that <strong>strength isn't loud</strong>; sometimes it's quiet persistence.<br/>
      You modelled grace under pressure, laughter through tears,<br/>
      and the art of making people feel seen.<br/><br/>
      Every good thing we carry — a piece of it came from <span class="mum-name" id="letter-name-3">you</span>.
    </div>
  </div>
</section>

<!-- ═══════════ PAGE 4: Small Things ═══════════ -->
<section class="page page-p4">
  <span class="petal" style="left:15%;--dx:60px;--dr:280deg;animation-duration:9s;animation-delay:2s;">💜</span>
  <span class="petal" style="left:75%;--dx:-50px;--dr:350deg;animation-duration:13s;animation-delay:0s;">🌙</span>

  <div class="page-inner" data-page="4">
    <span class="page-number">~ Page Four ~</span>
    <p class="page-chapter">Chapter Four</p>
    <h2 class="page-heading">The Small Things Were<br/>Never <em>Small</em></h2>
    <div class="ornament">❧ ✦ ❧</div>

    <!-- SVG SCENE 4: Night sky & warm window -->
    <div class="scene-wrap">
      <svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="sky4" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#1a0a3e"/>
            <stop offset="100%" stop-color="#3d1a5c"/>
          </linearGradient>
          <radialGradient id="windowGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#ffd580" stop-opacity="0.7"/>
            <stop offset="100%" stop-color="#ffd580" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="380" height="200" fill="url(#sky4)"/>
        <!-- stars (tap to sparkle) -->
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="30" cy="25" r="2.5" fill="#ffd580"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="80" cy="15" r="2" fill="white" opacity="0.8"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="140" cy="30" r="2.5" fill="#c9b8e8"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="200" cy="12" r="2" fill="white"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="260" cy="28" r="2.5" fill="#ffd580"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="320" cy="18" r="2" fill="white" opacity="0.7"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="355" cy="40" r="2.5" fill="#c9b8e8"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="50" cy="55" r="1.5" fill="white" opacity="0.6"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="110" cy="48" r="1.5" fill="#ffd580"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="360" cy="70" r="1.5" fill="white"/>
        <!-- moon (tap to bloom) -->
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="320" cy="48" r="24" fill="#ffd580" opacity="0.9"/>
        <circle cx="332" cy="40" r="18" fill="#3d1a5c"/>
        <!-- house silhouette -->
        <rect x="80" y="100" width="220" height="100" fill="#1a0830" rx="2"/>
        <polygon points="68,102 190,42 312,102" fill="#150622"/>
        <!-- warm glowing window -->
        <rect x="150" y="110" width="80" height="60" fill="#ffd580" opacity="0.85" rx="4"/>
        <ellipse cx="190" cy="140" rx="50" ry="40" fill="url(#windowGlow)"/>
        <!-- window cross -->
        <line x1="190" y1="110" x2="190" y2="170" stroke="#c97020" stroke-width="1.5" opacity="0.5"/>
        <line x1="150" y1="140" x2="230" y2="140" stroke="#c97020" stroke-width="1.5" opacity="0.5"/>
        <!-- chimney with smoke -->
        <rect x="235" y="58" width="14" height="36" fill="#150622"/>
        <circle class="tap-obj pop" onclick="tapAnim(this,'pop')" cx="242" cy="52" r="7" fill="rgba(255,255,255,0.25)"/>
        <circle class="tap-obj pop" onclick="tapAnim(this,'pop')" cx="246" cy="42" r="5" fill="rgba(255,255,255,0.18)"/>
        <!-- door -->
        <rect x="170" y="145" width="40" height="55" fill="#0f0420" rx="3"/>
        <circle cx="206" cy="172" r="3" fill="#ffd580" opacity="0.6"/>
        <!-- path -->
        <ellipse cx="190" cy="195" rx="28" ry="8" fill="#c9b8e8" opacity="0.15"/>
        <!-- foreground flowers -->
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="60" cy="172" r="7" fill="#e8607a" opacity="0.7"/>
        <rect x="58" y="172" width="4" height="10" fill="#5ea665" opacity="0.6"/>
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="330" cy="170" r="6" fill="#c9b8e8" opacity="0.7"/>
        <rect x="328" y="170" width="4" height="10" fill="#5ea665" opacity="0.6"/>
      </svg>
    </div>
    <p class="tap-hint">✦ Tap stars, moon & flowers ✦</p>

    <div class="photo-frame">
      {photo_slot(PHOTO_4, "photo4", shape="rect")}
    </div>
    <p class="photo-caption">An everyday moment ✦</p>

    <div class="story-card">
      <p class="page-text">
        The extra blanket. The cup of tea that appeared without asking.
        The text that just said <strong>"thinking of you."</strong><br/><br/>
        The way you remembered our favourite things —
        and showed up, again and again, without keeping score.
      </p>
    </div>
    <p class="page-text" style="font-style:italic;opacity:0.72;">We notice. We always noticed.</p>
  </div>
</section>

<!-- ═══════════ PAGE 5: Letter ═══════════ -->
<section class="page page-p5">
  <span class="petal" style="left:8%;--dx:40px;--dr:420deg;animation-duration:12s;animation-delay:1s;">🌹</span>
  <span class="petal" style="left:78%;--dx:-35px;--dr:300deg;animation-duration:10s;animation-delay:3s;">🌸</span>

  <div class="page-inner" data-page="5">
    <span class="page-number">~ Page Five ~</span>
    <p class="page-chapter">Chapter Five</p>
    <h2 class="page-heading">A Letter We've Been<br/>Meaning to <em>Write</em></h2>
    <div class="ornament">❧ ✦ ❧</div>

    <!-- SVG SCENE 5: Writing desk with roses -->
    <div class="scene-wrap">
      <svg viewBox="0 0 380 200" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="sky5" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#fdf0f5"/>
            <stop offset="100%" stop-color="#f0e8f5"/>
          </linearGradient>
        </defs>
        <rect width="380" height="200" fill="url(#sky5)"/>
        <!-- desk surface -->
        <rect x="30" y="120" width="320" height="14" fill="#d4a853" opacity="0.7" rx="3"/>
        <rect x="40" y="133" width="8" height="55" fill="#c09030" opacity="0.5" rx="2"/>
        <rect x="332" y="133" width="8" height="55" fill="#c09030" opacity="0.5" rx="2"/>
        <!-- letter / paper -->
        <rect x="110" y="75" width="160" height="48" fill="#fdf6ec" stroke="#d4a853" stroke-width="1" rx="3"/>
        <line x1="122" y1="86" x2="258" y2="86" stroke="#c9b8e8" stroke-width="1" opacity="0.6"/>
        <line x1="122" y1="95" x2="258" y2="95" stroke="#c9b8e8" stroke-width="1" opacity="0.6"/>
        <line x1="122" y1="104" x2="220" y2="104" stroke="#c9b8e8" stroke-width="1" opacity="0.6"/>
        <text x="122" y="84" font-size="7" fill="#e8607a" font-style="italic" font-family="serif">Dear </text>
        <text id="svg-name-5" x="146" y="84" font-size="7" fill="#e8607a" font-style="italic" font-family="serif">Mum,</text>
        <!-- quill pen -->
        <line x1="240" y1="68" x2="258" y2="120" stroke="#8B6914" stroke-width="2"/>
        <path d="M240,68 Q228,48 250,40 Q262,55 258,120" fill="#ffd580" opacity="0.7"/>
        <!-- ink pot -->
        <ellipse cx="275" cy="118" rx="14" ry="7" fill="#2d1b4e" opacity="0.8"/>
        <rect x="261" y="108" width="28" height="10" fill="#2d1b4e" opacity="0.8" rx="3"/>
        <!-- roses (tap to bloom) -->
        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="68" cy="108" r="16" fill="#e8607a" opacity="0.85"/>
        <circle cx="58" cy="116" r="10" fill="#d4506a" opacity="0.7"/>
        <circle cx="78" cy="116" r="9" fill="#d4506a" opacity="0.6"/>
        <rect x="66" y="120" width="4" height="20" fill="#7ca982"/>
        <!-- leaves -->
        <ellipse cx="58" cy="136" rx="12" ry="5" fill="#5ea665" opacity="0.7" transform="rotate(-25,58,136)"/>
        <ellipse cx="80" cy="134" rx="10" ry="5" fill="#5ea665" opacity="0.6" transform="rotate(20,80,134)"/>

        <circle class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="314" cy="110" r="14" fill="#f2b5c3" opacity="0.85"/>
        <circle cx="305" cy="117" r="9" fill="#e8a0b5" opacity="0.7"/>
        <circle cx="323" cy="117" r="8" fill="#e8a0b5" opacity="0.6"/>
        <rect x="312" y="120" width="4" height="18" fill="#7ca982"/>
        <ellipse cx="304" cy="133" rx="10" ry="4.5" fill="#5ea665" opacity="0.6" transform="rotate(-20,304,133)"/>
        <ellipse cx="323" cy="132" rx="9" ry="4" fill="#5ea665" opacity="0.5" transform="rotate(18,323,132)"/>

        <!-- heart wax seal (tap to pop) -->
        <circle class="tap-obj pop" onclick="tapAnim(this,'pop')" cx="190" cy="123" r="10" fill="#e8607a" opacity="0.9"/>
        <text x="185" y="127" font-size="9" fill="white">♡</text>

        <!-- candle -->
        <rect x="345" y="96" width="8" height="26" fill="#fdf6ec" stroke="#d4a853" stroke-width="0.5" rx="2"/>
        <ellipse class="tap-obj bloom" onclick="tapAnim(this,'bloom')" cx="349" cy="94" rx="5" ry="8" fill="#ffd580" opacity="0.8"/>
        <ellipse cx="349" cy="92" rx="3" ry="5" fill="#ff9020" opacity="0.7"/>
      </svg>
    </div>
    <p class="tap-hint">✦ Tap the roses, seal & candle ✦</p>

    <div class="love-letter" id="love-letter-5">
      Dear <span class="mum-name" id="letter-name-5">Mum</span>,<br/><br/>
      Thank you for the mornings you gave up sleep for us.<br/>
      Thank you for the worries you carried alone so we wouldn't have to.<br/>
      Thank you for believing in us when we barely believed in ourselves.<br/><br/>
      Thank you for being <strong>exactly you</strong> —
      flawed and wonderful and irreplaceable.<br/><br/>
      We love you more than these pages can hold.
    </div>
  </div>
</section>

<!-- ═══════════ FINAL PAGE ═══════════ -->
<section class="page page-final">
  <div class="page-inner final-content" data-page="6">
    <div class="photo-frame" style="border-color:rgba(212,168,83,0.6);box-shadow:0 0 0 6px rgba(212,168,83,0.1),0 8px 40px rgba(232,96,122,0.3);">
      {photo_slot(PHOTO_5, "photo5", shape="rect", dark=True)}
    </div>
    <span class="big-heart">💗</span>
    <h2 class="page-heading">Happy Mother's Day,<br/><span class="mum-name" id="final-name">Mum</span></h2>
    <div class="ornament" style="color:var(--gold);">✦ ✦ ✦</div>
    <p class="page-text">Today and every day — <span class="mum-name" id="final-name-2">you</span> are celebrated, cherished, and adored.</p>
    <div class="sparkle-row">🌸 🌺 🌼 🌷 🌻</div>
    <p class="signature">With all our love ♡</p>
  </div>
</section>

</div><!-- end #strip -->
</div><!-- end #book -->

<!-- ═══════════ NAV BAR ═══════════ -->
<div id="nav">
  <button class="nav-btn" id="prevBtn" onclick="navigate(-1)" aria-label="Previous page">‹</button>
  <div class="page-dots" id="dots"></div>
  <button class="nav-btn" id="nextBtn" onclick="navigate(1)" aria-label="Next page">›</button>
</div>

<script>
/* ─────────────────────────────────────────────
   HORIZONTAL BOOK ENGINE
───────────────────────────────────────────── */
(function() {{
  const TOTAL = 7; // cover + 5 chapters + final
  let cur = 0;
  let startX = 0, startY = 0, isDragging = false;

  const strip   = document.getElementById('strip');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const dotsEl  = document.getElementById('dots');

  // Build dots
  for (let i = 0; i < TOTAL; i++) {{
    const d = document.createElement('div');
    d.className = 'dot' + (i === 0 ? ' active' : '');
    d.setAttribute('aria-label', 'Go to page ' + (i + 1));
    d.onclick = () => goTo(i);
    dotsEl.appendChild(d);
  }}

  function goTo(n) {{
    cur = Math.max(0, Math.min(TOTAL - 1, n));
    strip.style.transform = `translateX(${{-cur * 100}}vw)`;
    prevBtn.disabled = cur === 0;
    nextBtn.disabled = cur === TOTAL - 1;
    document.querySelectorAll('.dot').forEach((d, i) => {{
      d.classList.toggle('active', i === cur);
    }});
    // trigger entrance animation for page-inner
    const inner = strip.children[cur]
                        .querySelector('.page-inner,[class*="page-inner"]');
    if (inner) {{
      inner.classList.remove('visible');
      requestAnimationFrame(() => requestAnimationFrame(() => inner.classList.add('visible')));
    }}
  }}

  window.navigate = function(dir) {{ goTo(cur + dir); }};

  // Swipe support
  strip.parentElement.addEventListener('touchstart', e => {{
    startX = e.touches[0].clientX;
    startY = e.touches[0].clientY;
    isDragging = true;
  }}, {{passive: true}});

  strip.parentElement.addEventListener('touchend', e => {{
    if (!isDragging) return;
    isDragging = false;
    const dx = e.changedTouches[0].clientX - startX;
    const dy = e.changedTouches[0].clientY - startY;
    if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {{
      navigate(dx < 0 ? 1 : -1);
    }}
  }}, {{passive: true}});

  // Keyboard
  document.addEventListener('keydown', e => {{
    if (e.key === 'ArrowRight') navigate(1);
    if (e.key === 'ArrowLeft')  navigate(-1);
  }});

  // Init
  goTo(0);
}})();

/* ─────────────────────────────────────────────
   NAME PERSONALISER
───────────────────────────────────────────── */
function updateName(val) {{
  const name = val.trim() || null;
  const targets = document.querySelectorAll('.mum-name');
  targets.forEach(el => {{
    const id = el.id;
    if (id === 'final-name-2') {{
      el.textContent = name ? name : 'you';
    }} else if (id === 'heading-name-3') {{
      el.textContent = name ? name : 'You';
    }} else if (id === 'letter-name-3' || id === 'letter-name-5') {{
      el.textContent = name ? name : 'you';
    }} else {{
      el.textContent = name ? name : 'Mum';
    }}
  }});
  // Update tagline
  const tl = document.getElementById('tagline-name');
  if (tl) tl.textContent = name ? name : 'the woman who gave us everything';
  // Update SVG name
  const svgName = document.getElementById('svg-name-5');
  if (svgName) svgName.textContent = (name ? name : 'Mum') + ',';
}}

/* ─────────────────────────────────────────────
   TAP-TO-ANIMATE
───────────────────────────────────────────── */
window.tapAnim = function(el, type) {{
  el.classList.remove('pop','bloom','fly');
  // force reflow
  void el.offsetWidth;
  el.classList.add(type);
  el.addEventListener('animationend', () => {{
    el.classList.remove(type);
  }}, {{once: true}});
}};

/* ─────────────────────────────────────────────
   AMBIENT PARTICLES
───────────────────────────────────────────── */
(function() {{
  const c = document.getElementById('particles');
  const shapes = ['✦','·','∘','⋆','◦','✿'];
  const cols = [
    'rgba(232,96,122,0.5)','rgba(212,168,83,0.45)',
    'rgba(201,184,232,0.55)','rgba(242,181,195,0.6)'
  ];
  for (let i = 0; i < 28; i++) {{
    const el = document.createElement('span');
    el.className = 'particle';
    el.textContent = shapes[Math.floor(Math.random() * shapes.length)];
    el.style.cssText =
      `left:${{Math.random()*100}}%;` +
      `font-size:${{Math.random()*5+3}}px;` +
      `color:${{cols[Math.floor(Math.random()*cols.length)]}};` +
      `animation-duration:${{Math.random()*18+10}}s;` +
      `animation-delay:${{Math.random()*20}}s;`;
    c.appendChild(el);
  }}
}})();
</script>
</body>
</html>"""

components.html(STORYBOOK_HTML, height=900, scrolling=False)
