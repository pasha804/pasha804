"""
Master SVG Asset Builder for Pasha Dev Digital Engineering Command Center
Generates bespoke, editorial, technical SVG identity banners and diagrams.
Strict XML compliance, GitHub dark/light mode compatibility, zero fluff.
"""

import os
import xml.etree.ElementTree as ET

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(WORKSPACE_DIR, "assets")


# Shared Defs (LinearGradients, filters, patterns)
SHARED_DEFS = """
  <defs>
    <!-- Backgrounds -->
    <linearGradient id="bg-obsidian" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070a12" />
      <stop offset="50%" stop-color="#0b1120" />
      <stop offset="100%" stop-color="#05070d" />
    </linearGradient>

    <linearGradient id="bg-panel" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#090d16" />
    </linearGradient>

    <!-- Technical Accents -->
    <linearGradient id="accent-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>

    <linearGradient id="accent-blue" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#60a5fa" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>

    <linearGradient id="accent-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#c084fc" />
      <stop offset="100%" stop-color="#8b5cf6" />
    </linearGradient>

    <linearGradient id="accent-emerald" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#34d399" />
      <stop offset="100%" stop-color="#059669" />
    </linearGradient>

    <linearGradient id="border-subtle" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.5" />
      <stop offset="50%" stop-color="#334155" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0.5" />
    </linearGradient>

    <!-- Patterns -->
    <pattern id="tech-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#1e293b" stroke-width="0.75" stroke-opacity="0.45" />
    </pattern>

    <!-- Filters -->
    <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="card-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#000000" flood-opacity="0.7" />
    </filter>
  </defs>
"""


def get_hero_dark_svg():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 420" width="100%" height="100%">
  {SHARED_DEFS}
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; }}
    @keyframes pulse-subtle {{
      0%, 100% {{ opacity: 0.4; }}
      50% {{ opacity: 0.9; }}
    }}
    .pulse {{ animation: pulse-subtle 3s ease-in-out infinite; }}
  </style>

  <!-- Canvas -->
  <rect width="1100" height="420" rx="14" fill="url(#bg-obsidian)" stroke="url(#border-subtle)" stroke-width="1.5" filter="url(#card-shadow)" />
  <rect width="1100" height="420" rx="14" fill="url(#tech-grid)" opacity="0.6" />

  <!-- Top System Header Bar -->
  <g transform="translate(36, 28)">
    <circle cx="6" cy="6" r="4" fill="#10b981" filter="url(#soft-glow)" />
    <circle cx="6" cy="6" r="7" fill="none" stroke="#10b981" stroke-width="1" class="pulse" />
    <text x="22" y="10" fill="#38bdf8" class="mono" font-size="10" font-weight="700" letter-spacing="2">SYS::PASHA.DEV // DIGITAL ENGINEERING COMMAND CENTER</text>
    <text x="780" y="10" fill="#64748b" class="mono" font-size="10" letter-spacing="1">LOCATION::LAHORE, PK [31.52° N, 74.35° E]</text>
  </g>

  <line x1="36" y1="52" x2="1064" y2="52" stroke="#1e293b" stroke-width="1" />

  <!-- Left Main Editorial Title -->
  <g transform="translate(48, 90)">
    <!-- Small Category Label -->
    <rect width="160" height="22" rx="4" fill="#0c1929" stroke="#0284c7" stroke-width="1" />
    <text x="10" y="15" fill="#38bdf8" class="mono" font-size="10" font-weight="700" letter-spacing="1.5">SYSTEM ARCHITECT</text>

    <!-- Main Name Title -->
    <text x="0" y="72" fill="#f8fafc" class="sans" font-size="54" font-weight="900" letter-spacing="-1">PASHA DEV</text>
    
    <!-- Designation -->
    <text x="2" y="106" fill="#38bdf8" class="mono" font-size="18" font-weight="700" letter-spacing="3">AI FULL-STACK DEVELOPER</text>

    <!-- Mission / Vision statement -->
    <g transform="translate(2, 138)">
      <line x1="0" y1="0" x2="0" y2="46" stroke="#0284c7" stroke-width="2" />
      <text x="14" y="16" fill="#cbd5e1" class="sans" font-size="15" font-weight="500">Building intelligent software systems where</text>
      <text x="14" y="38" fill="#cbd5e1" class="sans" font-size="15" font-weight="500">
        <tspan fill="#38bdf8" font-weight="700">AI capabilities</tspan>, <tspan fill="#818cf8" font-weight="700">full-stack engineering</tspan>, and <tspan fill="#c084fc" font-weight="700">cinematic design</tspan> meet.
      </text>
    </g>

    <!-- Quick Status Tags -->
    <g transform="translate(2, 215)">
      <g>
        <rect width="125" height="28" rx="4" fill="#090d16" stroke="#1e293b" stroke-width="1" />
        <text x="12" y="18" fill="#94a3b8" class="mono" font-size="10">FOCUS // </text>
        <text x="65" y="18" fill="#f8fafc" class="mono" font-size="10" font-weight="700">AI+SYSTEMS</text>
      </g>
      <g transform="translate(135, 0)">
        <rect width="130" height="28" rx="4" fill="#090d16" stroke="#1e293b" stroke-width="1" />
        <text x="12" y="18" fill="#94a3b8" class="mono" font-size="10">BUILD // </text>
        <text x="65" y="18" fill="#c084fc" class="mono" font-size="10" font-weight="700">NEXORA</text>
      </g>
      <g transform="translate(275, 0)">
        <rect width="120" height="28" rx="4" fill="#090d16" stroke="#1e293b" stroke-width="1" />
        <text x="12" y="18" fill="#94a3b8" class="mono" font-size="10">MODE // </text>
        <text x="65" y="18" fill="#10b981" class="mono" font-size="10" font-weight="700">ACTIVE</text>
      </g>
    </g>
  </g>

  <!-- Right Technical HUD & Perspective Geometry -->
  <g transform="translate(680, 80)">
    <!-- Architectural HUD Framing Box -->
    <rect width="370" height="280" rx="10" fill="#080d1a" stroke="#1e293b" stroke-width="1.5" />
    <path d="M 0 0 L 370 0" stroke="url(#accent-cyan)" stroke-width="2" />

    <!-- Corner Accents -->
    <line x1="12" y1="12" x2="24" y2="12" stroke="#38bdf8" stroke-width="1.5" />
    <line x1="12" y1="12" x2="12" y2="24" stroke="#38bdf8" stroke-width="1.5" />
    <line x1="358" y1="12" x2="346" y2="12" stroke="#38bdf8" stroke-width="1.5" />
    <line x1="358" y1="12" x2="358" y2="24" stroke="#38bdf8" stroke-width="1.5" />

    <text x="24" y="32" fill="#38bdf8" class="mono" font-size="10" font-weight="700">SYSTEM TELEMETRY OVERLAY</text>
    <text x="346" y="32" fill="#64748b" class="mono" font-size="9" text-anchor="end">SYS_ID::804</text>
    <line x1="24" y1="42" x2="346" y2="42" stroke="#1e293b" stroke-width="1" />

    <!-- Telemetry Metrics Grid -->
    <g transform="translate(24, 60)">
      <!-- Item 1 -->
      <text x="0" y="16" fill="#64748b" class="mono" font-size="10">CORE ARCHITECTURE</text>
      <text x="322" y="16" fill="#f8fafc" class="mono" font-size="11" font-weight="700" text-anchor="end">FASTAPI + REACT + TS</text>
      <line x1="0" y1="26" x2="322" y2="26" stroke="#131c2e" stroke-width="1" />

      <!-- Item 2 -->
      <text x="0" y="48" fill="#64748b" class="mono" font-size="10">AI INTEGRATION</text>
      <text x="322" y="48" fill="#c084fc" class="mono" font-size="11" font-weight="700" text-anchor="end">LLM AGENTS • TOOL CALLING</text>
      <line x1="0" y1="58" x2="322" y2="58" stroke="#131c2e" stroke-width="1" />

      <!-- Item 3 -->
      <text x="0" y="80" fill="#64748b" class="mono" font-size="10">DATA &amp; STATE</text>
      <text x="322" y="80" fill="#34d399" class="mono" font-size="11" font-weight="700" text-anchor="end">POSTGRESQL • REDIS</text>
      <line x1="0" y1="90" x2="322" y2="90" stroke="#131c2e" stroke-width="1" />

      <!-- Item 4 -->
      <text x="0" y="112" fill="#64748b" class="mono" font-size="10">DESKTOP SYSTEM</text>
      <text x="322" y="112" fill="#38bdf8" class="mono" font-size="11" font-weight="700" text-anchor="end">ZORO 2.0 (TAURI + WIN)</text>
      <line x1="0" y1="122" x2="322" y2="122" stroke="#131c2e" stroke-width="1" />

      <!-- Item 5 -->
      <text x="0" y="144" fill="#64748b" class="mono" font-size="10">SYSTEM STATUS</text>
      <text x="322" y="144" fill="#10b981" class="mono" font-size="11" font-weight="800" text-anchor="end">● PRODUCTION ACTIVE</text>
    </g>

    <!-- Radar / Coordinate Node in corner -->
    <g transform="translate(185, 238)">
      <circle cx="0" cy="0" r="18" fill="none" stroke="#1e293b" stroke-width="1" />
      <circle cx="0" cy="0" r="9" fill="none" stroke="#0284c7" stroke-width="1" stroke-dasharray="3 3" />
      <circle cx="0" cy="0" r="3" fill="#38bdf8" />
      <text x="30" y="4" fill="#64748b" class="mono" font-size="9">PORTFOLIO v6 // NETLIFY ACTIVE</text>
    </g>
  </g>

  <!-- Bottom Command Line Ticker -->
  <g transform="translate(36, 380)">
    <rect width="1028" height="24" rx="4" fill="#060911" stroke="#1e293b" stroke-width="1" />
    <text x="14" y="16" fill="#10b981" class="mono" font-size="10" font-weight="700">&gt; pasha@core:~$</text>
    <text x="130" y="16" fill="#94a3b8" class="mono" font-size="10">sys.init --profile pasha804 --mode fullstack --ai-native --latency 14ms --status nominal</text>
    <text x="1014" y="16" fill="#38bdf8" class="mono" font-size="10" font-weight="700" text-anchor="end">SYNC: VERIFIED</text>
  </g>
</svg>"""


def get_hero_light_svg():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 420" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-light" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="50%" stop-color="#f8fafc" />
      <stop offset="100%" stop-color="#f1f5f9" />
    </linearGradient>
    <pattern id="light-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#e2e8f0" stroke-width="0.75" />
    </pattern>
  </defs>
  <style>
    .mono {{ font-family: 'JetBrains Mono', Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
  </style>

  <rect width="1100" height="420" rx="14" fill="url(#bg-light)" stroke="#cbd5e1" stroke-width="1.5" />
  <rect width="1100" height="420" rx="14" fill="url(#light-grid)" opacity="0.8" />

  <g transform="translate(36, 28)">
    <circle cx="6" cy="6" r="4" fill="#059669" />
    <text x="22" y="10" fill="#0284c7" class="mono" font-size="10" font-weight="700" letter-spacing="2">SYS::PASHA.DEV // DIGITAL ENGINEERING COMMAND CENTER</text>
    <text x="780" y="10" fill="#64748b" class="mono" font-size="10">LOCATION::LAHORE, PK [31.52° N, 74.35° E]</text>
  </g>

  <line x1="36" y1="52" x2="1064" y2="52" stroke="#e2e8f0" stroke-width="1.5" />

  <g transform="translate(48, 90)">
    <rect width="160" height="22" rx="4" fill="#e0f2fe" stroke="#0284c7" stroke-width="1" />
    <text x="10" y="15" fill="#0284c7" class="mono" font-size="10" font-weight="700" letter-spacing="1.5">SYSTEM ARCHITECT</text>

    <text x="0" y="72" fill="#0f172a" class="sans" font-size="54" font-weight="900" letter-spacing="-1">PASHA DEV</text>
    <text x="2" y="106" fill="#0284c7" class="mono" font-size="18" font-weight="700" letter-spacing="3">AI FULL-STACK DEVELOPER</text>

    <g transform="translate(2, 138)">
      <line x1="0" y1="0" x2="0" y2="46" stroke="#0284c7" stroke-width="2" />
      <text x="14" y="16" fill="#334155" class="sans" font-size="15" font-weight="500">Building intelligent software systems where</text>
      <text x="14" y="38" fill="#334155" class="sans" font-size="15" font-weight="500">
        <tspan fill="#0284c7" font-weight="700">AI capabilities</tspan>, <tspan fill="#4f46e5" font-weight="700">full-stack engineering</tspan>, and <tspan fill="#7c3aed" font-weight="700">cinematic design</tspan> meet.
      </text>
    </g>

    <g transform="translate(2, 215)">
      <rect width="125" height="28" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
      <text x="12" y="18" fill="#64748b" class="mono" font-size="10">FOCUS // </text>
      <text x="65" y="18" fill="#0f172a" class="mono" font-size="10" font-weight="700">AI+SYSTEMS</text>

      <g transform="translate(135, 0)">
        <rect width="130" height="28" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
        <text x="12" y="18" fill="#64748b" class="mono" font-size="10">BUILD // </text>
        <text x="65" y="18" fill="#7c3aed" class="mono" font-size="10" font-weight="700">NEXORA</text>
      </g>
    </g>
  </g>

  <g transform="translate(680, 80)">
    <rect width="370" height="280" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <path d="M 0 0 L 370 0" stroke="#0284c7" stroke-width="2" />
    <text x="24" y="32" fill="#0284c7" class="mono" font-size="10" font-weight="700">SYSTEM TELEMETRY OVERLAY</text>
    <text x="346" y="32" fill="#64748b" class="mono" font-size="9" text-anchor="end">SYS_ID::804</text>
    <line x1="24" y1="42" x2="346" y2="42" stroke="#e2e8f0" stroke-width="1" />

    <g transform="translate(24, 60)">
      <text x="0" y="16" fill="#64748b" class="mono" font-size="10">CORE ARCHITECTURE</text>
      <text x="322" y="16" fill="#0f172a" class="mono" font-size="11" font-weight="700" text-anchor="end">FASTAPI + REACT + TS</text>
      <line x1="0" y1="26" x2="322" y2="26" stroke="#f1f5f9" stroke-width="1" />

      <text x="0" y="48" fill="#64748b" class="mono" font-size="10">AI INTEGRATION</text>
      <text x="322" y="48" fill="#7c3aed" class="mono" font-size="11" font-weight="700" text-anchor="end">LLM AGENTS • TOOL CALLING</text>
      <line x1="0" y1="58" x2="322" y2="58" stroke="#f1f5f9" stroke-width="1" />

      <text x="0" y="80" fill="#64748b" class="mono" font-size="10">DATA &amp; STATE</text>
      <text x="322" y="80" fill="#059669" class="mono" font-size="11" font-weight="700" text-anchor="end">POSTGRESQL • REDIS</text>
      <line x1="0" y1="90" x2="322" y2="90" stroke="#f1f5f9" stroke-width="1" />

      <text x="0" y="112" fill="#64748b" class="mono" font-size="10">DESKTOP SYSTEM</text>
      <text x="322" y="112" fill="#0284c7" class="mono" font-size="11" font-weight="700" text-anchor="end">ZORO 2.0 (TAURI + WIN)</text>
      <line x1="0" y1="122" x2="322" y2="122" stroke="#f1f5f9" stroke-width="1" />

      <text x="0" y="144" fill="#64748b" class="mono" font-size="10">SYSTEM STATUS</text>
      <text x="322" y="144" fill="#059669" class="mono" font-size="11" font-weight="800" text-anchor="end">● PRODUCTION ACTIVE</text>
    </g>
  </g>
</svg>"""


def get_boot_sequence_svg():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 180" width="100%" height="100%">
  {SHARED_DEFS}
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }}
    @keyframes blink-cursor {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    .cursor {{ animation: blink-cursor 1s infinite; }}
  </style>

  <rect width="940" height="180" rx="10" fill="#070a13" stroke="#1e293b" stroke-width="1.5" />

  <!-- Terminal Header -->
  <g transform="translate(20, 20)">
    <circle cx="6" cy="6" r="4" fill="#ef4444" />
    <circle cx="20" cy="6" r="4" fill="#f59e0b" />
    <circle cx="34" cy="6" r="4" fill="#10b981" />
    <text x="54" y="10" fill="#38bdf8" class="mono" font-size="10" font-weight="700">TERMINAL // SYSTEM INITIALIZATION</text>
    <text x="890" y="10" fill="#64748b" class="mono" font-size="10" text-anchor="end">SECURE PROTOCOL v2.4</text>
  </g>

  <line x1="20" y1="40" x2="920" y2="40" stroke="#1e293b" stroke-width="1" />

  <!-- Boot Log Lines -->
  <g transform="translate(24, 62)" class="mono" font-size="11">
    <text x="0" y="0" fill="#38bdf8">$ boot pasha.dev --subsystems all</text>
    
    <g transform="translate(0, 20)">
      <text x="0" y="0" fill="#10b981">[ OK ]</text>
      <text x="50" y="0" fill="#94a3b8">identity loaded</text>
      <text x="280" y="0" fill="#64748b">// Muhammad Mubashar (Pasha Dev) • Lahore, PK</text>
    </g>

    <g transform="translate(0, 40)">
      <text x="0" y="0" fill="#10b981">[ OK ]</text>
      <text x="50" y="0" fill="#94a3b8">engineering core online</text>
      <text x="280" y="0" fill="#64748b">// React • Next.js • TypeScript • Python • FastAPI</text>
    </g>

    <g transform="translate(0, 60)">
      <text x="0" y="0" fill="#10b981">[ OK ]</text>
      <text x="50" y="0" fill="#94a3b8">product lab mounted</text>
      <text x="280" y="0" fill="#64748b">// Nexora (PvP Growth) • Pasha Tools • Wishora • Zoro 2.0</text>
    </g>

    <g transform="translate(0, 80)">
      <text x="0" y="0" fill="#10b981">[ OK ]</text>
      <text x="50" y="0" fill="#94a3b8">github telemetry stream</text>
      <text x="280" y="0" fill="#64748b">// 59 public repositories • 226 verified events</text>
    </g>

    <g transform="translate(0, 100)">
      <text x="0" y="0" fill="#38bdf8">&gt; SYSTEM STATUS:</text>
      <text x="130" y="0" fill="#10b981" font-weight="700">ONLINE (LATENCY: 12ms)</text>
      <rect x="310" y="-10" width="7" height="13" fill="#38bdf8" class="cursor" />
    </g>
  </g>
</svg>"""


def get_cli_terminal_svg():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 220" width="100%" height="100%">
  {SHARED_DEFS}
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }}
  </style>

  <rect width="940" height="220" rx="10" fill="#080c16" stroke="#1e293b" stroke-width="1.5" />

  <!-- Terminal Top -->
  <g transform="translate(20, 20)">
    <circle cx="6" cy="6" r="4" fill="#ef4444" />
    <circle cx="20" cy="6" r="4" fill="#f59e0b" />
    <circle cx="34" cy="6" r="4" fill="#10b981" />
    <text x="54" y="10" fill="#64748b" class="mono" font-size="10">zsh — pasha@dev: ~</text>
  </g>
  <line x1="20" y1="38" x2="920" y2="38" stroke="#1e293b" stroke-width="1" />

  <!-- 2 Column CLI Session -->
  <g transform="translate(28, 62)" class="mono">
    <!-- Left Column -->
    <g font-size="11">
      <text x="0" y="0" fill="#38bdf8">$ whoami</text>
      <text x="0" y="18" fill="#f8fafc" font-weight="700">pasha804 // Muhammad Mubashar</text>

      <text x="0" y="44" fill="#38bdf8">$ role</text>
      <text x="0" y="62" fill="#cbd5e1">AI Full-Stack Developer &amp; Systems Architect</text>

      <text x="0" y="88" fill="#38bdf8">$ current_build</text>
      <text x="0" y="106" fill="#c084fc" font-weight="700">NEXORA (Gamify Professional Growth)</text>

      <text x="0" y="132" fill="#38bdf8">$ mission</text>
      <text x="0" y="150" fill="#10b981" font-weight="700">Think → Architect → Build → Test → Ship → Iterate</text>
    </g>

    <!-- Right Column: System Profile Panel -->
    <g transform="translate(520, -10)">
      <rect width="365" height="155" rx="8" fill="#0b1220" stroke="#1e293b" stroke-width="1.2" />
      <path d="M 0 0 L 365 0" stroke="url(#accent-purple)" stroke-width="2" />
      <text x="16" y="24" fill="#c084fc" font-size="10" font-weight="700">GUI SYSTEM PROFILE</text>

      <g transform="translate(16, 46)" font-size="11">
        <rect width="155" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
        <circle cx="12" cy="13" r="3" fill="#38bdf8" />
        <text x="24" y="17" fill="#f8fafc">AI Engineering</text>

        <g transform="translate(168, 0)">
          <rect width="160" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
          <circle cx="12" cy="13" r="3" fill="#818cf8" />
          <text x="24" y="17" fill="#f8fafc">Full-Stack Web</text>
        </g>

        <g transform="translate(0, 36)">
          <rect width="155" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
          <circle cx="12" cy="13" r="3" fill="#c084fc" />
          <text x="24" y="17" fill="#f8fafc">Native Desktop</text>
        </g>

        <g transform="translate(168, 36)">
          <rect width="160" height="26" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1" />
          <circle cx="12" cy="13" r="3" fill="#34d399" />
          <text x="24" y="17" fill="#f8fafc">Automation &amp; RAG</text>
        </g>
      </g>
    </g>
  </g>
</svg>"""


def get_tech_universe_svg():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 440" width="100%" height="100%">
  {SHARED_DEFS}
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
  </style>

  <rect width="940" height="440" rx="14" fill="#070a13" stroke="#1e293b" stroke-width="1.5" />
  <rect width="940" height="440" rx="14" fill="url(#tech-grid)" opacity="0.4" />

  <!-- Top Title -->
  <g transform="translate(36, 28)">
    <text x="0" y="16" fill="#f8fafc" class="sans" font-size="18" font-weight="900">TECHNOLOGY UNIVERSE</text>
    <text x="250" y="16" fill="#64748b" class="mono" font-size="11">// VISUAL ECOSYSTEM (NO GENERIC BADGE WALLS)</text>
  </g>
  <line x1="36" y1="56" x2="904" y2="56" stroke="#1e293b" stroke-width="1" />

  <!-- Center Core Node -->
  <g transform="translate(470, 240)">
    <circle cx="0" cy="0" r="48" fill="#0b1426" stroke="#38bdf8" stroke-width="1.5" filter="url(#soft-glow)" />
    <circle cx="0" cy="0" r="38" fill="#0f1f38" stroke="#0284c7" stroke-width="1" />
    <text x="0" y="-6" fill="#38bdf8" class="mono" font-size="10" font-weight="800" text-anchor="middle">PASHA DEV</text>
    <text x="0" y="10" fill="#f8fafc" class="sans" font-size="11" font-weight="800" text-anchor="middle">CORE ENGINE</text>
  </g>

  <!-- 6 Orbiting Sectors -->
  <!-- 1. Frontend (Top Left) -->
  <g transform="translate(36, 75)">
    <rect width="265" height="145" rx="8" fill="#080e1a" stroke="#1e293b" stroke-width="1.2" />
    <path d="M 0 0 L 265 0" stroke="#38bdf8" stroke-width="2" />
    <text x="14" y="22" fill="#38bdf8" class="mono" font-size="10" font-weight="800">01 // FRONTEND</text>
    <g transform="translate(14, 38)" class="mono" font-size="10">
      <rect width="65" height="22" rx="3" fill="#0f172a" stroke="#38bdf8" stroke-width="1" /><text x="32" y="15" fill="#f8fafc" text-anchor="middle">React</text>
      <rect x="73" width="75" height="22" rx="3" fill="#0f172a" stroke="#38bdf8" stroke-width="1" /><text x="110" y="15" fill="#f8fafc" text-anchor="middle">Next.js</text>
      <rect x="156" width="90" height="22" rx="3" fill="#0f172a" stroke="#38bdf8" stroke-width="1" /><text x="201" y="15" fill="#f8fafc" text-anchor="middle">TypeScript</text>
      <g transform="translate(0, 30)">
        <rect width="75" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="37" y="15" fill="#94a3b8" text-anchor="middle">Tailwind</text>
        <rect x="83" width="60" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="113" y="15" fill="#94a3b8" text-anchor="middle">Vite</text>
        <rect x="151" width="95" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="198" y="15" fill="#94a3b8" text-anchor="middle">shadcn/ui</text>
      </g>
      <g transform="translate(0, 60)">
        <rect width="115" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="57" y="15" fill="#94a3b8" text-anchor="middle">Framer Motion</text>
        <rect x="123" width="123" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="184" y="15" fill="#94a3b8" text-anchor="middle">TanStack Query</text>
      </g>
    </g>
  </g>

  <!-- 2. Backend (Top Center/Right) -->
  <g transform="translate(337, 75)">
    <rect width="265" height="145" rx="8" fill="#080e1a" stroke="#1e293b" stroke-width="1.2" />
    <path d="M 0 0 L 265 0" stroke="#818cf8" stroke-width="2" />
    <text x="14" y="22" fill="#818cf8" class="mono" font-size="10" font-weight="800">02 // BACKEND</text>
    <g transform="translate(14, 38)" class="mono" font-size="10">
      <rect width="70" height="22" rx="3" fill="#0f172a" stroke="#818cf8" stroke-width="1" /><text x="35" y="15" fill="#f8fafc" text-anchor="middle">Python</text>
      <rect x="78" width="75" height="22" rx="3" fill="#0f172a" stroke="#818cf8" stroke-width="1" /><text x="115" y="15" fill="#f8fafc" text-anchor="middle">FastAPI</text>
      <rect x="161" width="85" height="22" rx="3" fill="#0f172a" stroke="#818cf8" stroke-width="1" /><text x="203" y="15" fill="#f8fafc" text-anchor="middle">Node.js</text>
      <g transform="translate(0, 30)">
        <rect width="75" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="37" y="15" fill="#94a3b8" text-anchor="middle">Express</text>
        <rect x="83" width="75" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="120" y="15" fill="#94a3b8" text-anchor="middle">Pydantic</text>
        <rect x="166" width="80" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="206" y="15" fill="#94a3b8" text-anchor="middle">AsyncIO</text>
      </g>
      <g transform="translate(0, 60)">
        <rect width="115" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="57" y="15" fill="#94a3b8" text-anchor="middle">WebSockets</text>
        <rect x="123" width="123" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="184" y="15" fill="#94a3b8" text-anchor="middle">REST Services</text>
      </g>
    </g>
  </g>

  <!-- 3. AI & Multipliers (Top Right) -->
  <g transform="translate(638, 75)">
    <rect width="265" height="145" rx="8" fill="#080e1a" stroke="#1e293b" stroke-width="1.2" />
    <path d="M 0 0 L 265 0" stroke="#c084fc" stroke-width="2" />
    <text x="14" y="22" fill="#c084fc" class="mono" font-size="10" font-weight="800">03 // AI SUBSYSTEMS</text>
    <g transform="translate(14, 38)" class="mono" font-size="10">
      <rect width="65" height="22" rx="3" fill="#0f172a" stroke="#c084fc" stroke-width="1" /><text x="32" y="15" fill="#f8fafc" text-anchor="middle">LLMs</text>
      <rect x="73" width="85" height="22" rx="3" fill="#0f172a" stroke="#c084fc" stroke-width="1" /><text x="115" y="15" fill="#f8fafc" text-anchor="middle">AI Agents</text>
      <rect x="166" width="80" height="22" rx="3" fill="#0f172a" stroke="#c084fc" stroke-width="1" /><text x="206" y="15" fill="#f8fafc" text-anchor="middle">AI APIs</text>
      <g transform="translate(0, 30)">
        <rect width="115" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="57" y="15" fill="#94a3b8" text-anchor="middle">Tool Calling</text>
        <rect x="123" width="123" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="184" y="15" fill="#94a3b8" text-anchor="middle">Prompt Eng</text>
      </g>
      <g transform="translate(0, 60)">
        <rect width="115" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="57" y="15" fill="#94a3b8" text-anchor="middle">Voice Pipelines</text>
        <rect x="123" width="123" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="184" y="15" fill="#94a3b8" text-anchor="middle">Automation</text>
      </g>
    </g>
  </g>

  <!-- 4. Data (Bottom Left) -->
  <g transform="translate(36, 245)">
    <rect width="265" height="155" rx="8" fill="#080e1a" stroke="#1e293b" stroke-width="1.2" />
    <path d="M 0 0 L 265 0" stroke="#34d399" stroke-width="2" />
    <text x="14" y="22" fill="#34d399" class="mono" font-size="10" font-weight="800">04 // DATA &amp; STORAGE</text>
    <g transform="translate(14, 38)" class="mono" font-size="10">
      <rect width="90" height="22" rx="3" fill="#0f172a" stroke="#34d399" stroke-width="1" /><text x="45" y="15" fill="#f8fafc" text-anchor="middle">PostgreSQL</text>
      <rect x="98" width="65" height="22" rx="3" fill="#0f172a" stroke="#34d399" stroke-width="1" /><text x="130" y="15" fill="#f8fafc" text-anchor="middle">Redis</text>
      <rect x="171" width="75" height="22" rx="3" fill="#0f172a" stroke="#34d399" stroke-width="1" /><text x="208" y="15" fill="#f8fafc" text-anchor="middle">SQLite</text>
      <g transform="translate(0, 30)">
        <rect width="85" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="42" y="15" fill="#94a3b8" text-anchor="middle">Supabase</text>
        <rect x="93" width="90" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="138" y="15" fill="#94a3b8" text-anchor="middle">SQLAlchemy</text>
        <rect x="191" width="55" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="218" y="15" fill="#94a3b8" text-anchor="middle">Alembic</text>
      </g>
    </g>
  </g>

  <!-- 5. Infra (Bottom Center) -->
  <g transform="translate(337, 245)">
    <rect width="265" height="155" rx="8" fill="#080e1a" stroke="#1e293b" stroke-width="1.2" />
    <path d="M 0 0 L 265 0" stroke="#f59e0b" stroke-width="2" />
    <text x="14" y="22" fill="#f59e0b" class="mono" font-size="10" font-weight="800">05 // INFRASTRUCTURE</text>
    <g transform="translate(14, 38)" class="mono" font-size="10">
      <rect width="70" height="22" rx="3" fill="#0f172a" stroke="#f59e0b" stroke-width="1" /><text x="35" y="15" fill="#f8fafc" text-anchor="middle">Docker</text>
      <rect x="78" width="80" height="22" rx="3" fill="#0f172a" stroke="#f59e0b" stroke-width="1" /><text x="118" y="15" fill="#f8fafc" text-anchor="middle">Railway</text>
      <rect x="166" width="80" height="22" rx="3" fill="#0f172a" stroke="#f59e0b" stroke-width="1" /><text x="206" y="15" fill="#f8fafc" text-anchor="middle">Vercel</text>
      <g transform="translate(0, 30)">
        <rect width="55" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="27" y="15" fill="#94a3b8" text-anchor="middle">Git</text>
        <rect x="63" width="110" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="118" y="15" fill="#94a3b8" text-anchor="middle">GitHub Actions</text>
        <rect x="181" width="65" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="213" y="15" fill="#94a3b8" text-anchor="middle">CI/CD</text>
      </g>
    </g>
  </g>

  <!-- 6. Creative (Bottom Right) -->
  <g transform="translate(638, 245)">
    <rect width="265" height="155" rx="8" fill="#080e1a" stroke="#1e293b" stroke-width="1.2" />
    <path d="M 0 0 L 265 0" stroke="#ec4899" stroke-width="2" />
    <text x="14" y="22" fill="#ec4899" class="mono" font-size="10" font-weight="800">06 // CREATIVE &amp; MOTION</text>
    <g transform="translate(14, 38)" class="mono" font-size="10">
      <rect width="65" height="22" rx="3" fill="#0f172a" stroke="#ec4899" stroke-width="1" /><text x="32" y="15" fill="#f8fafc" text-anchor="middle">Figma</text>
      <rect x="73" width="80" height="22" rx="3" fill="#0f172a" stroke="#ec4899" stroke-width="1" /><text x="113" y="15" fill="#f8fafc" text-anchor="middle">Three.js</text>
      <rect x="161" width="85" height="22" rx="3" fill="#0f172a" stroke="#ec4899" stroke-width="1" /><text x="203" y="15" fill="#f8fafc" text-anchor="middle">Blender</text>
      <g transform="translate(0, 30)">
        <rect width="70" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="35" y="15" fill="#94a3b8" text-anchor="middle">WebGL</text>
        <rect x="78" width="70" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="113" y="15" fill="#94a3b8" text-anchor="middle">Framer</text>
        <rect x="156" width="90" height="22" rx="3" fill="#0f172a" stroke="#334155" stroke-width="1" /><text x="201" y="15" fill="#94a3b8" text-anchor="middle">Motion UX</text>
      </g>
    </g>
  </g>
</svg>"""


def get_architecture_svg():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 320" width="100%" height="100%">
  {SHARED_DEFS}
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
  </style>

  <rect width="940" height="320" rx="14" fill="#070a13" stroke="#1e293b" stroke-width="1.5" />

  <g transform="translate(36, 28)">
    <text x="0" y="16" fill="#f8fafc" class="sans" font-size="18" font-weight="900">SYSTEM ARCHITECTURE BLUEPRINT</text>
    <text x="330" y="16" fill="#64748b" class="mono" font-size="11">// HOW I DESIGN RESILIENT PRODUCTION SYSTEMS</text>
  </g>
  <line x1="36" y1="56" x2="904" y2="56" stroke="#1e293b" stroke-width="1" />

  <!-- 4 Tier Horizontal Flow -->
  <g transform="translate(36, 85)">
    <!-- Tier 1: Client Interfaces -->
    <g>
      <rect width="190" height="180" rx="8" fill="#09101d" stroke="#38bdf8" stroke-width="1.5" />
      <path d="M 0 0 L 190 0" stroke="#38bdf8" stroke-width="2" />
      <text x="16" y="24" fill="#38bdf8" class="mono" font-size="10" font-weight="800">TIER 01 // CLIENTS</text>
      
      <g transform="translate(16, 44)" class="mono" font-size="11">
        <text x="0" y="16" fill="#f8fafc" font-weight="700">Web App (React/Next)</text>
        <text x="0" y="36" fill="#94a3b8">Native Win (Tauri)</text>
        <text x="0" y="56" fill="#94a3b8">Mobile Responsive</text>
        <text x="0" y="76" fill="#94a3b8">Canvas / WebGL</text>
        <text x="0" y="106" fill="#64748b" font-size="9">60 FPS • Type Safe</text>
      </g>
    </g>

    <!-- Connector 1 -->
    <line x1="190" y1="90" x2="225" y2="90" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 4" />

    <!-- Tier 2: Gateway & API -->
    <g transform="translate(225, 0)">
      <rect width="190" height="180" rx="8" fill="#0e1124" stroke="#818cf8" stroke-width="1.5" />
      <path d="M 0 0 L 190 0" stroke="#818cf8" stroke-width="2" />
      <text x="16" y="24" fill="#818cf8" class="mono" font-size="10" font-weight="800">TIER 02 // API &amp; CORE</text>
      
      <g transform="translate(16, 44)" class="mono" font-size="11">
        <text x="0" y="16" fill="#f8fafc" font-weight="700">FastAPI Async</text>
        <text x="0" y="36" fill="#94a3b8">WebSockets Pub/Sub</text>
        <text x="0" y="56" fill="#94a3b8">Pydantic Schemas</text>
        <text x="0" y="76" fill="#94a3b8">Rate Limiting &amp; Auth</text>
        <text x="0" y="106" fill="#64748b" font-size="9">Docker Microservices</text>
      </g>
    </g>

    <!-- Connector 2 -->
    <line x1="415" y1="90" x2="450" y2="90" stroke="#818cf8" stroke-width="2" stroke-dasharray="4 4" />

    <!-- Tier 3: AI Engine -->
    <g transform="translate(450, 0)">
      <rect width="200" height="180" rx="8" fill="#140d24" stroke="#c084fc" stroke-width="1.5" />
      <path d="M 0 0 L 200 0" stroke="#c084fc" stroke-width="2" />
      <text x="16" y="24" fill="#c084fc" class="mono" font-size="10" font-weight="800">TIER 03 // AI RUNTIME</text>
      
      <g transform="translate(16, 44)" class="mono" font-size="11">
        <text x="0" y="16" fill="#f8fafc" font-weight="700">LLM Reasoning</text>
        <text x="0" y="36" fill="#94a3b8">Autonomous Agents</text>
        <text x="0" y="56" fill="#94a3b8">Tool &amp; Function Call</text>
        <text x="0" y="76" fill="#94a3b8">Memory &amp; Context RAG</text>
        <text x="0" y="106" fill="#64748b" font-size="9">Evaluation &amp; Judging</text>
      </g>
    </g>

    <!-- Connector 3 -->
    <line x1="650" y1="90" x2="685" y2="90" stroke="#c084fc" stroke-width="2" stroke-dasharray="4 4" />

    <!-- Tier 4: Persistent Data -->
    <g transform="translate(685, 0)">
      <rect width="185" height="180" rx="8" fill="#081414" stroke="#34d399" stroke-width="1.5" />
      <path d="M 0 0 L 185 0" stroke="#34d399" stroke-width="2" />
      <text x="16" y="24" fill="#34d399" class="mono" font-size="10" font-weight="800">TIER 04 // DATA LAYER</text>
      
      <g transform="translate(16, 44)" class="mono" font-size="11">
        <text x="0" y="16" fill="#f8fafc" font-weight="700">PostgreSQL (Relational)</text>
        <text x="0" y="36" fill="#94a3b8">Redis (Cache &amp; Queue)</text>
        <text x="0" y="56" fill="#94a3b8">Vector Embeddings</text>
        <text x="0" y="76" fill="#94a3b8">Cloudflare CDN Edge</text>
        <text x="0" y="106" fill="#64748b" font-size="9">ACID Compliant</text>
      </g>
    </g>
  </g>
</svg>"""


def get_pakistan_global_svg():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 160" width="100%" height="100%">
  {SHARED_DEFS}
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
  </style>

  <rect width="940" height="160" rx="12" fill="#070c14" stroke="#1e293b" stroke-width="1.5" />

  <g transform="translate(36, 32)">
    <circle cx="8" cy="8" r="6" fill="#10b981" filter="url(#soft-glow)" />
    <text x="26" y="13" fill="#f8fafc" class="sans" font-size="17" font-weight="900">LAHORE, PAKISTAN ──────► GLOBAL INTERNET</text>
    <text x="26" y="36" fill="#38bdf8" class="mono" font-size="11" font-weight="700">COORDINATES: 31.5204° N, 74.3587° E • TIMEZONE: PKT (UTC+5)</text>
    <text x="26" y="66" fill="#94a3b8" class="sans" font-size="13">
      Building from Pakistan with global standards. Creating software systems, AI tooling, and products that serve developers and users worldwide.
    </text>
  </g>

  <!-- Right Side Visual Marker -->
  <g transform="translate(820, 80)">
    <circle cx="0" cy="0" r="34" fill="none" stroke="#1e293b" stroke-width="1.5" />
    <circle cx="0" cy="0" r="22" fill="none" stroke="#10b981" stroke-width="1" stroke-dasharray="4 4" />
    <circle cx="0" cy="0" r="5" fill="#10b981" />
    <text x="0" y="48" fill="#64748b" class="mono" font-size="9" text-anchor="middle">PK::ACTIVE</text>
  </g>
</svg>"""


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    print(f"[*] Building master asset SVGs in: {ASSETS_DIR}")

    assets = {
        "hero-dark.svg": get_hero_dark_svg(),
        "hero-light.svg": get_hero_light_svg(),
        "boot-sequence.svg": get_boot_sequence_svg(),
        "cli-terminal.svg": get_cli_terminal_svg(),
        "tech-universe.svg": get_tech_universe_svg(),
        "architecture.svg": get_architecture_svg(),
        "pakistan-global.svg": get_pakistan_global_svg(),
    }

    for fname, content in assets.items():
        fpath = os.path.join(ASSETS_DIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        # Validate XML
        try:
            ET.parse(fpath)
            print(f"  [OK] Valid XML & generated: assets/{fname}")
        except Exception as e:
            print(f"  [ERR] Invalid XML in assets/{fname}: {e}")

    print("[*] Master SVG assets built successfully!")


if __name__ == "__main__":
    main()
