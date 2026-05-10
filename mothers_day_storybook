import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Mother's Day 🌸",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default chrome
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .stApp { background: #1a0a2e; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

STORYBOOK_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Happy Mother's Day</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,600&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet"/>
<style>
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --rose:      #e8607a;
  --blush:     #f2b5c3;
  --gold:      #d4a853;
  --cream:     #fdf6ec;
  --sage:      #7ca982;
  --lavender:  #c9b8e8;
  --midnight:  #1a0a2e;
  --parchment: #f5ead6;
  --ink:       #2d1b4e;
}

html { scroll-behavior: smooth; }

body {
  font-family: 'Cormorant Garamond', serif;
  background: var(--midnight);
  color: var(--ink);
  overflow-x: hidden;
}

/* ── PARTICLES ── */
#particles {
  position: fixed; inset: 0; pointer-events: none; z-index: 0;
  overflow: hidden;
}
.particle {
  position: absolute;
  border-radius: 50%;
  animation: floatUp linear infinite;
  opacity: 0;
}
@keyframes floatUp {
  0%   { transform: translateY(100vh) rotate(0deg);   opacity: 0; }
  10%  { opacity: 0.7; }
  90%  { opacity: 0.4; }
  100% { transform: translateY(-10vh) rotate(720deg); opacity: 0; }
}

/* ── COVER PAGE ── */
#cover {
  min-height: 100vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  position: relative;
  background: radial-gradient(ellipse at 50% 60%,
    #3d1a5c 0%, #1a0a2e 60%, #0d0518 100%);
  overflow: hidden;
  padding: 40px 20px;
}

.cover-decoration {
  position: absolute; inset: 0; pointer-events: none;
}

.cover-border {
  position: absolute; inset: 20px;
  border: 2px solid rgba(212,168,83,0.3);
  border-radius: 4px;
  animation: borderGlow 3s ease-in-out infinite alternate;
}
.cover-border::before {
  content: '';
  position: absolute; inset: 6px;
  border: 1px solid rgba(212,168,83,0.15);
  border-radius: 2px;
}

@keyframes borderGlow {
  from { border-color: rgba(212,168,83,0.2); box-shadow: inset 0 0 40px rgba(212,168,83,0.03); }
  to   { border-color: rgba(212,168,83,0.5); box-shadow: inset 0 0 80px rgba(212,168,83,0.08); }
}

.corner-ornament {
  position: absolute; width: 60px; height: 60px;
  border-color: var(--gold); border-style: solid; opacity: 0.5;
}
.corner-ornament.tl { top: 28px; left: 28px; border-width: 2px 0 0 2px; }
.corner-ornament.tr { top: 28px; right: 28px; border-width: 2px 2px 0 0; }
.corner-ornament.bl { bottom: 28px; left: 28px; border-width: 0 0 2px 2px; }
.corner-ornament.br { bottom: 28px; right: 28px; border-width: 0 2px 2px 0; }

.cover-floral {
  font-size: 5rem; margin-bottom: 10px;
  animation: sway 4s ease-in-out infinite;
  filter: drop-shadow(0 0 20px rgba(232,96,122,0.5));
}
@keyframes sway {
  0%,100% { transform: rotate(-5deg) scale(1); }
  50%      { transform: rotate(5deg) scale(1.05); }
}

.cover-subtitle {
  font-family: 'Dancing Script', cursive;
  font-size: clamp(1rem, 3vw, 1.4rem);
  color: var(--blush);
  letter-spacing: 4px;
  text-transform: uppercase;
  margin-bottom: 20px;
  opacity: 0;
  animation: fadeSlideUp 1s ease 0.3s forwards;
}

.cover-title {
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.8rem, 8vw, 6rem);
  font-style: italic;
  color: var(--cream);
  text-align: center;
  line-height: 1.1;
  text-shadow: 0 0 60px rgba(232,96,122,0.3);
  opacity: 0;
  animation: fadeSlideUp 1s ease 0.6s forwards;
}
.cover-title span { color: var(--rose); }

.cover-divider {
  width: 120px; height: 2px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  margin: 24px auto;
  opacity: 0;
  animation: fadeSlideUp 1s ease 0.9s forwards;
}

.cover-tagline {
  font-size: clamp(1rem, 2.5vw, 1.25rem);
  font-style: italic;
  color: var(--blush);
  text-align: center;
  max-width: 500px;
  line-height: 1.7;
  opacity: 0;
  animation: fadeSlideUp 1s ease 1.2s forwards;
}

.scroll-hint {
  position: absolute; bottom: 40px;
  display: flex; flex-direction: column; align-items: center; gap: 8px;
  color: rgba(242,181,195,0.6);
  font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase;
  opacity: 0;
  animation: fadeSlideUp 1s ease 2s forwards;
}
.scroll-arrow {
  width: 2px; height: 40px;
  background: linear-gradient(to bottom, transparent, var(--blush));
  animation: scrollBounce 2s ease-in-out infinite;
}
@keyframes scrollBounce {
  0%,100% { transform: scaleY(1); opacity: 0.5; }
  50%      { transform: scaleY(1.3); opacity: 1; }
}

@keyframes fadeSlideUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── PAGES ── */
.page {
  min-height: 100vh;
  display: flex; align-items: center; justify-content: center;
  padding: 60px 20px;
  position: relative;
  overflow: hidden;
}

.page-inner {
  max-width: 820px; width: 100%;
  display: flex; flex-direction: column; align-items: center;
  gap: 32px; text-align: center;
  position: relative; z-index: 2;
  opacity: 0; transform: translateY(40px);
  transition: opacity 0.9s ease, transform 0.9s ease;
}
.page-inner.visible { opacity: 1; transform: translateY(0); }

/* Page backgrounds */
.page-1 { background: linear-gradient(160deg, #fdf0f5 0%, #f5dce8 40%, #e8c5d5 100%); }
.page-2 { background: linear-gradient(160deg, #f0f5ed 0%, #d8ead5 40%, #b8d4b5 100%); }
.page-3 { background: linear-gradient(160deg, #fdf6ec 0%, #f5e8c8 40%, #e8d4a0 100%); }
.page-4 { background: linear-gradient(160deg, #ede8f5 0%, #d8ccef 40%, #c0b0e0 100%); }
.page-5 { background: linear-gradient(160deg, #f5edf0 0%, #e8d0d8 40%, #d4b0c0 100%); }
.page-final { background: radial-gradient(ellipse at 50% 40%, #3d1a5c, #1a0a2e 70%); }

/* Texture overlay */
.page::before {
  content: '';
  position: absolute; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  opacity: 0.3; pointer-events: none;
}

.page-number {
  font-family: 'Dancing Script', cursive;
  font-size: 0.9rem;
  color: rgba(45,27,78,0.4);
  letter-spacing: 3px;
}

.page-chapter {
  font-family: 'Dancing Script', cursive;
  font-size: clamp(1.2rem, 3vw, 1.6rem);
  color: var(--rose);
  letter-spacing: 2px;
}

.page-emoji {
  font-size: clamp(3.5rem, 8vw, 5rem);
  animation: gentlePulse 3s ease-in-out infinite;
  filter: drop-shadow(0 4px 15px rgba(0,0,0,0.12));
}
@keyframes gentlePulse {
  0%,100% { transform: scale(1) rotate(-2deg); }
  50%      { transform: scale(1.06) rotate(2deg); }
}

.page-heading {
  font-family: 'Playfair Display', serif;
  font-size: clamp(1.8rem, 5vw, 3rem);
  font-style: italic;
  color: var(--ink);
  line-height: 1.2;
}
.page-heading em { color: var(--rose); font-style: normal; }

.ornament {
  font-size: 1.4rem; color: var(--gold); letter-spacing: 8px;
  opacity: 0.7;
}

.page-text {
  font-size: clamp(1rem, 2.5vw, 1.22rem);
  line-height: 1.9;
  color: #3a2040;
  max-width: 640px;
  font-weight: 300;
}
.page-text strong {
  font-weight: 600; color: var(--rose);
  font-style: italic;
}

/* Illustrated card */
.story-card {
  background: rgba(255,255,255,0.55);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.8);
  border-radius: 16px;
  padding: 32px 36px;
  box-shadow: 0 8px 40px rgba(0,0,0,0.08), inset 0 1px 0 rgba(255,255,255,0.9);
  max-width: 640px; width: 100%;
  position: relative;
}
.story-card::before {
  content: '"';
  position: absolute; top: -10px; left: 24px;
  font-family: 'Playfair Display', serif;
  font-size: 5rem; color: var(--rose); opacity: 0.15; line-height: 1;
}

/* Attributes list */
.attributes {
  display: flex; flex-wrap: wrap; gap: 12px; justify-content: center;
  list-style: none;
}
.attributes li {
  background: rgba(255,255,255,0.7);
  border: 1px solid rgba(212,168,83,0.3);
  border-radius: 30px;
  padding: 8px 20px;
  font-size: 0.95rem;
  color: var(--ink);
  font-style: italic;
  backdrop-filter: blur(6px);
  transition: transform 0.2s, box-shadow 0.2s;
}
.attributes li:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(232,96,122,0.2);
}

/* Love letter */
.love-letter {
  background: var(--parchment);
  border: 1px solid rgba(212,168,83,0.4);
  border-radius: 4px;
  padding: 36px 40px;
  font-style: italic;
  line-height: 2;
  font-size: clamp(1rem, 2vw, 1.15rem);
  color: #3a2040;
  box-shadow: 4px 4px 20px rgba(0,0,0,0.08), -2px -2px 8px rgba(255,255,255,0.8);
  max-width: 600px; width: 100%;
  position: relative;
}
.love-letter::after {
  content: '❧';
  display: block; text-align: right;
  font-size: 1.4rem; color: var(--rose);
  margin-top: 16px;
}

/* Final page */
.final-content { color: var(--cream); }
.final-content .page-heading { color: var(--cream); }
.final-content .page-text { color: rgba(242,181,195,0.85); }

.big-heart {
  font-size: clamp(5rem, 15vw, 8rem);
  animation: heartbeat 1.5s ease-in-out infinite;
  filter: drop-shadow(0 0 30px rgba(232,96,122,0.6));
  display: block; line-height: 1;
}
@keyframes heartbeat {
  0%,100% { transform: scale(1); }
  14%      { transform: scale(1.1); }
  28%      { transform: scale(1); }
  42%      { transform: scale(1.05); }
  70%      { transform: scale(1); }
}

.signature {
  font-family: 'Dancing Script', cursive;
  font-size: clamp(1.4rem, 4vw, 2rem);
  color: var(--gold);
  margin-top: 8px;
}

.sparkle-row {
  display: flex; gap: 16px; justify-content: center;
  font-size: 1.8rem;
  animation: sparkleRow 2s ease-in-out infinite;
}
@keyframes sparkleRow {
  0%,100% { opacity: 0.7; transform: scale(1); }
  50%      { opacity: 1;   transform: scale(1.05); }
}

/* Page separator */
.page-divider {
  width: 100%;
  height: 6px;
  background: linear-gradient(90deg,
    var(--midnight) 0%,
    var(--rose) 20%, var(--gold) 50%, var(--rose) 80%,
    var(--midnight) 100%);
  position: relative; z-index: 10;
}

/* Floating petals on pages */
.petal {
  position: absolute; pointer-events: none;
  font-size: clamp(1rem, 2vw, 1.5rem);
  opacity: 0.15;
  animation: petalDrift linear infinite;
}
@keyframes petalDrift {
  0%   { transform: translate(0, -20px) rotate(0deg); opacity: 0; }
  10%  { opacity: 0.2; }
  100% { transform: translate(var(--dx, 30px), 110vh) rotate(var(--dr, 360deg)); opacity: 0; }
}

/* Responsive */
@media (max-width: 600px) {
  .love-letter { padding: 24px 20px; }
  .story-card  { padding: 24px 20px; }
}
</style>
</head>
<body>

<!-- Floating particles -->
<div id="particles"></div>

<!-- ══ COVER ══ -->
<section id="cover">
  <div class="cover-decoration">
    <div class="cover-border"></div>
    <div class="corner-ornament tl"></div>
    <div class="corner-ornament tr"></div>
    <div class="corner-ornament bl"></div>
    <div class="corner-ornament br"></div>
  </div>

  <div class="cover-subtitle">A storybook for</div>
  <div class="cover-floral">🌸</div>
  <h1 class="cover-title">Happy<br/><span>Mother's</span> Day</h1>
  <div class="cover-divider"></div>
  <p class="cover-tagline">
    A small collection of words for the woman who gave us everything — 
    told in pages, petals, and love.
  </p>

  <div class="scroll-hint">
    <span>Scroll to read</span>
    <div class="scroll-arrow"></div>
  </div>
</section>

<!-- ══ PAGE 1 — In the beginning ══ -->
<div class="page-divider"></div>
<section class="page page-1">
  <!-- petals -->
  <span class="petal" style="left:5%;  --dx:20px;  --dr:200deg; animation-duration:9s;  animation-delay:0s;">🌸</span>
  <span class="petal" style="left:85%; --dx:-30px; --dr:300deg; animation-duration:11s; animation-delay:2s;">🌺</span>
  <span class="petal" style="left:50%; --dx:40px;  --dr:180deg; animation-duration:13s; animation-delay:5s;">🌷</span>

  <div class="page-inner" data-scroll>
    <span class="page-number">~ Page One ~</span>
    <div class="page-emoji">✨</div>
    <p class="page-chapter">Chapter One</p>
    <h2 class="page-heading">In the Beginning,<br/>there was <em>You</em></h2>
    <div class="ornament">❧ ✦ ❧</div>
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

<!-- ══ PAGE 2 — The things you do ══ -->
<div class="page-divider"></div>
<section class="page page-2">
  <span class="petal" style="left:10%; --dx:50px;  --dr:400deg; animation-duration:10s; animation-delay:1s;">🍃</span>
  <span class="petal" style="left:70%; --dx:-20px; --dr:260deg; animation-duration:12s; animation-delay:3s;">🌿</span>

  <div class="page-inner" data-scroll>
    <span class="page-number">~ Page Two ~</span>
    <div class="page-emoji">🌿</div>
    <p class="page-chapter">Chapter Two</p>
    <h2 class="page-heading">The Magic You<br/>Made Ordinary</h2>
    <div class="ornament">❧ ✦ ❧</div>
    <p class="page-text">
      You turned simple mornings into rituals, 
      ordinary dinners into celebrations, 
      and hard days into stories that made us stronger.<br/><br/>
      There is a kind of magic only mothers know — 
      the kind that hides in <strong>band-aids and bedtime stories</strong>, 
      in packed lunches and prayers whispered in the dark.
    </p>
    <ul class="attributes">
      <li>🤍 Always patient</li>
      <li>🌸 Endlessly warm</li>
      <li>⭐ Quietly brave</li>
      <li>🌿 Rooted and strong</li>
      <li>✨ Fiercely loving</li>
      <li>☀️ Steadily there</li>
    </ul>
  </div>
</section>

<!-- ══ PAGE 3 — What we learned ══ -->
<div class="page-divider"></div>
<section class="page page-3">
  <span class="petal" style="left:20%; --dx:30px;  --dr:320deg; animation-duration:14s; animation-delay:0s;">🌼</span>
  <span class="petal" style="left:60%; --dx:-40px; --dr:240deg; animation-duration:11s; animation-delay:4s;">✿</span>

  <div class="page-inner" data-scroll>
    <span class="page-number">~ Page Three ~</span>
    <div class="page-emoji">📖</div>
    <p class="page-chapter">Chapter Three</p>
    <h2 class="page-heading">Everything We Know,<br/>We Learned from <em>You</em></h2>
    <div class="ornament">❧ ✦ ❧</div>
    <div class="love-letter">
      You taught us how to be kind — not just politely, but deeply.<br/>
      You showed us that <strong>strength isn't loud</strong>; sometimes it's quiet persistence.<br/>
      You modelled grace under pressure, laughter through tears,<br/>
      and the art of making people feel seen.<br/><br/>
      Every good thing we carry — a piece of it came from you.
    </div>
  </div>
</section>

<!-- ══ PAGE 4 — The small things ══ -->
<div class="page-divider"></div>
<section class="page page-4">
  <span class="petal" style="left:15%; --dx:60px;  --dr:280deg; animation-duration:9s;  animation-delay:2s;">💜</span>
  <span class="petal" style="left:75%; --dx:-50px; --dr:350deg; animation-duration:13s; animation-delay:0s;">🌙</span>

  <div class="page-inner" data-scroll>
    <span class="page-number">~ Page Four ~</span>
    <div class="page-emoji">🫶</div>
    <p class="page-chapter">Chapter Four</p>
    <h2 class="page-heading">The Small Things Were<br/>Never <em>Small</em></h2>
    <div class="ornament">❧ ✦ ❧</div>
    <div class="story-card">
      <p class="page-text">
        The extra blanket. The cup of tea that appeared without asking. 
        The text that just said <strong>"thinking of you."</strong><br/><br/>
        The way you remembered our favourite things. 
        The way you showed up, again and again, 
        without fanfare, without keeping score — 
        just because that's who you are.
      </p>
    </div>
    <p class="page-text" style="font-style:italic; opacity:0.8;">
      We notice. We always noticed. We just didn't always say it enough.
    </p>
  </div>
</section>

<!-- ══ PAGE 5 — Thank you ══ -->
<div class="page-divider"></div>
<section class="page page-5">
  <span class="petal" style="left:8%;  --dx:40px;  --dr:420deg; animation-duration:12s; animation-delay:1s;">🌹</span>
  <span class="petal" style="left:80%; --dx:-35px; --dr:300deg; animation-duration:10s; animation-delay:3s;">🌸</span>
  <span class="petal" style="left:45%; --dx:25px;  --dr:200deg; animation-duration:15s; animation-delay:6s;">💐</span>

  <div class="page-inner" data-scroll>
    <span class="page-number">~ Page Five ~</span>
    <div class="page-emoji">💌</div>
    <p class="page-chapter">Chapter Five</p>
    <h2 class="page-heading">A Letter We've Been<br/>Meaning to <em>Write</em></h2>
    <div class="ornament">❧ ✦ ❧</div>
    <div class="love-letter">
      Dear Mum,<br/><br/>
      Thank you for the mornings you gave up sleep for us.<br/>
      Thank you for the worries you carried alone so we wouldn't have to.<br/>
      Thank you for believing in us when we barely believed in ourselves.<br/><br/>
      Thank you for being <strong>exactly you</strong> — 
      flawed and wonderful and irreplaceable.<br/><br/>
      We love you more than these pages can hold.
    </div>
  </div>
</section>

<!-- ══ FINAL ══ -->
<div class="page-divider"></div>
<section class="page page-final">
  <div class="page-inner final-content" data-scroll>
    <span class="big-heart">💗</span>
    <h2 class="page-heading">Happy Mother's Day</h2>
    <div class="ornament" style="color:var(--gold);">✦ ✦ ✦</div>
    <p class="page-text">
      Today and every day — you are celebrated, cherished, and adored.
    </p>
    <div class="sparkle-row">🌸 🌺 🌼 🌷 🌻</div>
    <p class="signature">With all our love ♡</p>
  </div>
</section>

<script>
/* ── Particles ── */
(function(){
  const container = document.getElementById('particles');
  const symbols = ['✦','·','∘','⋆','✿','◦'];
  const colors  = ['rgba(232,96,122,0.6)','rgba(212,168,83,0.5)',
                   'rgba(201,184,232,0.6)','rgba(242,181,195,0.7)'];
  for(let i=0;i<35;i++){
    const el = document.createElement('span');
    el.className='particle';
    const size  = Math.random()*6+4;
    const left  = Math.random()*100;
    const dur   = Math.random()*18+10;
    const delay = Math.random()*20;
    el.textContent = symbols[Math.floor(Math.random()*symbols.length)];
    el.style.cssText=`
      left:${left}%;
      font-size:${size}px;
      color:${colors[Math.floor(Math.random()*colors.length)]};
      animation-duration:${dur}s;
      animation-delay:${delay}s;
    `;
    container.appendChild(el);
  }
})();

/* ── Scroll reveal ── */
(function(){
  const items = document.querySelectorAll('[data-scroll]');
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){ e.target.classList.add('visible'); io.unobserve(e.target); }
    });
  },{ threshold: 0.15 });
  items.forEach(el=>io.observe(el));
})();
</script>
</body>
</html>
"""

components.html(STORYBOOK_HTML, height=900, scrolling=True)
