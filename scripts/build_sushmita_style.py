"""
Master SVG & Asset Builder for Pasha Dev (Muhammad Mubashar)
Editorial Profile in Black & Electric Blue Theme (Inspired by Sushmita Dasari design architecture)
Generates high-precision, bespoke SVGs with embedded user portrait, animated glowing gradients,
and strict XML compliance.
"""

import os
import base64
from io import BytesIO
from PIL import Image
import xml.etree.ElementTree as ET

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(WORKSPACE_DIR, "assets")
PROFILE_DIR = os.path.join(WORKSPACE_DIR, "profile")
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(PROFILE_DIR, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# 1. OPTIMIZE & BASE64 ENCODE USER PORTRAIT
# ─────────────────────────────────────────────────────────────────────────────
def get_user_portrait_base64():
    selfie_path = os.path.join(WORKSPACE_DIR, "Fisheye Selfie in a Tech Bedroom.png")
    if not os.path.exists(selfie_path):
        raise FileNotFoundError(f"Missing {selfie_path}")
    
    im = Image.open(selfie_path)
    # Crop around user's face, glasses, dark shirt, and background tech monitor
    cropped = im.crop((160, 100, 1100, 1160))
    resized = cropped.resize((480, 540), Image.Resampling.LANCZOS)
    
    buf = BytesIO()
    resized.save(buf, format="JPEG", quality=88, optimize=True)
    jpg_bytes = buf.getvalue()
    
    # Save optimized standalone jpg for reference
    portrait_jpg_path = os.path.join(ASSETS_DIR, "pasha-portrait.jpg")
    with open(portrait_jpg_path, "wb") as f:
        f.write(jpg_bytes)
        
    return base64.b64encode(jpg_bytes).decode("utf-8")


# ─────────────────────────────────────────────────────────────────────────────
# 2. HERO PORTRAIT SVG (1200 x 480)
# ─────────────────────────────────────────────────────────────────────────────
def build_hero_portrait_svg(b64_img):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-label="Muhammad Mubashar (Pasha Dev) — AI Systems Architect, Full-Stack Developer, Creative Technologist">
  <defs>
    <linearGradient id="hero-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#030712"/>
      <stop offset="50" stop-color="#061026"/>
      <stop offset="100" stop-color="#02050e"/>
    </linearGradient>
    <radialGradient id="hero-glow-left" cx="20%" cy="40%" r="65%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".25"/>
      <stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-glow-right" cx="80%" cy="50%" r="60%">
      <stop offset="0" stop-color="#00D2FF" stop-opacity=".3"/>
      <stop offset="60%" stop-color="#0066FF" stop-opacity=".12"/>
      <stop offset="100%" stop-color="#030712" stop-opacity="0"/>
    </radialGradient>
    <pattern id="hero-grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 H 0 V 32" fill="none" stroke="#38BDF8" stroke-opacity=".06"/>
      <circle cx="32" cy="32" r=".75" fill="#38BDF8" fill-opacity=".15"/>
    </pattern>
    <linearGradient id="hero-rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#38BDF8"/>
      <stop offset=".5" stop-color="#0066FF"/>
      <stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-name-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#38BDF8"/>
      <stop offset=".6" stop-color="#60A5FA"/>
      <stop offset="1" stop-color="#93C5FD"/>
    </linearGradient>
    <linearGradient id="hero-sheen" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#F0F9FF" stop-opacity="0"/>
      <stop offset=".45" stop-color="#FFFFFF" stop-opacity=".95"/>
      <stop offset=".55" stop-color="#38BDF8" stop-opacity=".95"/>
      <stop offset="1" stop-color="#F0F9FF" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1600 0;1600 0" keyTimes="0;.45;1" dur="7s" begin="1.2s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="hero-frame-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#38BDF8"/>
      <stop offset=".5" stop-color="#0066FF"/>
      <stop offset="1" stop-color="#1E3A8A"/>
    </linearGradient>
    <linearGradient id="hero-photo-grade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".14"/>
      <stop offset="70" stop-color="#030712" stop-opacity=".04"/>
      <stop offset="100%" stop-color="#030712" stop-opacity=".65"/>
    </linearGradient>
    <linearGradient id="hero-photo-sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset=".5" stop-color="#38BDF8" stop-opacity=".35"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <filter id="hero-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="hero-arch">
      <path d="M 846 394 V 186 A 118 118 0 0 1 1082 186 V 394 Z"/>
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
    .hero-signal {{ stroke-dasharray: 320; stroke-dashoffset: 320; animation: hero-draw 2.2s cubic-bezier(.65,0,.35,1) 1s forwards; }}
    .hero-frame {{ stroke-dasharray: 900; stroke-dashoffset: 900; animation: hero-draw 2s cubic-bezier(.65,0,.35,1) .4s forwards; }}
    @keyframes hero-rise {{ from {{ opacity: 0; transform: translateY(16px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes hero-fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes hero-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .hero-rise, .hero-fade {{ animation: none; opacity: 1; transform: none; }}
      .hero-draw, .hero-signal, .hero-frame {{ stroke-dashoffset: 0; }}
    }}
  </style>

  <!-- Canvas Background -->
  <rect width="1200" height="480" rx="18" fill="url(#hero-bg)"/>
  <rect width="1200" height="480" rx="18" fill="url(#hero-grid)"/>
  <rect width="1200" height="480" rx="18" fill="url(#hero-glow-left)"/>
  <rect width="1200" height="480" rx="18" fill="url(#hero-glow-right)"/>

  <!-- Arch Portrait & Celestial Ring Group -->
  <g id="portrait-group">
    <!-- Rotating Celestial Node Rings -->
    <g transform="translate(964, 236)" class="hero-fade d4">
      <circle r="150" fill="none" stroke="#0066FF" stroke-opacity=".22" stroke-dasharray="4 8"/>
      <circle r="185" fill="none" stroke="#38BDF8" stroke-opacity=".14"/>
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="75s" repeatCount="indefinite"/>
        <circle cx="185" cy="0" r="4" fill="#38BDF8" filter="url(#hero-glow)"/>
        <circle cx="-130" cy="-130" r="2.5" fill="#60A5FA"/>
        <circle cx="0" cy="-185" r="2" fill="#93C5FD"/>
      </g>
      <!-- Technical Layer Pins -->
      <g class="hero-mono" font-size="10" letter-spacing="1.5" fill="#94A3B8">
        <g transform="translate(-130, -152)"><circle r="3" fill="#38BDF8"/><text x="8" y="4" fill="#E0F2FE">AI · AGENTS</text></g>
        <g transform="translate(142, -92)"><circle r="3" fill="#38BDF8"/><text x="8" y="4" fill="#E0F2FE">FASTAPI</text></g>
        <g transform="translate(142, 108)"><circle r="3" fill="#38BDF8"/><text x="8" y="4" fill="#E0F2FE">REACT · NEXT</text></g>
        <g transform="translate(-160, 36)"><circle r="3" fill="#38BDF8"/><text x="-10" y="4" text-anchor="end" fill="#E0F2FE">TAURI · RUST</text></g>
        <g transform="translate(-20, 196)"><circle r="3" fill="#38BDF8"/><text x="8" y="4" fill="#E0F2FE">THREE.JS · GLSL</text></g>
      </g>
    </g>

    <!-- Arched Portrait Clipping Frame -->
    <g class="hero-fade d2">
      <g clip-path="url(#hero-arch)">
        <image href="data:image/jpeg;base64,{b64_img}" x="846" y="68" width="236" height="330" preserveAspectRatio="xMidYMid slice"/>
        <rect x="846" y="68" width="236" height="330" fill="url(#hero-photo-grade)"/>
        <rect x="700" y="68" width="90" height="330" fill="url(#hero-photo-sheen)" transform="skewX(-14)">
          <animate attributeName="x" values="700;1260;1260" keyTimes="0;.3;1" dur="8.5s" begin="2.5s" repeatCount="indefinite"/>
        </rect>
      </g>
      <!-- Arched Accent Border -->
      <path class="hero-frame" d="M 846 394 V 186 A 118 118 0 0 1 1082 186 V 394 Z" fill="none" stroke="url(#hero-frame-grad)" stroke-width="1.8"/>
      <!-- Technical Reticle Brackets -->
      <path d="M 828 300 v-22 h 22" fill="none" stroke="#38BDF8" stroke-opacity=".85" stroke-width="1.5"/>
      <path d="M 1100 412 v-22 M 1100 412 h-22" fill="none" stroke="#38BDF8" stroke-opacity=".85" stroke-width="1.5"/>
    </g>
  </g>

  <!-- Left Content: Terminal Indicator -->
  <g class="hero-fade d1" transform="translate(68, 54)">
    <rect width="338" height="34" rx="17" fill="#070E1E" stroke="#38BDF8" stroke-opacity=".35"/>
    <circle cx="20" cy="17" r="4.5" fill="#10B981" filter="url(#hero-glow)">
      <animate attributeName="opacity" values="1;.4;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text class="hero-mono" x="36" y="21.5" font-size="12" fill="#94A3B8">~/pasha<tspan fill="#38BDF8"> $ </tspan><tspan fill="#F0F9FF">build --intelligent</tspan></text>
    <rect x="312" y="10" width="7" height="14" fill="#38BDF8">
      <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1s" repeatCount="indefinite"/>
    </rect>
  </g>

  <!-- Eyebrow Category -->
  <g class="hero-rise d2">
    <line x1="68" y1="126" x2="102" y2="126" stroke="#38BDF8" stroke-width="1.5"/>
    <text class="hero-mono" x="114" y="130" font-size="12" letter-spacing="3.2" fill="#38BDF8">AI SYSTEMS · FULL-STACK ARCHITECTURE · EXPERIENTIAL 3D</text>
  </g>

  <!-- Large Headline Name -->
  <text class="hero-serif hero-rise d3" x="64" y="218" font-size="86" font-weight="300" letter-spacing="-2" fill="#F0F9FF">Muhammad Mubashar</text>
  <text class="hero-serif hero-rise d4" x="64" y="302" font-size="86" font-style="italic" font-weight="300" letter-spacing="-2" fill="url(#hero-name-grad)">Pasha<tspan fill="#38BDF8">.</tspan></text>

  <!-- Light Sheen Sweeping Across Headline -->
  <g class="hero-fade d6" pointer-events="none">
    <text class="hero-serif" x="64" y="218" font-size="86" font-weight="300" letter-spacing="-2" fill="url(#hero-sheen)">Muhammad Mubashar</text>
    <text class="hero-serif" x="64" y="302" font-size="86" font-style="italic" font-weight="300" letter-spacing="-2" fill="url(#hero-sheen)">Pasha.</text>
  </g>

  <!-- Glowing Curvature Underline -->
  <path class="hero-draw" d="M 68 328 C 210 324, 410 334, 590 324" fill="none" stroke="url(#hero-rule)" stroke-width="2.2" stroke-linecap="round" filter="url(#hero-glow)"/>

  <!-- Signal Curve Drawing into Portrait -->
  <path class="hero-signal" d="M 590 324 C 680 320, 740 310, 780 295 S 824 278, 846 278" fill="none" stroke="#38BDF8" stroke-opacity=".4" stroke-width="1.2"/>
  <circle cx="590" cy="324" r="3.2" fill="#E0F2FE" filter="url(#hero-glow)" opacity=".9">
    <animateMotion dur="5.5s" repeatCount="indefinite" begin="3.8s" path="M 590 324 C 680 320, 740 310, 780 295 S 824 278, 846 278" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".45 0 .55 1"/>
  </circle>

  <!-- Positioning Subtitle & Ethos -->
  <text class="hero-mono hero-rise d5" x="68" y="366" font-size="12.5" letter-spacing="2.4" fill="#E0F2FE">AI/ML SYSTEMS ARCHITECT  ·  FULL-STACK DEVELOPER  ·  CREATIVE TECHNOLOGIST</text>
  <text class="hero-serif hero-rise d6" x="68" y="402" font-size="18" font-style="italic" fill="#94A3B8">Engineering intelligence. Architecting resilient platforms. Designing experiences.</text>

  <!-- Meta Strip -->
  <g class="hero-fade d6">
    <line x1="68" y1="432" x2="1132" y2="432" stroke="#38BDF8" stroke-opacity=".16"/>
    <text class="hero-mono" x="68" y="454" font-size="10.5" letter-spacing="2" fill="#94A3B8">LAHORE, PAKISTAN  ·  31.52° N, 74.35° E</text>
    <text class="hero-mono" x="1132" y="454" text-anchor="end" font-size="10.5" letter-spacing="2" fill="#38BDF8">FOUNDER &amp; ARCHITECT · PASHA DEVPILOT (HACKATHON) · NEXORA · OPENCLUELY</text>
  </g>

  <!-- Subtle Outer Border -->
  <rect x=".5" y=".5" width="1199" height="479" rx="17.5" fill="none" stroke="#38BDF8" stroke-opacity=".22"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 3. SECTION TITLE GENERATOR (1200 x 120)
# ─────────────────────────────────────────────────────────────────────────────
def build_title_svg(num, title_word, title_rest, subtitle, right_tag):
    # XML escape text fields
    clean_subtitle = subtitle.replace("&", "&amp;")
    clean_right_tag = right_tag.replace("&", "&amp;")
    clean_title_rest = title_rest.replace("&", "&amp;")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="img" aria-label="{num} {title_word} {clean_title_rest}">
  <defs>
    <linearGradient id="ta-line-{num}" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="1160" y2="0">
      <stop offset="0" stop-color="#38BDF8"/>
      <stop offset=".6" stop-color="#0066FF"/>
      <stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ta-sheen-{num}" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#93C5FD"/>
      <stop offset=".5" stop-color="#F0F9FF"/>
      <stop offset="1" stop-color="#93C5FD"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1500 0;1500 0" keyTimes="0;.4;1" dur="7s" begin="1.5s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="ta-pulse-{num}"><stop offset="0" stop-color="#F0F9FF"/><stop offset=".5" stop-color="#38BDF8" stop-opacity=".7"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/></radialGradient>
  </defs>
  <style>
    .ta-serif {{ font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }}
    .ta-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }}
    .ta-in {{ animation: ta-in 1.1s cubic-bezier(.16,1,.3,1) both; }}
    .ta-d2 {{ animation-delay: .2s; }} .ta-d3 {{ animation-delay: .45s; }}
    .ta-draw {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: ta-draw 1.8s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes ta-in {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes ta-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ta-in {{ animation: none; }} .ta-draw {{ stroke-dashoffset: 0; }} }}
  </style>
  <g class="ta-in">
    <text class="ta-mono" x="40" y="34" font-size="12" letter-spacing="3" fill="#38BDF8"><tspan fill="#60A5FA">{num}</tspan>   {title_word.upper()}</text>
  </g>
  <g class="ta-in ta-d2">
    <text class="ta-serif" x="38" y="84" font-size="44" font-weight="300" letter-spacing="-1" fill="#F0F9FF">{title_word}, <tspan font-style="italic" fill="url(#ta-sheen-{num})">{clean_title_rest}</tspan></text>
  </g>
  <g class="ta-in ta-d3">
    <text class="ta-mono" x="1160" y="34" text-anchor="end" font-size="10.5" letter-spacing="2.4" fill="#94A3B8">{clean_right_tag}</text>
    <text class="ta-mono" x="1160" y="84" text-anchor="end" font-size="11" letter-spacing="1.5" fill="#38BDF8">{clean_subtitle}</text>
  </g>
  <path class="ta-draw" d="M40 106 H1160" stroke="url(#ta-line-{num})" stroke-width="1.2"/>
  <circle cx="40" cy="106" r="7" fill="url(#ta-pulse-{num})" opacity="0">
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
      <stop offset="0" stop-color="#040916"/>
      <stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <pattern id="ai-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 H 0 V 24" fill="none" stroke="#1E3A8A" stroke-opacity=".18"/>
    </pattern>
    <radialGradient id="ai-glow" cx="15%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".22"/>
      <stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
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
    <text class="ai-mono" font-size="11.5" letter-spacing="2.5" fill="#38BDF8">DISCIPLINE BUILDS FREEDOM  //  ZERO FRICTION  //  SURVIVAL BEFORE ABSTRACTION</text>

    <!-- Main Editorial Bio -->
    <text class="ai-sans" y="44" font-size="18" fill="#F0F9FF" font-weight="300" line-height="1.6">
      <tspan x="0" dy="0">I am an AI Systems Architect &amp; Full-Stack Engineer based in Lahore, Pakistan, focused on building enduring,</tspan>
      <tspan x="0" dy="30">high-velocity software. My work lives at the intersection of autonomous multi-agent intelligence, resilient</tspan>
      <tspan x="0" dy="30">distributed microservices, and immersive 3D computing.</tspan>
    </text>

    <!-- Ethos Quote Box -->
    <g transform="translate(0, 126)">
      <rect width="1088" height="54" rx="8" fill="#071126" stroke="#0066FF" stroke-opacity=".35"/>
      <line x1="0" y1="0" x2="0" y2="54" stroke="#38BDF8" stroke-width="4"/>
      <text class="ai-serif" x="24" y="33" font-size="16" font-style="italic" fill="#E0F2FE">"Survival before abstraction. Precision before shortcuts. Zero-friction execution. AI as the ultimate force multiplier."</text>
    </g>

    <!-- Three Technical Pillars -->
    <g transform="translate(0, 206)" class="ai-mono" font-size="11.5" fill="#94A3B8">
      <g transform="translate(0, 0)">
        <circle cx="5" cy="4" r="3.5" fill="#38BDF8"/>
        <text x="16" y="8" fill="#F0F9FF" font-weight="700">AUTONOMOUS AI</text>
        <text x="16" y="24" fill="#64748B">LLM pipelines · Vision OCR · Whisper STT · Live referees</text>
      </g>
      <g transform="translate(370, 0)">
        <circle cx="5" cy="4" r="3.5" fill="#38BDF8"/>
        <text x="16" y="8" fill="#F0F9FF" font-weight="700">SYSTEMS &amp; BACKENDS</text>
        <text x="16" y="24" fill="#64748B">FastAPI · Node.js · PostgreSQL · Redis · Docker · Rust</text>
      </g>
      <g transform="translate(740, 0)">
        <circle cx="5" cy="4" r="3.5" fill="#38BDF8"/>
        <text x="16" y="8" fill="#F0F9FF" font-weight="700">EXPERIENTIAL 3D &amp; WEB</text>
        <text x="16" y="24" fill="#64748B">Next.js 15 · Three.js · GLSL Shaders · Framer Motion</text>
      </g>
    </g>
  </g>

  <!-- Card Border -->
  <rect x=".5" y=".5" width="1199" height="299" rx="15.5" fill="none" stroke="#38BDF8" stroke-opacity=".22"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 5. SECTION 02: PROOF & RECOGNITION (1200 x 280)
# ─────────────────────────────────────────────────────────────────────────────
def build_achievement_motif_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 280" width="1200" height="280" role="img" aria-label="Proof and Highlights">
  <defs>
    <linearGradient id="rec-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/>
      <stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="rec-glow" cx="85%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".22"/>
      <stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="rec-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 H 0 V 28" fill="none" stroke="#1E3A8A" stroke-opacity=".15"/>
    </pattern>
  </defs>
  <style>
    .rec-serif {{ font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }}
    .rec-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }}
    .rec-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }}
  </style>

  <rect width="1200" height="280" rx="16" fill="url(#rec-bg)"/>
  <rect width="1200" height="280" rx="16" fill="url(#rec-grid)"/>
  <rect width="1200" height="280" rx="16" fill="url(#rec-glow)"/>

  <!-- 4 Verified Metrics Cards -->
  <g transform="translate(48, 40)">
    <!-- Card 1 -->
    <g transform="translate(0, 0)">
      <rect width="258" height="198" rx="10" fill="#071228" stroke="#1E3A8A" stroke-opacity=".5"/>
      <line x1="0" y1="0" x2="258" y2="0" stroke="#38BDF8" stroke-width="2"/>
      <text class="rec-mono" x="20" y="34" font-size="11" letter-spacing="1.5" fill="#38BDF8">TELEMETRY // RECORD</text>
      <text class="rec-serif" x="20" y="88" font-size="44" font-weight="300" fill="#F0F9FF">50+</text>
      <text class="rec-sans" x="20" y="118" font-size="15" font-weight="600" fill="#E0F2FE">Repositories Shipped</text>
      <text class="rec-mono" x="20" y="146" font-size="10.5" fill="#64748B">Web platforms, AI tools, 3D engines &amp; desktop assistants</text>
    </g>

    <!-- Card 2 -->
    <g transform="translate(282, 0)">
      <rect width="258" height="198" rx="10" fill="#071228" stroke="#1E3A8A" stroke-opacity=".5"/>
      <line x1="0" y1="0" x2="258" y2="0" stroke="#0066FF" stroke-width="2"/>
      <text class="rec-mono" x="20" y="34" font-size="11" letter-spacing="1.5" fill="#38BDF8">🏆 HACKATHON // FLAGSHIP</text>
      <text class="rec-serif" x="20" y="88" font-size="36" font-weight="300" fill="#F0F9FF">IBM Bob</text>
      <text class="rec-sans" x="20" y="118" font-size="15" font-weight="600" fill="#E0F2FE">Pasha DevPilot SDLC</text>
      <text class="rec-mono" x="20" y="146" font-size="10.5" fill="#64748B">7-state autonomous AI software engineer, AST scanner &amp; sandbox</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(564, 0)">
      <rect width="258" height="198" rx="10" fill="#071228" stroke="#1E3A8A" stroke-opacity=".5"/>
      <line x1="0" y1="0" x2="258" y2="0" stroke="#60A5FA" stroke-width="2"/>
      <text class="rec-mono" x="20" y="34" font-size="11" letter-spacing="1.5" fill="#38BDF8">GRAPHICS // SHADERS</text>
      <text class="rec-serif" x="20" y="88" font-size="44" font-weight="300" fill="#F0F9FF">60 FPS</text>
      <text class="rec-sans" x="20" y="118" font-size="15" font-weight="600" fill="#E0F2FE">Raymarching WebGL</text>
      <text class="rec-mono" x="20" y="146" font-size="10.5" fill="#64748B">Draco-compressed metallic clear-coat reflections in 3D showroom</text>
    </g>

    <!-- Card 4 -->
    <g transform="translate(846, 0)">
      <rect width="258" height="198" rx="10" fill="#071228" stroke="#1E3A8A" stroke-opacity=".5"/>
      <line x1="0" y1="0" x2="258" y2="0" stroke="#34D399" stroke-width="2"/>
      <text class="rec-mono" x="20" y="34" font-size="11" letter-spacing="1.5" fill="#34D399">PRODUCTION // UPTIME</text>
      <text class="rec-serif" x="20" y="88" font-size="44" font-weight="300" fill="#F0F9FF">100%</text>
      <text class="rec-sans" x="20" y="118" font-size="15" font-weight="600" fill="#E0F2FE">Shipping Focus</text>
      <text class="rec-mono" x="20" y="146" font-size="10.5" fill="#64748B">Active user traffic across Pasha Tools, Wishora &amp; live apps</text>
    </g>
  </g>

  <!-- Border -->
  <rect x=".5" y=".5" width="1199" height="279" rx="15.5" fill="none" stroke="#38BDF8" stroke-opacity=".22"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 6. BESPOKE PROJECT CARDS (1200 x 370 each)
# ─────────────────────────────────────────────────────────────────────────────
def build_project_nexora_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p1-t">
  <title id="p1-t">Nexora: AI-powered skill social platform with live coding challenges &amp; autonomous referee</title>
  <defs>
    <linearGradient id="p1-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="p1-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".3"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p1-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="p1-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="p1-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="p1-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0F9FF"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
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
      <text class="p1-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">01 · FLAGSHIP · AI SOCIAL ARENA · 2026</text>
      <text class="p1-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F0F9FF">NEXORA</text>
      <text class="p1-sans" y="94" font-size="16.5" fill="#94A3B8">Gamified social identity, guild communities, and peer coding battles.</text>
      <text class="p1-mono" y="126" font-size="12" fill="#E0F2FE"><tspan fill="#38BDF8">BUILT ›</tspan> Autonomous AI Referee, real-time code evaluation, Redis queuing, FastAPI</text>
      <line class="p1-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="p1-serif" font-size="32" font-weight="300" fill="#F0F9FF">100%</text>
        <text class="p1-sans" y="22" font-size="12" fill="#94A3B8">Autonomous AI Referee</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="p1-serif" font-size="32" font-weight="300" fill="#F0F9FF">&lt;80ms</text>
        <text class="p1-sans" y="22" font-size="12" fill="#94A3B8">Evaluation Latency</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="p1-serif" font-size="32" font-weight="300" fill="#34D399">v1.0</text>
        <text class="p1-sans" y="22" font-size="12" fill="#94A3B8">Private Alpha Live</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="64" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p1-mono" x="32" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">React</text></g>
        <g transform="translate(72, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p1-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">TypeScript</text></g>
        <g transform="translate(170, 0)"><rect width="70" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p1-mono" x="35" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">FastAPI</text></g>
        <g transform="translate(248, 0)"><rect width="94" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p1-mono" x="47" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">PostgreSQL</text></g>
        <g transform="translate(350, 0)"><rect width="60" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p1-mono" x="30" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Redis</text></g>
        <g transform="translate(418, 0)"><rect width="68" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p1-mono" x="34" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Docker</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Arena Battle Board & AI Referee -->
    <g transform="translate(740, 60)" class="p1-in">
      <!-- Arena Dual Panel -->
      <rect width="390" height="240" rx="12" fill="#071228" stroke="#1E3A8A" stroke-opacity=".6"/>
      <!-- Header Bar -->
      <rect width="390" height="34" rx="12" fill="#0A1838"/>
      <circle cx="20" cy="17" r="4" fill="#EF4444"/>
      <circle cx="34" cy="17" r="4" fill="#F59E0B"/>
      <circle cx="48" cy="17" r="4" fill="#10B981"/>
      <text class="p1-mono" x="70" y="21" font-size="11" fill="#E0F2FE">NEXORA // LIVE ARENA CODE REF</text>

      <!-- Live Comparison Windows -->
      <rect x="20" y="50" width="165" height="110" rx="6" fill="#040916" stroke="#1E3A8A" stroke-opacity=".4"/>
      <text class="p1-mono" x="30" y="68" font-size="9.5" fill="#60A5FA">PLAYER_01 (O(N))</text>
      <rect x="30" y="80" width="120" height="4" rx="2" fill="#38BDF8" fill-opacity=".3"/>
      <rect x="30" y="92" width="90" height="4" rx="2" fill="#38BDF8" fill-opacity=".3"/>
      <rect x="30" y="104" width="135" height="4" rx="2" fill="#10B981" filter="url(#p1-glowf)"/>
      <text class="p1-mono" x="30" y="132" font-size="9" fill="#10B981">✓ PASSED 28/28 TESTS</text>

      <rect x="205" y="50" width="165" height="110" rx="6" fill="#040916" stroke="#1E3A8A" stroke-opacity=".4"/>
      <text class="p1-mono" x="215" y="68" font-size="9.5" fill="#94A3B8">PLAYER_02 (O(N²))</text>
      <rect x="215" y="80" width="110" height="4" rx="2" fill="#94A3B8" fill-opacity=".2"/>
      <rect x="215" y="92" width="130" height="4" rx="2" fill="#94A3B8" fill-opacity=".2"/>
      <rect x="215" y="104" width="80" height="4" rx="2" fill="#F59E0B" filter="url(#p1-glowf)"/>
      <text class="p1-mono" x="215" y="132" font-size="9" fill="#F59E0B">⏱ 142ms LATENCY</text>

      <!-- Autonomous AI Referee Center Pill -->
      <g transform="translate(45, 175)">
        <rect width="300" height="44" rx="8" fill="#0B1A3D" stroke="#0066FF" stroke-width="1.2"/>
        <circle cx="22" cy="22" r="6" fill="#38BDF8" filter="url(#p1-glowf)">
          <animate attributeName="r" values="5;7;5" dur="2s" repeatCount="indefinite"/>
        </circle>
        <text class="p1-mono" x="38" y="20" font-size="10.5" fill="#F0F9FF">AI REFEREE: VERDICT DECLARED</text>
        <text class="p1-mono" x="38" y="34" font-size="9.5" fill="#38BDF8">P1 WINNER · TIME O(N) · ELO +34</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#1E3A8A" stroke-opacity=".4"/>
    <rect class="p1-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#p1-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_opencluely_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p2-t">
  <title id="p2-t">OpenCluely: Undetectable desktop AI assistant for technical interviews and algorithmic mastery</title>
  <defs>
    <linearGradient id="p2-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="p2-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#00D2FF" stop-opacity=".25"/><stop offset="100%" stop-color="#00D2FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p2-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="p2-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="p2-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="p2-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0F9FF"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
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
      <text class="p2-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">02 · DESKTOP AI · STEALTH OCR · 2026</text>
      <text class="p2-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F0F9FF">OpenCluely</text>
      <text class="p2-sans" y="94" font-size="16.5" fill="#94A3B8">Undetectable frameless desktop AI overlay for technical interviews.</text>
      <text class="p2-mono" y="126" font-size="12" fill="#E0F2FE"><tspan fill="#38BDF8">BUILT ›</tspan> Transparent Tauri canvas, Vision OCR stream, Whisper audio, Gemini AI</text>
      <line class="p2-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="p2-serif" font-size="32" font-weight="300" fill="#F0F9FF">0-Footprint</text>
        <text class="p2-sans" y="22" font-size="12" fill="#94A3B8">Invisible Screen Capture</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="p2-serif" font-size="32" font-weight="300" fill="#F0F9FF">O(N)</text>
        <text class="p2-sans" y="22" font-size="12" fill="#94A3B8">Optimal Proof Engine</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="p2-serif" font-size="32" font-weight="300" fill="#34D399">MIT</text>
        <text class="p2-sans" y="22" font-size="12" fill="#94A3B8">Open Source Codebase</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p2-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Tauri (Rust)</text></g>
        <g transform="translate(98, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p2-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">TypeScript</text></g>
        <g transform="translate(196, 0)"><rect width="84" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p2-mono" x="42" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Gemini AI</text></g>
        <g transform="translate(288, 0)"><rect width="88" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p2-mono" x="44" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Vision OCR</text></g>
        <g transform="translate(384, 0)"><rect width="76" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p2-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Whisper</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Stealth HUD & OCR Scan Beam -->
    <g transform="translate(740, 60)" class="p2-in">
      <rect width="390" height="240" rx="12" fill="#050C1F" stroke="#00D2FF" stroke-opacity=".4"/>
      <rect width="390" height="34" rx="12" fill="#081534"/>
      <text class="p2-mono" x="20" y="22" font-size="11" fill="#38BDF8">STEALTH_OVERLAY // INVISIBLE HUD</text>
      <text class="p2-mono" x="370" y="22" text-anchor="end" font-size="10" fill="#10B981">● ACTIVE</text>

      <!-- Screen Scanner Visualizer -->
      <rect x="24" y="52" width="342" height="110" rx="6" fill="#020713" stroke="#1E3A8A" stroke-opacity=".4"/>
      <!-- Scanning Line Animation -->
      <line x1="24" y1="75" x2="366" y2="75" stroke="#38BDF8" stroke-width="1.8" filter="url(#p2-glowf)">
        <animate attributeName="y1" values="55;155;55" dur="4s" repeatCount="indefinite"/>
        <animate attributeName="y2" values="55;155;55" dur="4s" repeatCount="indefinite"/>
      </line>
      <text class="p2-mono" x="36" y="74" font-size="10" fill="#64748B">int maxSubArray(vector&lt;int&gt;&amp; nums) {</text>
      <text class="p2-mono" x="56" y="94" font-size="10" fill="#38BDF8">int cur = 0, best = INT_MIN;</text>
      <text class="p2-mono" x="56" y="114" font-size="10" fill="#60A5FA">for(int x : nums) { cur = max(x, cur+x); ... }</text>
      <text class="p2-mono" x="36" y="134" font-size="10" fill="#64748B">}</text>

      <!-- Proof Pill -->
      <g transform="translate(24, 176)">
        <rect width="342" height="46" rx="8" fill="#0A1838" stroke="#38BDF8" stroke-width="1"/>
        <text class="p2-mono" x="16" y="20" font-size="10.5" fill="#F0F9FF">ALGORITHMIC PROOF: Kadane's Dynamic DP</text>
        <text class="p2-mono" x="16" y="36" font-size="9.5" fill="#34D399">✓ Time: O(N) · Space: O(1) · Optimal Verification Passed</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#1E3A8A" stroke-opacity=".4"/>
    <rect class="p2-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#p2-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_pashatools_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p3-t">
  <title id="p3-t">Pasha Tools: High-speed browser media suite for instant audio/video manipulation</title>
  <defs>
    <linearGradient id="p3-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="p3-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".3"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p3-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="p3-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="p3-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="p3-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0F9FF"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .p3-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .p3-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .p3-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .p3-in { animation: p3-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .p3-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: p3-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes p3-in { from { opacity: 0; } to { opacity: 1; } }
    @keyframes p3-draw { to { stroke-dashoffset: 0; } }
    .p3-trace { stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: p3-trace 7s linear infinite; }
    @keyframes p3-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .p3-in { animation: none; } .p3-draw { animation: none; } .p3-trace { display: none; } }
  </style>

  <g clip-path="url(#p3-clip)">
    <rect width="1200" height="370" fill="url(#p3-bg)"/>
    <rect x="700" width="500" height="370" fill="url(#p3-grid)"/>
    <rect width="1200" height="370" fill="url(#p3-glow)"/>

    <!-- Left Details -->
    <g class="p3-in" transform="translate(56, 48)">
      <text class="p3-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">03 · UTILITY PLATFORM · MEDIA ENGINE · 2026</text>
      <text class="p3-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F0F9FF">Pasha Tools</text>
      <text class="p3-sans" y="94" font-size="16.5" fill="#94A3B8">High-speed browser media suite engineered for zero-friction workflows.</text>
      <text class="p3-mono" y="126" font-size="12" fill="#E0F2FE"><tspan fill="#38BDF8">BUILT ›</tspan> In-memory FFmpeg video converter, audio extraction, instant document suite</text>
      <line class="p3-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="p3-serif" font-size="32" font-weight="300" fill="#F0F9FF">0s</text>
        <text class="p3-sans" y="22" font-size="12" fill="#94A3B8">Zero Signup Barrier</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="p3-serif" font-size="32" font-weight="300" fill="#F0F9FF">100%</text>
        <text class="p3-sans" y="22" font-size="12" fill="#94A3B8">Client-Side Privacy</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="p3-serif" font-size="32" font-weight="300" fill="#34D399">Live</text>
        <text class="p3-sans" y="22" font-size="12" fill="#94A3B8">Production Global Edge</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="64" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p3-mono" x="32" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">React</text></g>
        <g transform="translate(72, 0)"><rect width="70" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p3-mono" x="35" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">FastAPI</text></g>
        <g transform="translate(150, 0)"><rect width="66" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p3-mono" x="33" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Python</text></g>
        <g transform="translate(224, 0)"><rect width="72" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p3-mono" x="36" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">FFmpeg</text></g>
        <g transform="translate(304, 0)"><rect width="68" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p3-mono" x="34" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Docker</text></g>
        <g transform="translate(380, 0)"><rect width="74" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p3-mono" x="37" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Railway</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Audio Wave & Conversion Stream -->
    <g transform="translate(740, 60)" class="p3-in">
      <rect width="390" height="240" rx="12" fill="#071228" stroke="#1E3A8A" stroke-opacity=".6"/>
      <rect width="390" height="34" rx="12" fill="#0A1838"/>
      <text class="p3-mono" x="20" y="21" font-size="11" fill="#E0F2FE">FFMPEG // IN-MEMORY STREAM PIPELINE</text>

      <!-- Conversion Flow Blocks -->
      <g transform="translate(24, 52)">
        <rect width="90" height="74" rx="8" fill="#0B1A3D" stroke="#0066FF"/>
        <text class="p3-mono" x="45" y="34" text-anchor="middle" font-size="12" fill="#F0F9FF">.MP4</text>
        <text class="p3-mono" x="45" y="52" text-anchor="middle" font-size="9" fill="#94A3B8">4K H.264</text>

        <!-- Dynamic Arrow -->
        <line x1="96" y1="37" x2="140" y2="37" stroke="#38BDF8" stroke-width="2" filter="url(#p3-glowf)"/>
        <polygon points="144,37 136,33 136,41" fill="#38BDF8"/>

        <rect x="150" width="90" height="74" rx="8" fill="#0B1A3D" stroke="#38BDF8"/>
        <text class="p3-mono" x="195" y="34" text-anchor="middle" font-size="12" fill="#38BDF8">WASM</text>
        <text class="p3-mono" x="195" y="52" text-anchor="middle" font-size="9" fill="#E0F2FE">FFMPEG</text>

        <!-- Dynamic Arrow -->
        <line x1="246" y1="37" x2="290" y2="37" stroke="#38BDF8" stroke-width="2" filter="url(#p3-glowf)"/>
        <polygon points="294,37 286,33 286,41" fill="#38BDF8"/>

        <rect x="300" width="40" height="74" rx="8" fill="#0B1A3D" stroke="#10B981"/>
        <text class="p3-mono" x="320" y="34" text-anchor="middle" font-size="11" fill="#10B981">MP3</text>
        <text class="p3-mono" x="320" y="52" text-anchor="middle" font-size="9" fill="#34D399">HQ</text>
      </g>

      <!-- Waveform Visualization -->
      <g transform="translate(24, 146)">
        <rect width="342" height="74" rx="8" fill="#040916" stroke="#1E3A8A" stroke-opacity=".5"/>
        <g fill="#38BDF8" filter="url(#p3-glowf)">
          <rect x="20" y="24" width="4" height="26" rx="2"><animate attributeName="height" values="26;12;26" dur="1.2s" repeatCount="indefinite"/></rect>
          <rect x="32" y="16" width="4" height="42" rx="2"><animate attributeName="height" values="42;20;42" dur="1.5s" repeatCount="indefinite"/></rect>
          <rect x="44" y="28" width="4" height="18" rx="2"><animate attributeName="height" values="18;35;18" dur="1.1s" repeatCount="indefinite"/></rect>
          <rect x="56" y="12" width="4" height="50" rx="2"><animate attributeName="height" values="50;15;50" dur="1.8s" repeatCount="indefinite"/></rect>
          <rect x="68" y="20" width="4" height="34" rx="2"><animate attributeName="height" values="34;48;34" dur="1.4s" repeatCount="indefinite"/></rect>
          <rect x="80" y="14" width="4" height="46" rx="2"><animate attributeName="height" values="46;22;46" dur="1.3s" repeatCount="indefinite"/></rect>
          <rect x="92" y="26" width="4" height="22" rx="2"><animate attributeName="height" values="22;40;22" dur="1.6s" repeatCount="indefinite"/></rect>
          <rect x="104" y="10" width="4" height="54" rx="2"><animate attributeName="height" values="54;18;54" dur="1.7s" repeatCount="indefinite"/></rect>
          <rect x="116" y="22" width="4" height="30" rx="2"/>
          <rect x="128" y="14" width="4" height="46" rx="2"/>
          <rect x="140" y="30" width="4" height="14" rx="2"/>
        </g>
        <text class="p3-mono" x="170" y="36" font-size="10.5" fill="#F0F9FF">AUDIO LOSSLESS RIP</text>
        <text class="p3-mono" x="170" y="52" font-size="9" fill="#10B981">✓ Zero Memory Leak · 320 kbps</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#1E3A8A" stroke-opacity=".4"/>
    <rect class="p3-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#p3-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_bmw7_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p4-t">
  <title id="p4-t">BMW 7-Series 3D Experience: Photorealistic 3D automotive configurator engineered with custom GLSL raymarching shaders</title>
  <defs>
    <linearGradient id="p4-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="p4-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#38BDF8" stop-opacity=".25"/><stop offset="100%" stop-color="#38BDF8" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p4-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="p4-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="p4-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="p4-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0F9FF"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
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
      <text class="p4-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">04 · 3D COMPUTING · GLSL SHADERS · 2026</text>
      <text class="p4-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F0F9FF">BMW 7-Series 3D</text>
      <text class="p4-sans" y="94" font-size="16.5" fill="#94A3B8">Photorealistic automotive showroom running seamlessly in the browser.</text>
      <text class="p4-mono" y="126" font-size="12" fill="#E0F2FE"><tspan fill="#38BDF8">BUILT ›</tspan> Custom GLSL raymarching shaders, cinematic camera director orbits, Draco</text>
      <line class="p4-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="p4-serif" font-size="32" font-weight="300" fill="#F0F9FF">60 FPS</text>
        <text class="p4-sans" y="22" font-size="12" fill="#94A3B8">WebGL Raymarching</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="p4-serif" font-size="32" font-weight="300" fill="#F0F9FF">Draco</text>
        <text class="p4-sans" y="22" font-size="12" fill="#94A3B8">Mesh Compression</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="p4-serif" font-size="32" font-weight="300" fill="#34D399">Live</text>
        <text class="p4-sans" y="22" font-size="12" fill="#94A3B8">Interactive 3D Showroom</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="76" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p4-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Three.js</text></g>
        <g transform="translate(84, 0)"><rect width="70" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p4-mono" x="35" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">WebGL</text></g>
        <g transform="translate(162, 0)"><rect width="98" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p4-mono" x="49" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">GLSL Shaders</text></g>
        <g transform="translate(268, 0)"><rect width="64" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p4-mono" x="32" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">React</text></g>
        <g transform="translate(340, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p4-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">TypeScript</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: 3D Wireframe Car & Orbital Orbit -->
    <g transform="translate(740, 60)" class="p4-in">
      <rect width="390" height="240" rx="12" fill="#071228" stroke="#1E3A8A" stroke-opacity=".6"/>
      <rect width="390" height="34" rx="12" fill="#0A1838"/>
      <text class="p4-mono" x="20" y="21" font-size="11" fill="#E0F2FE">GLSL SHADER // 3D AUTOMOTIVE VIEWPORT</text>

      <!-- 3D Car Wireframe Silhouette -->
      <g transform="translate(45, 60)">
        <ellipse cx="150" cy="80" rx="140" ry="25" fill="none" stroke="#1E3A8A" stroke-dasharray="4 6"/>
        <ellipse cx="150" cy="80" rx="110" ry="18" fill="none" stroke="#38BDF8" stroke-opacity=".3"/>

        <!-- Streamlined Vehicle Silhouette -->
        <path d="M 20 80 Q 45 40, 95 38 Q 145 20, 205 28 Q 260 38, 280 80 Z" fill="#071536" stroke="#38BDF8" stroke-width="1.8" filter="url(#p4-glowf)"/>
        <!-- Cockpit Glass -->
        <path d="M 95 38 Q 135 24, 185 28 Q 215 36, 225 48 L 85 48 Z" fill="#38BDF8" fill-opacity=".25" stroke="#60A5FA"/>
        <!-- Wheel Wells -->
        <circle cx="70" cy="80" r="16" fill="#030712" stroke="#38BDF8" stroke-width="1.5"/>
        <circle cx="230" cy="80" r="16" fill="#030712" stroke="#38BDF8" stroke-width="1.5"/>

        <!-- Orbiting Camera Marker -->
        <circle cx="270" cy="65" r="4.5" fill="#38BDF8" filter="url(#p4-glowf)">
          <animate attributeName="cx" values="270;30;270" dur="6s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
        </circle>
      </g>

      <!-- Shaders HUD Details -->
      <g transform="translate(24, 174)">
        <rect width="342" height="46" rx="8" fill="#0B1A3D" stroke="#0066FF" stroke-width="1.2"/>
        <text class="p4-mono" x="16" y="20" font-size="10.5" fill="#F0F9FF">CLEAR-COAT GLSL RAYMARCHING</text>
        <text class="p4-mono" x="16" y="36" font-size="9.5" fill="#38BDF8">Metallic Flake: 0.85 · Roughness: 0.12 · Draco Compressed</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#1E3A8A" stroke-opacity=".4"/>
    <rect class="p4-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#p4-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_wishora_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p5-t">
  <title id="p5-t">Wishora: Instant personalized greeting card platform featuring frictionless client-side canvas rendering</title>
  <defs>
    <linearGradient id="p5-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="p5-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".3"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p5-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="p5-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="p5-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="p5-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0F9FF"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .p5-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .p5-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .p5-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .p5-in { animation: p5-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .p5-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: p5-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes p5-in { from { opacity: 0; } to { opacity: 1; } }
    @keyframes p5-draw { to { stroke-dashoffset: 0; } }
    .p5-trace { stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: p5-trace 7s linear infinite; }
    @keyframes p5-trace { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .p5-in { animation: none; } .p5-draw { animation: none; } .p5-trace { display: none; } }
  </style>

  <g clip-path="url(#p5-clip)">
    <rect width="1200" height="370" fill="url(#p5-bg)"/>
    <rect x="700" width="500" height="370" fill="url(#p5-grid)"/>
    <rect width="1200" height="370" fill="url(#p5-glow)"/>

    <!-- Left Details -->
    <g class="p5-in" transform="translate(56, 48)">
      <text class="p5-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">05 · INTERACTIVE WEB · CANVAS MOTION · 2026</text>
      <text class="p5-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F0F9FF">Wishora</text>
      <text class="p5-sans" y="94" font-size="16.5" fill="#94A3B8">Instant personalized greeting card platform featuring 60 FPS neon canvas motion.</text>
      <text class="p5-mono" y="126" font-size="12" fill="#E0F2FE"><tspan fill="#38BDF8">BUILT ›</tspan> Client-side HTML5 canvas rendering, instant PNG export, Framer Motion</text>
      <line class="p5-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="p5-serif" font-size="32" font-weight="300" fill="#F0F9FF">60 FPS</text>
        <text class="p5-sans" y="22" font-size="12" fill="#94A3B8">Fluid Canvas Motion</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="p5-serif" font-size="32" font-weight="300" fill="#F0F9FF">Instant</text>
        <text class="p3-sans" y="22" font-size="12" fill="#94A3B8">Client PNG Export</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="p5-serif" font-size="32" font-weight="300" fill="#34D399">Live</text>
        <text class="p5-sans" y="22" font-size="12" fill="#94A3B8">Production Worldwide</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p5-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Next.js 15</text></g>
        <g transform="translate(98, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p5-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">TypeScript</text></g>
        <g transform="translate(196, 0)"><rect width="96" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p5-mono" x="48" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Tailwind CSS</text></g>
        <g transform="translate(300, 0)"><rect width="106" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="p5-mono" x="53" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Framer Motion</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Digital Greeting Card Canvas -->
    <g transform="translate(740, 60)" class="p5-in">
      <rect width="390" height="240" rx="12" fill="#071228" stroke="#1E3A8A" stroke-opacity=".6"/>
      <rect width="390" height="34" rx="12" fill="#0A1838"/>
      <text class="p5-mono" x="20" y="21" font-size="11" fill="#E0F2FE">CANVAS 2D // REAL-TIME GREETING STUDIO</text>

      <!-- Card Frame inside Canvas -->
      <g transform="translate(45, 52)">
        <rect width="300" height="110" rx="10" fill="#0B1A3D" stroke="#38BDF8" stroke-width="1.5"/>
        <circle cx="150" cy="45" r="24" fill="#0066FF" fill-opacity=".3" filter="url(#p5-glowf)"/>
        <text class="p5-serif" x="150" y="52" text-anchor="middle" font-size="20" font-style="italic" fill="#F0F9FF">Happy Celebrations</text>
        <text class="p5-mono" x="150" y="74" text-anchor="middle" font-size="10" fill="#38BDF8">Crafted with Wishora Engine</text>

        <!-- Floating Sparkles -->
        <circle cx="60" cy="30" r="2.5" fill="#60A5FA"/>
        <circle cx="240" cy="35" r="2" fill="#93C5FD"/>
        <circle cx="75" cy="85" r="1.5" fill="#38BDF8"/>
        <circle cx="225" cy="80" r="2" fill="#60A5FA"/>
      </g>

      <!-- Instant Export Pill -->
      <g transform="translate(24, 176)">
        <rect width="342" height="46" rx="8" fill="#050E24" stroke="#0066FF" stroke-width="1.2"/>
        <text class="p5-mono" x="16" y="20" font-size="10.5" fill="#F0F9FF">INSTANT HARDWARE ACCELERATED PNG</text>
        <text class="p5-mono" x="16" y="36" font-size="9.5" fill="#34D399">✓ 300 DPI Export · Zero Server Load · P2P Viral Distribution</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#1E3A8A" stroke-opacity=".4"/>
    <rect class="p5-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#p5-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


def build_project_devpilot_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="pdp-t">
  <title id="pdp-t">Pasha DevPilot: Autonomous AI Software Engineer built for IBM Bob 2.0 Hackathon</title>
  <defs>
    <linearGradient id="pdp-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="pdp-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".3"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="pdp-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="pdp-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="pdp-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="pdp-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0F9FF"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
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
      <text class="pdp-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">🏆 HACKATHON FLAGSHIP · AUTONOMOUS SDLC · 2026</text>
      <text class="pdp-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F0F9FF">Pasha DevPilot</text>
      <text class="pdp-sans" y="94" font-size="16.5" fill="#94A3B8">Your autonomous AI software engineer — Understand, Plan, Build, Verify, Ship.</text>
      <text class="pdp-mono" y="126" font-size="12" fill="#E0F2FE"><tspan fill="#38BDF8">BUILT ›</tspan> 7-state automated SDLC pipeline, AST defect scanner, pytest auto-healing, IBM Bob 2.0</text>
      <line class="pdp-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="pdp-serif" font-size="32" font-weight="300" fill="#F0F9FF">7 States</text>
        <text class="pdp-sans" y="22" font-size="12" fill="#94A3B8">Autonomous Pipeline</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="pdp-serif" font-size="32" font-weight="300" fill="#F0F9FF">11/11</text>
        <text class="pdp-sans" y="22" font-size="12" fill="#94A3B8">Pytest Auto-Healed</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="pdp-serif" font-size="32" font-weight="300" fill="#34D399">IBM Bob</text>
        <text class="pdp-sans" y="22" font-size="12" fill="#94A3B8">Hackathon Entry Live</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pdp-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Next.js 15</text></g>
        <g transform="translate(98, 0)"><rect width="70" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pdp-mono" x="35" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">FastAPI</text></g>
        <g transform="translate(176, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pdp-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">IBM Bob 2.0</text></g>
        <g transform="translate(274, 0)"><rect width="80" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pdp-mono" x="40" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Python</text></g>
        <g transform="translate(362, 0)"><rect width="68" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pdp-mono" x="34" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Docker</text></g>
        <g transform="translate(438, 0)"><rect width="74" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pdp-mono" x="37" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Railway</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: 7-State SDLC Autonomous Agent Pipeline -->
    <g transform="translate(740, 60)" class="pdp-in">
      <rect width="390" height="240" rx="12" fill="#071228" stroke="#1E3A8A" stroke-opacity=".6"/>
      <rect width="390" height="34" rx="12" fill="#0A1838"/>
      <text class="pdp-mono" x="20" y="21" font-size="11" fill="#E0F2FE">AUTONOMOUS SDLC // 7-STATE ENGINE</text>
      <text class="pdp-mono" x="370" y="21" text-anchor="end" font-size="10" fill="#10B981">● SHIPPED</text>

      <!-- Pipeline Steps Row 1 -->
      <g transform="translate(20, 52)">
        <g transform="translate(0, 0)">
          <rect width="76" height="50" rx="6" fill="#0B1A3D" stroke="#38BDF8" stroke-width="1.2"/>
          <text class="pdp-mono" x="38" y="22" text-anchor="middle" font-size="10" fill="#38BDF8">01 SCAN</text>
          <text class="pdp-mono" x="38" y="38" text-anchor="middle" font-size="8.5" fill="#94A3B8">AST Tree</text>
        </g>
        <line x1="76" y1="25" x2="92" y2="25" stroke="#38BDF8" stroke-width="1.5"/>

        <g transform="translate(92, 0)">
          <rect width="76" height="50" rx="6" fill="#0B1A3D" stroke="#0066FF" stroke-width="1.2"/>
          <text class="pdp-mono" x="38" y="22" text-anchor="middle" font-size="10" fill="#E0F2FE">02 REASON</text>
          <text class="pdp-mono" x="38" y="38" text-anchor="middle" font-size="8.5" fill="#38BDF8">IBM Bob</text>
        </g>
        <line x1="168" y1="25" x2="184" y2="25" stroke="#38BDF8" stroke-width="1.5"/>

        <g transform="translate(184, 0)">
          <rect width="76" height="50" rx="6" fill="#0B1A3D" stroke="#0066FF" stroke-width="1.2"/>
          <text class="pdp-mono" x="38" y="22" text-anchor="middle" font-size="10" fill="#E0F2FE">03 PLAN</text>
          <text class="pdp-mono" x="38" y="38" text-anchor="middle" font-size="8.5" fill="#94A3B8">Patch Graph</text>
        </g>
        <line x1="260" y1="25" x2="276" y2="25" stroke="#38BDF8" stroke-width="1.5"/>

        <g transform="translate(276, 0)">
          <rect width="74" height="50" rx="6" fill="#0B1A3D" stroke="#10B981" stroke-width="1.2"/>
          <text class="pdp-mono" x="37" y="22" text-anchor="middle" font-size="10" fill="#10B981">04 BUILD</text>
          <text class="pdp-mono" x="37" y="38" text-anchor="middle" font-size="8.5" fill="#34D399">Auto-Code</text>
        </g>
      </g>

      <!-- Pipeline Steps Row 2 -->
      <g transform="translate(20, 114)">
        <g transform="translate(0, 0)">
          <rect width="108" height="46" rx="6" fill="#0B1A3D" stroke="#38BDF8" stroke-width="1.2"/>
          <text class="pdp-mono" x="54" y="20" text-anchor="middle" font-size="10" fill="#38BDF8">05 SANDBOX</text>
          <text class="pdp-mono" x="54" y="35" text-anchor="middle" font-size="8.5" fill="#94A3B8">Isolated Exec</text>
        </g>
        <line x1="108" y1="23" x2="124" y2="23" stroke="#38BDF8" stroke-width="1.5"/>

        <g transform="translate(124, 0)">
          <rect width="112" height="46" rx="6" fill="#0B1A3D" stroke="#10B981" stroke-width="1.2"/>
          <text class="pdp-mono" x="56" y="20" text-anchor="middle" font-size="10" fill="#10B981">06 VERIFY</text>
          <text class="pdp-mono" x="56" y="35" text-anchor="middle" font-size="8.5" fill="#34D399">11/11 Passed</text>
        </g>
        <line x1="236" y1="23" x2="252" y2="23" stroke="#38BDF8" stroke-width="1.5"/>

        <g transform="translate(252, 0)">
          <rect width="98" height="46" rx="6" fill="#0B1A3D" stroke="#34D399" stroke-width="1.5"/>
          <text class="pdp-mono" x="49" y="20" text-anchor="middle" font-size="10" fill="#34D399">07 SHIP</text>
          <text class="pdp-mono" x="49" y="35" text-anchor="middle" font-size="8.5" fill="#E0F2FE">1-Click Push</text>
        </g>
      </g>

      <!-- Bottom Status Pill -->
      <g transform="translate(20, 172)">
        <rect width="350" height="50" rx="8" fill="#040916" stroke="#0066FF" stroke-width="1.2"/>
        <text class="pdp-mono" x="16" y="22" font-size="10.5" fill="#F0F9FF">DEFECTS RESOLVED &amp; VERIFIED</text>
        <text class="pdp-mono" x="16" y="38" font-size="9.5" fill="#34D399">✓ 9 AST defects resolved · Zero-PAT OAuth · Production Live</text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#1E3A8A" stroke-opacity=".4"/>
    <rect class="pdp-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#pdp-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""




# ─────────────────────────────────────────────────────────────────────────────
# BESPOKE PROJECT: SYNCFORGE (1200 x 370)
# ─────────────────────────────────────────────────────────────────────────────
def build_project_syncforge_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="psf-t">
  <title id="psf-t">SyncForge: Real-Time Multi-Cursor Collaborative Code Editor and Mesh Voice Studio</title>
  <defs>
    <linearGradient id="psf-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="psf-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".3"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="psf-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="psf-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="psf-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="psf-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0F9FF"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
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
      <text class="psf-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">02 · REAL-TIME DISTRIBUTED SYSTEMS · WEBRTC · 2026</text>
      <text class="psf-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F0F9FF">SyncForge</text>
      <text class="psf-sans" y="94" font-size="16.5" fill="#94A3B8">Real-time multi-cursor collaboration, instant rooms &amp; peer-to-peer voice mesh.</text>
      <text class="psf-mono" y="126" font-size="12" fill="#E0F2FE"><tspan fill="#38BDF8">BUILT ›</tspan> Monaco Editor, delta-sync WebSockets, WebRTC mesh audio, FastAPI, React 19</text>
      <line class="psf-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="psf-serif" font-size="32" font-weight="300" fill="#F0F9FF">&lt; 10ms</text>
        <text class="psf-sans" y="22" font-size="12" fill="#94A3B8">Delta Sync Latency</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="psf-serif" font-size="32" font-weight="300" fill="#F0F9FF">10+ Langs</text>
        <text class="psf-sans" y="22" font-size="12" fill="#94A3B8">Monaco IntelliSense</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="psf-serif" font-size="32" font-weight="300" fill="#34D399">Mesh Voice</text>
        <text class="psf-sans" y="22" font-size="12" fill="#94A3B8">WebRTC P2P Audio</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="84" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="psf-mono" x="42" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">React 19</text></g>
        <g transform="translate(92, 0)"><rect width="70" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="psf-mono" x="35" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Vite 6</text></g>
        <g transform="translate(170, 0)"><rect width="114" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="psf-mono" x="57" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Monaco Editor</text></g>
        <g transform="translate(292, 0)"><rect width="76" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="psf-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">FastAPI</text></g>
        <g transform="translate(376, 0)"><rect width="98" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="psf-mono" x="49" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">WebSockets</text></g>
        <g transform="translate(482, 0)"><rect width="76" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="psf-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">WebRTC</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Monaco Multi-Cursor & WebRTC Mesh Room -->
    <g transform="translate(740, 60)" class="psf-in">
      <rect width="390" height="240" rx="12" fill="#071228" stroke="#1E3A8A" stroke-opacity=".6"/>
      <rect width="390" height="34" rx="12" fill="#0A1838"/>
      <text class="psf-mono" x="20" y="21" font-size="11" fill="#E0F2FE">SYNCFORGE // ROOM #SYNC-992</text>
      <text class="psf-mono" x="370" y="21" text-anchor="end" font-size="10" fill="#10B981">● 3 PEERS LIVE</text>

      <!-- Monaco Editor Code View -->
      <g transform="translate(18, 48)">
        <rect width="354" height="136" rx="8" fill="#030814" stroke="#1E3A8A" stroke-opacity=".5"/>
        <text class="psf-mono" x="14" y="24" font-size="9.5" fill="#64748B">01  <tspan fill="#60A5FA">// Broadcast AST delta with sub-10ms lock</tspan></text>
        <text class="psf-mono" x="14" y="44" font-size="9.5" fill="#64748B">02  <tspan fill="#38BDF8">export async function</tspan> <tspan fill="#F0F9FF">syncCode</tspan>(delta: <tspan fill="#34D399">Delta</tspan>) {</text>
        <text class="psf-mono" x="14" y="64" font-size="9.5" fill="#64748B">03    <tspan fill="#38BDF8">await</tspan> ws.<tspan fill="#F0F9FF">broadcast</tspan>(<tspan fill="#34D399">"code-change"</tspan>, delta);</text>
        <text class="psf-mono" x="14" y="84" font-size="9.5" fill="#64748B">04    webrtc.<tspan fill="#F0F9FF">relayVoiceMesh</tspan>(room.peers);</text>
        <text class="psf-mono" x="14" y="104" font-size="9.5" fill="#64748B">05  }</text>

        <!-- Pasha Cursor Tag -->
        <g transform="translate(230, 52)">
          <line x1="0" y1="0" x2="0" y2="16" stroke="#38BDF8" stroke-width="2"/>
          <rect x="0" y="-12" width="54" height="14" rx="3" fill="#0066FF"/>
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
        <rect width="354" height="32" rx="6" fill="#0A1838" stroke="#1E3A8A" stroke-opacity=".7"/>
        <text class="psf-mono" x="14" y="20" font-size="9.5" fill="#94A3B8">WS: <tspan fill="#38BDF8">DELTA SYNC</tspan> · AUDIO: <tspan fill="#34D399">WEBRTC MESH</tspan> · LATENCY: <tspan fill="#10B981">8ms</tspan></text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#1E3A8A" stroke-opacity=".4"/>
    <rect class="psf-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#psf-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# BESPOKE PROJECT: PRIVATEDOC (1200 x 370)
# ─────────────────────────────────────────────────────────────────────────────
def build_project_privatedoc_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="ppd-t">
  <title id="ppd-t">PrivateDoc: On-Device Private AI Document Intelligence with Local Llama 3.2</title>
  <defs>
    <linearGradient id="ppd-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="ppd-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".3"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="ppd-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="ppd-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="ppd-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="ppd-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0F9FF"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
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
      <text class="ppd-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">03 · ON-DEVICE EDGE AI · ZERO CLOUD LEAK · 2026</text>
      <text class="ppd-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F0F9FF">PrivateDoc</text>
      <text class="ppd-sans" y="94" font-size="16.5" fill="#94A3B8">Your family's offline document AI — zero cloud telemetry, 100% on-device SLM.</text>
      <text class="ppd-mono" y="126" font-size="12" fill="#E0F2FE"><tspan fill="#38BDF8">BUILT ›</tspan> Android 36, ExecuTorch 1.3, Llama 3.2 1B (SpinQuant INT4), ML Kit OCR, Compose</text>
      <line class="ppd-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="ppd-serif" font-size="32" font-weight="300" fill="#34D399">0 KB</text>
        <text class="ppd-sans" y="22" font-size="12" fill="#94A3B8">Cloud Telemetry Leak</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="ppd-serif" font-size="32" font-weight="300" fill="#F0F9FF">Llama 3.2</text>
        <text class="ppd-sans" y="22" font-size="12" fill="#94A3B8">1B INT4 On-Device</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="ppd-serif" font-size="32" font-weight="300" fill="#F0F9FF">100% Offline</text>
        <text class="ppd-sans" y="22" font-size="12" fill="#94A3B8">Zero Network Permission</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="ppd-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Android 36</text></g>
        <g transform="translate(98, 0)"><rect width="80" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="ppd-mono" x="40" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Kotlin 2.3</text></g>
        <g transform="translate(186, 0)"><rect width="102" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="ppd-mono" x="51" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">ExecuTorch 1.3</text></g>
        <g transform="translate(296, 0)"><rect width="128" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="ppd-mono" x="64" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Llama 3.2 (INT4)</text></g>
        <g transform="translate(432, 0)"><rect width="90" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="ppd-mono" x="45" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">ML Kit OCR</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Local On-Device Inference HUD -->
    <g transform="translate(740, 60)" class="ppd-in">
      <rect width="390" height="240" rx="12" fill="#071228" stroke="#1E3A8A" stroke-opacity=".6"/>
      <rect width="390" height="34" rx="12" fill="#0A1838"/>
      <text class="ppd-mono" x="20" y="21" font-size="11" fill="#E0F2FE">PRIVATEDOC // LOCAL SLM INFERENCE</text>
      <text class="ppd-mono" x="370" y="21" text-anchor="end" font-size="10" fill="#10B981">🛡️ AIR-GAPPED</text>

      <!-- Scan & Inference Container -->
      <g transform="translate(18, 48)">
        <rect width="354" height="136" rx="8" fill="#030814" stroke="#1E3A8A" stroke-opacity=".5"/>
        <text class="ppd-mono" x="14" y="24" font-size="9.5" fill="#64748B">SCAN › <tspan fill="#38BDF8">Prescription_Rx08.pdf</tspan> · <tspan fill="#34D399">OCR 99.4%</tspan></text>
        <line x1="14" y1="34" x2="340" y2="34" stroke="#1E3A8A" stroke-opacity=".4"/>
        <text class="ppd-mono" x="14" y="54" font-size="9.5" fill="#94A3B8">USER: <tspan fill="#F0F9FF">"What is the daily dosage for Amoxicillin?"</tspan></text>
        
        <!-- SLM Response Box -->
        <rect x="14" y="68" width="326" height="52" rx="6" fill="#07142E" stroke="#38BDF8" stroke-width="1"/>
        <text class="ppd-mono" x="24" y="88" font-size="9.5" fill="#38BDF8">EXECUTORCH (LLAMA 3.2 1B INT4):</text>
        <text class="ppd-mono" x="24" y="106" font-size="9.5" fill="#34D399">✓ "Take 500mg every 8 hours with water after meals."</text>
      </g>

      <!-- Bottom Status Pill -->
      <g transform="translate(18, 196)">
        <rect width="354" height="32" rx="6" fill="#0A1838" stroke="#1E3A8A" stroke-opacity=".7"/>
        <text class="ppd-mono" x="14" y="20" font-size="9.5" fill="#94A3B8">NETWORK: <tspan fill="#10B981">DISABLED</tspan> · ON-DEVICE: <tspan fill="#38BDF8">140ms</tspan> · DATA EXPORT: <tspan fill="#10B981">0 BYTES</tspan></text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#1E3A8A" stroke-opacity=".4"/>
    <rect class="ppd-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#ppd-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# BESPOKE PROJECT: GHOSTREVIEW (1200 x 370)
# ─────────────────────────────────────────────────────────────────────────────
def build_project_ghostreview_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="pgr-t">
  <title id="pgr-t">GhostReview: AI-Powered Code Intelligence and Autonomous PR Review Engine</title>
  <defs>
    <linearGradient id="pgr-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="pgr-glow" cx="80%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".3"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="pgr-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="pgr-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="pgr-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="pgr-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F0F9FF"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/>
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
      <text class="pgr-mono" font-size="12" letter-spacing="2.6" fill="#38BDF8">04 · REPOSITORY AUDITING · GROQ LLM INFERENCE · 2026</text>
      <text class="pgr-serif" y="58" font-size="48" font-weight="300" letter-spacing="-1.5" fill="#F0F9FF">GhostReview</text>
      <text class="pgr-sans" y="94" font-size="16.5" fill="#94A3B8">AI-powered code intelligence — automated bug hunting, PR reviews &amp; doc generation.</text>
      <text class="pgr-mono" y="126" font-size="12" fill="#E0F2FE"><tspan fill="#38BDF8">BUILT ›</tspan> React 19, FastAPI, Groq LLM sub-second reasoning, Celery, Redis, Vite 8</text>
      <line class="pgr-draw" x1="0" y1="148" x2="620" y2="148" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(0, 186)">
        <text class="pgr-serif" font-size="32" font-weight="300" fill="#34D399">24 / 24</text>
        <text class="pgr-sans" y="22" font-size="12" fill="#94A3B8">Pytest Tests Passed</text>
      </g>
      <g transform="translate(200, 186)">
        <text class="pgr-serif" font-size="32" font-weight="300" fill="#F0F9FF">&lt; 300ms</text>
        <text class="pgr-sans" y="22" font-size="12" fill="#94A3B8">Groq LLM Latency</text>
      </g>
      <g transform="translate(400, 186)">
        <text class="pgr-serif" font-size="32" font-weight="300" fill="#F0F9FF">0 Errors</text>
        <text class="pgr-sans" y="22" font-size="12" fill="#94A3B8">TypeScript &amp; ESLint</text>
      </g>

      <!-- Tech Stack Chips -->
      <g transform="translate(0, 246)">
        <g transform="translate(0, 0)"><rect width="84" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pgr-mono" x="42" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">React 19</text></g>
        <g transform="translate(92, 0)"><rect width="76" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pgr-mono" x="38" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">FastAPI</text></g>
        <g transform="translate(176, 0)"><rect width="88" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pgr-mono" x="44" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Groq LLM</text></g>
        <g transform="translate(272, 0)"><rect width="74" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pgr-mono" x="37" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Celery</text></g>
        <g transform="translate(354, 0)"><rect width="68" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pgr-mono" x="34" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Redis</text></g>
        <g transform="translate(430, 0)"><rect width="88" height="26" rx="13" fill="#071228" stroke="#1E3A8A"/><text class="pgr-mono" x="44" y="17" text-anchor="middle" font-size="11.5" fill="#38BDF8">Tailwind 4</text></g>
      </g>
    </g>

    <!-- Right Graphic Illustration: Repository Audit Console -->
    <g transform="translate(740, 60)" class="pgr-in">
      <rect width="390" height="240" rx="12" fill="#071228" stroke="#1E3A8A" stroke-opacity=".6"/>
      <rect width="390" height="34" rx="12" fill="#0A1838"/>
      <text class="pgr-mono" x="20" y="21" font-size="11" fill="#E0F2FE">GHOSTREVIEW // REPO AUDIT CONSOLE</text>
      <text class="pgr-mono" x="370" y="21" text-anchor="end" font-size="10" fill="#10B981">⚡ GROQ LPU</text>

      <!-- Terminal View -->
      <g transform="translate(18, 48)">
        <rect width="354" height="136" rx="8" fill="#030814" stroke="#1E3A8A" stroke-opacity=".5"/>
        <text class="pgr-mono" x="14" y="24" font-size="9.5" fill="#64748B">&gt; ghost review --repo pasha804/auth-service</text>
        <text class="pgr-mono" x="14" y="44" font-size="9.5" fill="#38BDF8">[+] AST Analysis: 1,420 lines parsed</text>
        <text class="pgr-mono" x="14" y="64" font-size="9.5" fill="#EF4444">[!] Bug detected (L42): Unhandled null pointer in token refresh</text>
        <text class="pgr-mono" x="14" y="84" font-size="9.5" fill="#34D399">[✓] Auto-patch generated via Groq LLM (240ms)</text>
        <text class="pgr-mono" x="14" y="104" font-size="9.5" fill="#60A5FA">[✓] PR summary &amp; architectural impact compiled</text>
      </g>

      <!-- Bottom Status Pill -->
      <g transform="translate(18, 196)">
        <rect width="354" height="32" rx="6" fill="#0A1838" stroke="#1E3A8A" stroke-opacity=".7"/>
        <text class="pgr-mono" x="14" y="20" font-size="9.5" fill="#94A3B8">TESTS: <tspan fill="#34D399">24/24 PASS</tspan> · LATENCY: <tspan fill="#38BDF8">240ms</tspan> · STATUS: <tspan fill="#10B981">READY TO MERGE</tspan></text>
      </g>
    </g>

    <!-- Animated Border Tracing -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#1E3A8A" stroke-opacity=".4"/>
    <rect class="pgr-trace" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#pgr-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 7. SECTION 04: TOOLKIT / TECH CONSTELLATION (1200 x 440)
# ─────────────────────────────────────────────────────────────────────────────
def build_tech_constellation_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="1200" height="440" role="img" aria-label="Tech Stack and Arsenal">
  <defs>
    <linearGradient id="tc-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="tc-glow" cx="50%" cy="50%" r="65%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".2"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="tc-grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 H 0 V 30" fill="none" stroke="#1E3A8A" stroke-opacity=".15"/>
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
      <rect width="210" height="360" rx="10" fill="#071228" stroke="#1E3A8A" stroke-opacity=".5"/>
      <line x1="0" y1="0" x2="210" y2="0" stroke="#38BDF8" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#38BDF8">01 // LANGUAGES</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F0F9FF">Core Foundation</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E0F2FE">
        <text y="0"><tspan fill="#38BDF8">▸</tspan> TypeScript</text>
        <text y="30"><tspan fill="#38BDF8">▸</tspan> JavaScript (ESNext)</text>
        <text y="60"><tspan fill="#38BDF8">▸</tspan> Python (Asyncio)</text>
        <text y="90"><tspan fill="#38BDF8">▸</tspan> Rust (Tauri / Core)</text>
        <text y="120"><tspan fill="#38BDF8">▸</tspan> SQL (Postgres)</text>
        <text y="150"><tspan fill="#38BDF8">▸</tspan> C / C++</text>
        <text y="180"><tspan fill="#38BDF8">▸</tspan> HTML5 / CSS3</text>
        <text y="210"><tspan fill="#38BDF8">▸</tspan> GLSL Shaders</text>
      </g>
    </g>

    <!-- Column 2: AI & Machine Learning -->
    <g transform="translate(228, 0)">
      <rect width="210" height="360" rx="10" fill="#071228" stroke="#1E3A8A" stroke-opacity=".5"/>
      <line x1="0" y1="0" x2="210" y2="0" stroke="#0066FF" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#38BDF8">02 // AI &amp; ML</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F0F9FF">Intelligence</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E0F2FE">
        <text y="0"><tspan fill="#60A5FA">▸</tspan> Autonomous Agents</text>
        <text y="30"><tspan fill="#60A5FA">▸</tspan> LLM Orchestration</text>
        <text y="60"><tspan fill="#60A5FA">▸</tspan> Vision OCR Engines</text>
        <text y="90"><tspan fill="#60A5FA">▸</tspan> Whisper Audio STT</text>
        <text y="120"><tspan fill="#60A5FA">▸</tspan> Prompt Architecture</text>
        <text y="150"><tspan fill="#60A5FA">▸</tspan> Vector Embeddings</text>
        <text y="180"><tspan fill="#60A5FA">▸</tspan> Live Judging Logic</text>
        <text y="210"><tspan fill="#60A5FA">▸</tspan> Local &amp; Edge Inference</text>
      </g>
    </g>

    <!-- Column 3: Frontend & 3D -->
    <g transform="translate(456, 0)">
      <rect width="210" height="360" rx="10" fill="#071228" stroke="#1E3A8A" stroke-opacity=".5"/>
      <line x1="0" y1="0" x2="210" y2="0" stroke="#38BDF8" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#38BDF8">03 // FRONTEND</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F0F9FF">Interface &amp; 3D</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E0F2FE">
        <text y="0"><tspan fill="#38BDF8">▸</tspan> React 19 / Modern</text>
        <text y="30"><tspan fill="#38BDF8">▸</tspan> Next.js App Router</text>
        <text y="60"><tspan fill="#38BDF8">▸</tspan> Three.js / WebGL</text>
        <text y="90"><tspan fill="#38BDF8">▸</tspan> Raymarching Shaders</text>
        <text y="120"><tspan fill="#38BDF8">▸</tspan> Tailwind CSS</text>
        <text y="150"><tspan fill="#38BDF8">▸</tspan> Framer Motion</text>
        <text y="180"><tspan fill="#38BDF8">▸</tspan> HTML5 Canvas 2D</text>
        <text y="210"><tspan fill="#38BDF8">▸</tspan> Responsive UI/UX</text>
      </g>
    </g>

    <!-- Column 4: Backend & Systems -->
    <g transform="translate(684, 0)">
      <rect width="210" height="360" rx="10" fill="#071228" stroke="#1E3A8A" stroke-opacity=".5"/>
      <line x1="0" y1="0" x2="210" y2="0" stroke="#0066FF" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#38BDF8">04 // BACKEND</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F0F9FF">Engines &amp; Data</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E0F2FE">
        <text y="0"><tspan fill="#60A5FA">▸</tspan> FastAPI (Python)</text>
        <text y="30"><tspan fill="#60A5FA">▸</tspan> Node.js / Express</text>
        <text y="60"><tspan fill="#60A5FA">▸</tspan> PostgreSQL</text>
        <text y="90"><tspan fill="#60A5FA">▸</tspan> Redis Pub/Sub</text>
        <text y="120"><tspan fill="#60A5FA">▸</tspan> Docker / Compose</text>
        <text y="150"><tspan fill="#60A5FA">▸</tspan> REST APIs &amp; WS</text>
        <text y="180"><tspan fill="#60A5FA">▸</tspan> FFmpeg Pipelines</text>
        <text y="210"><tspan fill="#60A5FA">▸</tspan> Microservices</text>
      </g>
    </g>

    <!-- Column 5: Desktop & DevOps -->
    <g transform="translate(912, 0)">
      <rect width="192" height="360" rx="10" fill="#071228" stroke="#1E3A8A" stroke-opacity=".5"/>
      <line x1="0" y1="0" x2="192" y2="0" stroke="#34D399" stroke-width="2.5"/>
      <text class="tc-mono" x="18" y="32" font-size="11" letter-spacing="1.5" fill="#34D399">05 // PLATFORMS</text>
      <text class="tc-serif" x="18" y="62" font-size="20" fill="#F0F9FF">Desktop &amp; CI/CD</text>

      <g transform="translate(18, 90)" class="tc-mono" font-size="12" fill="#E0F2FE">
        <text y="0"><tspan fill="#34D399">▸</tspan> Tauri (Rust/Win)</text>
        <text y="30"><tspan fill="#34D399">▸</tspan> Git &amp; GitHub</text>
        <text y="60"><tspan fill="#34D399">▸</tspan> Actions CI/CD</text>
        <text y="90"><tspan fill="#34D399">▸</tspan> Postman Suite</text>
        <text y="120"><tspan fill="#34D399">▸</tspan> Linux / Bash</text>
        <text y="150"><tspan fill="#34D399">▸</tspan> Vercel &amp; Railway</text>
        <text y="180"><tspan fill="#34D399">▸</tspan> Zero-Config Prod</text>
        <text y="210"><tspan fill="#34D399">▸</tspan> Performance Audit</text>
      </g>
    </g>
  </g>

  <!-- Border -->
  <rect x=".5" y=".5" width="1199" height="439" rx="15.5" fill="none" stroke="#38BDF8" stroke-opacity=".22"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 8. SECTION 06: SYSTEM ARCHITECTURE (1200 x 360)
# ─────────────────────────────────────────────────────────────────────────────
def build_architecture_blueprint_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="1200" height="360" role="img" aria-label="System Architecture Blueprint">
  <defs>
    <linearGradient id="ab-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="ab-glow" cx="50%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".2"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="ab-grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 H 0 V 30" fill="none" stroke="#1E3A8A" stroke-opacity=".15"/>
    </pattern>
    <filter id="ab-glowf" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style>
    .ab-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .ab-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
    .ab-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
  </style>

  <rect width="1200" height="360" rx="16" fill="url(#ab-bg)"/>
  <rect width="1200" height="360" rx="16" fill="url(#ab-grid)"/>
  <rect width="1200" height="360" rx="16" fill="url(#ab-glow)"/>

  <!-- Multi-Tier Pipeline Architecture -->
  <g transform="translate(48, 45)">
    <!-- Node 1: Client Surface -->
    <g transform="translate(0, 40)">
      <rect width="180" height="190" rx="10" fill="#071228" stroke="#1E3A8A" stroke-width="1.2"/>
      <rect width="180" height="30" rx="10" fill="#0A1838"/>
      <text class="ab-mono" x="14" y="20" font-size="11" fill="#38BDF8">01 // CLIENT TIER</text>
      <g transform="translate(14, 52)" class="ab-mono" font-size="11" fill="#E0F2FE">
        <text y="0">Next.js 15 Web</text>
        <text y="24">React Single Page</text>
        <text y="48">Tauri Windows HUD</text>
        <text y="72">Three.js 3D Viewport</text>
        <text y="96">Canvas 2D Engine</text>
      </g>
    </g>

    <!-- Bus 1 -> 2 -->
    <line x1="180" y1="135" x2="250" y2="135" stroke="#38BDF8" stroke-width="2" filter="url(#ab-glowf)"/>
    <circle cx="215" cy="135" r="3.5" fill="#F0F9FF">
      <animate attributeName="cx" values="180;250" dur="2s" repeatCount="indefinite"/>
    </circle>

    <!-- Node 2: Gateway & Edge -->
    <g transform="translate(250, 40)">
      <rect width="180" height="190" rx="10" fill="#071228" stroke="#0066FF" stroke-width="1.2"/>
      <rect width="180" height="30" rx="10" fill="#0A1838"/>
      <text class="ab-mono" x="14" y="20" font-size="11" fill="#38BDF8">02 // EDGE ROUTER</text>
      <g transform="translate(14, 52)" class="ab-mono" font-size="11" fill="#E0F2FE">
        <text y="0">Global CDN / Edge</text>
        <text y="24">Rate Limiting Guard</text>
        <text y="48">JWT Authentication</text>
        <text y="72">WebSocket Gateway</text>
        <text y="96">CORS &amp; SSL Proxy</text>
      </g>
    </g>

    <!-- Bus 2 -> 3 -->
    <line x1="430" y1="135" x2="500" y2="135" stroke="#38BDF8" stroke-width="2" filter="url(#ab-glowf)"/>
    <circle cx="465" cy="135" r="3.5" fill="#F0F9FF">
      <animate attributeName="cx" values="430;500" dur="2s" repeatCount="indefinite"/>
    </circle>

    <!-- Node 3: AI Inference Core -->
    <g transform="translate(500, 20)">
      <rect width="210" height="230" rx="10" fill="#0B1A3D" stroke="#38BDF8" stroke-width="1.8"/>
      <rect width="210" height="34" rx="10" fill="#0F2454"/>
      <text class="ab-mono" x="14" y="22" font-size="11.5" font-weight="700" fill="#F0F9FF">03 // AI INFERENCE CORE</text>
      <g transform="translate(14, 56)" class="ab-mono" font-size="11" fill="#E0F2FE">
        <text y="0" fill="#38BDF8">★ Autonomous Referee</text>
        <text y="24">LLM Reasoning Chains</text>
        <text y="48">Vision OCR Pipeline</text>
        <text y="72">Whisper Audio Stream</text>
        <text y="96">Algorithmic Verification</text>
        <text y="120">Async FastAPI Workers</text>
        <text y="144" fill="#34D399">&lt;80ms Low Latency</text>
      </g>
    </g>

    <!-- Bus 3 -> 4 -->
    <line x1="710" y1="135" x2="780" y2="135" stroke="#38BDF8" stroke-width="2" filter="url(#ab-glowf)"/>
    <circle cx="745" cy="135" r="3.5" fill="#F0F9FF">
      <animate attributeName="cx" values="710;780" dur="2s" repeatCount="indefinite"/>
    </circle>

    <!-- Node 4: Services & Cache -->
    <g transform="translate(780, 40)">
      <rect width="180" height="190" rx="10" fill="#071228" stroke="#0066FF" stroke-width="1.2"/>
      <rect width="180" height="30" rx="10" fill="#0A1838"/>
      <text class="ab-mono" x="14" y="20" font-size="11" fill="#38BDF8">04 // MICROSERVICES</text>
      <g transform="translate(14, 52)" class="ab-mono" font-size="11" fill="#E0F2FE">
        <text y="0">Redis Pub/Sub Bus</text>
        <text y="24">Job Task Queue</text>
        <text y="48">FFmpeg In-Memory</text>
        <text y="72">Docker Container</text>
        <text y="96">Health Checks</text>
      </g>
    </g>

    <!-- Bus 4 -> 5 -->
    <line x1="960" y1="135" x2="1010" y2="135" stroke="#38BDF8" stroke-width="2" filter="url(#ab-glowf)"/>
    <circle cx="985" cy="135" r="3.5" fill="#F0F9FF">
      <animate attributeName="cx" values="960;1010" dur="2s" repeatCount="indefinite"/>
    </circle>

    <!-- Node 5: Storage Layer -->
    <g transform="translate(1010, 40)">
      <rect width="94" height="190" rx="10" fill="#071228" stroke="#1E3A8A" stroke-width="1.2"/>
      <rect width="94" height="30" rx="10" fill="#0A1838"/>
      <text class="ab-mono" x="8" y="20" font-size="10.5" fill="#38BDF8">05 // DATA</text>
      <g transform="translate(10, 52)" class="ab-mono" font-size="10.5" fill="#E0F2FE">
        <text y="0">Postgres</text>
        <text y="24">Redis</text>
        <text y="48">Vectors</text>
        <text y="72">S3 Media</text>
        <text y="96">Git Log</text>
      </g>
    </g>
  </g>

  <!-- Bottom Legend -->
  <g transform="translate(56, 318)" class="ab-mono" font-size="11" fill="#94A3B8">
    <circle cx="6" cy="4" r="3.5" fill="#38BDF8"/>
    <text x="18" y="8" fill="#F0F9FF">HIGH-THROUGHPUT PIPELINE</text>
    <text x="210" y="8" fill="#64748B">Zero bottleneck design · Strict state isolation · End-to-end type safety</text>
  </g>

  <!-- Border -->
  <rect x=".5" y=".5" width="1199" height="359" rx="15.5" fill="none" stroke="#38BDF8" stroke-opacity=".22"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 9. SECTION 07: FOOTER SIGNATURE (1200 x 220)
# ─────────────────────────────────────────────────────────────────────────────
def build_footer_signature_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 220" width="1200" height="220" role="img" aria-label="Muhammad Mubashar Signature">
  <defs>
    <linearGradient id="fs-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#040916"/><stop offset="100%" stop-color="#02050E"/>
    </linearGradient>
    <radialGradient id="fs-glow" cx="50%" cy="50%" r="55%">
      <stop offset="0" stop-color="#0066FF" stop-opacity=".25"/><stop offset="100%" stop-color="#0066FF" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="fs-sheen" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#F0F9FF" stop-opacity="0"/>
      <stop offset=".5" stop-color="#38BDF8" stop-opacity=".9"/>
      <stop offset="1" stop-color="#F0F9FF" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1600 0;1600 0" keyTimes="0;.45;1" dur="7s" begin="1s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <style>
    .fs-serif { font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif; }
    .fs-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace; }
  </style>

  <rect width="1200" height="220" rx="16" fill="url(#fs-bg)"/>
  <rect width="1200" height="220" rx="16" fill="url(#fs-glow)"/>

  <g transform="translate(60, 48)">
    <text class="fs-mono" font-size="11.5" letter-spacing="3" fill="#38BDF8">SYSTEM SIGNATURE // FINAL LOG</text>
    <text class="fs-serif" y="52" font-size="34" font-style="italic" font-weight="300" fill="#F0F9FF">"Survival before abstraction. Precision before speed. Systems that endure."</text>
    <text class="fs-serif" y="52" font-size="34" font-style="italic" font-weight="300" fill="url(#fs-sheen)" pointer-events="none">"Survival before abstraction. Precision before speed. Systems that endure."</text>

    <line x1="0" y1="84" x2="1080" y2="84" stroke="#38BDF8" stroke-opacity=".25" stroke-width="1.2"/>

    <g transform="translate(0, 114)" class="fs-mono" font-size="11.5">
      <text fill="#E0F2FE">MUHAMMAD MUBASHAR (PASHA DEV)</text>
      <text x="360" fill="#64748B">LAHORE, PK // 31.5204° N, 74.3587° E</text>
      <text x="1080" text-anchor="end" fill="#38BDF8">BUILD · SHIP · ITERATE</text>
    </g>
  </g>

  <!-- Border -->
  <rect x=".5" y=".5" width="1199" height="219" rx="15.5" fill="none" stroke="#38BDF8" stroke-opacity=".22"/>
</svg>"""


# ─────────────────────────────────────────────────────────────────────────────
# 10. GENERATE ALL SVGS & VALIDATE
# ─────────────────────────────────────────────────────────────────────────────
def main():
    print("=== Step 1: Processing User Portrait ===")
    b64_img = get_user_portrait_base64()
    print(f"Base64 generated successfully ({len(b64_img)} chars)")

    print("\n=== Step 2: Generating All Editorial SVGs ===")
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
        "project-pashatools.svg": build_project_pashatools_svg(),
        "project-wishora.svg": build_project_wishora_svg(),
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
        print("\nAll bespoke SVGs generated and passed XML validation perfectly!")
    else:
        print(f"\n{errors} SVGs failed XML validation!")

if __name__ == "__main__":
    main()
