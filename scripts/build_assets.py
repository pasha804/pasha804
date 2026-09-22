"""
Asset Builder for Pasha Dev Profile
Generates 3D-styled, cybernetic, animated SVG assets for the repository:
- assets/hero-dark.svg
- assets/hero-light.svg
- assets/hero.svg
- assets/typing.svg
- assets/nexora.svg
- assets/pasha-tools.svg
- assets/wishora.svg
- assets/zoro.svg
- assets/creative-lab.svg
- assets/tech-orbit.svg
- assets/ai-workflow.svg
- assets/footer.svg
"""

import os

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(WORKSPACE_DIR, "assets")


def get_hero_dark():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="100%" height="100%">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811" />
      <stop offset="50%" stop-color="#0a1022" />
      <stop offset="100%" stop-color="#04060b" />
    </linearGradient>

    <!-- Neon Gradients -->
    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="40%" stop-color="#38bdf8" />
      <stop offset="80%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>

    <linearGradient id="cyber-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>

    <linearGradient id="cyber-purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc" />
      <stop offset="100%" stop-color="#7c3aed" />
    </linearGradient>

    <linearGradient id="border-glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#818cf8" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0.8" />
    </linearGradient>

    <!-- Glow & 3D Shadow Filters -->
    <filter id="bloom-high" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="12" result="blur1" />
      <feGaussianBlur stdDeviation="4" result="blur2" />
      <feMerge>
        <feMergeNode in="blur1" />
        <feMergeNode in="blur2" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="card-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="20" stdDeviation="25" flood-color="#000000" flood-opacity="0.9" />
    </filter>

    <filter id="hologram-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; }
    
    @keyframes float-polyhedron {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      50% { transform: translateY(-16px) rotate(5deg); }
    }
    @keyframes pulse-ring {
      0%, 100% { opacity: 0.3; transform: scale(0.98); }
      50% { opacity: 0.8; transform: scale(1.02); }
    }
    @keyframes sweep-beam {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    @keyframes star-twinkle {
      0%, 100% { opacity: 0.2; }
      50% { opacity: 0.9; }
    }
    
    .floating-3d { animation: float-polyhedron 7s ease-in-out infinite; transform-origin: 980px 240px; }
    .pulsing-ring { animation: pulse-ring 4s ease-in-out infinite; transform-origin: 980px 240px; }
    .star-1 { animation: star-twinkle 2s infinite; }
    .star-2 { animation: star-twinkle 3s infinite 1s; }
  </style>

  <!-- Background Base Canvas -->
  <rect width="1200" height="480" rx="20" fill="url(#hero-bg)" stroke="url(#border-glow)" stroke-width="2" filter="url(#card-shadow)" />

  <!-- 3D Perspective Grid Flooring -->
  <g opacity="0.22">
    <line x1="0" y1="360" x2="1200" y2="360" stroke="#38bdf8" stroke-width="1.5" />
    <line x1="0" y1="390" x2="1200" y2="390" stroke="#38bdf8" stroke-width="1.5" />
    <line x1="0" y1="425" x2="1200" y2="425" stroke="#38bdf8" stroke-width="2" />
    <line x1="0" y1="465" x2="1200" y2="465" stroke="#38bdf8" stroke-width="2.5" />
    
    <!-- Vanishing Perspective Lines -->
    <line x1="600" y1="280" x2="0" y2="480" stroke="#38bdf8" stroke-width="1.2" />
    <line x1="600" y1="280" x2="150" y2="480" stroke="#38bdf8" stroke-width="1.2" />
    <line x1="600" y1="280" x2="350" y2="480" stroke="#38bdf8" stroke-width="1.2" />
    <line x1="600" y1="280" x2="550" y2="480" stroke="#38bdf8" stroke-width="1.2" />
    <line x1="600" y1="280" x2="650" y2="480" stroke="#38bdf8" stroke-width="1.2" />
    <line x1="600" y1="280" x2="850" y2="480" stroke="#38bdf8" stroke-width="1.2" />
    <line x1="600" y1="280" x2="1050" y2="480" stroke="#38bdf8" stroke-width="1.2" />
    <line x1="600" y1="280" x2="1200" y2="480" stroke="#38bdf8" stroke-width="1.2" />
  </g>

  <!-- Ambient Micro Particles -->
  <circle cx="120" cy="80" r="1.5" fill="#38bdf8" class="star-1" />
  <circle cx="280" cy="140" r="2" fill="#c084fc" class="star-2" />
  <circle cx="540" cy="60" r="1" fill="#38bdf8" class="star-1" />
  <circle cx="720" cy="110" r="2" fill="#ffffff" class="star-2" />
  <circle cx="860" cy="70" r="1.5" fill="#818cf8" class="star-1" />

  <!-- Top System Ribbon -->
  <g transform="translate(60, 48)">
    <rect width="180" height="28" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
    <circle cx="16" cy="14" r="5" fill="#10b981" />
    <text x="32" y="18" fill="#38bdf8" class="mono" font-size="10" font-weight="800" letter-spacing="2">SYSTEM ONLINE</text>

    <text x="760" y="18" fill="#64748b" class="mono" font-size="11" letter-spacing="1">ARCH // NEURAL FULL-STACK</text>
    <text x="960" y="18" fill="#94a3b8" class="mono" font-size="11">VER // 2026.4</text>
  </g>

  <line x1="60" y1="92" x2="1140" y2="92" stroke="#1e293b" stroke-width="1" />

  <!-- Main Hero Brand Typography -->
  <g transform="translate(60, 150)">
    <!-- Subtitle Flag -->
    <g transform="translate(0, 0)">
      <rect width="210" height="24" rx="4" fill="#0369a1" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1" />
      <text x="12" y="16" fill="#38bdf8" class="mono" font-size="11" font-weight="800" letter-spacing="2.5">STUDIO COMMAND CENTER</text>
    </g>

    <!-- Master Name Title -->
    <text x="0" y="80" fill="url(#title-grad)" class="sans" font-size="68" font-weight="900" letter-spacing="-1.5" filter="url(#hologram-glow)">PASHA DEV</text>
    
    <!-- Primary Designation -->
    <text x="2" y="125" fill="#f8fafc" class="sans" font-size="28" font-weight="800" letter-spacing="3">AI FULL-STACK DEVELOPER</text>

    <!-- Mission Statement Copy -->
    <text x="4" y="170" fill="#94a3b8" class="sans" font-size="17" font-weight="400">
      Building intelligent products where <tspan fill="#38bdf8" font-weight="600">AI</tspan>, <tspan fill="#818cf8" font-weight="600">systems engineering</tspan>, and <tspan fill="#c084fc" font-weight="600">cinematic design</tspan> meet.
    </text>

    <!-- Interactive Badges / Stack Anchors -->
    <g transform="translate(4, 215)">
      <g>
        <rect width="110" height="34" rx="6" fill="#090d16" stroke="#334155" stroke-width="1" />
        <circle cx="16" cy="17" r="4" fill="#38bdf8" />
        <text x="30" y="22" fill="#f8fafc" class="mono" font-size="12" font-weight="700">FASTAPI</text>
      </g>
      <g transform="translate(125, 0)">
        <rect width="110" height="34" rx="6" fill="#090d16" stroke="#334155" stroke-width="1" />
        <circle cx="16" cy="17" r="4" fill="#818cf8" />
        <text x="30" y="22" fill="#f8fafc" class="mono" font-size="12" font-weight="700">REACT / TS</text>
      </g>
      <g transform="translate(250, 0)">
        <rect width="125" height="34" rx="6" fill="#090d16" stroke="#334155" stroke-width="1" />
        <circle cx="16" cy="17" r="4" fill="#c084fc" />
        <text x="30" y="22" fill="#f8fafc" class="mono" font-size="12" font-weight="700">AI AGENTS</text>
      </g>
      <g transform="translate(390, 0)">
        <rect width="125" height="34" rx="6" fill="#090d16" stroke="#334155" stroke-width="1" />
        <circle cx="16" cy="17" r="4" fill="#34d399" />
        <text x="30" y="22" fill="#f8fafc" class="mono" font-size="12" font-weight="700">POSTGRES</text>
      </g>
    </g>
  </g>

  <!-- Right Side 3D Isometric Hologram System -->
  <g transform="translate(960, 230)">
    <!-- Concentric Orbital Circles -->
    <circle cx="0" cy="0" r="140" fill="none" stroke="#1e293b" stroke-width="1.5" />
    <circle cx="0" cy="0" r="110" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="8 6" opacity="0.4" class="pulsing-ring" />
    <circle cx="0" cy="0" r="75" fill="none" stroke="#818cf8" stroke-width="1" opacity="0.3" />

    <!-- 3D Floating Isometric Polyhedron Structure -->
    <g class="floating-3d">
      <!-- Outer Isometric Cube Shell -->
      <!-- Top Face -->
      <polygon points="0,-70 65,-32 0,6 -65,-32" fill="url(#cyber-cyan)" fill-opacity="0.85" filter="url(#bloom-high)" />
      <!-- Left Face -->
      <polygon points="-65,-32 0,6 0,82 -65,44" fill="#0284c7" fill-opacity="0.9" />
      <!-- Right Face -->
      <polygon points="0,6 65,-32 65,44 0,82" fill="#0369a1" fill-opacity="0.95" />

      <!-- Inner Holographic Energy Cube -->
      <polygon points="0,-35 32,-16 0,3 -32,-16" fill="#ffffff" fill-opacity="0.9" />
      <polygon points="-32,-16 0,3 0,41 -32,22" fill="#c084fc" fill-opacity="0.8" />
      <polygon points="0,3 32,-16 32,22 0,41" fill="#7c3aed" fill-opacity="0.85" />

      <!-- Circuit Traces & Nodes -->
      <circle cx="0" cy="3" r="5" fill="#ffffff" filter="url(#bloom-high)" />
      <line x1="0" y1="-70" x2="0" y2="-100" stroke="#38bdf8" stroke-width="2" />
      <circle cx="0" cy="-100" r="4" fill="#38bdf8" />
      
      <line x1="65" y1="44" x2="105" y2="65" stroke="#c084fc" stroke-width="2" />
      <circle cx="105" cy="65" r="4" fill="#c084fc" />

      <line x1="-65" y1="44" x2="-105" y2="65" stroke="#34d399" stroke-width="2" />
      <circle cx="-105" cy="65" r="4" fill="#34d399" />
    </g>

    <!-- Floating Coordinates Tag -->
    <g transform="translate(-75, 120)">
      <rect width="150" height="24" rx="4" fill="#090d16" stroke="#1e293b" stroke-width="1" />
      <text x="75" y="16" fill="#64748b" class="mono" font-size="10" text-anchor="middle">COORD // 31.52° N, 74.35° E</text>
    </g>
  </g>
</svg>"""


def get_hero_light():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="100%" height="100%">
  <defs>
    <linearGradient id="hero-bg-light" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" />
      <stop offset="50%" stop-color="#f1f5f9" />
      <stop offset="100%" stop-color="#e2e8f0" />
    </linearGradient>

    <linearGradient id="title-grad-light" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#6366f1" />
    </linearGradient>

    <filter id="shadow-light" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#0f172a" flood-opacity="0.12" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    @keyframes float-light {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-12px); }
    }
    .floating-light { animation: float-light 6s ease-in-out infinite; }
  </style>

  <rect width="1200" height="480" rx="20" fill="url(#hero-bg-light)" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadow-light)" />

  <!-- Light Grid -->
  <g opacity="0.35">
    <line x1="0" y1="360" x2="1200" y2="360" stroke="#94a3b8" stroke-width="1" />
    <line x1="0" y1="400" x2="1200" y2="400" stroke="#94a3b8" stroke-width="1" />
    <line x1="0" y1="440" x2="1200" y2="440" stroke="#94a3b8" stroke-width="1" />
    <line x1="600" y1="280" x2="0" y2="480" stroke="#94a3b8" stroke-width="1" />
    <line x1="600" y1="280" x2="300" y2="480" stroke="#94a3b8" stroke-width="1" />
    <line x1="600" y1="280" x2="900" y2="480" stroke="#94a3b8" stroke-width="1" />
    <line x1="600" y1="280" x2="1200" y2="480" stroke="#94a3b8" stroke-width="1" />
  </g>

  <!-- Top System Ribbon -->
  <g transform="translate(60, 48)">
    <rect width="180" height="28" rx="6" fill="#e2e8f0" stroke="#0284c7" stroke-width="1" />
    <circle cx="16" cy="14" r="5" fill="#059669" />
    <text x="32" y="18" fill="#0284c7" class="mono" font-size="10" font-weight="800" letter-spacing="2">SYSTEM ONLINE</text>
    <text x="760" y="18" fill="#64748b" class="mono" font-size="11" letter-spacing="1">ARCH // NEURAL FULL-STACK</text>
    <text x="960" y="18" fill="#475569" class="mono" font-size="11">VER // 2026.4</text>
  </g>

  <line x1="60" y1="92" x2="1140" y2="92" stroke="#e2e8f0" stroke-width="1.5" />

  <!-- Typography -->
  <g transform="translate(60, 150)">
    <rect width="210" height="24" rx="4" fill="#e0f2fe" stroke="#0284c7" stroke-width="1" />
    <text x="12" y="16" fill="#0284c7" class="mono" font-size="11" font-weight="800" letter-spacing="2.5">STUDIO COMMAND CENTER</text>

    <text x="0" y="80" fill="url(#title-grad-light)" class="sans" font-size="68" font-weight="900" letter-spacing="-1.5">PASHA DEV</text>
    <text x="2" y="125" fill="#0f172a" class="sans" font-size="28" font-weight="800" letter-spacing="3">AI FULL-STACK DEVELOPER</text>

    <text x="4" y="170" fill="#475569" class="sans" font-size="17">
      Building intelligent products where <tspan fill="#0284c7" font-weight="600">AI</tspan>, <tspan fill="#4f46e5" font-weight="600">systems engineering</tspan>, and <tspan fill="#7c3aed" font-weight="600">cinematic design</tspan> meet.
    </text>

    <g transform="translate(4, 215)">
      <g>
        <rect width="110" height="34" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
        <circle cx="16" cy="17" r="4" fill="#0284c7" />
        <text x="30" y="22" fill="#0f172a" class="mono" font-size="12" font-weight="700">FASTAPI</text>
      </g>
      <g transform="translate(125, 0)">
        <rect width="110" height="34" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
        <circle cx="16" cy="17" r="4" fill="#4f46e5" />
        <text x="30" y="22" fill="#0f172a" class="mono" font-size="12" font-weight="700">REACT / TS</text>
      </g>
      <g transform="translate(250, 0)">
        <rect width="125" height="34" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
        <circle cx="16" cy="17" r="4" fill="#7c3aed" />
        <text x="30" y="22" fill="#0f172a" class="mono" font-size="12" font-weight="700">AI AGENTS</text>
      </g>
      <g transform="translate(390, 0)">
        <rect width="125" height="34" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
        <circle cx="16" cy="17" r="4" fill="#059669" />
        <text x="30" y="22" fill="#0f172a" class="mono" font-size="12" font-weight="700">POSTGRES</text>
      </g>
    </g>
  </g>

  <!-- Right Side 3D Isometric Element (Light) -->
  <g transform="translate(960, 230)" class="floating-light">
    <circle cx="0" cy="0" r="130" fill="none" stroke="#cbd5e1" stroke-width="1.5" />
    <circle cx="0" cy="0" r="95" fill="none" stroke="#0284c7" stroke-width="1" stroke-dasharray="6 6" opacity="0.4" />
    
    <!-- 3D Cube -->
    <polygon points="0,-60 55,-28 0,5 -55,-28" fill="#38bdf8" />
    <polygon points="-55,-28 0,5 0,70 -55,37" fill="#0284c7" />
    <polygon points="0,5 55,-28 55,37 0,70" fill="#0369a1" />

    <polygon points="0,-25 25,-12 0,2 -25,-12" fill="#ffffff" />
    <polygon points="-25,-12 0,2 0,28 -25,14" fill="#818cf8" />
    <polygon points="0,2 25,-12 25,14 0,28" fill="#4f46e5" />
  </g>
</svg>"""


def get_typing_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 64" width="100%" height="100%">
  <defs>
    <linearGradient id="typing-bg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0a1022" />
      <stop offset="50%" stop-color="#0e172e" />
      <stop offset="100%" stop-color="#0a1022" />
    </linearGradient>
    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }
    @keyframes cursor-blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
    @keyframes type-in {
      0% { width: 0; }
      70%, 100% { width: 100%; }
    }
    .cursor { animation: cursor-blink 0.9s infinite; }
  </style>

  <rect width="900" height="64" rx="10" fill="url(#typing-bg)" stroke="#1e293b" stroke-width="1.5" />

  <!-- Terminal Prefix -->
  <g transform="translate(24, 20)">
    <text x="0" y="16" fill="#10b981" class="mono" font-size="16" font-weight="900">~/pasha $</text>
    <text x="110" y="16" fill="url(#text-grad)" class="mono" font-size="15" font-weight="700">AI Full-Stack Developer • Systems Architect • Creative Technologist</text>
    <!-- Blinking Cursor -->
    <rect x="745" y="2" width="9" height="18" rx="1" fill="#38bdf8" class="cursor" />
  </g>
</svg>"""


def get_nexora_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 480" width="100%" height="100%">
  <defs>
    <linearGradient id="nexora-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c071d" />
      <stop offset="50%" stop-color="#140c2e" />
      <stop offset="100%" stop-color="#080414" />
    </linearGradient>

    <linearGradient id="nexora-purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc" />
      <stop offset="100%" stop-color="#9333ea" />
    </linearGradient>

    <linearGradient id="nexora-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>

    <filter id="purple-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="node-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.8" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    @keyframes pulse-flow {
      0% { stroke-dashoffset: 60; }
      100% { stroke-dashoffset: 0; }
    }
    @keyframes float-box {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-5px); }
    }
    .flow-line { stroke-dasharray: 6 6; animation: pulse-flow 2s linear infinite; }
    .floating-node { animation: float-box 5s ease-in-out infinite; }
  </style>

  <rect width="940" height="480" rx="16" fill="url(#nexora-bg)" stroke="#4c1d95" stroke-width="1.5" />

  <!-- Header Banner -->
  <g transform="translate(36, 32)">
    <rect width="36" height="36" rx="8" fill="#2e1065" stroke="#a855f7" stroke-width="1.5" />
    <!-- Nexora Icon: 3D Crystal Hexagon -->
    <polygon points="18,6 28,12 28,24 18,30 8,24 8,12" fill="#a855f7" />
    <polygon points="18,6 28,12 18,18 8,12" fill="#d8b4fe" />
    <polygon points="8,12 18,18 18,30 8,24" fill="#9333ea" />

    <text x="48" y="20" fill="#f8fafc" class="sans" font-size="20" font-weight="900" letter-spacing="1">NEXORA</text>
    <text x="48" y="34" fill="#c084fc" class="mono" font-size="11" font-weight="700">GAMIFY PROFESSIONAL GROWTH // AI SKILL PLATFORM</text>

    <!-- Status -->
    <rect x="740" y="6" width="130" height="24" rx="4" fill="#1e103a" stroke="#a855f7" stroke-width="1" />
    <circle cx="754" cy="18" r="4" fill="#10b981" />
    <text x="766" y="22" fill="#d8b4fe" class="mono" font-size="10" font-weight="700">CURRENT SPRINT</text>
  </g>

  <line x1="36" y1="84" x2="904" y2="84" stroke="#2e1065" stroke-width="1" />

  <!-- 3D Architecture Diagram -->
  <g transform="translate(36, 105)">
    <!-- Central Nexora Core Node (Level 1) -->
    <g transform="translate(350, 0)" class="floating-node">
      <rect width="170" height="50" rx="10" fill="#1f1147" stroke="#a855f7" stroke-width="2" filter="url(#purple-glow)" />
      <text x="85" y="25" fill="#f8fafc" class="sans" font-size="14" font-weight="900" text-anchor="middle">NEXORA CORE</text>
      <text x="85" y="40" fill="#c084fc" class="mono" font-size="9" text-anchor="middle">PLATFORM CONTROLLER</text>
    </g>

    <!-- Flow Lines Down to Subsystems -->
    <path d="M 435 50 L 435 85 L 140 85 L 140 120" fill="none" stroke="#38bdf8" stroke-width="2" class="flow-line" />
    <path d="M 435 50 L 435 120" fill="none" stroke="#a855f7" stroke-width="2" class="flow-line" />
    <path d="M 435 50 L 435 85 L 730 85 L 730 120" fill="none" stroke="#f43f5e" stroke-width="2" class="flow-line" />

    <!-- Level 2: Three Pillars -->
    <!-- Pillar 1: Frontend Client -->
    <g transform="translate(40, 120)" class="floating-node">
      <rect width="200" height="120" rx="10" fill="#0d1527" stroke="#38bdf8" stroke-width="1.5" filter="url(#node-shadow)" />
      <rect x="0" y="0" width="200" height="4" rx="2" fill="#38bdf8" />
      <text x="16" y="28" fill="#38bdf8" class="mono" font-size="10" font-weight="800">01 // CLIENT TIER</text>
      <text x="16" y="48" fill="#f8fafc" class="sans" font-size="16" font-weight="800">React + TS</text>
      <text x="16" y="68" fill="#94a3b8" class="mono" font-size="10">Vite • Tailwind • Framer</text>
      <text x="16" y="86" fill="#94a3b8" class="mono" font-size="10">shadcn/ui • TanStack Query</text>
      <rect x="16" y="96" width="168" height="14" rx="3" fill="#0369a1" fill-opacity="0.3" />
      <text x="24" y="106" fill="#38bdf8" class="mono" font-size="8">FEED • COMMUNITY • PVP UI</text>
    </g>

    <!-- Pillar 2: High Performance API -->
    <g transform="translate(335, 120)" class="floating-node">
      <rect width="200" height="120" rx="10" fill="#140b2b" stroke="#a855f7" stroke-width="1.5" filter="url(#node-shadow)" />
      <rect x="0" y="0" width="200" height="4" rx="2" fill="#a855f7" />
      <text x="16" y="28" fill="#c084fc" class="mono" font-size="10" font-weight="800">02 // BACKEND API</text>
      <text x="16" y="48" fill="#f8fafc" class="sans" font-size="16" font-weight="800">FastAPI Async</text>
      <text x="16" y="68" fill="#94a3b8" class="mono" font-size="10">Python 3.12+ • Pydantic</text>
      <text x="16" y="86" fill="#94a3b8" class="mono" font-size="10">Docker • Microservices</text>
      <rect x="16" y="96" width="168" height="14" rx="3" fill="#6b21a8" fill-opacity="0.3" />
      <text x="24" y="106" fill="#c084fc" class="mono" font-size="8">AUTH • WEBSOCKETS • LOGIC</text>
    </g>

    <!-- Pillar 3: AI Intelligence Engine -->
    <g transform="translate(630, 120)" class="floating-node">
      <rect width="200" height="120" rx="10" fill="#200d1d" stroke="#f43f5e" stroke-width="1.5" filter="url(#node-shadow)" />
      <rect x="0" y="0" width="200" height="4" rx="2" fill="#f43f5e" />
      <text x="16" y="28" fill="#fb7185" class="mono" font-size="10" font-weight="800">03 // AI SUBSYSTEM</text>
      <text x="16" y="48" fill="#f8fafc" class="sans" font-size="16" font-weight="800">Coach &amp; Judge</text>
      <text x="16" y="68" fill="#94a3b8" class="mono" font-size="10">LLM Reasoning • Agents</text>
      <text x="16" y="86" fill="#94a3b8" class="mono" font-size="10">Automated PvP Judging</text>
      <rect x="16" y="96" width="168" height="14" rx="3" fill="#be123c" fill-opacity="0.3" />
      <text x="24" y="106" fill="#fb7185" class="mono" font-size="8">SKILL SCORING • FEEDBACK</text>
    </g>

    <!-- Flow Lines Down to Data Layer -->
    <path d="M 140 240 L 140 270 L 350 270 L 350 295" fill="none" stroke="#38bdf8" stroke-width="2" class="flow-line" />
    <path d="M 435 240 L 435 295" fill="none" stroke="#a855f7" stroke-width="2" class="flow-line" />
    <path d="M 730 240 L 730 270 L 520 270 L 520 295" fill="none" stroke="#f43f5e" stroke-width="2" class="flow-line" />

    <!-- Level 3: Dual Database Foundation -->
    <g transform="translate(245, 295)">
      <!-- PostgreSQL Block -->
      <g>
        <rect width="180" height="60" rx="8" fill="#09101d" stroke="#38bdf8" stroke-width="1.5" />
        <circle cx="20" cy="30" r="10" fill="#0369a1" />
        <text x="38" y="26" fill="#f8fafc" class="mono" font-size="12" font-weight="800">PostgreSQL</text>
        <text x="38" y="42" fill="#94a3b8" class="mono" font-size="9">RELATIONAL DATA &amp; PROFILES</text>
      </g>

      <!-- Redis Cache Block -->
      <g transform="translate(200, 0)">
        <rect width="180" height="60" rx="8" fill="#1b0a13" stroke="#f43f5e" stroke-width="1.5" />
        <circle cx="20" cy="30" r="10" fill="#be123c" />
        <text x="38" y="26" fill="#f8fafc" class="mono" font-size="12" font-weight="800">Redis</text>
        <text x="38" y="42" fill="#94a3b8" class="mono" font-size="9">IN-MEMORY STATE &amp; QUEUES</text>
      </g>
    </g>
  </g>
</svg>"""


def get_pasha_tools_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 380" width="100%" height="100%">
  <defs>
    <linearGradient id="pt-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08101e" />
      <stop offset="100%" stop-color="#040810" />
    </linearGradient>
    <linearGradient id="pt-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <filter id="pt-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    @keyframes pulse-dot {
      0%, 100% { opacity: 0.4; }
      50% { opacity: 1; }
    }
    .pulsing-dot { animation: pulse-dot 2s infinite; }
  </style>

  <rect width="540" height="380" rx="14" fill="url(#pt-bg)" stroke="#1e3a5f" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(28, 28)">
    <rect width="32" height="32" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" />
    <!-- Wrench / Tool 3D Icon -->
    <path d="M 12 10 L 22 20 M 18 10 C 22 10 24 12 24 16 L 20 18 L 18 16 L 12 22 L 10 20 L 16 14 L 14 12 Z" fill="#38bdf8" />
    
    <text x="44" y="16" fill="#f8fafc" class="sans" font-size="18" font-weight="900">PASHA TOOLS</text>
    <text x="44" y="30" fill="#38bdf8" class="mono" font-size="10" font-weight="700">pashatools.com // MULTI-TOOL SUITE</text>

    <rect x="360" y="4" width="115" height="22" rx="4" fill="#0369a1" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1" />
    <circle cx="372" cy="15" r="4" fill="#10b981" class="pulsing-dot" />
    <text x="382" y="19" fill="#38bdf8" class="mono" font-size="9" font-weight="700">PRODUCTION LIVE</text>
  </g>

  <line x1="28" y1="74" x2="512" y2="74" stroke="#1e293b" stroke-width="1" />

  <!-- Content & Feature Modules -->
  <g transform="translate(28, 92)">
    <text x="0" y="16" fill="#94a3b8" class="sans" font-size="13">High-speed web utilities engine built for automated media &amp; document transformations.</text>

    <!-- 3D Pipeline Stack Cards -->
    <g transform="translate(0, 36)">
      <!-- Card 1 -->
      <g>
        <rect width="235" height="75" rx="8" fill="#0a1224" stroke="#1e293b" stroke-width="1" />
        <rect x="0" y="0" width="4" height="75" rx="2" fill="#38bdf8" />
        <text x="16" y="24" fill="#38bdf8" class="mono" font-size="10" font-weight="700">ENGINEERING</text>
        <text x="16" y="44" fill="#f8fafc" class="sans" font-size="14" font-weight="700">React + FastAPI</text>
        <text x="16" y="62" fill="#64748b" class="mono" font-size="9">Railway Backend • Vercel Frontend</text>
      </g>

      <!-- Card 2 -->
      <g transform="translate(250, 0)">
        <rect width="235" height="75" rx="8" fill="#0a1224" stroke="#1e293b" stroke-width="1" />
        <rect x="0" y="0" width="4" height="75" rx="2" fill="#818cf8" />
        <text x="16" y="24" fill="#818cf8" class="mono" font-size="10" font-weight="700">CORE PIPELINE</text>
        <text x="16" y="44" fill="#f8fafc" class="sans" font-size="14" font-weight="700">FFmpeg &amp; yt-dlp</text>
        <text x="16" y="62" fill="#64748b" class="mono" font-size="9">Lossless Conversion &amp; Streams</text>
      </g>

      <!-- Card 3 -->
      <g transform="translate(0, 88)">
        <rect width="235" height="75" rx="8" fill="#0a1224" stroke="#1e293b" stroke-width="1" />
        <rect x="0" y="0" width="4" height="75" rx="2" fill="#c084fc" />
        <text x="16" y="24" fill="#c084fc" class="mono" font-size="10" font-weight="700">PROCESSING</text>
        <text x="16" y="44" fill="#f8fafc" class="sans" font-size="14" font-weight="700">PDF &amp; File Engine</text>
        <text x="16" y="62" fill="#64748b" class="mono" font-size="9">Fast In-Memory Byte Stream</text>
      </g>

      <!-- Card 4 -->
      <g transform="translate(250, 88)">
        <rect width="235" height="75" rx="8" fill="#0a1224" stroke="#1e293b" stroke-width="1" />
        <rect x="0" y="0" width="4" height="75" rx="2" fill="#34d399" />
        <text x="16" y="24" fill="#34d399" class="mono" font-size="10" font-weight="700">GROWTH ARCHITECTURE</text>
        <text x="16" y="44" fill="#f8fafc" class="sans" font-size="14" font-weight="700">SEO &amp; AdSense Ready</text>
        <text x="16" y="62" fill="#64748b" class="mono" font-size="9">Automated Canonical Routing</text>
      </g>
    </g>
  </g>

  <!-- Bottom Terminal Tag -->
  <g transform="translate(28, 335)">
    <rect width="484" height="26" rx="4" fill="#050a12" stroke="#1e293b" stroke-width="1" />
    <text x="12" y="17" fill="#64748b" class="mono" font-size="9">&gt; pashatools.com --status 200 --latency 42ms</text>
    <text x="472" y="17" fill="#38bdf8" class="mono" font-size="9" text-anchor="end">PRODUCTION READY</text>
  </g>
</svg>"""


def get_wishora_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 380" width="100%" height="100%">
  <defs>
    <linearGradient id="wish-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#150a24" />
      <stop offset="100%" stop-color="#080312" />
    </linearGradient>
    <linearGradient id="wish-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#c084fc" />
      <stop offset="100%" stop-color="#f43f5e" />
    </linearGradient>
    <filter id="wish-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    @keyframes sparkle {
      0%, 100% { opacity: 0.3; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.1); }
    }
    .sparkling { animation: sparkle 3s ease-in-out infinite; }
  </style>

  <rect width="540" height="380" rx="14" fill="url(#wish-bg)" stroke="#4c1d95" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(28, 28)">
    <rect width="32" height="32" rx="8" fill="#2e1065" stroke="#c084fc" stroke-width="1.5" />
    <!-- 3D Heart/Gift Card -->
    <path d="M 16 10 C 13 6 8 8 8 13 C 8 18 16 24 16 24 C 16 24 24 18 24 13 C 24 8 19 6 16 10 Z" fill="#c084fc" />

    <text x="44" y="16" fill="#f8fafc" class="sans" font-size="18" font-weight="900">WISHORA</text>
    <text x="44" y="30" fill="#c084fc" class="mono" font-size="10" font-weight="700">PERSONALIZED DIGITAL GREETING PLATFORM</text>

    <rect x="360" y="4" width="115" height="22" rx="4" fill="#3b0764" stroke="#c084fc" stroke-width="1" />
    <text x="417" y="19" fill="#f5d0fe" class="mono" font-size="9" font-weight="800" text-anchor="middle">CREATIVE WEB</text>
  </g>

  <line x1="28" y1="74" x2="512" y2="74" stroke="#2e1065" stroke-width="1" />

  <!-- Content -->
  <g transform="translate(28, 92)">
    <!-- Positioning Banner -->
    <rect width="484" height="34" rx="6" fill="#1f0d38" stroke="#c084fc" stroke-width="1" />
    <text x="242" y="21" fill="url(#wish-grad)" class="mono" font-size="11" font-weight="900" text-anchor="middle" letter-spacing="1">
      FREE FOREVER • NO SIGNUP • INSTANT DOWNLOAD
    </text>

    <!-- Cards Grid -->
    <g transform="translate(0, 48)">
      <g>
        <rect width="235" height="85" rx="8" fill="#130822" stroke="#2e1065" stroke-width="1" />
        <text x="16" y="24" fill="#c084fc" class="mono" font-size="10" font-weight="700">ARCHITECTURE</text>
        <text x="16" y="46" fill="#f8fafc" class="sans" font-size="15" font-weight="800">Next.js App Router</text>
        <text x="16" y="66" fill="#94a3b8" class="mono" font-size="9">Server Components &amp; Edge Delivery</text>
      </g>

      <g transform="translate(250, 0)">
        <rect width="235" height="85" rx="8" fill="#130822" stroke="#2e1065" stroke-width="1" />
        <text x="16" y="24" fill="#f43f5e" class="mono" font-size="10" font-weight="700">ANIMATION SYSTEM</text>
        <text x="16" y="46" fill="#f8fafc" class="sans" font-size="15" font-weight="800">Framer Motion</text>
        <text x="16" y="66" fill="#94a3b8" class="mono" font-size="9">60 FPS Micro-Interactions</text>
      </g>

      <g transform="translate(0, 98)">
        <rect width="235" height="85" rx="8" fill="#130822" stroke="#2e1065" stroke-width="1" />
        <text x="16" y="24" fill="#38bdf8" class="mono" font-size="10" font-weight="700">TYPE SAFETY</text>
        <text x="16" y="46" fill="#f8fafc" class="sans" font-size="15" font-weight="800">Strict TypeScript</text>
        <text x="16" y="66" fill="#94a3b8" class="mono" font-size="9">Zero Runtime Type Failures</text>
      </g>

      <g transform="translate(250, 98)">
        <rect width="235" height="85" rx="8" fill="#130822" stroke="#2e1065" stroke-width="1" />
        <text x="16" y="24" fill="#34d399" class="mono" font-size="10" font-weight="700">CLIENT EXPERIENCE</text>
        <text x="16" y="46" fill="#f8fafc" class="sans" font-size="15" font-weight="800">Instant Canvas Export</text>
        <text x="16" y="66" fill="#94a3b8" class="mono" font-size="9">High-Res PNG Card Generation</text>
      </g>
    </g>
  </g>

  <g transform="translate(28, 345)">
    <text x="0" y="14" fill="#64748b" class="mono" font-size="9">DESIGNED FOR EMOTION &amp; MAXIMUM FRICTIONLESS ADOPTION</text>
  </g>
</svg>"""


def get_zoro_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 380" width="100%" height="100%">
  <defs>
    <linearGradient id="zoro-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#04121d" />
      <stop offset="100%" stop-color="#02080f" />
    </linearGradient>
    <linearGradient id="zoro-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    @keyframes pulse-wave {
      0%, 100% { height: 6px; }
      50% { height: 24px; }
    }
    .wave-1 { animation: pulse-wave 1.2s infinite; }
    .wave-2 { animation: pulse-wave 1.5s infinite 0.2s; }
    .wave-3 { animation: pulse-wave 0.9s infinite 0.4s; }
  </style>

  <rect width="540" height="380" rx="14" fill="url(#zoro-bg)" stroke="#0e7490" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(28, 28)">
    <rect width="32" height="32" rx="8" fill="#082f49" stroke="#38bdf8" stroke-width="1.5" />
    <!-- Bot / Windows Chip Icon -->
    <rect x="8" y="8" width="16" height="16" rx="3" fill="#38bdf8" />
    <circle cx="12" cy="14" r="2" fill="#082f49" />
    <circle cx="20" cy="14" r="2" fill="#082f49" />
    <line x1="12" y1="19" x2="20" y2="19" stroke="#082f49" stroke-width="1.5" />

    <text x="44" y="16" fill="#f8fafc" class="sans" font-size="18" font-weight="900">ZORO 2.0</text>
    <text x="44" y="30" fill="#38bdf8" class="mono" font-size="10" font-weight="700">NATIVE WINDOWS AI ASSISTANT (DESKTOP)</text>

    <rect x="345" y="4" width="130" height="22" rx="4" fill="#075985" fill-opacity="0.4" stroke="#38bdf8" stroke-width="1" />
    <text x="410" y="19" fill="#bae6fd" class="mono" font-size="9" font-weight="800" text-anchor="middle">WINDOWS NATIVE</text>
  </g>

  <line x1="28" y1="74" x2="512" y2="74" stroke="#164e63" stroke-width="1" />

  <!-- 3D Architecture Visual Flow -->
  <g transform="translate(28, 92)">
    <!-- Warning Banner: Not a Web App -->
    <rect width="484" height="26" rx="4" fill="#082f49" stroke="#0284c7" stroke-width="1" />
    <text x="14" y="17" fill="#38bdf8" class="mono" font-size="9" font-weight="700">ARCHITECTURE // NATIVE DESKTOP SUBSYSTEM (NOT A WEB APP)</text>

    <!-- Stack Flow -->
    <g transform="translate(0, 38)">
      <!-- Tier 1: Tauri Host -->
      <g>
        <rect width="110" height="70" rx="6" fill="#061826" stroke="#0284c7" stroke-width="1.2" />
        <text x="55" y="24" fill="#38bdf8" class="mono" font-size="10" font-weight="800" text-anchor="middle">TAURI</text>
        <text x="55" y="42" fill="#f8fafc" class="sans" font-size="11" font-weight="700" text-anchor="middle">Native Shell</text>
        <text x="55" y="58" fill="#64748b" class="mono" font-size="8" text-anchor="middle">Rust Core Bridge</text>
      </g>

      <text x="122" y="40" fill="#38bdf8" class="mono" font-size="14" font-weight="900">→</text>

      <!-- Tier 2: React UI -->
      <g transform="translate(136, 0)">
        <rect width="110" height="70" rx="6" fill="#061826" stroke="#0284c7" stroke-width="1.2" />
        <text x="55" y="24" fill="#818cf8" class="mono" font-size="10" font-weight="800" text-anchor="middle">REACT UI</text>
        <text x="55" y="42" fill="#f8fafc" class="sans" font-size="11" font-weight="700" text-anchor="middle">Cyber HUD</text>
        <text x="55" y="58" fill="#64748b" class="mono" font-size="8" text-anchor="middle">Voice Visualizer</text>
      </g>

      <text x="258" y="40" fill="#38bdf8" class="mono" font-size="14" font-weight="900">→</text>

      <!-- Tier 3: Python AI Core -->
      <g transform="translate(272, 0)">
        <rect width="110" height="70" rx="6" fill="#061826" stroke="#c084fc" stroke-width="1.2" />
        <text x="55" y="24" fill="#c084fc" class="mono" font-size="10" font-weight="800" text-anchor="middle">PYTHON</text>
        <text x="55" y="42" fill="#f8fafc" class="sans" font-size="11" font-weight="700" text-anchor="middle">Brain &amp; Memory</text>
        <text x="55" y="58" fill="#64748b" class="mono" font-size="8" text-anchor="middle">LLM Tool Calling</text>
      </g>

      <text x="394" y="40" fill="#38bdf8" class="mono" font-size="14" font-weight="900">→</text>

      <!-- Tier 4: Windows OS -->
      <g transform="translate(408, 0)">
        <rect width="76" height="70" rx="6" fill="#061826" stroke="#34d399" stroke-width="1.2" />
        <text x="38" y="24" fill="#34d399" class="mono" font-size="9" font-weight="800" text-anchor="middle">WIN OS</text>
        <text x="38" y="42" fill="#f8fafc" class="sans" font-size="10" font-weight="700" text-anchor="middle">Control</text>
        <text x="38" y="58" fill="#64748b" class="mono" font-size="8" text-anchor="middle">Automations</text>
      </g>
    </g>

    <!-- Capabilities Grid -->
    <g transform="translate(0, 130)">
      <rect width="484" height="95" rx="8" fill="#031018" stroke="#164e63" stroke-width="1" />
      <text x="16" y="24" fill="#38bdf8" class="mono" font-size="10" font-weight="700">CORE CAPABILITIES</text>
      
      <circle cx="22" cy="46" r="3" fill="#38bdf8" />
      <text x="34" y="50" fill="#f8fafc" class="sans" font-size="12">Real-time Voice Pipeline &amp; Neural Synthesis</text>

      <circle cx="22" cy="66" r="3" fill="#c084fc" />
      <text x="34" y="70" fill="#f8fafc" class="sans" font-size="12">Persistent Long-Term Memory &amp; Context Retrieval</text>

      <circle cx="22" cy="86" r="3" fill="#34d399" />
      <text x="34" y="90" fill="#f8fafc" class="sans" font-size="12">Automated Windows Desktop Workflows &amp; Tool Execution</text>
    </g>
  </g>

  <g transform="translate(28, 350)">
    <text x="0" y="14" fill="#64748b" class="mono" font-size="9">DESIGNED FOR SEAMLESS HIGH-SPEED HUMAN-AI DESKTOP COLLABORATION</text>
  </g>
</svg>"""


def get_creative_lab_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 380" width="100%" height="100%">
  <defs>
    <linearGradient id="cl-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0f1d" />
      <stop offset="100%" stop-color="#04060b" />
    </linearGradient>
    <linearGradient id="cl-orb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
    <filter id="cl-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    @keyframes rotate-ring {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    .rotating { transform-origin: 430px 180px; animation: rotate-ring 14s linear infinite; }
  </style>

  <rect width="540" height="380" rx="14" fill="url(#cl-bg)" stroke="#1e293b" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(28, 28)">
    <rect width="32" height="32" rx="8" fill="#0f172a" stroke="#818cf8" stroke-width="1.5" />
    <!-- 3D Sparkle / Prism -->
    <polygon points="16,6 24,16 16,26 8,16" fill="url(#cl-orb)" />

    <text x="44" y="16" fill="#f8fafc" class="sans" font-size="18" font-weight="900">CREATIVE WEB LAB</text>
    <text x="44" y="30" fill="#818cf8" class="mono" font-size="10" font-weight="700">CINEMATIC WEB &amp; INTERACTIVE EXPERIMENTS</text>

    <rect x="360" y="4" width="115" height="22" rx="4" fill="#312e81" stroke="#818cf8" stroke-width="1" />
    <text x="417" y="19" fill="#c7d2fe" class="mono" font-size="9" font-weight="800" text-anchor="middle">MOTION &amp; 3D</text>
  </g>

  <line x1="28" y1="74" x2="512" y2="74" stroke="#1e293b" stroke-width="1" />

  <!-- Left Side Capabilities -->
  <g transform="translate(28, 95)">
    <g>
      <rect width="280" height="50" rx="6" fill="#090d16" stroke="#1e293b" stroke-width="1" />
      <circle cx="16" cy="25" r="4" fill="#38bdf8" />
      <text x="32" y="22" fill="#f8fafc" class="sans" font-size="13" font-weight="700">Cinematic Landing Pages</text>
      <text x="32" y="38" fill="#64748b" class="mono" font-size="9">Hero narratives &amp; immersive design systems</text>
    </g>

    <g transform="translate(0, 60)">
      <rect width="280" height="50" rx="6" fill="#090d16" stroke="#1e293b" stroke-width="1" />
      <circle cx="16" cy="25" r="4" fill="#818cf8" />
      <text x="32" y="22" fill="#f8fafc" class="sans" font-size="13" font-weight="700">Interactive 3D Experiences</text>
      <text x="32" y="38" fill="#64748b" class="mono" font-size="9">Three.js • WebGL • Shader experiments</text>
    </g>

    <g transform="translate(0, 120)">
      <rect width="280" height="50" rx="6" fill="#090d16" stroke="#1e293b" stroke-width="1" />
      <circle cx="16" cy="25" r="4" fill="#c084fc" />
      <text x="32" y="22" fill="#f8fafc" class="sans" font-size="13" font-weight="700">Motion-Driven Interfaces</text>
      <text x="32" y="38" fill="#64748b" class="mono" font-size="9">Framer Motion • 60 FPS transitions</text>
    </g>

    <g transform="translate(0, 180)">
      <rect width="280" height="50" rx="6" fill="#090d16" stroke="#1e293b" stroke-width="1" />
      <circle cx="16" cy="25" r="4" fill="#34d399" />
      <text x="32" y="22" fill="#f8fafc" class="sans" font-size="13" font-weight="700">Digital Cards &amp; Experiences</text>
      <text x="32" y="38" fill="#64748b" class="mono" font-size="9">Interactive personalized web artifacts</text>
    </g>
  </g>

  <!-- Right Side 3D Rotating Gyro / Sphere -->
  <g transform="translate(420, 205)">
    <circle cx="0" cy="0" r="65" fill="none" stroke="#1e293b" stroke-width="1.5" />
    <ellipse cx="0" cy="0" rx="65" ry="25" fill="none" stroke="#38bdf8" stroke-width="1" opacity="0.6" class="rotating" />
    <ellipse cx="0" cy="0" rx="25" ry="65" fill="none" stroke="#c084fc" stroke-width="1" opacity="0.6" class="rotating" />
    <circle cx="0" cy="0" r="16" fill="url(#cl-orb)" filter="url(#cl-glow)" />
  </g>

  <g transform="translate(28, 350)">
    <text x="0" y="14" fill="#64748b" class="mono" font-size="9">EXPLORING THE SEAMLESS SYNTHESIS OF CODE, DEPTH AND EMOTION</text>
  </g>
</svg>"""


def get_tech_orbit_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 440" width="100%" height="100%">
  <defs>
    <linearGradient id="orbit-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c14" />
      <stop offset="50%" stop-color="#0e1526" />
      <stop offset="100%" stop-color="#05080f" />
    </linearGradient>

    <linearGradient id="tech-card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0.1" />
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    @keyframes orbit-pulse {
      0%, 100% { opacity: 0.3; }
      50% { opacity: 0.7; }
    }
    .pulsing-orbit { animation: orbit-pulse 4s infinite; }
  </style>

  <rect width="940" height="440" rx="16" fill="url(#orbit-bg)" stroke="#1e293b" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(36, 32)">
    <rect width="8" height="20" fill="#38bdf8" rx="2" />
    <text x="20" y="16" fill="#f8fafc" class="sans" font-size="18" font-weight="900">TECHNOLOGY UNIVERSE</text>
    <text x="260" y="16" fill="#64748b" class="mono" font-size="11">VISUALLY ORGANIZED PRODUCTION SYSTEM (ZERO BADGE OVERLOAD)</text>
  </g>

  <line x1="36" y1="68" x2="904" y2="68" stroke="#1e293b" stroke-width="1" />

  <!-- 6 Structured Category Blocks -->
  <g transform="translate(36, 88)">
    <!-- 1. Frontend -->
    <g>
      <rect width="270" height="150" rx="10" fill="#090e1a" stroke="#1e293b" stroke-width="1.5" />
      <path d="M 0 0 L 270 0" stroke="#38bdf8" stroke-width="2.5" />
      <text x="18" y="26" fill="#38bdf8" class="mono" font-size="11" font-weight="800">01 // FRONTEND</text>
      
      <g transform="translate(18, 42)">
        <rect width="66" height="22" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
        <text x="33" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">React</text>

        <rect x="74" width="76" height="22" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
        <text x="112" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Next.js</text>

        <rect x="158" width="76" height="22" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1" />
        <text x="196" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">TypeScript</text>
      </g>

      <g transform="translate(18, 72)">
        <rect width="76" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="38" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Tailwind</text>

        <rect x="84" width="60" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="114" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Vite</text>

        <rect x="152" width="82" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="193" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">shadcn/ui</text>
      </g>

      <g transform="translate(18, 102)">
        <rect width="105" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="52" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Framer Motion</text>

        <rect x="113" width="121" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="173" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">TanStack Query</text>
      </g>
    </g>

    <!-- 2. Backend & Systems -->
    <g transform="translate(295, 0)">
      <rect width="270" height="150" rx="10" fill="#090e1a" stroke="#1e293b" stroke-width="1.5" />
      <path d="M 0 0 L 270 0" stroke="#818cf8" stroke-width="2.5" />
      <text x="18" y="26" fill="#818cf8" class="mono" font-size="11" font-weight="800">02 // BACKEND &amp; SYSTEMS</text>

      <g transform="translate(18, 42)">
        <rect width="70" height="22" rx="4" fill="#0f172a" stroke="#818cf8" stroke-width="1" />
        <text x="35" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Python</text>

        <rect x="78" width="76" height="22" rx="4" fill="#0f172a" stroke="#818cf8" stroke-width="1" />
        <text x="116" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">FastAPI</text>

        <rect x="162" width="72" height="22" rx="4" fill="#0f172a" stroke="#818cf8" stroke-width="1" />
        <text x="198" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Node.js</text>
      </g>

      <g transform="translate(18, 72)">
        <rect width="76" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="38" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Express</text>

        <rect x="84" width="76" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="122" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Pydantic</text>

        <rect x="168" width="66" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="201" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">AsyncIO</text>
      </g>

      <g transform="translate(18, 102)">
        <rect width="105" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="52" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">REST APIs</text>

        <rect x="113" width="121" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="173" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">WebSockets</text>
      </g>
    </g>

    <!-- 3. AI & Neural Multipliers -->
    <g transform="translate(590, 0)">
      <rect width="270" height="150" rx="10" fill="#090e1a" stroke="#1e293b" stroke-width="1.5" />
      <path d="M 0 0 L 270 0" stroke="#c084fc" stroke-width="2.5" />
      <text x="18" y="26" fill="#c084fc" class="mono" font-size="11" font-weight="800">03 // AI &amp; AGENTIC SYSTEMS</text>

      <g transform="translate(18, 42)">
        <rect width="66" height="22" rx="4" fill="#0f172a" stroke="#c084fc" stroke-width="1" />
        <text x="33" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">LLMs</text>

        <rect x="74" width="86" height="22" rx="4" fill="#0f172a" stroke="#c084fc" stroke-width="1" />
        <text x="117" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">AI Agents</text>

        <rect x="168" width="66" height="22" rx="4" fill="#0f172a" stroke="#c084fc" stroke-width="1" />
        <text x="201" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">OpenAI</text>
      </g>

      <g transform="translate(18, 72)">
        <rect width="90" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="45" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Function Call</text>

        <rect x="98" width="136" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="166" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Prompt Engineering</text>
      </g>

      <g transform="translate(18, 102)">
        <rect width="115" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="57" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Voice Pipelines</text>

        <rect x="123" width="111" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="178" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Local Models</text>
      </g>
    </g>

    <!-- 4. Data Layer -->
    <g transform="translate(0, 168)">
      <rect width="270" height="150" rx="10" fill="#090e1a" stroke="#1e293b" stroke-width="1.5" />
      <path d="M 0 0 L 270 0" stroke="#34d399" stroke-width="2.5" />
      <text x="18" y="26" fill="#34d399" class="mono" font-size="11" font-weight="800">04 // DATA &amp; STORAGE</text>

      <g transform="translate(18, 42)">
        <rect width="86" height="22" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1" />
        <text x="43" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">PostgreSQL</text>

        <rect x="94" width="60" height="22" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1" />
        <text x="124" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Redis</text>

        <rect x="162" width="72" height="22" rx="4" fill="#0f172a" stroke="#34d399" stroke-width="1" />
        <text x="198" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Supabase</text>
      </g>

      <g transform="translate(18, 72)">
        <rect width="66" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="33" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">SQLite</text>

        <rect x="74" width="76" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="112" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">SQLAlchemy</text>

        <rect x="158" width="76" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="196" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Alembic</text>
      </g>

      <g transform="translate(18, 102)">
        <rect width="125" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="62" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Indexing &amp; RAG</text>

        <rect x="133" width="101" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="183" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Vector DBs</text>
      </g>
    </g>

    <!-- 5. Infrastructure & Cloud -->
    <g transform="translate(295, 168)">
      <rect width="270" height="150" rx="10" fill="#090e1a" stroke="#1e293b" stroke-width="1.5" />
      <path d="M 0 0 L 270 0" stroke="#f59e0b" stroke-width="2.5" />
      <text x="18" y="26" fill="#f59e0b" class="mono" font-size="11" font-weight="800">05 // INFRA &amp; DEPLOYMENT</text>

      <g transform="translate(18, 42)">
        <rect width="66" height="22" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="1" />
        <text x="33" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Docker</text>

        <rect x="74" width="76" height="22" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="1" />
        <text x="112" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Railway</text>

        <rect x="158" width="76" height="22" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="1" />
        <text x="196" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Vercel</text>
      </g>

      <g transform="translate(18, 72)">
        <rect width="66" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="33" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Git</text>

        <rect x="74" width="96" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="122" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">GitHub Actions</text>

        <rect x="178" width="56" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="206" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">CI/CD</text>
      </g>

      <g transform="translate(18, 102)">
        <rect width="86" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="43" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Cloudflare</text>

        <rect x="94" width="140" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="164" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Domain &amp; DNS Eng</text>
      </g>
    </g>

    <!-- 6. Creative & Motion -->
    <g transform="translate(590, 168)">
      <rect width="270" height="150" rx="10" fill="#090e1a" stroke="#1e293b" stroke-width="1.5" />
      <path d="M 0 0 L 270 0" stroke="#ec4899" stroke-width="2.5" />
      <text x="18" y="26" fill="#ec4899" class="mono" font-size="11" font-weight="800">06 // CREATIVE &amp; MOTION</text>

      <g transform="translate(18, 42)">
        <rect width="66" height="22" rx="4" fill="#0f172a" stroke="#ec4899" stroke-width="1" />
        <text x="33" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Figma</text>

        <rect x="74" width="76" height="22" rx="4" fill="#0f172a" stroke="#ec4899" stroke-width="1" />
        <text x="112" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Three.js</text>

        <rect x="158" width="76" height="22" rx="4" fill="#0f172a" stroke="#ec4899" stroke-width="1" />
        <text x="196" y="15" fill="#f8fafc" class="mono" font-size="10" font-weight="700" text-anchor="middle">Blender</text>
      </g>

      <g transform="translate(18, 72)">
        <rect width="76" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="38" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">WebGL</text>

        <rect x="84" width="76" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="122" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Framer</text>

        <rect x="168" width="66" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="201" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Canvas</text>
      </g>

      <g transform="translate(18, 102)">
        <rect width="125" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="62" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Micro-Animations</text>

        <rect x="133" width="101" height="22" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <text x="183" y="15" fill="#94a3b8" class="mono" font-size="10" text-anchor="middle">Design Systems</text>
      </g>
    </g>
  </g>
</svg>"""


def get_ai_workflow_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 320" width="100%" height="100%">
  <defs>
    <linearGradient id="wf-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16" />
      <stop offset="50%" stop-color="#0d1424" />
      <stop offset="100%" stop-color="#050810" />
    </linearGradient>

    <linearGradient id="beam-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>

    <filter id="wf-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    @keyframes packet-flow {
      0% { stroke-dashoffset: 80; }
      100% { stroke-dashoffset: 0; }
    }
    .flow-packet { stroke-dasharray: 8 8; animation: packet-flow 2.5s linear infinite; }
  </style>

  <rect width="940" height="320" rx="16" fill="url(#wf-bg)" stroke="#1e293b" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(36, 30)">
    <rect width="8" height="20" fill="#c084fc" rx="2" />
    <text x="20" y="16" fill="#f8fafc" class="sans" font-size="18" font-weight="900">AI × ENGINEERING PIPELINE</text>
    <text x="320" y="16" fill="#64748b" class="mono" font-size="11">AI IS AN ENGINEERING MULTIPLIER • HUMAN RETAINS ARCHITECTURAL COMMAND</text>
  </g>

  <line x1="36" y1="64" x2="904" y2="64" stroke="#1e293b" stroke-width="1" />

  <!-- Pipeline Flow Nodes: Row 1 -->
  <g transform="translate(36, 85)">
    <!-- Node 1: IDEA -->
    <g>
      <rect width="150" height="60" rx="8" fill="#0b1220" stroke="#38bdf8" stroke-width="1.5" />
      <text x="14" y="24" fill="#38bdf8" class="mono" font-size="9" font-weight="800">PHASE 01</text>
      <text x="14" y="44" fill="#f8fafc" class="sans" font-size="15" font-weight="800">IDEA &amp; VISION</text>
    </g>

    <!-- Arrow 1 -->
    <line x1="150" y1="30" x2="180" y2="30" stroke="#38bdf8" stroke-width="2" class="flow-packet" />

    <!-- Node 2: RESEARCH -->
    <g transform="translate(180, 0)">
      <rect width="150" height="60" rx="8" fill="#0b1220" stroke="#38bdf8" stroke-width="1.5" />
      <text x="14" y="24" fill="#38bdf8" class="mono" font-size="9" font-weight="800">PHASE 02</text>
      <text x="14" y="44" fill="#f8fafc" class="sans" font-size="15" font-weight="800">RESEARCH</text>
    </g>

    <!-- Arrow 2 -->
    <line x1="330" y1="30" x2="360" y2="30" stroke="#818cf8" stroke-width="2" class="flow-packet" />

    <!-- Node 3: ARCHITECTURE (Highlight) -->
    <g transform="translate(360, 0)">
      <rect width="170" height="60" rx="8" fill="#151b34" stroke="#818cf8" stroke-width="2" filter="url(#wf-glow)" />
      <text x="14" y="24" fill="#818cf8" class="mono" font-size="9" font-weight="800">PHASE 03 // CORE</text>
      <text x="14" y="44" fill="#f8fafc" class="sans" font-size="15" font-weight="900">ARCHITECTURE</text>
    </g>

    <!-- Arrow 3 -->
    <line x1="530" y1="30" x2="560" y2="30" stroke="#c084fc" stroke-width="2" class="flow-packet" />

    <!-- Node 4: AI IMPLEMENTATION (Highlight) -->
    <g transform="translate(560, 0)">
      <rect width="180" height="60" rx="8" fill="#1e1236" stroke="#c084fc" stroke-width="2" filter="url(#wf-glow)" />
      <text x="14" y="24" fill="#c084fc" class="mono" font-size="9" font-weight="800">PHASE 04 // MULTIPLY</text>
      <text x="14" y="44" fill="#f8fafc" class="sans" font-size="15" font-weight="900">AI IMPLEMENT</text>
    </g>

    <!-- Arrow 4 -->
    <line x1="740" y1="30" x2="770" y2="30" stroke="#f43f5e" stroke-width="2" class="flow-packet" />

    <!-- Node 5: TESTING -->
    <g transform="translate(770, 0)">
      <rect width="100" height="60" rx="8" fill="#0b1220" stroke="#f43f5e" stroke-width="1.5" />
      <text x="12" y="24" fill="#f43f5e" class="mono" font-size="9" font-weight="800">PHASE 05</text>
      <text x="12" y="44" fill="#f8fafc" class="sans" font-size="14" font-weight="800">TESTING</text>
    </g>
  </g>

  <!-- Connective Flow Down to Row 2 -->
  <path d="M 820 145 L 820 175 L 790 175" fill="none" stroke="#f43f5e" stroke-width="2" class="flow-packet" />

  <!-- Pipeline Flow Nodes: Row 2 (Return Path) -->
  <g transform="translate(36, 175)">
    <!-- Node 6: REVIEW & AUDIT -->
    <g transform="translate(640, 0)">
      <rect width="150" height="60" rx="8" fill="#0b1220" stroke="#34d399" stroke-width="1.5" />
      <text x="14" y="24" fill="#34d399" class="mono" font-size="9" font-weight="800">PHASE 06</text>
      <text x="14" y="44" fill="#f8fafc" class="sans" font-size="15" font-weight="800">CODE REVIEW</text>
    </g>

    <line x1="640" y1="30" x2="610" y2="30" stroke="#34d399" stroke-width="2" class="flow-packet" />

    <!-- Node 7: OPTIMIZATION -->
    <g transform="translate(430, 0)">
      <rect width="180" height="60" rx="8" fill="#0b1220" stroke="#34d399" stroke-width="1.5" />
      <text x="14" y="24" fill="#34d399" class="mono" font-size="9" font-weight="800">PHASE 07</text>
      <text x="14" y="44" fill="#f8fafc" class="sans" font-size="15" font-weight="800">OPTIMIZATION</text>
    </g>

    <line x1="430" y1="30" x2="400" y2="30" stroke="#38bdf8" stroke-width="2" class="flow-packet" />

    <!-- Node 8: DEPLOYMENT -->
    <g transform="translate(220, 0)">
      <rect width="180" height="60" rx="8" fill="#0b1220" stroke="#38bdf8" stroke-width="1.5" />
      <text x="14" y="24" fill="#38bdf8" class="mono" font-size="9" font-weight="800">PHASE 08</text>
      <text x="14" y="44" fill="#f8fafc" class="sans" font-size="15" font-weight="800">DEPLOYMENT</text>
    </g>

    <line x1="220" y1="30" x2="190" y2="30" stroke="#38bdf8" stroke-width="2" class="flow-packet" />

    <!-- Node 9: OBSERVABILITY -->
    <g transform="translate(0, 0)">
      <rect width="190" height="60" rx="8" fill="#082338" stroke="#38bdf8" stroke-width="2" filter="url(#wf-glow)" />
      <text x="14" y="24" fill="#38bdf8" class="mono" font-size="9" font-weight="800">PHASE 09 // PRODUCTION</text>
      <text x="14" y="44" fill="#f8fafc" class="sans" font-size="15" font-weight="900">OBSERVABILITY</text>
    </g>
  </g>

  <!-- Bottom Principle Callout -->
  <g transform="translate(36, 275)">
    <rect width="868" height="30" rx="6" fill="#070c14" stroke="#1e293b" stroke-width="1" />
    <text x="16" y="19" fill="#10b981" class="mono" font-size="10" font-weight="700">&gt; PRINCIPLE:</text>
    <text x="110" y="19" fill="#94a3b8" class="mono" font-size="10">AI accelerates syntax and exploratory velocity. Engineering determines architecture, security, and durability.</text>
  </g>
</svg>"""


def get_footer_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="100%" height="100%">
  <defs>
    <linearGradient id="ft-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811" />
      <stop offset="50%" stop-color="#0a1020" />
      <stop offset="100%" stop-color="#04060c" />
    </linearGradient>

    <linearGradient id="ft-text" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>

    <filter id="ft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    @keyframes beacon-pulse {
      0%, 100% { opacity: 0.4; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.08); }
    }
    .beacon { animation: beacon-pulse 3s infinite; transform-origin: 600px 75px; }
  </style>

  <rect width="1200" height="240" rx="16" fill="url(#ft-bg)" stroke="#1e293b" stroke-width="1.5" />

  <!-- Center Holographic Gateway -->
  <g transform="translate(600, 75)" class="beacon">
    <ellipse cx="0" cy="0" rx="220" ry="40" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="6 6" opacity="0.4" />
    <ellipse cx="0" cy="0" rx="140" ry="25" fill="none" stroke="#818cf8" stroke-width="1.5" opacity="0.6" />
    <circle cx="0" cy="0" r="10" fill="#ffffff" filter="url(#ft-glow)" />
  </g>

  <!-- Big Statement -->
  <g transform="translate(600, 80)">
    <text x="0" y="0" fill="url(#ft-text)" class="sans" font-size="44" font-weight="900" letter-spacing="4" text-anchor="middle" filter="url(#ft-glow)">
      BUILD. SHIP. ITERATE.
    </text>
  </g>

  <!-- Subtitle -->
  <g transform="translate(600, 125)">
    <text x="0" y="0" fill="#f8fafc" class="sans" font-size="16" font-weight="700" text-anchor="middle">
      From Lahore, Pakistan — building for the web, AI and the future.
    </text>
  </g>

  <!-- Coordinates & Hash -->
  <g transform="translate(600, 165)">
    <rect x="-190" y="-14" width="380" height="28" rx="6" fill="#090d16" stroke="#1e293b" stroke-width="1" />
    <text x="0" y="4" fill="#38bdf8" class="mono" font-size="10" font-weight="700" text-anchor="middle" letter-spacing="1">
      LAHORE, PK // 31.5204° N, 74.3587° E • PASHA DEV
    </text>
  </g>

  <!-- Bottom Micro Tagline -->
  <g transform="translate(600, 215)">
    <text x="0" y="0" fill="#64748b" class="mono" font-size="10" text-anchor="middle">
      CURIOSITY • ARCHITECTURE • EXPERIMENTATION • PERSISTENCE
    </text>
  </g>
</svg>"""


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    print(f"[*] Building static 3D-styled SVGs in: {ASSETS_DIR}")

    assets = {
        "hero-dark.svg": get_hero_dark(),
        "hero-light.svg": get_hero_light(),
        "hero.svg": get_hero_dark(),
        "typing.svg": get_typing_svg(),
        "nexora.svg": get_nexora_svg(),
        "pasha-tools.svg": get_pasha_tools_svg(),
        "wishora.svg": get_wishora_svg(),
        "zoro.svg": get_zoro_svg(),
        "creative-lab.svg": get_creative_lab_svg(),
        "tech-orbit.svg": get_tech_orbit_svg(),
        "ai-workflow.svg": get_ai_workflow_svg(),
        "footer.svg": get_footer_svg()
    }

    for fname, content in assets.items():
        fpath = os.path.join(ASSETS_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"  [OK] Generated: assets/{fname}")

    print("[*] All static assets generated successfully!")


if __name__ == "__main__":
    main()
