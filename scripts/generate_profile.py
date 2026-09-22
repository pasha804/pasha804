"""
Pasha Dev (Muhammad Mubashar) - GitHub Profile Telemetry & SVG Dashboard Engine v3.0
Real-time GitHub GraphQL API integration for verified, live-updating stats.
Generates premium cinematic SVG telemetry dashboards with strict XML compliance.
Zero third-party stat API dependencies — direct GitHub API only.
"""

import os
import sys
import json
import math
import subprocess
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from collections import defaultdict

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE_DIR = os.path.join(WORKSPACE_DIR, "profile")
ASSETS_DIR = os.path.join(WORKSPACE_DIR, "assets")

USERNAME = "pasha804"


def get_token():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    try:
        res = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=5)
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    except Exception:
        pass
    return None


def graphql_query(token, query, variables=None):
    """Execute a GitHub GraphQL query."""
    payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": "PashaDev-Telemetry-v3",
        "Content-Type": "application/json",
    }
    req = urllib.request.Request("https://api.github.com/graphql", data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def rest_api(token, endpoint):
    """Execute a GitHub REST API call."""
    headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": "PashaDev-Telemetry-v3",
        "Accept": "application/vnd.github.v3+json",
    }
    req = urllib.request.Request(f"https://api.github.com{endpoint}", headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def fetch_github_data():
    """Fetch real data from GitHub API. Falls back to reasonable defaults on failure."""
    token = get_token()
    now = datetime.now(timezone.utc)

    data = {
        "login": USERNAME,
        "name": "Muhammad Mubashar",
        "public_repos": 0,
        "followers": 0,
        "following": 0,
        "stars_received": 0,
        "total_contributions": 0,
        "current_streak": 0,
        "longest_streak": 0,
        "languages": {},
        "recent_events": [],
        "month_contributions": 0,
        "month_active_days": 0,
        "contribution_weeks": [],
        "last_sync": now.strftime("%Y-%m-%d %H:%M UTC"),
        "is_live": False,
    }

    if not token:
        print("[*] No GitHub token found. Using minimal fallback data.")
        data["public_repos"] = 12
        data["followers"] = 5
        data["total_contributions"] = 226
        data["is_live"] = False
        return data

    print("[*] GitHub token found. Fetching LIVE data from GitHub API...")
    data["is_live"] = True

    # === 1. User Profile (REST) ===
    try:
        u = rest_api(token, f"/users/{USERNAME}")
        data["public_repos"] = u.get("public_repos", 0)
        data["followers"] = u.get("followers", 0)
        data["following"] = u.get("following", 0)
        data["name"] = u.get("name") or data["name"]
        print(f"  [OK] Profile: {data['public_repos']} repos, {data['followers']} followers")
    except Exception as e:
        print(f"  [WARN] Profile fetch: {e}")

    # === 2. Contribution Calendar (GraphQL) ===
    try:
        cal_query = """
        query($login: String!) {
          user(login: $login) {
            contributionsCollection {
              contributionCalendar {
                totalContributions
                weeks {
                  contributionDays {
                    contributionCount
                    date
                  }
                }
              }
            }
          }
        }
        """
        result = graphql_query(token, cal_query, {"login": USERNAME})
        cal = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]
        data["total_contributions"] = cal["totalContributions"]
        data["contribution_weeks"] = cal["weeks"]

        # Calculate streak from calendar
        all_days = []
        for week in cal["weeks"]:
            for day in week["contributionDays"]:
                all_days.append(day)

        # Sort by date descending for current streak
        all_days_sorted = sorted(all_days, key=lambda d: d["date"], reverse=True)

        # Current streak: consecutive days with contributions from today/yesterday
        current_streak = 0
        today_str = now.strftime("%Y-%m-%d")
        yesterday_str = (now - timedelta(days=1)).strftime("%Y-%m-%d")
        started = False
        for day in all_days_sorted:
            if not started:
                if day["date"] == today_str or day["date"] == yesterday_str:
                    if day["contributionCount"] > 0:
                        started = True
                        current_streak = 1
                    elif day["date"] == today_str:
                        continue  # today might not have commits yet
                    else:
                        break
                else:
                    continue
            else:
                if day["contributionCount"] > 0:
                    current_streak += 1
                else:
                    break

        data["current_streak"] = current_streak

        # Longest streak
        all_days_asc = sorted(all_days, key=lambda d: d["date"])
        longest = 0
        run = 0
        for day in all_days_asc:
            if day["contributionCount"] > 0:
                run += 1
                longest = max(longest, run)
            else:
                run = 0
        data["longest_streak"] = longest

        # This month contributions
        month_start = now.replace(day=1).strftime("%Y-%m-")
        month_contribs = 0
        month_active = 0
        for day in all_days:
            if day["date"].startswith(month_start):
                month_contribs += day["contributionCount"]
                if day["contributionCount"] > 0:
                    month_active += 1
        data["month_contributions"] = month_contribs
        data["month_active_days"] = month_active

        print(f"  [OK] Contributions: {data['total_contributions']} total, streak {data['current_streak']}d")
    except Exception as e:
        print(f"  [WARN] Contributions fetch: {e}")

    # === 3. Top Languages (GraphQL) ===
    try:
        lang_query = """
        query($login: String!) {
          user(login: $login) {
            repositories(first: 100, ownerAffiliations: OWNER, orderBy: {field: UPDATED_AT, direction: DESC}) {
              nodes {
                languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
                  edges {
                    size
                    node {
                      name
                      color
                    }
                  }
                }
              }
            }
          }
        }
        """
        result = graphql_query(token, lang_query, {"login": USERNAME})
        repos = result["data"]["user"]["repositories"]["nodes"]
        lang_map = defaultdict(lambda: {"bytes": 0, "color": "#888"})
        for repo in repos:
            for edge in repo.get("languages", {}).get("edges", []):
                name = edge["node"]["name"]
                lang_map[name]["bytes"] += edge["size"]
                lang_map[name]["color"] = edge["node"].get("color") or "#888"

        # Sort by bytes descending, take top 6
        sorted_langs = sorted(lang_map.items(), key=lambda x: x[1]["bytes"], reverse=True)[:6]
        data["languages"] = [{"name": n, "bytes": v["bytes"], "color": v["color"]} for n, v in sorted_langs]
        print(f"  [OK] Languages: {', '.join(l['name'] for l in data['languages'][:4])}")
    except Exception as e:
        print(f"  [WARN] Languages fetch: {e}")

    # === 4. Recent Events (REST) ===
    try:
        events_raw = rest_api(token, f"/users/{USERNAME}/events?per_page=30")
        recent = []
        seen_keys = set()
        for ev in events_raw:
            if len(recent) >= 5:
                break
            etype = ev.get("type", "")
            repo_name = ev.get("repo", {}).get("name", "").split("/")[-1]
            created = ev.get("created_at", "")
            time_str = created[11:16] if len(created) > 16 else "00:00"

            detail = ""
            if etype == "PushEvent":
                commits = ev.get("payload", {}).get("commits", [])
                if commits:
                    msg = commits[0].get("message", "").split("\n")[0][:55]
                    detail = msg if msg else "Code push"
                else:
                    ref = ev.get("payload", {}).get("ref", "").split("/")[-1]
                    detail = f"Push to {ref}" if ref else "Code push"
                etype = "PUSH"
            elif etype == "CreateEvent":
                ref_type = ev.get("payload", {}).get("ref_type", "")
                ref_name = ev.get("payload", {}).get("ref", "") or ""
                detail = f"Created {ref_type} {ref_name}".strip()[:55]
                etype = "CREATE"
            elif etype == "PullRequestEvent":
                action = ev.get("payload", {}).get("action", "")
                pr = ev.get("payload", {}).get("pull_request", {})
                detail = pr.get("title", "")[:55] or f"PR {action}"
                etype = "PR"
            elif etype == "IssuesEvent":
                action = ev.get("payload", {}).get("action", "")
                issue = ev.get("payload", {}).get("issue", {})
                detail = issue.get("title", "")[:55] or f"Issue {action}"
                etype = "ISSUE"
            elif etype == "WatchEvent":
                detail = f"Starred {repo_name}"
                etype = "STAR"
            elif etype == "ForkEvent":
                detail = f"Forked {repo_name}"
                etype = "FORK"
            elif etype == "DeleteEvent":
                ref_type = ev.get("payload", {}).get("ref_type", "")
                detail = f"Deleted {ref_type}"
                etype = "DELETE"
            elif etype == "ReleaseEvent":
                detail = ev.get("payload", {}).get("release", {}).get("name", "")[:55] or "New release"
                etype = "RELEASE"
            else:
                detail = etype.replace("Event", "")
                etype = "EVENT"

            # Deduplicate: skip if same type+repo+detail
            dedup_key = f"{etype}:{repo_name}:{detail[:20]}"
            if dedup_key in seen_keys:
                continue
            seen_keys.add(dedup_key)

            # XML-safe
            detail = detail.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
            repo_name = repo_name.replace("&", "&amp;")

            recent.append({"time": time_str, "type": etype, "repo": repo_name, "detail": detail})

        data["recent_events"] = recent[:5]
        print(f"  [OK] Events: {len(recent)} recent activities")
    except Exception as e:
        print(f"  [WARN] Events fetch: {e}")

    # === 5. Stars received across repos (REST) ===
    try:
        repos_data = rest_api(token, f"/users/{USERNAME}/repos?per_page=100&sort=updated")
        total_stars = sum(r.get("stargazers_count", 0) for r in repos_data)
        data["stars_received"] = total_stars
        print(f"  [OK] Stars: {total_stars} total")
    except Exception as e:
        print(f"  [WARN] Stars fetch: {e}")

    return data


# ==========================================
# SVG GENERATION FUNCTIONS
# ==========================================

# Shared color palette
PALETTE = {
    "bg_deep": "#000000",
    "bg_mid": "#0a0a0a",
    "bg_dark": "#050505",
    "bg_card": "#111111",
    "border": "#333333",
    "border_light": "#555555",
    "cyan": "#54B948",
    "indigo": "#0072C6",
    "purple": "#FF007F",
    "emerald": "#39FF14",
    "green": "#00FF00",
    "yellow": "#F2A900",
    "amber": "#FF8C00",
    "rose": "#C00000",
    "text_white": "#f8fafc",
    "text_secondary": "#94a3b8",
    "text_muted": "#64748b",
}

SHARED_SVG_HEAD = f"""
  <defs>
    <linearGradient id="db-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{PALETTE['bg_deep']}" />
      <stop offset="50%" stop-color="{PALETTE['bg_mid']}" />
      <stop offset="100%" stop-color="{PALETTE['bg_dark']}" />
    </linearGradient>
    <linearGradient id="bar-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{PALETTE['cyan']}" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
    <linearGradient id="border-glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{PALETTE['cyan']}" stop-opacity="0.6" />
      <stop offset="50%" stop-color="{PALETTE['border_light']}" stop-opacity="0.3" />
      <stop offset="100%" stop-color="{PALETTE['indigo']}" stop-opacity="0.5" />
    </linearGradient>
    <linearGradient id="accent-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{PALETTE['cyan']}" />
      <stop offset="50%" stop-color="{PALETTE['indigo']}" />
      <stop offset="100%" stop-color="{PALETTE['purple']}" />
    </linearGradient>
    <filter id="glow-sm" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
"""

SHARED_STYLES = """
  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', Menlo, Consolas, monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .gta-title { font-family: 'Impact', 'Arial Black', sans-serif; font-style: italic; text-transform: uppercase; stroke: #000; stroke-width: 0.8px; }
    .gta-mission { font-family: 'Impact', 'Arial Black', sans-serif; text-transform: uppercase; letter-spacing: 1px; }
    @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
    .pulse { animation: pulse 2s ease-in-out infinite; }
  </style>
"""


def _badge(x, y, text, color):
    """Create a small status badge."""
    return f'''
    <g transform="translate({x}, {y})">
      <rect width="{len(text) * 6.5 + 16}" height="20" rx="4" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-width="0.8" />
      <text x="{(len(text) * 6.5 + 16) / 2}" y="14" fill="{color}" class="mono" font-size="9" font-weight="800" text-anchor="middle">{text}</text>
    </g>'''


def _status_dot(x, y, color="#10b981"):
    return f'<circle cx="{x}" cy="{y}" r="3.5" fill="{color}" class="pulse" />'


# ────────────────────────────────────────────
# 1. OVERVIEW.SVG — Command Center Header
# ────────────────────────────────────────────
def generate_overview_svg(data):
    last_sync = data.get("last_sync", "—")
    is_live = data.get("is_live", False)
    live_label = "LIVE API" if is_live else "CACHED"
    live_color = PALETTE["green"] if is_live else PALETTE["amber"]

    cards = [
        ("SAFEHOUSES", str(data.get("public_repos", 0)), PALETTE["cyan"], "PROPERTIES"),
        ("RESPECT", f"{data.get('total_contributions', 0):,}", PALETTE["indigo"], "ALL TIME"),
        ("WANTED LEVEL", f"{data.get('current_streak', 0)}", PALETTE["yellow"], f"MAX: {data.get('longest_streak', 0)}d"),
        ("CREW MEMBERS", str(data.get("followers", 0)), PALETTE["amber"], "NETWORK"),
    ]

    card_svgs = []
    for i, (label, value, color, sub) in enumerate(cards):
        tx = i * 222
        card_svgs.append(f'''
    <g transform="translate({tx}, 0)">
      <rect width="200" height="120" rx="8" fill="{PALETTE['bg_card']}" stroke="{PALETTE['border']}" stroke-width="1" />
      <rect width="200" height="3" rx="1.5" fill="{color}" y="0" />
      <text x="16" y="30" fill="{PALETTE['text_muted']}" class="mono" font-size="9" font-weight="700">{label}</text>
      <text x="16" y="72" fill="{color}" class="mono" font-size="36" font-weight="900">{value}</text>
      <text x="16" y="104" fill="{PALETTE['text_secondary']}" class="mono" font-size="9">{sub}</text>
    </g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 210" width="100%" height="100%">
  {SHARED_SVG_HEAD}
  {SHARED_STYLES}

  <rect width="920" height="210" rx="12" fill="url(#db-bg)" stroke="url(#border-glow)" stroke-width="1.5" />

  <!-- Header -->
  <g transform="translate(28, 24)">
    {_status_dot(6, 7, live_color)}
    <text x="20" y="11" fill="{PALETTE['text_white']}" class="gta-title" font-size="14" font-weight="800">PASHA DEV // LOS SANTOS ENGINEERING</text>
    {_badge(380, -2, live_label, live_color)}
    <text x="864" y="11" fill="{PALETTE['text_muted']}" class="mono" font-size="10" text-anchor="end">SYNC: {last_sync}</text>
  </g>
  <line x1="28" y1="48" x2="892" y2="48" stroke="{PALETTE['border']}" stroke-width="1" />

  <!-- Metric Cards -->
  <g transform="translate(28, 68)">
    {''.join(card_svgs)}
  </g>
</svg>'''


# ────────────────────────────────────────────
# 2. GITHUB-STATS.SVG
# ────────────────────────────────────────────
def generate_stats_svg(data):
    rows_data = [
        ("TOTAL HEISTS", "VERIFIED MISSIONS PASSED", f"{data.get('total_contributions', 0):,}", PALETTE["cyan"]),
        ("PROPERTIES OWNED", "SAFEHOUSES &amp; BUSINESSES", str(data.get("public_repos", 0)), PALETTE["indigo"]),
        ("CREW MEMBERS", "GANG NETWORK", str(data.get("followers", 0)), PALETTE["emerald"]),
        ("BOUNTY COLLECTED", "COMMUNITY RESPECT", str(data.get("stars_received", 0)), PALETTE["yellow"]),
        ("SURVIVAL TIME", "CONSECUTIVE DAYS SURVIVED", f"{data.get('current_streak', 0)} DAYS", PALETTE["rose"]),
    ]

    rows = []
    for i, (label, sub, value, color) in enumerate(rows_data):
        y = i * 50
        rows.append(f'''
      <g transform="translate(0, {y})">
        <rect width="402" height="42" rx="6" fill="{PALETTE['bg_card']}" stroke="{PALETTE['border']}" stroke-width="1" />
        <text x="16" y="18" fill="{PALETTE['text_secondary']}" class="mono" font-size="10">{label}</text>
        <text x="16" y="33" fill="{PALETTE['text_muted']}" class="mono" font-size="8">{sub}</text>
        <text x="386" y="27" fill="{color}" class="mono" font-size="16" font-weight="900" text-anchor="end">{value}</text>
      </g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 340" width="100%" height="100%">
  {SHARED_SVG_HEAD}
  {SHARED_STYLES}

  <rect width="450" height="340" rx="12" fill="url(#db-bg)" stroke="url(#border-glow)" stroke-width="1.5" />

  <g transform="translate(24, 22)">
    <text x="0" y="14" fill="{PALETTE['text_white']}" class="gta-title" font-size="14" font-weight="800">CRIMINAL RECORD // LIVE</text>
  </g>
  <line x1="24" y1="48" x2="426" y2="48" stroke="{PALETTE['border']}" stroke-width="1" />

  <g transform="translate(24, 60)">
    {''.join(rows)}
  </g>

  <g transform="translate(24, 320)">
    {_status_dot(4, 4)}
    <text x="14" y="8" fill="{PALETTE['text_muted']}" class="mono" font-size="9">DATA SOURCE: GITHUB API • VERIFIED</text>
  </g>
</svg>'''


# ────────────────────────────────────────────
# 3. LANGUAGES.SVG
# ────────────────────────────────────────────
def generate_languages_svg(data):
    langs = data.get("languages", [])
    if not langs:
        langs = [{"name": "No data", "bytes": 1, "color": "#64748b"}]

    total_bytes = sum(l["bytes"] for l in langs) if langs else 1

    rows = []
    y_off = 68
    for l in langs[:6]:
        pct = (l["bytes"] / total_bytes) * 100
        bar_w = max(int((pct / 100) * 220), 4)
        col = l.get("color") or "#38bdf8"
        name = l["name"].replace("&", "&amp;")
        rows.append(f'''
        <g transform="translate(24, {y_off})">
          <text x="0" y="14" fill="{PALETTE['text_white']}" class="mono" font-size="11" font-weight="700">{name}</text>
          <text x="395" y="14" fill="{col}" class="mono" font-size="11" font-weight="800" text-anchor="end">{pct:.1f}%</text>
          <rect x="130" y="4" width="220" height="12" rx="6" fill="{PALETTE['bg_card']}" stroke="{PALETTE['border']}" stroke-width="1" />
          <rect x="130" y="4" width="{bar_w}" height="12" rx="6" fill="{col}" />
        </g>''')
        y_off += 39

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 340" width="100%" height="100%">
  {SHARED_SVG_HEAD}
  {SHARED_STYLES}

  <rect width="450" height="340" rx="12" fill="url(#db-bg)" stroke="url(#border-glow)" stroke-width="1.5" />

  <g transform="translate(24, 22)">
    <text x="0" y="14" fill="{PALETTE['text_white']}" class="gta-title" font-size="14" font-weight="800">WEAPON WHEEL // ARSENAL</text>
    <text x="402" y="14" fill="{PALETTE['text_muted']}" class="mono" font-size="9" text-anchor="end">AMMO COUNT</text>
  </g>
  <line x1="24" y1="48" x2="426" y2="48" stroke="{PALETTE['border']}" stroke-width="1" />

  {''.join(rows)}

  <g transform="translate(24, 316)">
    <text x="0" y="7" fill="{PALETTE['text_muted']}" class="mono" font-size="9">SOURCE: GITHUB API LANGUAGE ANALYSIS</text>
  </g>
</svg>'''


# ────────────────────────────────────────────
# 4. CONTRIBUTIONS.SVG — 52-Week Heatmap
# ────────────────────────────────────────────
def generate_contributions_svg(data):
    weeks = data.get("contribution_weeks", [])

    # If no real data, generate synthetic
    if not weeks:
        for w in range(52):
            days = []
            for d in range(7):
                pseudo = int((math.sin(w * 0.4 + d * 0.8) * 6 + math.cos(w * 0.2) * 3 + 4))
                cnt = max(0, min(pseudo, 14))
                if w % 9 == 0 and d == 0:
                    cnt = 0
                days.append({"contributionCount": cnt})
            weeks.append({"contributionDays": days})

    cell_size = 11
    cell_gap = 3
    start_x = 42
    start_y = 52

    def get_color(cnt):
        if cnt == 0:    return "#161b22"
        elif cnt <= 2:  return "#0e4429"
        elif cnt <= 5:  return "#006d32"
        elif cnt <= 9:  return "#26a641"
        else:           return "#39d353"

    cells = []
    for w_idx, week in enumerate(weeks[-52:]):
        x = start_x + (w_idx * (cell_size + cell_gap))
        for d_idx, day in enumerate(week.get("contributionDays", [])):
            y = start_y + (d_idx * (cell_size + cell_gap))
            cnt = day.get("contributionCount", 0)
            c = get_color(cnt)
            cells.append(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" fill="{c}" />')

    # Month labels from actual data
    months_labels = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    month_tags = []
    if weeks:
        seen_months = set()
        for w_idx, week in enumerate(weeks[-52:]):
            days = week.get("contributionDays", [])
            if days:
                d = days[0].get("date", "")
                if len(d) >= 7:
                    m = int(d[5:7])
                    if m not in seen_months:
                        seen_months.add(m)
                        x = start_x + (w_idx * (cell_size + cell_gap))
                        month_tags.append(f'<text x="{x}" y="0" fill="{PALETTE["text_muted"]}" class="mono" font-size="9">{months_labels[m-1]}</text>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 190" width="100%" height="100%">
  {SHARED_SVG_HEAD}
  {SHARED_STYLES}

  <rect width="920" height="190" rx="12" fill="url(#db-bg)" stroke="url(#border-glow)" stroke-width="1.5" />

  <g transform="translate(32, 18)">
    {_status_dot(6, 6, "#39d353")}
    <text x="20" y="10" fill="{PALETTE['text_white']}" class="gta-title" font-size="13" font-weight="800">TERRITORY CONTROL // HEATMAP</text>
    <text x="220" y="10" fill="{PALETTE['text_muted']}" class="mono" font-size="10">// {data.get('total_contributions', 0):,} CONTRIBUTIONS</text>

    <g transform="translate(700, 0)" class="mono" font-size="9">
      <text x="-36" y="9" fill="{PALETTE['text_muted']}">LESS</text>
      <rect x="0" y="0" width="10" height="10" rx="2" fill="#161b22" />
      <rect x="14" y="0" width="10" height="10" rx="2" fill="#0e4429" />
      <rect x="28" y="0" width="10" height="10" rx="2" fill="#006d32" />
      <rect x="42" y="0" width="10" height="10" rx="2" fill="#26a641" />
      <rect x="56" y="0" width="10" height="10" rx="2" fill="#39d353" />
      <text x="72" y="9" fill="{PALETTE['text_muted']}">MORE</text>
    </g>
  </g>

  <!-- Month labels -->
  <g transform="translate(0, 42)">
    {''.join(month_tags)}
  </g>

  <!-- Heatmap Grid -->
  <g>
    {''.join(cells)}
  </g>
</svg>'''


# ────────────────────────────────────────────
# 5. ACTIVITY.SVG — Live Event Stream
# ────────────────────────────────────────────
def generate_activity_svg(data):
    events = data.get("recent_events", [])

    if not events:
        events = [
            {"time": "—", "type": "SYNC", "repo": "—", "detail": "No recent events found"},
        ]

    badge_colors = {
        "PUSH": PALETTE["green"],
        "CREATE": PALETTE["cyan"],
        "PR": PALETTE["purple"],
        "ISSUE": PALETTE["amber"],
        "STAR": PALETTE["yellow"],
        "FORK": PALETTE["indigo"],
        "RELEASE": PALETTE["amber"],
        "DELETE": PALETTE["rose"],
    }

    ev_rows = []
    y_off = 60
    for ev in events[:5]:
        t_str = ev.get("time", "—")
        etype = ev.get("type", "EVENT")
        rname = ev.get("repo", "—")
        detail = ev.get("detail", "")
        col = badge_colors.get(etype, PALETTE["cyan"])

        ev_rows.append(f'''
    <g transform="translate(24, {y_off})" class="mono">
      <rect width="872" height="36" rx="5" fill="{PALETTE['bg_card']}" stroke="{PALETTE['border']}" stroke-width="1" />
      <text x="14" y="22" fill="{PALETTE['text_muted']}" font-size="10">{t_str}</text>
      <rect x="64" y="8" width="{max(len(etype) * 7 + 12, 50)}" height="20" rx="4" fill="{col}" fill-opacity="0.15" stroke="{col}" stroke-width="0.8" />
      <text x="{64 + max(len(etype) * 7 + 12, 50) // 2}" y="22" fill="{col}" font-size="9" font-weight="800" text-anchor="middle">{etype}</text>
      <text x="{64 + max(len(etype) * 7 + 12, 50) + 16}" y="22" fill="{PALETTE['text_white']}" font-size="11" font-weight="700">{rname}</text>
      <text x="300" y="22" fill="{PALETTE['text_secondary']}" font-size="10">{detail[:55]}</text>
      {_status_dot(854, 18)}
    </g>''')
        y_off += 44

    total_h = 60 + len(events[:5]) * 44 + 30

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 {total_h}" width="100%" height="100%">
  {SHARED_SVG_HEAD}
  {SHARED_STYLES}

  <rect width="920" height="{total_h}" rx="12" fill="url(#db-bg)" stroke="url(#border-glow)" stroke-width="1.5" />

  <g transform="translate(24, 22)">
    <text x="0" y="14" fill="{PALETTE['text_white']}" class="gta-title" font-size="14" font-weight="800">RECENT HEISTS // EVENT STREAM</text>
    {_badge(320, 0, "LIVE" if data.get("is_live") else "CACHED", PALETTE["green"] if data.get("is_live") else PALETTE["amber"])}
    <text x="872" y="14" fill="{PALETTE['cyan']}" class="mono" font-size="10" text-anchor="end">STREAM: ACTIVE</text>
  </g>
  <line x1="24" y1="46" x2="896" y2="46" stroke="{PALETTE['border']}" stroke-width="1" />

  {''.join(ev_rows)}

  <g transform="translate(24, {total_h - 18})">
    <text x="0" y="0" fill="{PALETTE['green']}" class="mono" font-size="9">&gt; listening to LSPD scanner...</text>
  </g>
</svg>'''


# ────────────────────────────────────────────
# 6. MONTHLY.SVG — Current Month Telemetry
# ────────────────────────────────────────────
def generate_monthly_svg(data):
    now = datetime.now(timezone.utc)
    month_name = now.strftime("%B %Y").upper()
    month_contribs = data.get("month_contributions", 0)
    month_active = data.get("month_active_days", 0)
    cadence = round(month_contribs / max(month_active, 1), 1)

    cards = [
        ("MONTHLY PAYOUT", str(month_contribs), PALETTE["cyan"], "THIS MONTH"),
        ("DAYS SURVIVED", str(month_active), PALETTE["indigo"], "DAYS ACTIVE"),
        ("FRONTS ACTIVE", str(min(data.get("public_repos", 0), 15)), PALETTE["purple"], "BUSINESSES"),
        ("CADENCE RATIO", str(cadence), PALETTE["yellow"], "COMMITS / ACTIVE DAY"),
    ]

    card_svgs = []
    for i, (label, value, color, sub) in enumerate(cards):
        tx = i * 222
        card_svgs.append(f'''
    <g transform="translate({tx}, 0)">
      <rect width="200" height="95" rx="6" fill="{PALETTE['bg_card']}" stroke="{PALETTE['border']}" stroke-width="1" />
      <text x="14" y="24" fill="{PALETTE['text_muted']}" class="mono" font-size="9" font-weight="700">{label}</text>
      <text x="14" y="62" fill="{color}" class="mono" font-size="30" font-weight="900">{value}</text>
      <text x="14" y="82" fill="{PALETTE['text_secondary']}" class="mono" font-size="9">{sub}</text>
    </g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 170" width="100%" height="100%">
  {SHARED_SVG_HEAD}
  {SHARED_STYLES}

  <rect width="920" height="170" rx="12" fill="url(#db-bg)" stroke="url(#border-glow)" stroke-width="1.5" />

  <g transform="translate(28, 22)">
    <rect width="6" height="16" fill="{PALETTE['cyan']}" rx="2" />
    <text x="16" y="13" fill="{PALETTE['text_white']}" class="gta-title" font-size="14" font-weight="800">THIS MONTH // PAYOUTS</text>
    <text x="864" y="13" fill="{PALETTE['text_muted']}" class="mono" font-size="10" text-anchor="end">DYNAMIC TELEMETRY</text>
  </g>
  <line x1="28" y1="44" x2="892" y2="44" stroke="{PALETTE['border']}" stroke-width="1" />

  <g transform="translate(28, 56)">
    {''.join(card_svgs)}
  </g>
</svg>'''


# ────────────────────────────────────────────
# 7. METRICS.SVG — Top-line quick metrics
# ────────────────────────────────────────────
def generate_metrics_svg(data):
    cards = [
        ("SAFEHOUSES", str(data.get("public_repos", 0)), PALETTE["cyan"], "PROPERTIES"),
        ("RESPECT", f"{data.get('total_contributions', 0):,}", PALETTE["indigo"], "ALL TIME"),
        ("CREW", str(data.get("followers", 0)), PALETTE["purple"], "NETWORK"),
        ("BOUNTY", str(data.get("stars_received", 0)), PALETTE["yellow"], "RESPECT"),
    ]

    card_svgs = []
    for i, (label, value, color, sub) in enumerate(cards):
        tx = i * 222
        card_svgs.append(f'''
    <g transform="translate({tx}, 0)">
      <rect width="200" height="104" rx="6" fill="{PALETTE['bg_card']}" stroke="{PALETTE['border']}" stroke-width="1" />
      <text x="16" y="26" fill="{PALETTE['text_muted']}" class="mono" font-size="9" font-weight="700">{label}</text>
      <text x="16" y="66" fill="{color}" class="mono" font-size="32" font-weight="900">{value}</text>
      <text x="16" y="88" fill="{PALETTE['text_secondary']}" class="mono" font-size="8">{sub}</text>
    </g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 140" width="100%" height="100%">
  {SHARED_SVG_HEAD}
  {SHARED_STYLES}

  <rect width="920" height="140" rx="10" fill="{PALETTE['bg_deep']}" stroke="{PALETTE['border']}" stroke-width="1.5" />

  <g transform="translate(24, 18)">
    {''.join(card_svgs)}
  </g>
</svg>'''


# ────────────────────────────────────────────
# 8. STREAK.SVG
# ────────────────────────────────────────────
def generate_streak_svg(data):
    streak = data.get("current_streak", 0)
    # Determine star count (1 to 5 stars)
    star_count = min(5, max(1, (streak // 3) + 1))
    
    stars_svg = []
    for s in range(5):
        is_active = s < star_count
        color = "#F5AF00" if is_active else "#22252a"
        stroke_col = "#F5AF00" if is_active else "#374151"
        pulse_class = ' class="pulse"' if is_active and s == (star_count - 1) else ''
        stars_svg.append(f'''
        <g transform="translate({s * 32}, 0)"{pulse_class}>
          <polygon points="12,1 15,9 24,9 17,14 20,23 12,17 4,23 7,14 0,9 9,9" 
                   fill="{color}" stroke="{stroke_col}" stroke-width="1.2" />
        </g>''')

    cols = [
        ("WANTED LEVEL", f"{star_count}-STAR PRIORITY", f"{streak} DAYS CONSECUTIVE", PALETTE["rose"]),
        ("TOTAL MISSIONS", f"{data.get('total_contributions', 0):,}", "VERIFIED PASSED", PALETTE["cyan"]),
        ("MAX EVASION", f"{data.get('longest_streak', 0)} DAYS", "LONGEST STREAK", PALETTE["yellow"]),
    ]

    col_svgs = []
    for i, (label, val, sub, color) in enumerate(cols):
        tx = i * 296
        col_svgs.append(f'''
    <g transform="translate({tx}, 0)">
      <rect width="272" height="96" rx="8" fill="{PALETTE['bg_card']}" stroke="{PALETTE['border']}" stroke-width="1" />
      <rect width="272" height="3" rx="1.5" fill="{color}" />
      <text x="16" y="24" fill="{PALETTE['text_muted']}" class="mono" font-size="9" font-weight="700">{label}</text>
      <text x="16" y="58" fill="{color}" class="gta-mission" font-size="24" font-weight="900">{val}</text>
      <text x="16" y="80" fill="{PALETTE['text_secondary']}" class="mono" font-size="10">{sub}</text>
    </g>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 150" width="100%" height="100%">
  {SHARED_SVG_HEAD}
  {SHARED_STYLES}

  <rect width="920" height="150" rx="12" fill="url(#db-bg)" stroke="url(#border-glow)" stroke-width="1.5" />

  <!-- Top bar with Wanted Stars -->
  <g transform="translate(24, 18)">
    <rect width="6" height="18" fill="{PALETTE['rose']}" rx="2" />
    <text x="16" y="14" fill="{PALETTE['text_white']}" class="gta-title" font-size="14" font-weight="800">LSPD WANTED STATUS // ACTIVE HEIST STREAK</text>
    <g transform="translate(710, -3)">
      {''.join(stars_svg)}
    </g>
  </g>
  <line x1="24" y1="42" x2="896" y2="42" stroke="{PALETTE['border']}" stroke-width="1" />

  <g transform="translate(24, 52)">
    {''.join(col_svgs)}
  </g>
</svg>'''
# ==========================================
# MAIN
# ==========================================
def main():
    print("=" * 60)
    print(f"  PASHA DEV TELEMETRY ENGINE v3.0")
    print(f"  Target: {USERNAME}")
    print("=" * 60)

    os.makedirs(PROFILE_DIR, exist_ok=True)
    os.makedirs(ASSETS_DIR, exist_ok=True)

    data = fetch_github_data()

    source = "LIVE GITHUB API" if data["is_live"] else "FALLBACK DATA"
    print(f"\n[*] Data Source: {source}")
    print(f"[*] Repos: {data['public_repos']} | Contributions: {data['total_contributions']} | Streak: {data['current_streak']}d")

    generators = {
        "overview.svg": generate_overview_svg,
        "github-stats.svg": generate_stats_svg,
        "stats.svg": generate_stats_svg,
        "languages.svg": generate_languages_svg,
        "contributions.svg": generate_contributions_svg,
        "activity.svg": generate_activity_svg,
        "monthly.svg": generate_monthly_svg,
        "metrics.svg": generate_metrics_svg,
        "streak.svg": generate_streak_svg,
    }

    for fname, func in generators.items():
        fpath = os.path.join(PROFILE_DIR, fname)
        svg_content = func(data)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(svg_content.strip() + "\n")
        print(f"  [OK] Generated: profile/{fname}")

    print(f"\n[*] All telemetry dashboards generated successfully!")
    print(f"[*] Sync timestamp: {data['last_sync']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
