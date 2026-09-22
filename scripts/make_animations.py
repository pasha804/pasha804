import os
import shutil
import math
from PIL import Image, ImageDraw

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(WORKSPACE_DIR, "assets")
BRAIN_DIR = r"C:\Users\USER\.gemini\antigravity-ide\brain\2af3d674-43e2-42eb-9a37-01a4c15ac2bf"

source_images = {
    "hero": os.path.join(BRAIN_DIR, "pasha_hero_banner_1790093459826.jpg"),
    "nexora": os.path.join(BRAIN_DIR, "nexora_platform_1790093485398.jpg"),
    "zoro": os.path.join(BRAIN_DIR, "zoro_windows_ai_1790093515970.jpg"),
    "pasha-tools": os.path.join(BRAIN_DIR, "pasha_tools_3d_1790093552208.jpg"),
    "wishora": os.path.join(BRAIN_DIR, "wishora_platform_3d_1790093596211.jpg"),
}

# 1. Copy still 4K renders into assets
for key, src in source_images.items():
    dst = os.path.join(ASSETS_DIR, f"{key}-3d.jpg")
    shutil.copy2(src, dst)
    print(f"[OK] Copied {key}-3d.jpg to assets")


# 2. 3D Rotating Polyhedron Hologram (75 KB)
def generate_3d_polyhedron_gif(out_path, num_frames=24, size=220):
    frames = []
    vertices = [
        (0, 1.2, 0), (0, -1.2, 0),
        (1.0, 0, 0), (-1.0, 0, 0),
        (0, 0, 1.0), (0, 0, -1.0)
    ]
    edges = [
        (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 4), (4, 3), (3, 5), (5, 2)
    ]
    c = 0.5
    cube_verts = [(x, y, z) for x in (-c, c) for y in (-c, c) for z in (-c, c)]
    cube_edges = [
        (0,1), (1,3), (3,2), (2,0),
        (4,5), (5,7), (7,6), (6,4),
        (0,4), (1,5), (2,6), (3,7)
    ]

    for frame_idx in range(num_frames):
        angle = (2 * math.pi * frame_idx) / num_frames
        angle_y = angle
        angle_x = math.sin(angle) * 0.4 + 0.3

        im = Image.new("RGBA", (size, size), (5, 8, 17, 255))
        draw = ImageDraw.Draw(im)
        center = size // 2
        for r, col in [(size//2 - 10, (30, 50, 80, 120)), (size//2 - 30, (56, 189, 248, 60))]:
            draw.ellipse([center - r, center - r, center + r, center + r], outline=col, width=1)

        def project(v, scale):
            x, y, z = v
            x1 = x * math.cos(angle_y) + z * math.sin(angle_y)
            y1 = y
            z1 = -x * math.sin(angle_y) + z * math.cos(angle_y)
            x2 = x1
            y2 = y1 * math.cos(angle_x) - z1 * math.sin(angle_x)
            z2 = y1 * math.sin(angle_x) + z1 * math.cos(angle_x)
            fov = 3.5
            dist = fov / (fov + z2)
            px = center + int(x2 * scale * dist)
            py = center - int(y2 * scale * dist)
            return (px, py), z2

        proj_oct = [project(v, 65) for v in vertices]
        for p1_idx, p2_idx in edges:
            (p1, z1), (p2, z2) = proj_oct[p1_idx], proj_oct[p2_idx]
            depth_alpha = int(140 + 115 * ((z1 + z2) / 4))
            draw.line([p1, p2], fill=(56, 189, 248, depth_alpha), width=2)

        for (px, py), z in proj_oct:
            draw.ellipse([px-3, py-3, px+3, py+3], fill=(192, 132, 252, 240), outline=(255, 255, 255, 255))

        proj_cube = [project(v, 65) for v in cube_verts]
        for p1_idx, p2_idx in cube_edges:
            (p1, z1), (p2, z2) = proj_cube[p1_idx], proj_cube[p2_idx]
            draw.line([p1, p2], fill=(129, 140, 248, 200), width=1)

        core_r = int(6 + 2 * math.sin(angle * 2))
        draw.ellipse([center - core_r, center - core_r, center + core_r, center + core_r], fill=(255, 255, 255, 220))

        frames.append(im.convert("P", palette=Image.Palette.ADAPTIVE, colors=64))

    frames[0].save(out_path, save_all=True, append_images=frames[1:], optimize=True, duration=50, loop=0)
    print(f"[OK] Saved {out_path}")


# 3. Optimized Hero 3D Motion Banner
def generate_hero_motion_gif(base_img_path, out_path, num_frames=16):
    base = Image.open(base_img_path).convert("RGB")
    target_w, target_h = 800, 446
    base = base.resize((target_w, target_h), Image.Resampling.LANCZOS)
    w, h = base.size
    frames = []

    for f in range(num_frames):
        t = f / num_frames
        frame = base.copy()
        draw = ImageDraw.Draw(frame, "RGBA")

        # Holographic scanline
        scan_y = int(t * h)
        draw.line([(0, scan_y), (w, scan_y)], fill=(56, 189, 248, 160), width=2)
        draw.rectangle([(0, scan_y - 4), (w, scan_y + 4)], fill=(56, 189, 248, 40))

        # Center pulse on "PASHA DEV"
        pulse_alpha = int(70 + 50 * math.sin(t * 2 * math.pi))
        cx, cy = int(w * 0.51), int(h * 0.44)
        r = int(45 + 12 * math.sin(t * 2 * math.pi))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(56, 189, 248, pulse_alpha // 3))

        # Floating ambient sparkles
        for i in range(8):
            seed = i * 41
            px = int((seed * 37 + f * 6) % w)
            py = int((seed * 23 + math.sin(t * 2 * math.pi + i) * 12 + seed) % h)
            draw.ellipse([px, py, px + 3, py + 3], fill=(192, 132, 252, 180))

        frames.append(frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=96))

    frames[0].save(out_path, save_all=True, append_images=frames[1:], optimize=True, duration=70, loop=0)
    print(f"[OK] Saved {out_path}")


# 4. Optimized Zoro 3D Motion Banner
def generate_zoro_motion_gif(base_img_path, out_path, num_frames=16):
    base = Image.open(base_img_path).convert("RGB")
    target_w, target_h = 800, 446
    base = base.resize((target_w, target_h), Image.Resampling.LANCZOS)
    w, h = base.size
    frames = []

    wave_x1, wave_y1 = int(w * 0.35), int(h * 0.32)
    wave_x2, wave_y2 = int(w * 0.65), int(h * 0.54)
    wave_mid_y = (wave_y1 + wave_y2) // 2

    for f in range(num_frames):
        t = f / num_frames
        frame = base.copy()
        draw = ImageDraw.Draw(frame, "RGBA")

        # Neural brain pulse
        brain_cx, brain_cy = int(w * 0.78), int(h * 0.42)
        b_pulse = int(50 + 35 * math.sin(t * 2 * math.pi))
        draw.ellipse([brain_cx - 40, brain_cy - 30, brain_cx + 40, brain_cy + 30], fill=(56, 189, 248, b_pulse // 2))

        # Real-time audio waveform animation
        num_bars = 24
        bar_step = (wave_x2 - wave_x1) // num_bars
        for i in range(num_bars):
            bx = wave_x1 + i * bar_step
            freq = math.sin(t * 2 * math.pi + i * 0.7) * math.cos(t * math.pi + i * 0.4)
            bar_h = int(abs(freq) * 32 + 5)
            draw.line([(bx, wave_mid_y - bar_h), (bx, wave_mid_y + bar_h)], fill=(56, 189, 248, 210), width=3)
            draw.ellipse([bx - 2, wave_mid_y - bar_h - 2, bx + 2, wave_mid_y - bar_h + 2], fill=(255, 255, 255, 240))

        frames.append(frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=96))

    frames[0].save(out_path, save_all=True, append_images=frames[1:], optimize=True, duration=60, loop=0)
    print(f"[OK] Saved {out_path}")


# 5. Optimized Nexora 3D Motion Banner
def generate_nexora_motion_gif(base_img_path, out_path, num_frames=16):
    base = Image.open(base_img_path).convert("RGB")
    target_w, target_h = 800, 446
    base = base.resize((target_w, target_h), Image.Resampling.LANCZOS)
    w, h = base.size
    frames = []

    hub_x, hub_y = int(w * 0.50), int(h * 0.44)

    for f in range(num_frames):
        t = f / num_frames
        frame = base.copy()
        draw = ImageDraw.Draw(frame, "RGBA")

        # Pulsing center arena ring
        ring_r = int(36 + 8 * math.sin(t * 2 * math.pi))
        ring_alpha = int(90 + 50 * math.cos(t * 2 * math.pi))
        draw.ellipse([hub_x - ring_r, hub_y - ring_r, hub_x + ring_r, hub_y + ring_r], outline=(56, 189, 248, ring_alpha), width=3)

        # Left energy burst
        left_t = (t) % 1.0
        left_px = int(hub_x - left_t * (hub_x - w * 0.22))
        left_py = int(hub_y + left_t * (h * 0.56 - hub_y))
        draw.ellipse([left_px - 5, left_py - 5, left_px + 5, left_py + 5], fill=(56, 189, 248, 240))

        # Right energy burst
        right_t = (t + 0.5) % 1.0
        right_px = int(hub_x + right_t * (w * 0.78 - hub_x))
        right_py = int(hub_y + right_t * (h * 0.56 - hub_y))
        draw.ellipse([right_px - 5, right_py - 5, right_px + 5, right_py + 5], fill=(192, 132, 252, 240))

        frames.append(frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=96))

    frames[0].save(out_path, save_all=True, append_images=frames[1:], optimize=True, duration=60, loop=0)
    print(f"[OK] Saved {out_path}")


# 6. Pasha Tools 3D Motion Banner
def generate_pasha_tools_motion_gif(base_img_path, out_path, num_frames=16):
    base = Image.open(base_img_path).convert("RGB")
    target_w, target_h = 800, 446
    base = base.resize((target_w, target_h), Image.Resampling.LANCZOS)
    w, h = base.size
    frames = []

    center_x, center_y = int(w * 0.50), int(h * 0.52)

    for f in range(num_frames):
        t = f / num_frames
        frame = base.copy()
        draw = ImageDraw.Draw(frame, "RGBA")

        # Rotating energy pulse around central core
        r = int(32 + 6 * math.sin(t * 2 * math.pi))
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], outline=(56, 189, 248, 140), width=2)

        # Data packets flowing to modules
        packet_x = int(center_x - (t % 1.0) * (center_x - w * 0.25))
        draw.ellipse([packet_x - 4, center_y - 4, packet_x + 4, center_y + 4], fill=(56, 189, 248, 230))

        packet_x2 = int(center_x + (t % 1.0) * (w * 0.75 - center_x))
        draw.ellipse([packet_x2 - 4, center_y - 4, packet_x2 + 4, center_y + 4], fill=(56, 189, 248, 230))

        frames.append(frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=96))

    frames[0].save(out_path, save_all=True, append_images=frames[1:], optimize=True, duration=60, loop=0)
    print(f"[OK] Saved {out_path}")


# 7. Wishora 3D Motion Banner
def generate_wishora_motion_gif(base_img_path, out_path, num_frames=16):
    base = Image.open(base_img_path).convert("RGB")
    target_w, target_h = 800, 446
    base = base.resize((target_w, target_h), Image.Resampling.LANCZOS)
    w, h = base.size
    frames = []

    for f in range(num_frames):
        t = f / num_frames
        frame = base.copy()
        draw = ImageDraw.Draw(frame, "RGBA")

        # Shimmering golden ribbon wave
        for i in range(12):
            seed = i * 29
            px = int((seed * 31 + f * 8) % w)
            py = int(h * 0.35 + math.sin(t * 2 * math.pi + i) * 20)
            star_r = int(3 + 2 * math.sin(t * 4 * math.pi + i))
            draw.ellipse([px - star_r, py - star_r, px + star_r, py + star_r], fill=(254, 240, 138, 220))

        frames.append(frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=96))

    frames[0].save(out_path, save_all=True, append_images=frames[1:], optimize=True, duration=60, loop=0)
    print(f"[OK] Saved {out_path}")


def main():
    generate_3d_polyhedron_gif(os.path.join(ASSETS_DIR, "hologram-cube.gif"))
    generate_hero_motion_gif(source_images["hero"], os.path.join(ASSETS_DIR, "hero-3d-motion.gif"))
    generate_zoro_motion_gif(source_images["zoro"], os.path.join(ASSETS_DIR, "zoro-3d-motion.gif"))
    generate_nexora_motion_gif(source_images["nexora"], os.path.join(ASSETS_DIR, "nexora-3d-motion.gif"))
    generate_pasha_tools_motion_gif(source_images["pasha-tools"], os.path.join(ASSETS_DIR, "pasha-tools-3d-motion.gif"))
    generate_wishora_motion_gif(source_images["wishora"], os.path.join(ASSETS_DIR, "wishora-3d-motion.gif"))
    print("[*] All optimized 3D animations and motion graphics created successfully!")


if __name__ == "__main__":
    main()
