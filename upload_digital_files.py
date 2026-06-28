#!/usr/bin/env python3
"""
upload_digital_files.py
Attaches the digital download file to each of the 15 divine listings.
Run with the same env vars as create_divine_listings.py.
"""

import os, time, requests
from pathlib import Path

ETSY_API_KEY      = os.getenv("ETSY_API_KEY", "")
ETSY_ACCESS_TOKEN = os.getenv("ETSY_ACCESS_TOKEN", "")
SHOP_ID           = 45562671
IMAGES_DIR        = Path(__file__).parent / "divine_collection" / "jpeg_export"
BASE_URL          = "https://openapi.etsy.com/v3/application"

HEADERS = {
    "x-api-key":     ETSY_API_KEY,
    "Authorization": f"Bearer {ETSY_ACCESS_TOKEN}",
}

# All 15 listings created (IDs from terminal output + JSON)
LISTINGS = [
    (4529197197, "1_Majestic Angel Wings with Golden Mandala.jpg"),
    (4529197223, "2_Radiant Angel Wings and Sacred Geometry.jpg"),
    (4529197231, "3_Warrior Archangel Michael in Gleaming Armor.jpg"),
    (4529197257, "4_Untitled design.jpg"),
    (4529197277, "5_Majestic Baroque Angel Art Print.jpg"),
    (4529210110, "7_Elegant Baroque Angel Wall Art.jpg"),
    (4529210134, "8_Ethereal Angel with Graceful Typography.jpg"),
    (4529197359, "9_Luxurious Baroque Angel Poster.jpg"),
    (4529210176, "10_Warrior Archangel Michael with Shield and Sword.jpg"),
    (4529200425, "11_Dynamic Angel Poster with Ascendant Typography.jpg"),
    (4529213328, "12_Poster - Experience the divine protection and guidance of your guardian angel today..jpg"),
    (4529213344, "14_Soaring Angel Wings with Ethereal Glow.jpg"),
    (4529200475, "15_Serene Angel Poster with Typography.jpg"),
    (4529213370, "17_Dark Armored Archangel with Ethereal Flames.jpg"),
    (4529213398, "18_Bold Angel Wings Graphic with 'RISE'.jpg"),
]

def safe_filename(name):
    import re
    stem, ext = name.rsplit(".", 1)
    safe = re.sub(r"[^a-zA-Z0-9._-]", "_", stem)
    # Truncate so total length (stem + dot + ext) stays ≤ 70
    max_stem = 70 - len(ext) - 1
    return f"{safe[:max_stem]}.{ext}"

def upload_file(listing_id, image_path):
    url = f"{BASE_URL}/shops/{SHOP_ID}/listings/{listing_id}/files"
    fname = safe_filename(image_path.name)
    with open(image_path, "rb") as f:
        r = requests.post(
            url,
            headers=HEADERS,
            files={"file": (fname, f, "image/jpeg")},
            data={"name": fname, "rank": 1},
        )
    if not r.ok:
        print(f"  ❌ HTTP {r.status_code}: {r.text}")
        r.raise_for_status()
    return r.json()

def main():
    if not ETSY_API_KEY:
        print("❌ Set ETSY_API_KEY and ETSY_ACCESS_TOKEN env vars first.")
        return

    for i, (listing_id, filename) in enumerate(LISTINGS[10:], 11):  # resume from #11
        image_path = IMAGES_DIR / filename
        if not image_path.exists():
            print(f"[{i}/15] ⚠️  File not found: {filename} — skipping")
            continue

        print(f"[{i}/15] Uploading digital file to listing {listing_id}...")
        result = upload_file(listing_id, image_path)
        print(f"  ✅ Done — file ID: {result.get('listing_file_id', result)}")
        time.sleep(0.5)

    print("\n✅ All digital files uploaded!")
    print("🔗 Go publish: https://www.etsy.com/your/shops/J2DAO/tools/listings?state=draft")

if __name__ == "__main__":
    main()
