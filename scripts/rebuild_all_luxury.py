"""
Luxury Edition SVG & Asset Generator for Pasha Dev (Muhammad Mubashar)
Obsidian & Luminous Cyber Amethyst / Royal Indigo / Ice Cyan Palette
Zero-overlap hero portrait layout, studio-enhanced portrait grading,
and rock-solid XML validation.
"""

import os
import base64
from io import BytesIO
from PIL import Image, ImageEnhance
import xml.etree.ElementTree as ET

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(WORKSPACE_DIR, "assets")
PROFILE_DIR = os.path.join(WORKSPACE_DIR, "profile")
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(PROFILE_DIR, exist_ok=True)


# ─────────────────────────────────────────────────────────────────────────────
# 1. OPTIMIZE & BASE64 ENCODE USER PORTRAIT WITH STUDIO GRADING
# ─────────────────────────────────────────────────────────────────────────────
def get_user_portrait_base64():
    selfie_path = os.path.join(WORKSPACE_DIR, "Fisheye Selfie in a Tech Bedroom.png")
    if not os.path.exists(selfie_path):
        raise FileNotFoundError(f"Missing {selfie_path}")
    
    im = Image.open(selfie_path)
    # Crop around user's face, glasses, dark shirt, and background tech monitor
    cropped = im.crop((160, 100, 1100, 1160)).resize((480, 540), Image.Resampling.LANCZOS)
    
    # Studio grade: gently enhance contrast & brightness for rich natural skin tones
    contrast = ImageEnhance.Contrast(cropped).enhance(1.08)
    enhanced = ImageEnhance.Brightness(contrast).enhance(1.03)
    
    buf = BytesIO()
    enhanced.save(buf, format="JPEG", quality=92, optimize=True)
    jpg_bytes = buf.getvalue()
    
    portrait_jpg_path = os.path.join(ASSETS_DIR, "pasha-portrait.jpg")
    with open(portrait_jpg_path, "wb") as f:
        f.write(jpg_bytes)
        
    return base64.b64encode(jpg_bytes).decode("utf-8")


# ─────────────────────────────────────────────────────────────────────────────
# 2. HERO PORTRAIT SVG (1200 x 480) - ZERO OVERLAP, LUXURY OBSIDIAN & AMETHYST
# ─────────────────────────────────────────────────────────────────────────────
def build_hero_portrait_svg(b64_img):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-label="Muhammad Mubashar (Pasha Dev) — AI Systems Architect, Full-Stack Developer, Creative Technologist">
  <defs>
    <linearGradient id="hero-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#06070B"/>
      <stop offset="50" stop-color="#0B0D15"/>
      <stop offset="100" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="hero-glow-left" cx="20%" cy="40%" r="65%">
      <stop offset="0" stop-color="#6366F1" stop-opacity=".18"/>
      <stop offset="100%" stop-color="#6366F1" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-glow-right" cx="82%" cy="48%" r="60%">
      <stop offset="0" stop-color="#A855F7" stop-opacity=".22"/>
      <stop offset="50" stop-color="#38BDF8" stop-opacity=".10"/>
      <stop offset="100%" stop-color="#06070B" stop-opacity="0"/>
    </radialGradient>
    <pattern id="hero-grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 H 0 V 32" fill="none" stroke="#1E2336" stroke-opacity=".15"/>
      <circle cx="32" cy="32" r=".7" fill="#8B5CF6" fill-opacity=".2"/>
    </pattern>
    <linearGradient id="hero-rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#A855F7"/>
      <stop offset=".5" stop-color="#6366F1"/>
      <stop offset="1" stop-color="#38BDF8" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-name-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#A855F7"/>
      <stop offset=".45" stop-color="#818CF8"/>
      <stop offset="1" stop-color="#38BDF8"/>
    </linearGradient>
    <linearGradient id="hero-sheen" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset=".45" stop-color="#FFFFFF" stop-opacity=".9"/>
      <stop offset=".55" stop-color="#C084FC" stop-opacity=".9"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1600 0;1600 0" keyTimes="0;.45;1" dur="7s" begin="1.2s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="hero-frame-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#A855F7"/>
      <stop offset=".5" stop-color="#6366F1"/>
      <stop offset="1" stop-color="#38BDF8"/>
    </linearGradient>
    <linearGradient id="hero-photo-grade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#A855F7" stop-opacity=".05"/>
      <stop offset="60%" stop-color="#06070B" stop-opacity="0"/>
      <stop offset="100%" stop-color="#06070B" stop-opacity=".72"/>
    </linearGradient>
    <filter id="hero-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="hero-arch">
      <path d="M 890 398 V 183 A 115 115 0 0 1 1120 183 V 398 Z"/>
    </clipPath>
  </defs>
  <style>
    .hero-serif {{ font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }}
    .hero-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }}
    .hero-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }}
    .hero-rise {{ animation: hero-rise 1s cubic-bezier(.16,1,.3,1) both; }}
    .hero-fade {{ animation: hero-fade 1.2s cubic-bezier(.16,1,.3,1) both; }}
    .d1 {{ animation-delay: .15s; }} .d2 {{ animation-delay: .3s; }}
    .d3 {{ animation-delay: .45s; }} .d4 {{ animation-delay: .6s; }}
    .d5 {{ animation-delay: .75s; }} .d6 {{ animation-delay: .9s; }}
    .hero-draw {{ stroke-dasharray: 600; stroke-dashoffset: 600; animation: hero-draw 1.8s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    .hero-signal {{ stroke-dasharray: 380; stroke-dashoffset: 380; animation: hero-draw 2.2s cubic-bezier(.65,0,.35,1) 1s forwards; }}
    .hero-frame {{ stroke-dasharray: 900; stroke-dashoffset: 900; animation: hero-draw 2s cubic-bezier(.65,0,.35,1) .4s forwards; }}
    @keyframes hero-rise {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes hero-fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes hero-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .hero-rise, .hero-fade {{ animation: none; opacity: 1; }}
      .hero-draw, .hero-signal, .hero-frame {{ stroke-dashoffset: 0; }}
    }}
  </style>

  <!-- Canvas Background -->
  <rect width="1200" height="480" rx="18" fill="url(#hero-bg)"/>
  <rect width="1200" height="480" rx="18" fill="url(#hero-grid)"/>
  <rect width="1200" height="480" rx="18" fill="url(#hero-glow-left)"/>
  <rect width="1200" height="480" rx="18" fill="url(#hero-glow-right)"/>

  <!-- Arch Portrait & Celestial Ring Group (Anchored at x=890..1120) -->
  <g id="portrait-group">
    <!-- Rotating Celestial Node Rings centered at (1005, 235) -->
    <g transform="translate(1005, 235)" class="hero-fade d4">
      <circle r="150" fill="none" stroke="#6366F1" stroke-opacity=".20" stroke-dasharray="4 8"/>
      <circle r="175" fill="none" stroke="#A855F7" stroke-opacity=".14"/>
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="75s" repeatCount="indefinite"/>
        <circle cx="175" cy="0" r="4" fill="#38BDF8" filter="url(#hero-glow)"/>
        <circle cx="-124" cy="-124" r="2.5" fill="#A855F7"/>
        <circle cx="0" cy="-175" r="2" fill="#818CF8"/>
      </g>
      <!-- Technical Layer Pins -->
      <g class="hero-mono" font-size="9.5" letter-spacing="1.5" fill="#94A3B8">
        <g transform="translate(-135, -135)"><circle r="3" fill="#A855F7"/><text x="8" y="3.5" fill="#E2E8F0">AI · AGENTS</text></g>
        <g transform="translate(120, -95)"><circle r="3" fill="#38BDF8"/><text x="8" y="3.5" fill="#E2E8F0">FASTAPI</text></g>
        <g transform="translate(120, 95)"><circle r="3" fill="#38BDF8"/><text x="8" y="3.5" fill="#E2E8F0">REACT 19</text></g>
        <g transform="translate(-145, 65)"><circle r="3" fill="#A855F7"/><text x="-8" y="3.5" text-anchor="end" fill="#E2E8F0">TAURI · RUST</text></g>
        <g transform="translate(-10, 165)"><circle r="3" fill="#6366F1"/><text x="8" y="3.5" fill="#E2E8F0">THREE.JS · GLSL</text></g>
      </g>
    </g>

    <!-- Arched Portrait Clipping Frame (Width 230, Radius 115) -->
    <g class="hero-fade d2">
      <g clip-path="url(#hero-arch)">
        <image href="data:image/jpeg;base64,{b64_img}" x="890" y="68" width="230" height="330" preserveAspectRatio="xMidYMid slice"/>
        <rect x="890" y="68" width="230" height="330" fill="url(#hero-photo-grade)"/>
      </g>
      <!-- Arched Accent Border -->
      <path class="hero-frame" d="M 890 398 V 183 A 115 115 0 0 1 1120 183 V 398 Z" fill="none" stroke="url(#hero-frame-grad)" stroke-width="1.8"/>
      <!-- Reticle Accent Brackets -->
      <path d="M 874 300 v-20 h 20" fill="none" stroke="#A855F7" stroke-opacity=".75" stroke-width="1.4"/>
      <path d="M 1136 414 v-20 M 1136 414 h-20" fill="none" stroke="#38BDF8" stroke-opacity=".75" stroke-width="1.4"/>
    </g>
  </g>

  <!-- Left Content: Terminal Indicator -->
  <g class="hero-fade d1" transform="translate(68, 50)">
    <rect width="338" height="32" rx="16" fill="#0C0E18" stroke="#8B5CF6" stroke-opacity=".35"/>
    <circle cx="18" cy="16" r="4" fill="#10B981" filter="url(#hero-glow)">
      <animate attributeName="opacity" values="1;.4;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text class="hero-mono" x="34" y="20" font-size="11.5" fill="#94A3B8">~/pasha<tspan fill="#A855F7"> $ </tspan><tspan fill="#F8FAFC">build --intelligent</tspan></text>
    <rect x="312" y="9" width="6" height="14" fill="#A855F7">
      <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1s" repeatCount="indefinite"/>
    </rect>
  </g>

  <!-- Eyebrow Category -->
  <g class="hero-rise d2">
    <line x1="68" y1="122" x2="98" y2="122" stroke="#A855F7" stroke-width="1.5"/>
    <text class="hero-mono" x="108" y="126" font-size="11.5" letter-spacing="3" fill="#A855F7">AI SYSTEMS ARCHITECT · AUTONOMOUS SDLC · EXPERIENTIAL 3D</text>
  </g>

  <!-- Large Headline Name: Width ~440px, well clear of arch at x=890 -->
  <text class="hero-serif hero-rise d3" x="68" y="194" font-size="52" font-weight="300" letter-spacing="-1.2" fill="#F8FAFC">Muhammad Mubashar</text>
  <text class="hero-serif hero-rise d4" x="68" y="268" font-size="64" font-weight="400" font-style="italic" letter-spacing="-1.2" fill="url(#hero-name-grad)">Pasha<tspan fill="#A855F7">.</tspan></text>

  <!-- Light Sheen Sweeping Across Headline -->
  <g class="hero-fade d6" pointer-events="none">
    <text class="hero-serif" x="68" y="194" font-size="52" font-weight="300" letter-spacing="-1.2" fill="url(#hero-sheen)">Muhammad Mubashar</text>
    <text class="hero-serif" x="68" y="268" font-size="64" font-style="italic" font-weight="400" letter-spacing="-1.2" fill="url(#hero-sheen)">Pasha.</text>
  </g>

  <!-- Glowing Curvature Underline -->
  <path class="hero-draw" d="M 68 296 C 180 292, 340 300, 480 294" fill="none" stroke="url(#hero-rule)" stroke-width="2" stroke-linecap="round" filter="url(#hero-glow)"/>

  <!-- Signal Curve Drawing toward Portrait Arch -->
  <path class="hero-signal" d="M 480 294 C 600 288, 740 274, 888 274" fill="none" stroke="#8B5CF6" stroke-opacity=".3" stroke-width="1.2"/>
  <circle cx="480" cy="294" r="3" fill="#C084FC" filter="url(#hero-glow)" opacity=".9">
    <animateMotion dur="5.5s" repeatCount="indefinite" begin="3.8s" path="M 480 294 C 600 288, 740 274, 888 274" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".45 0 .55 1"/>
  </circle>

  <!-- Positioning Subtitle & Ethos -->
  <text class="hero-mono hero-rise d5" x="68" y="338" font-size="12" letter-spacing="2" fill="#CBD5E1">AI/ML SYSTEMS ARCHITECT  ·  FULL-STACK DEVELOPER  ·  CREATIVE TECHNOLOGIST</text>
  <text class="hero-serif hero-rise d6" x="68" y="376" font-size="17" font-style="italic" fill="#94A3B8">Engineering intelligence. Architecting resilient platforms. Designing experiences.</text>

  <!-- Meta Strip -->
  <g class="hero-fade d6">
    <line x1="68" y1="428" x2="1132" y2="428" stroke="#1E2336" stroke-opacity=".6"/>
    <text class="hero-mono" x="68" y="450" font-size="10" letter-spacing="2" fill="#64748B">LAHORE, PAKISTAN  ·  31.52° N, 74.35° E</text>
    <text class="hero-mono" x="1132" y="450" text-anchor="end" font-size="10" letter-spacing="2" fill="#A855F7">FOUNDER &amp; ARCHITECT · PASHA DEVPILOT (HACKATHON) · SYNCFORGE · PRIVATEDOC</text>
  </g>

  <!-- Canvas Outer Border -->
  <rect x=".5" y=".5" width="1199" height="479" rx="17.5" fill="none" stroke="#252B42" stroke-opacity=".7"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 3. SECTION TITLES (1200 x 120 each) - OBSIDIAN & AMETHYST / CYAN
# ─────────────────────────────────────────────────────────────────────────────
def build_title_svg(num, title_word, title_rest, subtitle, right_tag):
    clean_subtitle = subtitle.replace("&", "&amp;")
    clean_right_tag = right_tag.replace("&", "&amp;")
    clean_title_rest = title_rest.replace("&", "&amp;")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="img" aria-label="{num} {title_word} {clean_title_rest}">
  <defs>
    <linearGradient id="ta-line-{num}" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="1160" y2="0">
      <stop offset="0" stop-color="#A855F7"/>
      <stop offset=".4" stop-color="#6366F1"/>
      <stop offset=".8" stop-color="#38BDF8"/>
      <stop offset="1" stop-color="#38BDF8" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ta-sheen-{num}" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#C084FC"/>
      <stop offset=".5" stop-color="#F8FAFC"/>
      <stop offset="1" stop-color="#C084FC"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1500 0;1500 0" keyTimes="0;.4;1" dur="7s" begin="1.5s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="ta-pulse-{num}"><stop offset="0" stop-color="#F8FAFC"/><stop offset=".5" stop-color="#A855F7" stop-opacity=".7"/><stop offset="1" stop-color="#6366F1" stop-opacity="0"/></radialGradient>
  </defs>
  <style>
    .ta-serif {{ font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }}
    .ta-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }}
    .ta-in {{ animation: ta-in 1.1s cubic-bezier(.16,1,.3,1) both; }}
    .ta-d2 {{ animation-delay: .2s; }} .ta-d3 {{ animation-delay: .45s; }}
    .ta-draw {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: ta-draw 1.8s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes ta-in {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes ta-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ta-in {{ animation: none; }} .ta-draw {{ stroke-dashoffset: 0; }} }}
  </style>
  <g class="ta-in">
    <text class="ta-mono" x="40" y="34" font-size="12" letter-spacing="3" fill="#A855F7"><tspan fill="#818CF8">{num}</tspan>   {title_word.upper()}</text>
  </g>
  <g class="ta-in ta-d2">
    <text class="ta-serif" x="38" y="84" font-size="44" font-weight="300" letter-spacing="-1" fill="#F8FAFC">{title_word}, <tspan font-style="italic" fill="url(#ta-sheen-{num})">{clean_title_rest}</tspan></text>
  </g>
  <g class="ta-in ta-d3">
    <text class="ta-mono" x="1160" y="34" text-anchor="end" font-size="10.5" letter-spacing="2.4" fill="#64748B">{clean_right_tag}</text>
    <text class="ta-mono" x="1160" y="84" text-anchor="end" font-size="11" letter-spacing="1.5" fill="#A855F7">{clean_subtitle}</text>
  </g>
  <path class="ta-draw" d="M40 106 H1160" stroke="url(#ta-line-{num})" stroke-width="1.2"/>
  <circle cx="40" cy="106" r="6" fill="url(#ta-pulse-{num})" opacity="0">
    <animate attributeName="cx" values="40;1160" dur="6s" begin="2.3s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines=".45 0 .55 1"/>
    <animate attributeName="opacity" values="0;1;0" keyTimes="0;.15;1" dur="6s" begin="2.3s" repeatCount="indefinite"/>
  </circle>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 4. SECTION 01: ABOUT INTRO CARD (1200 x 300)
# ─────────────────────────────────────────────────────────────────────────────
def build_about_intro_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300" role="img" aria-label="About Muhammad Mubashar">
  <defs>
    <linearGradient id="ai-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/>
      <stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <pattern id="ai-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 H 0 V 24" fill="none" stroke="#1E2336" stroke-opacity=".15"/>
    </pattern>
    <radialGradient id="ai-glow" cx="15%" cy="30%" r="55%">
      <stop offset="0" stop-color="#6366F1" stop-opacity=".18"/>
      <stop offset="100%" stop-color="#6366F1" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .ai-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .ai-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .ai-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
  </style>

  <rect width="1200" height="300" rx="16" fill="url(#ai-bg)"/>
  <rect width="1200" height="300" rx="16" fill="url(#ai-grid)"/>
  <rect width="1200" height="300" rx="16" fill="url(#ai-glow)"/>

  <g transform="translate(56, 44)">
    <!-- Header Monospace -->
    <text class="ai-mono" font-size="11.5" letter-spacing="2.5" fill="#A855F7">DISCIPLINE BUILDS FREEDOM  //  ZERO FRICTION  //  SURVIVAL BEFORE ABSTRACTION</text>

    <!-- Main Editorial Bio -->
    <text class="ai-sans" y="44" font-size="18" fill="#F8FAFC" font-weight="300" line-height="1.6">
      <tspan x="0" dy="0">I am an AI Systems Architect &amp; Full-Stack Engineer based in Lahore, Pakistan, focused on building enduring,</tspan>
      <tspan x="0" dy="30">high-velocity software. My work lives at the intersection of autonomous multi-agent intelligence, resilient</tspan>
      <tspan x="0" dy="30">distributed microservices, and immersive 3D computing.</tspan>
    </text>

    <!-- Ethos Quote Box -->
    <g transform="translate(0, 126)">
      <rect width="1088" height="54" rx="8" fill="#0D101C" stroke="#6366F1" stroke-opacity=".3"/>
      <line x1="0" y1="0" x2="0" y2="54" stroke="#A855F7" stroke-width="4"/>
      <text class="ai-serif" x="24" y="33" font-size="16" font-style="italic" fill="#E2E8F0">"Survival before abstraction. Precision before shortcuts. Zero-friction execution. AI as the ultimate force multiplier."</text>
    </g>

    <!-- Three Technical Pillars -->
    <g transform="translate(0, 206)" class="ai-mono" font-size="11.5" fill="#94A3B8">
      <g transform="translate(0, 0)">
        <circle cx="5" cy="4" r="3.5" fill="#A855F7"/>
        <text x="16" y="8" fill="#F8FAFC" font-weight="700">AUTONOMOUS AI</text>
        <text x="16" y="24" fill="#64748B">LLM pipelines · Vision OCR · Whisper STT · Live referees</text>
      </g>
      <g transform="translate(370, 0)">
        <circle cx="5" cy="4" r="3.5" fill="#6366F1"/>
        <text x="16" y="8" fill="#F8FAFC" font-weight="700">SYSTEMS &amp; BACKENDS</text>
        <text x="16" y="24" fill="#64748B">FastAPI · Node.js · PostgreSQL · Redis · Docker · Rust</text>
      </g>
      <g transform="translate(740, 0)">
        <circle cx="5" cy="4" r="3.5" fill="#38BDF8"/>
        <text x="16" y="8" fill="#F8FAFC" font-weight="700">EXPERIENTIAL 3D &amp; WEB</text>
        <text x="16" y="24" fill="#64748B">Next.js 15 · Three.js · GLSL Shaders · Framer Motion</text>
      </g>
    </g>
  </g>

  <!-- Card Border -->
  <rect x=".5" y=".5" width="1199" height="299" rx="15.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 5. SECTION 02: PROOF & RECOGNITION (1200 x 280)
# ─────────────────────────────────────────────────────────────────────────────
def build_achievement_motif_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 280" width="1200" height="280" role="img" aria-label="Proof and Highlights">
  <defs>
    <linearGradient id="rec-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/>
      <stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="rec-glow" cx="85%" cy="30%" r="55%">
      <stop offset="0" stop-color="#8B5CF6" stop-opacity=".18"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>
    <pattern id="rec-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 H 0 V 28" fill="none" stroke="#1E2336" stroke-opacity=".15"/>
    </pattern>
  </defs>
  <style>
    .rec-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .rec-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .rec-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
  </style>

  <rect width="1200" height="280" rx="16" fill="url(#rec-bg)"/>
  <rect width="1200" height="280" rx="16" fill="url(#rec-grid)"/>
  <rect width="1200" height="280" rx="16" fill="url(#rec-glow)"/>

  <!-- 4 Verified Metrics Cards -->
  <g transform="translate(48, 40)">
    <!-- Card 1 -->
    <g transform="translate(0, 0)">
      <rect width="258" height="198" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="258" y2="0" stroke="#A855F7" stroke-width="2.5"/>
      <text class="rec-mono" x="20" y="34" font-size="11" letter-spacing="1.5" fill="#A855F7">TELEMETRY // RECORD</text>
      <text class="rec-serif" x="20" y="88" font-size="44" font-weight="300" fill="#F8FAFC">50+</text>
      <text class="rec-sans" x="20" y="118" font-size="15" font-weight="600" fill="#E2E8F0">Repositories Shipped</text>
      <text class="rec-mono" x="20" y="146" font-size="10.5" fill="#64748B">Web platforms, AI tools, 3D engines &amp; desktop assistants</text>
    </g>

    <!-- Card 2 -->
    <g transform="translate(282, 0)">
      <rect width="258" height="198" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="258" y2="0" stroke="#6366F1" stroke-width="2.5"/>
      <text class="rec-mono" x="20" y="34" font-size="11" letter-spacing="1.5" fill="#818CF8">🏆 HACKATHON // FLAGSHIP</text>
      <text class="rec-serif" x="20" y="88" font-size="36" font-weight="300" fill="#F8FAFC">IBM Bob</text>
      <text class="rec-sans" x="20" y="118" font-size="15" font-weight="600" fill="#E2E8F0">Pasha DevPilot SDLC</text>
      <text class="rec-mono" x="20" y="146" font-size="10.5" fill="#64748B">7-state autonomous AI software engineer, AST scanner &amp; sandbox</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(564, 0)">
      <rect width="258" height="198" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="258" y2="0" stroke="#38BDF8" stroke-width="2.5"/>
      <text class="rec-mono" x="20" y="34" font-size="11" letter-spacing="1.5" fill="#38BDF8">REAL-TIME // WEBRTC</text>
      <text class="rec-serif" x="20" y="88" font-size="44" font-weight="300" fill="#F8FAFC">&lt; 10ms</text>
      <text class="rec-sans" x="20" y="118" font-size="15" font-weight="600" fill="#E2E8F0">SyncForge Delta Sync</text>
      <text class="rec-mono" x="20" y="146" font-size="10.5" fill="#64748B">Sub-10ms multi-cursor Monaco lock &amp; mesh voice audio</text>
    </g>

    <!-- Card 4 -->
    <g transform="translate(846, 0)">
      <rect width="258" height="198" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="258" y2="0" stroke="#10B981" stroke-width="2.5"/>
      <text class="rec-mono" x="20" y="34" font-size="11" letter-spacing="1.5" fill="#34D399">ON-DEVICE // PRIVACY</text>
      <text class="rec-serif" x="20" y="88" font-size="44" font-weight="300" fill="#F8FAFC">100%</text>
      <text class="rec-sans" x="20" y="118" font-size="15" font-weight="600" fill="#E2E8F0">PrivateDoc Air-Gap</text>
      <text class="rec-mono" x="20" y="146" font-size="10.5" fill="#64748B">Zero cloud telemetry, on-device Llama 3.2 1B via ExecuTorch</text>
    </g>
  </g>

  <!-- Border -->
  <rect x=".5" y=".5" width="1199" height="279" rx="15.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 6. BESPOKE PROJECT CARDS (1200 x 370 each) - OBSIDIAN & AMETHYST / CYAN
# ─────────────────────────────────────────────────────────────────────────────

def build_project_devpilot_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="pdp-t">
  <title id="pdp-t">Pasha DevPilot: Autonomous AI Software Engineer built for IBM Bob 2.0 Hackathon</title>
  <defs>
    <linearGradient id="pdp-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="pdp-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#8B5CF6" stop-opacity=".25"/><stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>
    <pattern id="pdp-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#1E2336" stroke-opacity=".12"/>
    </pattern>
    <filter id="pdp-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="pdp-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="pdp-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".45" stop-color="#A855F7"/><stop offset="1" stop-color="#6366F1" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .pdp-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .pdp-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .pdp-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .pdp-in { animation: pdp-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .pdp-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: pdp-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes pdp-in { from { opacity: 0; } to { opacity: 1; } }
    @keyframes pdp-draw { to { stroke-dashoffset: 0; } }
    .pdp-trace { stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: pdp-trace 7s linear infinite; }
    @keyframes pdp-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .pdp-in { animation: none; } .pdp-draw { animation: none; } .pdp-trace { display: none; } }
  </style>

  <g clip-path="url(#pdp-clip)">
    <rect width="1200" height="370" fill="url(#pdp-bg)"/>
    <rect x="700" width="500" height="370" fill="url(#pdp-grid)"/>
    <rect width="1200" height="370" fill="url(#pdp-glow)"/>

    <!-- Left Details -->
    <g class="pdp-in" transform="translate(56, 48)">
      <text class="pdp-mono" font-size="12" letter-spacing="2.6" fill="#A855F7">🏆 HACKATHON FLAGSHIP · AUTONOMOUS SDLC · 2026</text>
      <text class="pdp-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">Pasha DevPilot</text>
      <text class="pdp-sans" y="94" font-size="16.5" fill="#94A3B8">Your autonomous AI software engineer — Understand, Plan, Build, Verify, Ship.</text>
      <text class="pdp-mono" y="126" font-size="12" fill="#E2E8F0"><tspan fill="#A855F7">BUILT ›</tspan> 7-state automated SDLC pipeline, AST defect scanner, pytest auto-healing, IBM Bob 2.0</text>
      <line class="pdp-draw" x1="0" y1="148" x2="620" y2="148" stroke="#8B5CF6" stroke-opacity=".35"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="pdp-serif" font-size="32" font-weight="300" fill="#F8FAFC">7 States</text>
        <text class="pdp-sans" y="22" font-size="12" fill="#94A3B8">Autonomous Pipeline</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="pdp-serif" font-size="32" font-weight="300" fill="#F8FAFC">11/11</text>
        <text class="pdp-sans" y="22" font-size="12" fill="#94A3B8">Pytest Auto-Healed</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="pdp-serif" font-size="32" font-weight="300" fill="#34D399">IBM Bob</text>
        <text class="pdp-sans" y="22" font-size="12" fill="#94A3B8">Hackathon Entry Live</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="90" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pdp-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Next.js 15</text></g>
        <g transform="translate(98, 0)"><rect width="70" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pdp-mono" x="35" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">FastAPI</text></g>
        <g transform="translate(176, 0)"><rect width="90" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pdp-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">IBM Bob 2.0</text></g>
        <g transform="translate(274, 0)"><rect width="80" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pdp-mono" x="40" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Python</text></g>
        <g transform="translate(362, 0)"><rect width="68" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pdp-mono" x="34" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Docker</text></g>
        <g transform="translate(438, 0)"><rect width="74" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pdp-mono" x="37" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Railway</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: 7-State SDLC Autonomous Agent Pipeline -->
    <g transform="translate(740, 60)" class="pdp-in">
      <rect width="390" height="240" rx="12" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <rect width="390" height="34" rx="12" fill="#121624"/>
      <text class="pdp-mono" x="20" y="21" font-size="11" fill="#E2E8F0">AUTONOMOUS SDLC // 7-STATE ENGINE</text>
      <text class="pdp-mono" x="370" y="21" text-anchor="end" font-size="10" fill="#10B981">● SHIPPED</text>

      <!-- Pipeline Steps Row 1 -->
      <g transform="translate(20, 52)">
        <g transform="translate(0, 0)">
          <rect width="76" height="50" rx="6" fill="#151A2B" stroke="#38BDF8" stroke-width="1.2"/>
          <text class="pdp-mono" x="38" y="22" text-anchor="middle" font-size="10" fill="#38BDF8">01 SCAN</text>
          <text class="pdp-mono" x="38" y="38" text-anchor="middle" font-size="8.5" fill="#94A3B8">AST Tree</text>
        </g>
        <line x1="76" y1="25" x2="92" y2="25" stroke="#38BDF8" stroke-width="1.5"/>

        <g transform="translate(92, 0)">
          <rect width="76" height="50" rx="6" fill="#151A2B" stroke="#8B5CF6" stroke-width="1.2"/>
          <text class="pdp-mono" x="38" y="22" text-anchor="middle" font-size="10" fill="#E2E8F0">02 REASON</text>
          <text class="pdp-mono" x="38" y="38" text-anchor="middle" font-size="8.5" fill="#A855F7">IBM Bob</text>
        </g>
        <line x1="168" y1="25" x2="184" y2="25" stroke="#8B5CF6" stroke-width="1.5"/>

        <g transform="translate(184, 0)">
          <rect width="76" height="50" rx="6" fill="#151A2B" stroke="#6366F1" stroke-width="1.2"/>
          <text class="pdp-mono" x="38" y="22" text-anchor="middle" font-size="10" fill="#E2E8F0">03 PLAN</text>
          <text class="pdp-mono" x="38" y="38" text-anchor="middle" font-size="8.5" fill="#94A3B8">Patch Graph</text>
        </g>
        <line x1="260" y1="25" x2="276" y2="25" stroke="#6366F1" stroke-width="1.5"/>

        <g transform="translate(276, 0)">
          <rect width="74" height="50" rx="6" fill="#151A2B" stroke="#10B981" stroke-width="1.2"/>
          <text class="pdp-mono" x="37" y="22" text-anchor="middle" font-size="10" fill="#10B981">04 BUILD</text>
          <text class="pdp-mono" x="37" y="38" text-anchor="middle" font-size="8.5" fill="#34D399">Auto-Code</text>
        </g>
      </g>

      <!-- Pipeline Steps Row 2 -->
      <g transform="translate(20, 114)">
        <g transform="translate(0, 0)">
          <rect width="90" height="42" rx="6" fill="#151A2B" stroke="#1E2336"/>
          <text class="pdp-mono" x="45" y="19" text-anchor="middle" font-size="9.5" fill="#94A3B8">05 SANDBOX</text>
          <text class="pdp-mono" x="45" y="32" text-anchor="middle" font-size="8" fill="#64748B">Isolated Exec</text>
        </g>
        <line x1="90" y1="21" x2="104" y2="21" stroke="#252B42" stroke-width="1.5"/>

        <g transform="translate(104, 0)">
          <rect width="94" height="42" rx="6" fill="#151A2B" stroke="#10B981" stroke-width="1.2"/>
          <text class="pdp-mono" x="47" y="19" text-anchor="middle" font-size="9.5" fill="#10B981">06 VERIFY</text>
          <text class="pdp-mono" x="47" y="32" text-anchor="middle" font-size="8" fill="#34D399">11/11 Passed</text>
        </g>
        <line x1="198" y1="21" x2="212" y2="21" stroke="#10B981" stroke-width="1.5"/>

        <g transform="translate(212, 0)">
          <rect width="138" height="42" rx="6" fill="#151A2B" stroke="#A855F7" stroke-width="1.2"/>
          <text class="pdp-mono" x="69" y="19" text-anchor="middle" font-size="9.5" fill="#A855F7">07 SHIP</text>
          <text class="pdp-mono" x="69" y="32" text-anchor="middle" font-size="8" fill="#F8FAFC">1-Click Push</text>
        </g>
      </g>

      <!-- Verification Badge -->
      <g transform="translate(20, 170)">
        <rect width="350" height="38" rx="6" fill="#121624" stroke="#252B42"/>
        <text class="pdp-mono" x="14" y="16" font-size="9" fill="#94A3B8">DEFECTS RESOLVED &amp; VERIFIED</text>
        <text class="pdp-mono" x="14" y="29" font-size="8.5" fill="#34D399">✓ 9 AST defects resolved · Zero-PAT OAuth · Production Live</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
    <rect class="pdp-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#pdp-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_syncforge_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="psf-t">
  <title id="psf-t">SyncForge: Real-Time Multi-Cursor Collaborative Code Editor and Mesh Voice Studio</title>
  <defs>
    <linearGradient id="psf-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="psf-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#6366F1" stop-opacity=".25"/><stop offset="100%" stop-color="#6366F1" stop-opacity="0"/>
    </radialGradient>
    <pattern id="psf-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#1E2336" stroke-opacity=".12"/>
    </pattern>
    <filter id="psf-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="psf-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="psf-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".45" stop-color="#6366F1"/><stop offset="1" stop-color="#38BDF8" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .psf-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .psf-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .psf-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .psf-in { animation: psf-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .psf-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: psf-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes psf-in { from { opacity: 0; } to { opacity: 1; } }
    @keyframes psf-draw { to { stroke-dashoffset: 0; } }
    .psf-trace { stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: psf-trace 7s linear infinite; }
    @keyframes psf-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .psf-in { animation: none; } .psf-draw { animation: none; } .psf-trace { display: none; } }
  </style>

  <g clip-path="url(#psf-clip)">
    <rect width="1200" height="370" fill="url(#psf-bg)"/>
    <rect x="700" width="500" height="370" fill="url(#psf-grid)"/>
    <rect width="1200" height="370" fill="url(#psf-glow)"/>

    <!-- Left Details -->
    <g class="psf-in" transform="translate(56, 48)">
      <text class="psf-mono" font-size="12" letter-spacing="2.6" fill="#6366F1">02 · REAL-TIME DISTRIBUTED SYSTEMS · WEBRTC · 2026</text>
      <text class="psf-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">SyncForge</text>
      <text class="psf-sans" y="94" font-size="16.5" fill="#94A3B8">Real-time multi-cursor collaboration, instant rooms &amp; peer-to-peer voice mesh.</text>
      <text class="psf-mono" y="126" font-size="12" fill="#E2E8F0"><tspan fill="#6366F1">BUILT ›</tspan> Monaco Editor, delta-sync WebSockets, WebRTC mesh audio, FastAPI, React 19</text>
      <line class="psf-draw" x1="0" y1="148" x2="620" y2="148" stroke="#6366F1" stroke-opacity=".35"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="psf-serif" font-size="32" font-weight="300" fill="#F8FAFC">&lt; 10ms</text>
        <text class="psf-sans" y="22" font-size="12" fill="#94A3B8">Delta Sync Latency</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="psf-serif" font-size="32" font-weight="300" fill="#F8FAFC">10+ Langs</text>
        <text class="psf-sans" y="22" font-size="12" fill="#94A3B8">Monaco IntelliSense</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="psf-serif" font-size="32" font-weight="300" fill="#34D399">Mesh Voice</text>
        <text class="psf-sans" y="22" font-size="12" fill="#94A3B8">WebRTC P2P Audio</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="84" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="psf-mono" x="42" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">React 19</text></g>
        <g transform="translate(92, 0)"><rect width="70" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="psf-mono" x="35" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">Vite 6</text></g>
        <g transform="translate(170, 0)"><rect width="114" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="psf-mono" x="57" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">Monaco Editor</text></g>
        <g transform="translate(292, 0)"><rect width="76" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="psf-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">FastAPI</text></g>
        <g transform="translate(376, 0)"><rect width="98" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="psf-mono" x="49" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">WebSockets</text></g>
        <g transform="translate(482, 0)"><rect width="76" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="psf-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">WebRTC</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Monaco Multi-Cursor & WebRTC Mesh Room -->
    <g transform="translate(740, 60)" class="psf-in">
      <rect width="390" height="240" rx="12" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <rect width="390" height="34" rx="12" fill="#121624"/>
      <text class="psf-mono" x="20" y="21" font-size="11" fill="#E2E8F0">SYNCFORGE // ROOM #SYNC-992</text>
      <text class="psf-mono" x="370" y="21" text-anchor="end" font-size="10" fill="#10B981">● 3 PEERS LIVE</text>

      <!-- Monaco Editor Code View -->
      <g transform="translate(18, 48)">
        <rect width="354" height="136" rx="8" fill="#060810" stroke="#1E2336" stroke-opacity=".6"/>
        <text class="psf-mono" x="14" y="24" font-size="9.5" fill="#64748B">01  <tspan fill="#818CF8">// Broadcast AST delta with sub-10ms lock</tspan></text>
        <text class="psf-mono" x="14" y="44" font-size="9.5" fill="#64748B">02  <tspan fill="#38BDF8">export async function</tspan> <tspan fill="#F8FAFC">syncCode</tspan>(delta: <tspan fill="#34D399">Delta</tspan>) {</text>
        <text class="psf-mono" x="14" y="64" font-size="9.5" fill="#64748B">03    <tspan fill="#38BDF8">await</tspan> ws.<tspan fill="#F8FAFC">broadcast</tspan>(<tspan fill="#34D399">"code-change"</tspan>, delta);</text>
        <text class="psf-mono" x="14" y="84" font-size="9.5" fill="#64748B">04    webrtc.<tspan fill="#F8FAFC">relayVoiceMesh</tspan>(room.peers);</text>
        <text class="psf-mono" x="14" y="104" font-size="9.5" fill="#64748B">05  }</text>

        <!-- Pasha Cursor Tag -->
        <g transform="translate(230, 52)">
          <line x1="0" y1="0" x2="0" y2="16" stroke="#38BDF8" stroke-width="2"/>
          <rect x="0" y="-12" width="54" height="14" rx="3" fill="#0284C7"/>
          <text class="psf-mono" x="27" y="-2" text-anchor="middle" font-size="8.5" fill="#FFFFFF">Pasha</text>
        </g>

        <!-- Peer Cursor Tag -->
        <g transform="translate(196, 72)">
          <line x1="0" y1="0" x2="0" y2="16" stroke="#34D399" stroke-width="2"/>
          <rect x="0" y="-12" width="46" height="14" rx="3" fill="#059669"/>
          <text class="psf-mono" x="23" y="-2" text-anchor="middle" font-size="8.5" fill="#FFFFFF">Peer #2</text>
        </g>
      </g>

      <!-- Bottom Status Pill -->
      <g transform="translate(18, 196)">
        <rect width="354" height="32" rx="6" fill="#121624" stroke="#1E2336"/>
        <text class="psf-mono" x="14" y="20" font-size="9.5" fill="#94A3B8">WS: <tspan fill="#38BDF8">DELTA SYNC</tspan> · AUDIO: <tspan fill="#34D399">WEBRTC MESH</tspan> · LATENCY: <tspan fill="#10B981">8ms</tspan></text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
    <rect class="psf-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#psf-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_privatedoc_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="ppd-t">
  <title id="ppd-t">PrivateDoc: On-Device Private AI Document Intelligence with Local Llama 3.2</title>
  <defs>
    <linearGradient id="ppd-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="ppd-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#10B981" stop-opacity=".22"/><stop offset="100%" stop-color="#10B981" stop-opacity="0"/>
    </radialGradient>
    <pattern id="ppd-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#1E2336" stroke-opacity=".12"/>
    </pattern>
    <filter id="ppd-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="ppd-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="ppd-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".45" stop-color="#10B981"/><stop offset="1" stop-color="#A855F7" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .ppd-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .ppd-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .ppd-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .ppd-in { animation: ppd-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .ppd-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: ppd-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes ppd-in { from { opacity: 0; } to { opacity: 1; } }
    @keyframes ppd-draw { to { stroke-dashoffset: 0; } }
    .ppd-trace { stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: ppd-trace 7s linear infinite; }
    @keyframes ppd-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .ppd-in { animation: none; } .ppd-draw { animation: none; } .ppd-trace { display: none; } }
  </style>

  <g clip-path="url(#ppd-clip)">
    <rect width="1200" height="370" fill="url(#ppd-bg)"/>
    <rect x="700" width="500" height="370" fill="url(#ppd-grid)"/>
    <rect width="1200" height="370" fill="url(#ppd-glow)"/>

    <!-- Left Details -->
    <g class="ppd-in" transform="translate(56, 48)">
      <text class="ppd-mono" font-size="12" letter-spacing="2.6" fill="#10B981">03 · ON-DEVICE EDGE AI · ZERO CLOUD LEAK · 2026</text>
      <text class="ppd-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">PrivateDoc</text>
      <text class="ppd-sans" y="94" font-size="16.5" fill="#94A3B8">Your family's offline document AI — zero cloud telemetry, 100% on-device SLM.</text>
      <text class="ppd-mono" y="126" font-size="12" fill="#E2E8F0"><tspan fill="#10B981">BUILT ›</tspan> Android 36, ExecuTorch 1.3, Llama 3.2 1B (SpinQuant INT4), ML Kit OCR, Compose</text>
      <line class="ppd-draw" x1="0" y1="148" x2="620" y2="148" stroke="#10B981" stroke-opacity=".35"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="ppd-serif" font-size="32" font-weight="300" fill="#34D399">0 KB</text>
        <text class="ppd-sans" y="22" font-size="12" fill="#94A3B8">Cloud Telemetry Leak</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="ppd-serif" font-size="32" font-weight="300" fill="#F8FAFC">Llama 3.2</text>
        <text class="ppd-sans" y="22" font-size="12" fill="#94A3B8">1B INT4 On-Device</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="ppd-serif" font-size="32" font-weight="300" fill="#F8FAFC">100% Offline</text>
        <text class="ppd-sans" y="22" font-size="12" fill="#94A3B8">Zero Network Permission</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="90" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="ppd-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#34D399">Android 36</text></g>
        <g transform="translate(98, 0)"><rect width="80" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="ppd-mono" x="40" y="17" text-anchor="middle" font-size="11.5" fill="#34D399">Kotlin 2.3</text></g>
        <g transform="translate(186, 0)"><rect width="102" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="ppd-mono" x="51" y="17" text-anchor="middle" font-size="11.5" fill="#34D399">ExecuTorch 1.3</text></g>
        <g transform="translate(296, 0)"><rect width="128" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="ppd-mono" x="64" y="17" text-anchor="middle" font-size="11.5" fill="#34D399">Llama 3.2 (INT4)</text></g>
        <g transform="translate(432, 0)"><rect width="90" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="ppd-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#34D399">ML Kit OCR</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Local On-Device Inference HUD -->
    <g transform="translate(740, 60)" class="ppd-in">
      <rect width="390" height="240" rx="12" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <rect width="390" height="34" rx="12" fill="#121624"/>
      <text class="ppd-mono" x="20" y="21" font-size="11" fill="#E2E8F0">PRIVATEDOC // LOCAL SLM INFERENCE</text>
      <text class="ppd-mono" x="370" y="21" text-anchor="end" font-size="10" fill="#10B981">🛡️ AIR-GAPPED</text>

      <!-- Scan & Inference Container -->
      <g transform="translate(18, 48)">
        <rect width="354" height="136" rx="8" fill="#060810" stroke="#1E2336" stroke-opacity=".6"/>
        <text class="ppd-mono" x="14" y="24" font-size="9.5" fill="#64748B">SCAN › <tspan fill="#38BDF8">Prescription_Rx08.pdf</tspan> · <tspan fill="#34D399">OCR 99.4%</tspan></text>
        <line x1="14" y1="34" x2="340" y2="34" stroke="#1E2336" stroke-opacity=".5"/>
        <text class="ppd-mono" x="14" y="54" font-size="9.5" fill="#94A3B8">USER: <tspan fill="#F8FAFC">"What is the daily dosage for Amoxicillin?"</tspan></text>
        
        <!-- SLM Response Box -->
        <rect x="14" y="68" width="326" height="52" rx="6" fill="#101824" stroke="#10B981" stroke-width="1"/>
        <text class="ppd-mono" x="24" y="88" font-size="9.5" fill="#A855F7">EXECUTORCH (LLAMA 3.2 1B INT4):</text>
        <text class="ppd-mono" x="24" y="106" font-size="9.5" fill="#34D399">✓ "Take 500mg every 8 hours with water after meals."</text>
      </g>

      <!-- Bottom Status Pill -->
      <g transform="translate(18, 196)">
        <rect width="354" height="32" rx="6" fill="#121624" stroke="#1E2336"/>
        <text class="ppd-mono" x="14" y="20" font-size="9.5" fill="#94A3B8">NETWORK: <tspan fill="#10B981">DISABLED</tspan> · ON-DEVICE: <tspan fill="#38BDF8">140ms</tspan> · DATA EXPORT: <tspan fill="#10B981">0 BYTES</tspan></text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
    <rect class="ppd-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#ppd-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_ghostreview_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="pgr-t">
  <title id="pgr-t">GhostReview: AI-Powered Code Intelligence and Autonomous PR Review Engine</title>
  <defs>
    <linearGradient id="pgr-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="pgr-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#A855F7" stop-opacity=".25"/><stop offset="100%" stop-color="#A855F7" stop-opacity="0"/>
    </radialGradient>
    <pattern id="pgr-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#1E2336" stroke-opacity=".12"/>
    </pattern>
    <filter id="pgr-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="pgr-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="pgr-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".45" stop-color="#A855F7"/><stop offset="1" stop-color="#6366F1" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .pgr-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .pgr-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .pgr-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .pgr-in { animation: pgr-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .pgr-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: pgr-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes pgr-in { from { opacity: 0; } to { opacity: 1; } }
    @keyframes pgr-draw { to { stroke-dashoffset: 0; } }
    .pgr-trace { stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: pgr-trace 7s linear infinite; }
    @keyframes pgr-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .pgr-in { animation: none; } .pgr-draw { animation: none; } .pgr-trace { display: none; } }
  </style>

  <g clip-path="url(#pgr-clip)">
    <rect width="1200" height="370" fill="url(#pgr-bg)"/>
    <rect x="700" width="500" height="370" fill="url(#pgr-grid)"/>
    <rect width="1200" height="370" fill="url(#pgr-glow)"/>

    <!-- Left Details -->
    <g class="pgr-in" transform="translate(56, 48)">
      <text class="pgr-mono" font-size="12" letter-spacing="2.6" fill="#A855F7">04 · REPOSITORY AUDITING · GROQ LLM INFERENCE · 2026</text>
      <text class="pgr-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">GhostReview</text>
      <text class="pgr-sans" y="94" font-size="16.5" fill="#94A3B8">AI-powered code intelligence — automated bug hunting, PR reviews &amp; doc generation.</text>
      <text class="pgr-mono" y="126" font-size="12" fill="#E2E8F0"><tspan fill="#A855F7">BUILT ›</tspan> React 19, FastAPI, Groq LLM sub-second reasoning, Celery, Redis, Vite 8</text>
      <line class="pgr-draw" x1="0" y1="148" x2="620" y2="148" stroke="#8B5CF6" stroke-opacity=".35"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="pgr-serif" font-size="32" font-weight="300" fill="#34D399">24 / 24</text>
        <text class="pgr-sans" y="22" font-size="12" fill="#94A3B8">Pytest Tests Passed</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="pgr-serif" font-size="32" font-weight="300" fill="#F8FAFC">&lt; 300ms</text>
        <text class="pgr-sans" y="22" font-size="12" fill="#94A3B8">Groq LLM Latency</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="pgr-serif" font-size="32" font-weight="300" fill="#F8FAFC">0 Errors</text>
        <text class="pgr-sans" y="22" font-size="12" fill="#94A3B8">TypeScript &amp; ESLint</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="84" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pgr-mono" x="42" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">React 19</text></g>
        <g transform="translate(92, 0)"><rect width="76" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pgr-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">FastAPI</text></g>
        <g transform="translate(176, 0)"><rect width="88" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pgr-mono" x="44" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Groq LLM</text></g>
        <g transform="translate(272, 0)"><rect width="74" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pdp-mono" x="37" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Celery</text></g>
        <g transform="translate(354, 0)"><rect width="68" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pgr-mono" x="34" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Redis</text></g>
        <g transform="translate(430, 0)"><rect width="88" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="pgr-mono" x="44" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Tailwind 4</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Repository Audit Console -->
    <g transform="translate(740, 60)" class="pgr-in">
      <rect width="390" height="240" rx="12" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <rect width="390" height="34" rx="12" fill="#121624"/>
      <text class="pgr-mono" x="20" y="21" font-size="11" fill="#E2E8F0">GHOSTREVIEW // REPO AUDIT CONSOLE</text>
      <text class="pgr-mono" x="370" y="21" text-anchor="end" font-size="10" fill="#10B981">⚡ GROQ LPU</text>

      <!-- Terminal View -->
      <g transform="translate(18, 48)">
        <rect width="354" height="136" rx="8" fill="#060810" stroke="#1E2336" stroke-opacity=".6"/>
        <text class="pgr-mono" x="14" y="24" font-size="9.5" fill="#64748B">&gt; ghost review --repo pasha804/auth-service</text>
        <text class="pgr-mono" x="14" y="44" font-size="9.5" fill="#38BDF8">[+] AST Analysis: 1,420 lines parsed</text>
        <text class="pgr-mono" x="14" y="64" font-size="9.5" fill="#EF4444">[!] Bug detected (L42): Unhandled null pointer in token refresh</text>
        <text class="pgr-mono" x="14" y="84" font-size="9.5" fill="#34D399">[✓] Auto-patch generated via Groq LLM (240ms)</text>
        <text class="pgr-mono" x="14" y="104" font-size="9.5" fill="#818CF8">[✓] PR summary &amp; architectural impact compiled</text>
      </g>

      <!-- Bottom Status Pill -->
      <g transform="translate(18, 196)">
        <rect width="354" height="32" rx="6" fill="#121624" stroke="#1E2336"/>
        <text class="pgr-mono" x="14" y="20" font-size="9.5" fill="#94A3B8">TESTS: <tspan fill="#34D399">24/24 PASS</tspan> · LATENCY: <tspan fill="#38BDF8">240ms</tspan> · STATUS: <tspan fill="#10B981">READY TO MERGE</tspan></text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
    <rect class="pgr-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#pgr-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_opencluely_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p2-t">
  <title id="p2-t">OpenCluely: Undetectable desktop AI assistant for technical interviews and algorithmic mastery</title>
  <defs>
    <linearGradient id="p2-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="p2-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#38BDF8" stop-opacity=".22"/><stop offset="100%" stop-color="#38BDF8" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p2-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#1E2336" stroke-opacity=".12"/>
    </pattern>
    <filter id="p2-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="p2-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="p2-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#6366F1" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .p2-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .p2-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .p2-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .p2-in { animation: p2-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .p2-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: p2-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes p2-in { from { opacity: 0; } to { opacity: 1; } }
    @keyframes p2-draw { to { stroke-dashoffset: 0; } }
    .p2-trace { stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: p2-trace 7s linear infinite; }
    @keyframes p2-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .p2-in { animation: none; } .p2-draw { animation: none; } .p2-trace { display: none; } }
  </style>

  <g clip-path="url(#p2-clip)">
    <rect width="1200" height="370" fill="url(#p2-bg)"/>
    <rect x="700" width="500" height="370" fill="url(#p2-grid)"/>
    <rect width="1200" height="370" fill="url(#p2-glow)"/>

    <!-- Left Details -->
    <g class="p2-in" transform="translate(56, 48)">
      <text class="p2-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">05 · DESKTOP AI · STEALTH OCR · 2026</text>
      <text class="p2-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">OpenCluely</text>
      <text class="p2-sans" y="94" font-size="16.5" fill="#94A3B8">Undetectable frameless desktop AI overlay for technical interviews.</text>
      <text class="p2-mono" y="126" font-size="12" fill="#E2E8F0"><tspan fill="#38BDF8">BUILT ›</tspan> Transparent Tauri canvas, Vision OCR stream, Whisper audio, Gemini AI</text>
      <line class="p2-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".35"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="p2-serif" font-size="32" font-weight="300" fill="#F8FAFC">0-Footprint</text>
        <text class="p2-sans" y="22" font-size="12" fill="#94A3B8">Invisible Screen Capture</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="p2-serif" font-size="32" font-weight="300" fill="#F8FAFC">O(N)</text>
        <text class="p2-sans" y="22" font-size="12" fill="#94A3B8">Optimal Proof Engine</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="p2-serif" font-size="32" font-weight="300" fill="#34D399">MIT</text>
        <text class="p2-sans" y="22" font-size="12" fill="#94A3B8">Open Source Codebase</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="90" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p2-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Tauri (Rust)</text></g>
        <g transform="translate(98, 0)"><rect width="90" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p2-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">TypeScript</text></g>
        <g transform="translate(196, 0)"><rect width="84" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p2-mono" x="42" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Gemini AI</text></g>
        <g transform="translate(288, 0)"><rect width="88" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p2-mono" x="44" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Vision OCR</text></g>
        <g transform="translate(384, 0)"><rect width="76" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p2-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Whisper</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Stealth HUD & OCR Scan Beam -->
    <g transform="translate(740, 60)" class="p2-in">
      <rect width="390" height="240" rx="12" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <rect width="390" height="34" rx="12" fill="#121624"/>
      <text class="p2-mono" x="20" y="22" font-size="11" fill="#38BDF8">STEALTH_OVERLAY // INVISIBLE HUD</text>
      <text class="p2-mono" x="370" y="22" text-anchor="end" font-size="10" fill="#10B981">● ACTIVE</text>

      <!-- Screen Scanner Visualizer -->
      <rect x="24" y="52" width="342" height="110" rx="6" fill="#060810" stroke="#1E2336" stroke-opacity=".6"/>
      <!-- Scanning Line Animation -->
      <line x1="24" y1="75" x2="366" y2="75" stroke="#38BDF8" stroke-width="1.8" filter="url(#p2-glowf)">
        <animate attributeName="y1" values="55;155;55" dur="4s" repeatCount="indefinite"/>
        <animate attributeName="y2" values="55;155;55" dur="4s" repeatCount="indefinite"/>
      </line>
      <text class="p2-mono" x="36" y="74" font-size="10" fill="#64748B">int maxSubArray(vector&lt;int&gt;&amp; nums) {</text>
      <text class="p2-mono" x="56" y="94" font-size="10" fill="#38BDF8">int cur = 0, best = INT_MIN;</text>
      <text class="p2-mono" x="56" y="114" font-size="10" fill="#818CF8">for(int x : nums) { cur = max(x, cur+x); ... }</text>
      <text class="p2-mono" x="36" y="134" font-size="10" fill="#64748B">}</text>

      <!-- Proof Pill -->
      <g transform="translate(24, 176)">
        <rect width="342" height="46" rx="8" fill="#121624" stroke="#1E2336"/>
        <text class="p2-mono" x="16" y="20" font-size="10.5" fill="#F8FAFC">ALGORITHMIC PROOF: Kadane's Dynamic DP</text>
        <text class="p2-mono" x="16" y="36" font-size="9.5" fill="#34D399">✓ Time: O(N) · Space: O(1) · Optimal Verification Passed</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
    <rect class="p2-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#p2-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_bmw7_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p4-t">
  <title id="p4-t">BMW 7-Series 3D Experience: Photorealistic 3D automotive configurator</title>
  <defs>
    <linearGradient id="p4-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="p4-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#6366F1" stop-opacity=".22"/><stop offset="100%" stop-color="#6366F1" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p4-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#1E2336" stroke-opacity=".12"/>
    </pattern>
    <clipPath id="p4-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="p4-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".45" stop-color="#818CF8"/><stop offset="1" stop-color="#6366F1" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .p4-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .p4-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .p4-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .p4-in { animation: p4-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .p4-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: p4-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes p4-in { from { opacity: 0; } to { opacity: 1; } }
    @keyframes p4-draw { to { stroke-dashoffset: 0; } }
    .p4-trace { stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: p4-trace 7s linear infinite; }
    @keyframes p4-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .p4-in { animation: none; } .p4-draw { animation: none; } .p4-trace { display: none; } }
  </style>

  <g clip-path="url(#p4-clip)">
    <rect width="1200" height="370" fill="url(#p4-bg)"/>
    <rect x="700" width="500" height="370" fill="url(#p4-grid)"/>
    <rect width="1200" height="370" fill="url(#p4-glow)"/>

    <!-- Left Details -->
    <g class="p4-in" transform="translate(56, 48)">
      <text class="p4-mono" font-size="12" letter-spacing="2.6" fill="#818CF8">06 · EXPERIENTIAL GRAPHICS · 3D WEBGL · 2026</text>
      <text class="p4-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">BMW 7-Series 3D</text>
      <text class="p4-sans" y="94" font-size="16.5" fill="#94A3B8">Photorealistic 3D automotive configurator engineered with custom GLSL shaders.</text>
      <text class="p4-mono" y="126" font-size="12" fill="#E2E8F0"><tspan fill="#818CF8">BUILT ›</tspan> Three.js, WebGL raymarching, Draco compression, React, TypeScript</text>
      <line class="p4-draw" x1="0" y1="148" x2="620" y2="148" stroke="#818CF8" stroke-opacity=".35"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="p4-serif" font-size="32" font-weight="300" fill="#F8FAFC">60 FPS</text>
        <text class="p4-sans" y="22" font-size="12" fill="#94A3B8">Hardware Render Speed</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="p4-serif" font-size="32" font-weight="300" fill="#F8FAFC">Draco GLTF</text>
        <text class="p4-sans" y="22" font-size="12" fill="#94A3B8">Compressed Geometry</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="p4-serif" font-size="32" font-weight="300" fill="#34D399">Custom GLSL</text>
        <text class="p4-sans" y="22" font-size="12" fill="#94A3B8">Metallic Clear-Coat</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="84" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p4-mono" x="42" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">Three.js</text></g>
        <g transform="translate(92, 0)"><rect width="76" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p4-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">WebGL</text></g>
        <g transform="translate(176, 0)"><rect width="102" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p4-mono" x="51" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">GLSL Shaders</text></g>
        <g transform="translate(286, 0)"><rect width="76" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p4-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">React</text></g>
        <g transform="translate(370, 0)"><rect width="90" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p4-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#818CF8">TypeScript</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: 3D Wireframe Viewport & Shader Telemetry -->
    <g transform="translate(740, 60)" class="p4-in">
      <rect width="390" height="240" rx="12" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <rect width="390" height="34" rx="12" fill="#121624"/>
      <text class="p4-mono" x="20" y="21" font-size="11" fill="#E2E8F0">GLSL_VIEWPORT // RAYMARCHING ENGINE</text>
      <text class="p4-mono" x="370" y="21" text-anchor="end" font-size="10" fill="#10B981">● 60 FPS</text>

      <!-- 3D Car Wireframe Grid Representation -->
      <g transform="translate(20, 52)">
        <rect width="350" height="114" rx="6" fill="#060810" stroke="#1E2336" stroke-opacity=".6"/>
        <!-- Perspective Grid -->
        <line x1="20" y1="90" x2="330" y2="90" stroke="#1E2336"/>
        <line x1="40" y1="104" x2="310" y2="104" stroke="#1E2336"/>
        <line x1="175" y1="20" x2="50" y2="114" stroke="#1E2336" stroke-opacity=".4"/>
        <line x1="175" y1="20" x2="300" y2="114" stroke="#1E2336" stroke-opacity=".4"/>

        <!-- Car Silhouette Path -->
        <path d="M 60 82 C 90 82, 110 56, 150 54 C 180 52, 220 54, 250 64 C 275 72, 290 82, 305 82 L 310 90 L 50 90 Z" fill="#151A2B" stroke="#6366F1" stroke-width="1.8"/>
        <!-- Wheels -->
        <circle cx="100" cy="88" r="14" fill="#0D101A" stroke="#38BDF8" stroke-width="2"/>
        <circle cx="265" cy="88" r="14" fill="#0D101A" stroke="#38BDF8" stroke-width="2"/>
        <!-- Headlight Beam -->
        <polygon points="310,80 345,70 345,95 310,88" fill="#38BDF8" fill-opacity=".25"/>
      </g>

      <!-- Shader Stats -->
      <g transform="translate(20, 180)">
        <rect width="350" height="38" rx="6" fill="#121624" stroke="#1E2336"/>
        <text class="p4-mono" x="14" y="16" font-size="9" fill="#94A3B8">METALLIC_CLEARCOAT.FRAG // COMPILED</text>
        <text class="p4-mono" x="14" y="29" font-size="8.5" fill="#34D399">Roughness: 0.12 · Transmission: 0.94 · IOR: 1.52 · Samples: 64</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
    <rect class="p4-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#p4-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_nexora_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p1-t">
  <title id="p1-t">Nexora: AI-powered skill social platform with live coding challenges &amp; autonomous referee</title>
  <defs>
    <linearGradient id="p1-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="p1-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#A855F7" stop-opacity=".22"/><stop offset="100%" stop-color="#A855F7" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p1-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#1E2336" stroke-opacity=".12"/>
    </pattern>
    <clipPath id="p1-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="p1-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".45" stop-color="#A855F7"/><stop offset="1" stop-color="#38BDF8" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .p1-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .p1-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .p1-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .p1-in { animation: p1-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .p1-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: p1-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes p1-in { from { opacity: 0; } to { opacity: 1; } }
    @keyframes p1-draw { to { stroke-dashoffset: 0; } }
    .p1-trace { stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: p1-trace 7s linear infinite; }
    @keyframes p1-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .p1-in { animation: none; } .p1-draw { stroke-dashoffset: 0; } .p1-trace { display: none; } }
  </style>

  <g clip-path="url(#p1-clip)">
    <rect width="1200" height="370" fill="url(#p1-bg)"/>
    <rect x="700" width="500" height="370" fill="url(#p1-grid)"/>
    <rect width="1200" height="370" fill="url(#p1-glow)"/>

    <!-- Left Details -->
    <g class="p1-in" transform="translate(56, 48)">
      <text class="p1-mono" font-size="12" letter-spacing="2.6" fill="#A855F7">07 · COMPETITIVE ARENA · DISTRIBUTED ENGINE · 2026</text>
      <text class="p1-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">NEXORA</text>
      <text class="p1-sans" y="94" font-size="16.5" fill="#94A3B8">Gamified social identity, guild communities, and peer coding battles.</text>
      <text class="p1-mono" y="126" font-size="12" fill="#E2E8F0"><tspan fill="#A855F7">BUILT ›</tspan> Autonomous AI Referee, real-time code evaluation, Redis queuing, FastAPI</text>
      <line class="p1-draw" x1="0" y1="148" x2="620" y2="148" stroke="#A855F7" stroke-opacity=".35"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="p1-serif" font-size="32" font-weight="300" fill="#F8FAFC">100%</text>
        <text class="p1-sans" y="22" font-size="12" fill="#94A3B8">Autonomous AI Referee</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="p1-serif" font-size="32" font-weight="300" fill="#F8FAFC">Sub-80ms</text>
        <text class="p1-sans" y="22" font-size="12" fill="#94A3B8">Judging Latency</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="p1-serif" font-size="32" font-weight="300" fill="#34D399">V1.0</text>
        <text class="p1-sans" y="22" font-size="12" fill="#94A3B8">Private Alpha Live</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="68" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p1-mono" x="34" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">React</text></g>
        <g transform="translate(76, 0)"><rect width="90" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p1-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">TypeScript</text></g>
        <g transform="translate(174, 0)"><rect width="76" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p1-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">FastAPI</text></g>
        <g transform="translate(258, 0)"><rect width="92" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p1-mono" x="46" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">PostgreSQL</text></g>
        <g transform="translate(358, 0)"><rect width="68" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p1-mono" x="34" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Redis</text></g>
        <g transform="translate(434, 0)"><rect width="74" height="26" rx="13" fill="#0D101A" stroke="#1E2336"/><text class="p1-mono" x="37" y="17" text-anchor="middle" font-size="11.5" fill="#A855F7">Docker</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Arena Battle Board & AI Referee -->
    <g transform="translate(740, 60)" class="p1-in">
      <rect width="390" height="240" rx="12" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <rect width="390" height="34" rx="12" fill="#121624"/>
      <circle cx="24" cy="17" r="4" fill="#EF4444"/>
      <circle cx="38" cy="17" r="4" fill="#F59E0B"/>
      <circle cx="52" cy="17" r="4" fill="#10B981"/>
      <text class="p1-mono" x="72" y="21" font-size="11" fill="#E2E8F0">NEXORA // LIVE ARENA CODE REF</text>

      <!-- Player 1 & 2 Cards -->
      <g transform="translate(20, 50)">
        <rect width="165" height="100" rx="8" fill="#151A2B" stroke="#252B42"/>
        <text class="p1-mono" x="12" y="20" font-size="9.5" fill="#A855F7">PLAYER_01 (O(N))</text>
        <line x1="12" y1="36" x2="153" y2="36" stroke="#10B981" stroke-width="2.5"/>
        <line x1="12" y1="46" x2="135" y2="46" stroke="#10B981" stroke-width="2.5"/>
        <line x1="12" y1="56" x2="110" y2="56" stroke="#10B981" stroke-width="2.5"/>
        <text class="p1-mono" x="12" y="82" font-size="8.5" fill="#34D399">✓ PASSED 28/28 TESTS</text>
      </g>

      <g transform="translate(205, 50)">
        <rect width="165" height="100" rx="8" fill="#151A2B" stroke="#252B42"/>
        <text class="p1-mono" x="12" y="20" font-size="9.5" fill="#EF4444">PLAYER_02 (O(N²))</text>
        <line x1="12" y1="36" x2="153" y2="36" stroke="#64748B" stroke-width="2.5"/>
        <line x1="12" y1="46" x2="153" y2="46" stroke="#64748B" stroke-width="2.5"/>
        <line x1="12" y1="56" x2="90" y2="56" stroke="#F59E0B" stroke-width="2.5"/>
        <text class="p1-mono" x="12" y="82" font-size="8.5" fill="#F59E0B">⏱ 142ms LATENCY</text>
      </g>

      <!-- Autonomous Referee Verdict Banner -->
      <g transform="translate(20, 162)">
        <rect width="350" height="54" rx="8" fill="#121624" stroke="#A855F7" stroke-width="1.2"/>
        <circle cx="22" cy="27" r="5" fill="#38BDF8"/>
        <text class="p1-mono" x="36" y="24" font-size="10" fill="#F8FAFC" font-weight="700">AI REFEREE: VERDICT DECLARED</text>
        <text class="p1-mono" x="36" y="40" font-size="9" fill="#34D399">P1 WINNER · TIME O(N) · ELO +34</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
    <rect class="p1-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#p1-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 7. SECTION 04: TOOLKIT / TECH CONSTELLATION (1200 x 440)
# ─────────────────────────────────────────────────────────────────────────────
def build_tech_constellation_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="1200" height="440" role="img" aria-label="Tech Stack and Arsenal">
  <defs>
    <linearGradient id="tc-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="tc-glow" cx="50%" cy="50%" r="65%">
      <stop offset="0" stop-color="#8B5CF6" stop-opacity=".18"/><stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>
    <pattern id="tc-grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 H 0 V 30" fill="none" stroke="#1E2336" stroke-opacity=".15"/>
    </pattern>
  </defs>
  <style>
    .tc-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .tc-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .tc-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
  </style>

  <rect width="1200" height="440" rx="16" fill="url(#tc-bg)"/>
  <rect width="1200" height="440" rx="16" fill="url(#tc-grid)"/>
  <rect width="1200" height="440" rx="16" fill="url(#tc-glow)"/>

  <!-- Five Core Categorized Clusters -->
  <g transform="translate(48, 38)">
    <!-- Column 1: Core Languages -->
    <g transform="translate(0, 0)">
      <rect width="210" height="360" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="210" y2="0" stroke="#A855F7" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#A855F7">01 // LANGUAGES</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F8FAFC">Core Foundation</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E2E8F0">
        <text y="0"><tspan fill="#A855F7">▸</tspan> TypeScript</text>
        <text y="30"><tspan fill="#A855F7">▸</tspan> JavaScript (ESNext)</text>
        <text y="60"><tspan fill="#A855F7">▸</tspan> Python (Asyncio)</text>
        <text y="90"><tspan fill="#A855F7">▸</tspan> Rust (Tauri / Core)</text>
        <text y="120"><tspan fill="#A855F7">▸</tspan> Kotlin (Android 36)</text>
        <text y="150"><tspan fill="#A855F7">▸</tspan> SQL (PostgreSQL)</text>
        <text y="180"><tspan fill="#A855F7">▸</tspan> C / C++</text>
        <text y="210"><tspan fill="#A855F7">▸</tspan> GLSL Shaders</text>
      </g>
    </g>

    <!-- Column 2: AI & Machine Learning -->
    <g transform="translate(228, 0)">
      <rect width="210" height="360" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="210" y2="0" stroke="#8B5CF6" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#8B5CF6">02 // AI &amp; ML</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F8FAFC">Intelligence</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E2E8F0">
        <text y="0"><tspan fill="#818CF8">▸</tspan> Autonomous SDLC</text>
        <text y="30"><tspan fill="#818CF8">▸</tspan> IBM Bob 2.0 Engine</text>
        <text y="60"><tspan fill="#818CF8">▸</tspan> ExecuTorch (Edge AI)</text>
        <text y="90"><tspan fill="#818CF8">▸</tspan> Llama 3.2 1B (INT4)</text>
        <text y="120"><tspan fill="#818CF8">▸</tspan> Groq LLM Inference</text>
        <text y="150"><tspan fill="#818CF8">▸</tspan> Google Gemini API</text>
        <text y="180"><tspan fill="#818CF8">▸</tspan> Vision OCR Engines</text>
        <text y="210"><tspan fill="#818CF8">▸</tspan> Whisper Audio STT</text>
      </g>
    </g>

    <!-- Column 3: Frontend & 3D Graphics -->
    <g transform="translate(456, 0)">
      <rect width="210" height="360" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="210" y2="0" stroke="#38BDF8" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#38BDF8">03 // FRONTEND &amp; 3D</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F8FAFC">Experiences</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E2E8F0">
        <text y="0"><tspan fill="#38BDF8">▸</tspan> React 19 / Vite 6</text>
        <text y="30"><tspan fill="#38BDF8">▸</tspan> Next.js 15 (App)</text>
        <text y="60"><tspan fill="#38BDF8">▸</tspan> Monaco Code Editor</text>
        <text y="90"><tspan fill="#38BDF8">▸</tspan> Three.js / WebGL</text>
        <text y="120"><tspan fill="#38BDF8">▸</tspan> GLSL Raymarching</text>
        <text y="150"><tspan fill="#38BDF8">▸</tspan> Tailwind CSS 4</text>
        <text y="180"><tspan fill="#38BDF8">▸</tspan> Framer Motion</text>
        <text y="210"><tspan fill="#38BDF8">▸</tspan> Jetpack Compose</text>
      </g>
    </g>

    <!-- Column 4: Backend & Distributed -->
    <g transform="translate(684, 0)">
      <rect width="210" height="360" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="210" y2="0" stroke="#6366F1" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#6366F1">04 // SYSTEMS</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F8FAFC">Backends &amp; Mesh</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E2E8F0">
        <text y="0"><tspan fill="#818CF8">▸</tspan> FastAPI (ASGI)</text>
        <text y="30"><tspan fill="#818CF8">▸</tspan> WebSockets Delta</text>
        <text y="60"><tspan fill="#818CF8">▸</tspan> WebRTC P2P Voice</text>
        <text y="90"><tspan fill="#818CF8">▸</tspan> Node.js / Express</text>
        <text y="120"><tspan fill="#818CF8">▸</tspan> PostgreSQL</text>
        <text y="150"><tspan fill="#818CF8">▸</tspan> Redis (Cache/PubSub)</text>
        <text y="180"><tspan fill="#818CF8">▸</tspan> Celery Worker Queues</text>
        <text y="210"><tspan fill="#818CF8">▸</tspan> Room State Sync</text>
      </g>
    </g>

    <!-- Column 5: Platform & DevOps -->
    <g transform="translate(912, 0)">
      <rect width="192" height="360" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="192" y2="0" stroke="#10B981" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#34D399">05 // DEVOPS</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F8FAFC">Platforms</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E2E8F0">
        <text y="0"><tspan fill="#34D399">▸</tspan> Docker Containers</text>
        <text y="30"><tspan fill="#34D399">▸</tspan> GitHub Actions</text>
        <text y="60"><tspan fill="#34D399">▸</tspan> Railway PaaS</text>
        <text y="90"><tspan fill="#34D399">▸</tspan> Vercel Edge</text>
        <text y="120"><tspan fill="#34D399">▸</tspan> Android SDK 36</text>
        <text y="150"><tspan fill="#34D399">▸</tspan> Linux / Bash</text>
        <text y="180"><tspan fill="#34D399">▸</tspan> Git Submodules</text>
        <text y="210"><tspan fill="#34D399">▸</tspan> FFmpeg Media</text>
      </g>
    </g>
  </g>

  <!-- Border -->
  <rect x=".5" y=".5" width="1199" height="439" rx="15.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 8. SECTION 06: ARCHITECTURE BLUEPRINT (1200 x 500)
# ─────────────────────────────────────────────────────────────────────────────
def build_architecture_blueprint_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="1200" height="500" role="img" aria-label="System Architecture Blueprint">
  <defs>
    <linearGradient id="ab-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="ab-glow" cx="50%" cy="50%" r="60%">
      <stop offset="0" stop-color="#8B5CF6" stop-opacity=".2"/><stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>
    <pattern id="ab-grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 H 0 V 30" fill="none" stroke="#1E2336" stroke-opacity=".15"/>
    </pattern>
    <filter id="ab-glowf">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style>
    .ab-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .ab-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .ab-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .ab-pulse { animation: ab-pulse 3s ease-in-out infinite alternate; }
    @keyframes ab-pulse { from { opacity: .4; } to { opacity: 1; } }
  </style>

  <rect width="1200" height="500" rx="16" fill="url(#ab-bg)"/>
  <rect width="1200" height="500" rx="16" fill="url(#ab-grid)"/>
  <rect width="1200" height="500" rx="16" fill="url(#ab-glow)"/>

  <!-- Architecture Header Strip -->
  <g transform="translate(56, 36)">
    <text class="ab-mono" font-size="11.5" letter-spacing="2.5" fill="#A855F7">END-TO-END RESILIENT PIPELINE // MULTI-TIER ARCHITECTURE BLUEPRINT</text>
  </g>

  <!-- Multi-Tier Architecture Blocks -->
  <g transform="translate(56, 75)">
    <!-- Tier 1: Client Ingress -->
    <g transform="translate(0, 0)">
      <rect width="190" height="350" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="190" y2="0" stroke="#A855F7" stroke-width="2.5"/>
      <text class="ab-mono" x="18" y="28" font-size="11" letter-spacing="1.5" fill="#A855F7">01 // CLIENT TIER</text>
      <text class="ab-serif" x="18" y="54" font-size="18" fill="#F8FAFC">Touchpoints</text>

      <g transform="translate(16, 75)">
        <rect width="158" height="50" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#E2E8F0">Web SPA / PWA</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#94A3B8">React 19 · Next.js 15</text>
      </g>
      <g transform="translate(16, 138)">
        <rect width="158" height="50" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#E2E8F0">Desktop AI</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#94A3B8">Tauri Rust · Stealth HUD</text>
      </g>
      <g transform="translate(16, 201)">
        <rect width="158" height="50" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#E2E8F0">On-Device Android</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#94A3B8">Compose · CameraX · Room</text>
      </g>
      <g transform="translate(16, 264)">
        <rect width="158" height="50" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#E2E8F0">3D WebGL Canvas</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#94A3B8">Three.js · GLSL Raymarching</text>
      </g>
    </g>

    <!-- Conduit 1 -> 2 -->
    <path d="M 190 175 H 225" stroke="#A855F7" stroke-width="2" stroke-dasharray="4 4"/>

    <!-- Tier 2: Edge & Ingress -->
    <g transform="translate(225, 0)">
      <rect width="180" height="350" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="180" y2="0" stroke="#8B5CF6" stroke-width="2.5"/>
      <text class="ab-mono" x="18" y="28" font-size="11" letter-spacing="1.5" fill="#8B5CF6">02 // EDGE GATEWAY</text>
      <text class="ab-serif" x="18" y="54" font-size="18" fill="#F8FAFC">Routing &amp; Auth</text>

      <g transform="translate(16, 85)">
        <rect width="148" height="65" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="22" font-size="10" fill="#E2E8F0">Vercel Edge Proxy</text>
        <text class="ab-mono" x="12" y="40" font-size="8.5" fill="#94A3B8">SSL · Geo-DNS · WAF</text>
      </g>
      <g transform="translate(16, 175)">
        <rect width="148" height="65" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="22" font-size="10" fill="#E2E8F0">JWT &amp; Rate Limits</text>
        <text class="ab-mono" x="12" y="40" font-size="8.5" fill="#94A3B8">Redis Sliding Window</text>
      </g>
    </g>

    <!-- Conduit 2 -> 3 -->
    <path d="M 405 175 H 440" stroke="#8B5CF6" stroke-width="2" stroke-dasharray="4 4"/>

    <!-- Tier 3: Autonomous AI Inference Engine -->
    <g transform="translate(440, 0)">
      <rect width="210" height="350" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="210" y2="0" stroke="#38BDF8" stroke-width="2.5"/>
      <text class="ab-mono" x="18" y="28" font-size="11" letter-spacing="1.5" fill="#38BDF8">03 // AI INFERENCE</text>
      <text class="ab-serif" x="18" y="54" font-size="18" fill="#F8FAFC">Autonomous Core</text>

      <g transform="translate(16, 75)">
        <rect width="178" height="50" rx="6" fill="#121624" stroke="#A855F7" stroke-width="1.2"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#A855F7">IBM Bob 2.0 SDLC</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#E2E8F0">7-State Auto Engineer</text>
      </g>
      <g transform="translate(16, 138)">
        <rect width="178" height="50" rx="6" fill="#121624" stroke="#38BDF8" stroke-width="1.2"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#38BDF8">ExecuTorch Llama 3.2</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#E2E8F0">On-Device Air-Gap SLM</text>
      </g>
      <g transform="translate(16, 201)">
        <rect width="178" height="50" rx="6" fill="#121624" stroke="#6366F1" stroke-width="1.2"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#6366F1">Groq LLM LPU</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#E2E8F0">Sub-300ms AST Review</text>
      </g>
      <g transform="translate(16, 264)">
        <rect width="178" height="50" rx="6" fill="#121624" stroke="#10B981" stroke-width="1.2"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#10B981">AI Referee Arena</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#E2E8F0">Sub-80ms Code Judging</text>
      </g>
    </g>

    <!-- Conduit 3 -> 4 -->
    <path d="M 650 175 H 685" stroke="#38BDF8" stroke-width="2" stroke-dasharray="4 4"/>

    <!-- Tier 4: Microservices & Real-Time Mesh -->
    <g transform="translate(685, 0)">
      <rect width="200" height="350" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="200" y2="0" stroke="#6366F1" stroke-width="2.5"/>
      <text class="ab-mono" x="18" y="28" font-size="11" letter-spacing="1.5" fill="#6366F1">04 // MICROSERVICES</text>
      <text class="ab-serif" x="18" y="54" font-size="18" fill="#F8FAFC">Real-Time Mesh</text>

      <g transform="translate(16, 75)">
        <rect width="168" height="50" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#E2E8F0">FastAPI Async Core</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#94A3B8">Pydantic v2 · Uvicorn</text>
      </g>
      <g transform="translate(16, 138)">
        <rect width="168" height="50" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#E2E8F0">WebSockets Delta</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#94A3B8">&lt; 10ms Multi-Cursor Sync</text>
      </g>
      <g transform="translate(16, 201)">
        <rect width="168" height="50" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#E2E8F0">WebRTC Voice Mesh</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#94A3B8">Peer-to-Peer 48kHz Audio</text>
      </g>
      <g transform="translate(16, 264)">
        <rect width="168" height="50" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="20" font-size="10" fill="#E2E8F0">Celery Task Queue</text>
        <text class="ab-mono" x="12" y="36" font-size="8.5" fill="#94A3B8">Async Job Workers</text>
      </g>
    </g>

    <!-- Conduit 4 -> 5 -->
    <path d="M 885 175 H 920" stroke="#6366F1" stroke-width="2" stroke-dasharray="4 4"/>

    <!-- Tier 5: Persistence & Edge State -->
    <g transform="translate(920, 0)">
      <rect width="168" height="350" rx="10" fill="#0D101A" stroke="#1E2336" stroke-opacity=".8"/>
      <line x1="0" y1="0" x2="168" y2="0" stroke="#10B981" stroke-width="2.5"/>
      <text class="ab-mono" x="18" y="28" font-size="11" letter-spacing="1.5" fill="#34D399">05 // PERSISTENCE</text>
      <text class="ab-serif" x="18" y="54" font-size="18" fill="#F8FAFC">Data Stores</text>

      <g transform="translate(14, 85)">
        <rect width="140" height="65" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="22" font-size="10" fill="#E2E8F0">PostgreSQL</text>
        <text class="ab-mono" x="12" y="40" font-size="8.5" fill="#94A3B8">ACID · Relational</text>
      </g>
      <g transform="translate(14, 175)">
        <rect width="140" height="65" rx="6" fill="#151A2B" stroke="#252B42"/>
        <text class="ab-mono" x="12" y="22" font-size="10" fill="#E2E8F0">Redis In-Memory</text>
        <text class="ab-mono" x="12" y="40" font-size="8.5" fill="#94A3B8">Pub/Sub · Caching</text>
      </g>
    </g>
  </g>

  <!-- Animated Data Packet -->
  <circle r="4" fill="#38BDF8" filter="url(#ab-glowf)">
    <animateMotion dur="7s" repeatCount="indefinite" path="M 246 250 H 1108"/>
  </circle>

  <!-- Border -->
  <rect x=".5" y=".5" width="1199" height="499" rx="15.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 9. SECTION 07: FOOTER & EDITORIAL SIGNATURE (1200 x 180)
# ─────────────────────────────────────────────────────────────────────────────
def build_footer_signature_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 180" width="1200" height="180" role="img" aria-label="Editorial Signature and Sign-off">
  <defs>
    <linearGradient id="fs-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08090E"/><stop offset="100%" stop-color="#040508"/>
    </linearGradient>
    <radialGradient id="fs-glow" cx="50%" cy="50%" r="60%">
      <stop offset="0" stop-color="#8B5CF6" stop-opacity=".15"/><stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .fs-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .fs-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
  </style>

  <rect width="1200" height="180" rx="16" fill="url(#fs-bg)"/>
  <rect width="1200" height="180" rx="16" fill="url(#fs-glow)"/>

  <g transform="translate(64, 48)">
    <text class="fs-serif" font-size="28" font-style="italic" fill="#F8FAFC">"Survival before abstraction. Precision before speed. Systems that endure."</text>
    <text class="fs-mono" y="44" font-size="12" letter-spacing="2.5" fill="#A855F7">MUHAMMAD MUBASHAR (PASHA DEV)  —  AI SYSTEMS ARCHITECT  ·  LAHORE, PAKISTAN</text>
    <text class="fs-mono" y="72" font-size="10.5" fill="#64748B">DESIGN ARCHITECTURE: BESPOKE EDITORIAL OBSIDIAN &amp; CYBER AMETHYST  ·  GITHUB PROFILE 2026</text>
  </g>

  <!-- Border -->
  <rect x=".5" y=".5" width="1199" height="179" rx="15.5" fill="none" stroke="#252B42" stroke-opacity=".6"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# MAIN GENERATOR
# ─────────────────────────────────────────────────────────────────────────────
def main():
    print("=== Step 1: Processing User Portrait with Studio Enhancements ===")
    b64_img = get_user_portrait_base64()
    print(f"Base64 generated successfully ({len(b64_img)} chars)")

    print("\n=== Step 2: Generating All Bespoke Luxury SVGs ===")
    svgs = {
        # Hero
        "pasha-hero-portrait.svg": build_hero_portrait_svg(b64_img),
        # Titles
        "title-about.svg": build_title_svg("01", "About", "Hello, I'm Mubashar.", "WHO I AM & WHAT DRIVES ME", "CORE DOSSIER"),
        "title-recognition.svg": build_title_svg("02", "Proof", "On the record.", "VERIFIED METRICS", "SYSTEM MILESTONES"),
        "title-work.svg": build_title_svg("03", "Selected work", "Products, not assignments.", "FLAGSHIP PRODUCTS", "PRODUCTION DEPLOYMENTS"),
        "title-toolkit.svg": build_title_svg("04", "Toolkit", "The tools I reach for.", "ENGINEERING ARSENAL", "STACK ARCHITECTURE"),
        "title-commits.svg": build_title_svg("05", "Commit log", "A cadence of shipping.", "LIVE TELEMETRY", "REAL-TIME SYNC"),
        "title-architecture.svg": build_title_svg("06", "Architecture", "Systems that scale with poise.", "END-TO-END PIPELINE", "ENGINEERING BLUEPRINT"),
        "title-connect.svg": build_title_svg("07", "Connect", "Let's build something extraordinary.", "DIRECT UPLINK", "CONTACT TERMINAL"),
        # Section Content Cards
        "about-intro.svg": build_about_intro_svg(),
        "achievement-motif-v2.svg": build_achievement_motif_svg(),
        "project-devpilot.svg": build_project_devpilot_svg(),
        "project-syncforge.svg": build_project_syncforge_svg(),
        "project-privatedoc.svg": build_project_privatedoc_svg(),
        "project-ghostreview.svg": build_project_ghostreview_svg(),
        "project-opencluely.svg": build_project_opencluely_svg(),
        "project-bmw7.svg": build_project_bmw7_svg(),
        "project-nexora.svg": build_project_nexora_svg(),
        "tech-constellation-v2.svg": build_tech_constellation_svg(),
        "architecture-blueprint.svg": build_architecture_blueprint_svg(),
        "footer-signature-v2.svg": build_footer_signature_svg(),
    }

    errors = 0
    for filename, content in svgs.items():
        out_path = os.path.join(ASSETS_DIR, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        try:
            ET.fromstring(content)
            print(f"  [OK - VALID XML] {filename} ({len(content):,} bytes)")
        except Exception as e:
            print(f"  [ERROR - XML FAIL] {filename}: {e}")
            errors += 1

    if errors == 0:
        print("\nAll bespoke Luxury SVGs generated and passed XML validation perfectly!")
    else:
        print(f"\n{errors} SVGs failed XML validation!")


if __name__ == "__main__":
    main()
