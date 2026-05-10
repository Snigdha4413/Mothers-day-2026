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
#  • Any photo      → upload to imgur.com → right-click image → "Copy image address"
#
#  Leave a value as "" to show a decorative placeholder instead.
# ─────────────────────────────────────────────────────────────────────
PHOTO_1 = ""   # Cover circle photo of Mum
PHOTO_2 = ""   # Chapter 2 — a favourite memory
PHOTO_3 = ""   # Chapter 3 — a together/family photo
PHOTO_4 = ""   # Chapter 4 — candid / everyday moment
PHOTO_5 = ""   # Final page photo
# ─────────────────────────────────────────────────────────────────────

def photo_or_placeholder(url, alt, placeholder_emoji="📷", placeholder_label="Paste your photo URL", dark=False):
    if url:
        bg = "linear-gradient(135deg,#3d1a5c,#6a2080)" if dark else "linear-gradient(135deg,#f2b5c3,#d4a0b8)"
        txt_color = "rgba(242,181,195,0.6)" if dark else "rgba(45,27,78,0.4)"
        return (
            f'<img src="{url}" alt="{alt}" '
            f'onerror="this.parentNode.innerHTML=\'<div class=photo-placeholder style=background:{bg}>'
            f'<span class=ph-icon style=opacity:0.6>{placeholder_emoji}</span>'
            f'<span style=color:{txt_color}>{placeholder_label}</span></div>\'" />'
        )
    bg = "linear-gradient(135deg,#3d1a5c,#6a2080)" if dark else "linear-gradient(135deg,#f2b5c3,#d4a0b8)"
    txt_color = "rgba(242,181,195,0.6)" if dark else "rgba(45,27,78,0.4)"
    return (
        f'<div class="photo-placeholder" style="background:{bg}">'
        f'<span class="ph-icon" style="opacity:0.6">{placeholder_emoji}</span>'
        f'<span style="color:{txt_color}">{placeholder_label}</span></div>'
    )

STORYBOOK_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no"/>
<title>Happy Mother's Day</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,600&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Dancing+Script:wght@400;700&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}
:root{{
  --rose:#e8607a;--blush:#f2b5c3;--gold:#d4a853;--cream:#fdf6ec;
  --sage:#7ca982;--lavender:#c9b8e8;--midnight:#1a0a2e;
  --parchment:#f5ead6;--ink:#2d1b4e;
}}
html{{scroll-behavior:smooth;}}
body{{
  font-family:'Cormorant Garamond',serif;
  background:var(--midnight);color:var(--ink);
  overflow-x:hidden;-webkit-font-smoothing:antialiased;
}}

/* PARTICLES */
#particles{{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;}}
.particle{{position:absolute;animation:floatUp linear infinite;opacity:0;}}
@keyframes floatUp{{
  0%{{transform:translateY(100vh) rotate(0deg);opacity:0;}}
  10%{{opacity:0.55;}}90%{{opacity:0.25;}}
  100%{{transform:translateY(-10vh) rotate(720deg);opacity:0;}}
}}

/* COVER */
#cover{{
  min-height:100svh;display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  position:relative;overflow:hidden;
  background:radial-gradient(ellipse at 50% 60%,#3d1a5c 0%,#1a0a2e 60%,#0d0518 100%);
  padding:60px 24px 90px;text-align:center;
}}
.cover-border{{
  position:absolute;inset:14px;
  border:1.5px solid rgba(212,168,83,0.35);border-radius:4px;
  pointer-events:none;
  animation:borderGlow 3s ease-in-out infinite alternate;
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
  overflow:hidden;margin-bottom:22px;flex-shrink:0;
  opacity:0;animation:fadeUp 1s ease 0.4s forwards;
}}
.cover-photo-wrap img{{width:100%;height:100%;object-fit:cover;}}
.cover-photo-placeholder{{
  width:100%;height:100%;
  background:radial-gradient(circle,#f2b5c3,#e8607a);
  display:flex;align-items:center;justify-content:center;font-size:3rem;
}}
.cover-subtitle{{
  font-family:'Dancing Script',cursive;
  font-size:clamp(0.85rem,3vw,1.15rem);
  color:var(--blush);letter-spacing:4px;text-transform:uppercase;margin-bottom:10px;
  opacity:0;animation:fadeUp 1s ease 0.65s forwards;
}}
.cover-title{{
  font-family:'Playfair Display',serif;
  font-size:clamp(2.2rem,11vw,5rem);
  font-style:italic;color:var(--cream);line-height:1.1;
  text-shadow:0 0 50px rgba(232,96,122,0.3);
  opacity:0;animation:fadeUp 1s ease 0.85s forwards;
}}
.cover-title span{{color:var(--rose);}}
.cover-divider{{
  width:90px;height:2px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
  margin:18px auto;
  opacity:0;animation:fadeUp 1s ease 1.05s forwards;
}}
.cover-tagline{{
  font-size:clamp(0.92rem,3vw,1.1rem);font-style:italic;
  color:var(--blush);max-width:300px;line-height:1.8;
  opacity:0;animation:fadeUp 1s ease 1.25s forwards;
}}
.scroll-hint{{
  position:absolute;bottom:26px;
  display:flex;flex-direction:column;align-items:center;gap:6px;
  color:rgba(242,181,195,0.55);
  font-size:0.72rem;letter-spacing:2px;text-transform:uppercase;
  opacity:0;animation:fadeUp 1s ease 2.2s forwards;
}}
.scroll-arrow{{
  width:2px;height:30px;
  background:linear-gradient(to bottom,transparent,var(--blush));
  animation:scrollBounce 2s ease-in-out infinite;
}}
@keyframes scrollBounce{{0%,100%{{transform:scaleY(1);opacity:0.5;}}50%{{transform:scaleY(1.3);opacity:1;}}}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(18px);}}to{{opacity:1;transform:translateY(0);}}}}

/* DIVIDER */
.page-divider{{
  width:100%;height:5px;
  background:linear-gradient(90deg,var(--midnight),var(--rose) 25%,var(--gold) 50%,var(--rose) 75%,var(--midnight));
  position:relative;z-index:10;
}}

/* PAGES */
.page{{
  min-height:100svh;display:flex;align-items:center;justify-content:center;
  padding:48px 18px 60px;position:relative;overflow:hidden;
}}
.page-1{{background:linear-gradient(160deg,#fdf0f5,#f5dce8 50%,#e8c5d5);}}
.page-2{{background:linear-gradient(160deg,#f0f5ed,#d8ead5 50%,#b8d4b5);}}
.page-3{{background:linear-gradient(160deg,#fdf6ec,#f5e8c8 50%,#e8d4a0);}}
.page-4{{background:linear-gradient(160deg,#ede8f5,#d8ccef 50%,#c0b0e0);}}
.page-5{{background:linear-gradient(160deg,#f5edf0,#e8d0d8 50%,#d4b0c0);}}
.page-final{{background:radial-gradient(ellipse at 50% 40%,#3d1a5c,#1a0a2e 70%);}}

.page-inner{{
  max-width:460px;width:100%;
  display:flex;flex-direction:column;align-items:center;
  gap:22px;text-align:center;position:relative;z-index:2;
  opacity:0;transform:translateY(36px);
  transition:opacity 0.8s ease,transform 0.8s ease;
}}
.page-inner.visible{{opacity:1;transform:translateY(0);}}

.page-number{{font-family:'Dancing Script',cursive;font-size:0.82rem;color:rgba(45,27,78,0.38);letter-spacing:3px;}}
.page-chapter{{font-family:'Dancing Script',cursive;font-size:clamp(1.05rem,4vw,1.45rem);color:var(--rose);letter-spacing:1px;}}
.page-emoji{{font-size:clamp(2.8rem,9vw,4rem);animation:gentlePulse 3s ease-in-out infinite;line-height:1;filter:drop-shadow(0 4px 12px rgba(0,0,0,0.1));}}
@keyframes gentlePulse{{0%,100%{{transform:scale(1) rotate(-2deg);}}50%{{transform:scale(1.06) rotate(2deg);}}}}
.page-heading{{font-family:'Playfair Display',serif;font-size:clamp(1.5rem,6vw,2.4rem);font-style:italic;color:var(--ink);line-height:1.2;}}
.page-heading em{{color:var(--rose);font-style:normal;}}
.ornament{{font-size:1.1rem;color:var(--gold);letter-spacing:8px;opacity:0.7;}}
.page-text{{font-size:clamp(0.96rem,3vw,1.12rem);line-height:1.9;color:#3a2040;font-weight:300;}}
.page-text strong{{font-weight:600;color:var(--rose);font-style:italic;}}

/* PHOTO FRAME */
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
.photo-caption{{font-family:'Dancing Script',cursive;font-size:0.9rem;color:rgba(45,27,78,0.45);font-style:italic;margin-top:-6px;}}

/* STORY CARD */
.story-card{{
  background:rgba(255,255,255,0.52);backdrop-filter:blur(10px);
  border:1px solid rgba(255,255,255,0.8);border-radius:14px;
  padding:22px 22px;
  box-shadow:0 6px 28px rgba(0,0,0,0.07),inset 0 1px 0 rgba(255,255,255,0.9);
  width:100%;position:relative;
}}
.story-card::before{{
  content:'"';position:absolute;top:-8px;left:16px;
  font-family:'Playfair Display',serif;font-size:3.5rem;color:var(--rose);opacity:0.11;line-height:1;
}}

/* ATTRIBUTES */
.attributes{{display:flex;flex-wrap:wrap;gap:9px;justify-content:center;list-style:none;}}
.attributes li{{
  background:rgba(255,255,255,0.68);border:1px solid rgba(212,168,83,0.3);
  border-radius:30px;padding:6px 14px;
  font-size:0.88rem;color:var(--ink);font-style:italic;
}}

/* LOVE LETTER */
.love-letter{{
  background:var(--parchment);border:1px solid rgba(212,168,83,0.4);
  border-radius:4px;padding:26px 22px;
  font-style:italic;line-height:1.95;
  font-size:clamp(0.93rem,2.8vw,1.08rem);
  color:#3a2040;
  box-shadow:4px 4px 16px rgba(0,0,0,0.07);width:100%;
}}
.love-letter::after{{content:'❧';display:block;text-align:right;font-size:1.2rem;color:var(--rose);margin-top:12px;}}

/* FINAL */
.final-content .page-heading{{color:var(--cream);}}
.final-content .page-text{{color:rgba(242,181,195,0.82);}}
.big-heart{{font-size:clamp(4rem,16vw,7rem);animation:heartbeat 1.5s ease-in-out infinite;filter:drop-shadow(0 0 25px rgba(232,96,122,0.6));line-height:1;}}
@keyframes heartbeat{{0%,100%{{transform:scale(1);}}14%{{transform:scale(1.1);}}28%{{transform:scale(1);}}42%{{transform:scale(1.05);}}70%{{transform:scale(1);}}}}
.signature{{font-family:'Dancing Script',cursive;font-size:clamp(1.25rem,5vw,1.85rem);color:var(--gold);margin-top:4px;}}
.sparkle-row{{display:flex;gap:10px;justify-content:center;font-size:1.5rem;animation:sparkleRow 2s ease-in-out infinite;}}
@keyframes sparkleRow{{0%,100%{{opacity:0.7;transform:scale(1);}}50%{{opacity:1;transform:scale(1.05);}}}}

/* PETALS */
.petal{{position:absolute;pointer-events:none;font-size:clamp(0.8rem,2vw,1.2rem);animation:petalDrift linear infinite;opacity:0;}}
@keyframes petalDrift{{
  0%{{transform:translate(0,-20px) rotate(0deg);opacity:0;}}
  10%{{opacity:0.18;}}
  100%{{transform:translate(var(--dx,30px),110vh) rotate(var(--dr,360deg));opacity:0;}}
}}

/* MOBILE */
@media(max-width:440px){{
  .love-letter{{padding:20px 16px;}}
  .story-card{{padding:18px 16px;}}
  .photo-frame{{max-width:100%;}}
  .photo-frame.portrait{{max-width:190px;}}
  .attributes li{{font-size:0.82rem;padding:5px 12px;}}
}}
</style>
</head>
<body>
<div id="particles"></div>

<!-- COVER -->
<section id="cover">
  <div class="cover-border"></div>
  <div class="corner tl"></div><div class="corner tr"></div>
  <div class="corner bl"></div><div class="corner br"></div>
  <div class="cover-photo-wrap">
    {photo_or_placeholder(PHOTO_1, "Mum", "🌸", "Your photo here")}
  </div>
  <div class="cover-subtitle">A storybook for</div>
  <h1 class="cover-title">Happy<br/><span>Mother's</span> Day</h1>
  <div class="cover-divider"></div>
  <p class="cover-tagline">A small collection of words for the woman who gave us everything.</p>
  <div class="scroll-hint">
    <span>Scroll to read</span>
    <div class="scroll-arrow"></div>
  </div>
</section>

<!-- PAGE 1 -->
<div class="page-divider"></div>
<section class="page page-1">
  <span class="petal" style="left:5%;--dx:20px;--dr:200deg;animation-duration:9s;animation-delay:0s;">🌸</span>
  <span class="petal" style="left:82%;--dx:-30px;--dr:300deg;animation-duration:11s;animation-delay:2s;">🌺</span>
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

<!-- PAGE 2 -->
<div class="page-divider"></div>
<section class="page page-2">
  <span class="petal" style="left:10%;--dx:50px;--dr:400deg;animation-duration:10s;animation-delay:1s;">🍃</span>
  <span class="petal" style="left:72%;--dx:-20px;--dr:260deg;animation-duration:12s;animation-delay:3s;">🌿</span>
  <div class="page-inner" data-scroll>
    <span class="page-number">~ Page Two ~</span>
    <p class="page-chapter">Chapter Two</p>
    <h2 class="page-heading">The Magic You<br/>Made Ordinary</h2>
    <div class="ornament">❧ ✦ ❧</div>
    <div class="photo-frame">
      {photo_or_placeholder(PHOTO_2, "A favourite memory")}
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

<!-- PAGE 3 -->
<div class="page-divider"></div>
<section class="page page-3">
  <span class="petal" style="left:20%;--dx:30px;--dr:320deg;animation-duration:14s;animation-delay:0s;">🌼</span>
  <span class="petal" style="left:65%;--dx:-40px;--dr:240deg;animation-duration:11s;animation-delay:4s;">✿</span>
  <div class="page-inner" data-scroll>
    <span class="page-number">~ Page Three ~</span>
    <p class="page-chapter">Chapter Three</p>
    <h2 class="page-heading">Everything We Know,<br/>We Learned from <em>You</em></h2>
    <div class="ornament">❧ ✦ ❧</div>
    <div class="photo-frame portrait">
      {photo_or_placeholder(PHOTO_3, "Together")}
    </div>
    <p class="photo-caption">Together ✦</p>
    <div class="love-letter">
      You taught us how to be kind — not just politely, but deeply.<br/>
      You showed us that <strong>strength isn't loud</strong>; sometimes it's quiet persistence.<br/>
      You modelled grace under pressure, laughter through tears,<br/>
      and the art of making people feel seen.<br/><br/>
      Every good thing we carry — a piece of it came from you.
    </div>
  </div>
</section>

<!-- PAGE 4 -->
<div class="page-divider"></div>
<section class="page page-4">
  <span class="petal" style="left:15%;--dx:60px;--dr:280deg;animation-duration:9s;animation-delay:2s;">💜</span>
  <span class="petal" style="left:75%;--dx:-50px;--dr:350deg;animation-duration:13s;animation-delay:0s;">🌙</span>
  <div class="page-inner" data-scroll>
    <span class="page-number">~ Page Four ~</span>
    <p class="page-chapter">Chapter Four</p>
    <h2 class="page-heading">The Small Things Were<br/>Never <em>Small</em></h2>
    <div class="ornament">❧ ✦ ❧</div>
    <div class="photo-frame">
      {photo_or_placeholder(PHOTO_4, "An everyday moment")}
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

<!-- PAGE 5 -->
<div class="page-divider"></div>
<section class="page page-5">
  <span class="petal" style="left:8%;--dx:40px;--dr:420deg;animation-duration:12s;animation-delay:1s;">🌹</span>
  <span class="petal" style="left:78%;--dx:-35px;--dr:300deg;animation-duration:10s;animation-delay:3s;">🌸</span>
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

<!-- FINAL -->
<div class="page-divider"></div>
<section class="page page-final">
  <div class="page-inner final-content" data-scroll>
    <div class="photo-frame" style="border-color:rgba(212,168,83,0.6);box-shadow:0 0 0 6px rgba(212,168,83,0.1),0 8px 40px rgba(232,96,122,0.3);">
      {photo_or_placeholder(PHOTO_5, "Mum", "🌸", "Your photo here", dark=True)}
    </div>
    <span class="big-heart">💗</span>
    <h2 class="page-heading">Happy Mother's Day</h2>
    <div class="ornament" style="color:var(--gold);">✦ ✦ ✦</div>
    <p class="page-text">Today and every day — you are celebrated, cherished, and adored.</p>
    <div class="sparkle-row">🌸 🌺 🌼 🌷 🌻</div>
    <p class="signature">With all our love ♡</p>
  </div>
</section>

<script>
(function(){{
  const c=document.getElementById('particles');
  const s=['✦','·','∘','⋆','◦','✿'];
  const col=['rgba(232,96,122,0.5)','rgba(212,168,83,0.45)','rgba(201,184,232,0.55)','rgba(242,181,195,0.6)'];
  for(let i=0;i<28;i++){{
    const el=document.createElement('span');
    el.className='particle';
    el.textContent=s[Math.floor(Math.random()*s.length)];
    el.style.cssText=`left:${{Math.random()*100}}%;font-size:${{Math.random()*5+3}}px;color:${{col[Math.floor(Math.random()*col.length)]}};animation-duration:${{Math.random()*18+10}}s;animation-delay:${{Math.random()*20}}s;`;
    c.appendChild(el);
  }}
}})();
(function(){{
  const items=document.querySelectorAll('[data-scroll]');
  const io=new IntersectionObserver(entries=>{{
    entries.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('visible');io.unobserve(e.target);}}  }});
  }},{{threshold:0.1}});
  items.forEach(el=>io.observe(el));
}})();
</script>
</body>
</html>"""

components.html(STORYBOOK_HTML, height=900, scrolling=True)
