"""
Updater script for scripts/build_sushmita_style.py
Adds bespoke SVG builders for SyncForge, PrivateDoc, and GhostReview,
fixes keyframe transform override bugs, and regenerates all assets.
"""

import os
import re

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "build_sushmita_style.py")

with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix @keyframes transform override in all project cards
content = re.sub(
    r"@keyframes (p\d+|pdp)-in \{ from \{ opacity: 0; transform: translateY\(12px\); \} to \{ opacity: 1; transform: none; \} \}",
    r"@keyframes \1-in { from { opacity: 0; } to { opacity: 1; } }",
    content
)

# 2. Define the new project SVG functions
NEW_FUNCTIONS = '''

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
'''

# Insert new functions right before build_tech_constellation_svg
target_marker = "# ─────────────────────────────────────────────────────────────────────────────\n# 7. SECTION 04: TOOLKIT / TECH CONSTELLATION"
if target_marker in content:
    content = content.replace(target_marker, NEW_FUNCTIONS + "\n\n" + target_marker)
else:
    print("Warning: target_marker not found exactly, attempting alternate insertion.")
    content = content.replace("def build_tech_constellation_svg():", NEW_FUNCTIONS + "\ndef build_tech_constellation_svg():")

# Update main() svgs dict to include the new cards
old_main_svgs = '''        "project-devpilot.svg": build_project_devpilot_svg(),
        "project-nexora.svg": build_project_nexora_svg(),
        "project-opencluely.svg": build_project_opencluely_svg(),
        "project-pashatools.svg": build_project_pashatools_svg(),
        "project-bmw7.svg": build_project_bmw7_svg(),
        "project-wishora.svg": build_project_wishora_svg(),'''

new_main_svgs = '''        "project-devpilot.svg": build_project_devpilot_svg(),
        "project-syncforge.svg": build_project_syncforge_svg(),
        "project-privatedoc.svg": build_project_privatedoc_svg(),
        "project-ghostreview.svg": build_project_ghostreview_svg(),
        "project-opencluely.svg": build_project_opencluely_svg(),
        "project-bmw7.svg": build_project_bmw7_svg(),
        "project-nexora.svg": build_project_nexora_svg(),
        "project-pashatools.svg": build_project_pashatools_svg(),
        "project-wishora.svg": build_project_wishora_svg(),'''

content = content.replace(old_main_svgs, new_main_svgs)

with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated build_sushmita_style.py successfully.")
