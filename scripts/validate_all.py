import os
import re
import xml.etree.ElementTree as ET

workspace = r"d:\Project in Github\pasha804"
readme_path = os.path.join(workspace, "README.md")

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all local asset references
local_refs = re.findall(r'(?:src|href)=["\'](\./(?:assets|profile)/[^"\']+)["\']', content)
print(f"Total local references in README: {len(local_refs)}")

missing = 0
for ref in local_refs:
    clean_path = ref.replace("./", "")
    full_path = os.path.join(workspace, clean_path.replace("/", os.sep))
    if os.path.exists(full_path):
        size = os.path.getsize(full_path)
        print(f"  [OK] {ref} -> {size:,} bytes")
    else:
        print(f"  [MISSING] {ref}")
        missing += 1

print(f"\nMissing files: {missing}")

# Check all SVGs for XML validity
svg_errors = 0
for folder in ["assets", "profile"]:
    folder_path = os.path.join(workspace, folder)
    if not os.path.exists(folder_path):
        continue
    for f in os.listdir(folder_path):
        if f.endswith(".svg"):
            full_path = os.path.join(folder_path, f)
            try:
                ET.parse(full_path)
                print(f"  [VALID XML] {folder}/{f}")
            except Exception as e:
                print(f"  [INVALID XML] {folder}/{f}: {e}")
                svg_errors += 1

print(f"\nTotal SVG XML errors: {svg_errors}")
if missing == 0 and svg_errors == 0:
    print("\n>>> ALL CHECKS PASSED PERFECTLY! <<<")
