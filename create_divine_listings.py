#!/usr/bin/env python3
"""
create_divine_listings.py
Creates the 13 missing Divine Collection listings on Etsy via API v3.

SETUP:
  1. Go to https://www.etsy.com/developers/your-apps
  2. Open your J2DAO app → copy your API key (keystring)
  3. Generate a fresh OAuth token (or use the one from .env)
  4. Fill in ETSY_API_KEY and ETSY_ACCESS_TOKEN below (or export as env vars)
  5. Run: python3 create_divine_listings.py
"""

import os, json, time, requests
from pathlib import Path

# ── CREDENTIALS ────────────────────────────────────────────────────────────────
ETSY_API_KEY    = os.getenv("ETSY_API_KEY",    "YOUR_API_KEY_HERE")
ETSY_ACCESS_TOKEN = os.getenv("ETSY_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN_HERE")
SHOP_ID         = 45562671        # J2DAO shop ID (confirmed from Etsy page)
IMAGES_DIR      = Path(__file__).parent / "divine_collection" / "jpeg_export"
# ── ────────────────────────────────────────────────────────────────────────────

BASE_URL = "https://openapi.etsy.com/v3/application"
HEADERS  = {
    "x-api-key":     ETSY_API_KEY,
    "Authorization": f"Bearer {ETSY_ACCESS_TOKEN}",
    "Content-Type":  "application/json",
}

# ── LISTING DEFINITIONS ────────────────────────────────────────────────────────
# These are the 13 MISSING designs (the 5 already listed on Etsy are skipped).
# Each entry: image filename → listing metadata.

LISTINGS = [
    {
        "image": "1_Majestic Angel Wings with Golden Mandala.jpg",
        "title": "Angel Wings Print | Majestic Golden Mandala Wall Art | Spiritual Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "Majestic angel wings intertwined with a radiant golden mandala. "
            "Sacred geometry meets divine protection in this stunning wall art print. "
            "Perfect for meditation spaces, bedrooms, living rooms, and gallery walls.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Spiritual home decor · Gallery wall · Meditation room · Gift for her · Housewarming\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["angel wings print","sacred geometry","spiritual wall art","golden mandala","divine protection","angel art","printable wall art","instant download","digital download","meditation decor","gallery wall","boho wall art","spiritual gift","angel print","celestial art"],
        "price": 6.99,
    },
    {
        "image": "2_Radiant Angel Wings and Sacred Geometry.jpg",
        "title": "Radiant Angel Wings Sacred Geometry Print | Spiritual Wall Art Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "Radiant angel wings surrounded by sacred geometry patterns. "
            "Light, divine energy, and protection radiate from every line. "
            "A powerful statement piece for any sacred space.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Spiritual home decor · Sacred geometry art · Meditation room · Boho decor · Gift for her\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["angel wings","sacred geometry","spiritual print","radiant angel","divine light","printable wall art","instant download","digital download","meditation art","boho wall art","spiritual decor","celestial print","angel art","gallery wall","housewarming gift"],
        "price": 6.99,
    },
    {
        "image": "3_Warrior Archangel Michael in Gleaming Armor.jpg",
        "title": "Archangel Michael Warrior Print | Gleaming Armor Spiritual Wall Art | Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "Archangel Michael in gleaming battle armor — the ultimate protector. "
            "Powerful, commanding, and radiating divine authority. "
            "A bold statement piece channeling strength and spiritual protection.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Spiritual home decor · Protection art · Men's room decor · Gallery wall · Spiritual gift\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["archangel michael","warrior angel","spiritual wall art","protection print","angel art","printable wall art","instant download","digital download","divine protection","angel warrior","catholic art","spiritual gift","gallery wall","archangel print","celestial art"],
        "price": 6.99,
    },
    {
        "image": "4_Untitled design.jpg",
        "title": "Divine Vision Angel Art Print | Celestial Wall Art Spiritual Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "A breathtaking celestial vision — divine art that transforms any wall into a sacred space. "
            "Ethereal, luminous, and full of divine energy.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Spiritual home decor · Celestial art · Meditation room · Gallery wall · Gift for her\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["divine vision","celestial art","spiritual print","angel art","printable wall art","instant download","digital download","meditation decor","spiritual home decor","ethereal art","celestial wall art","gallery wall","boho decor","spiritual gift","angelic art"],
        "price": 6.99,
    },
    {
        "image": "5_Majestic Baroque Angel Art Print.jpg",
        "title": "Majestic Baroque Angel Art Print | Spiritual Wall Decor Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "A majestic baroque angel rendered in rich, classical detail. "
            "Old masters meets divine energy — timeless and commanding. "
            "Perfect for statement walls and sacred spaces.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Baroque home decor · Spiritual art · Living room · Gallery wall · Housewarming gift\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["baroque angel","majestic angel","spiritual wall art","classical art print","angel art","printable wall art","instant download","digital download","baroque decor","spiritual home decor","gallery wall","housewarming gift","angel print","divine art","celestial art"],
        "price": 6.99,
    },
    {
        "image": "7_Elegant Baroque Angel Wall Art.jpg",
        "title": "Elegant Baroque Angel Wall Art | Spiritual Print Instant Digital Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "Elegant baroque angel art with timeless grace and divine beauty. "
            "Refined, luminous, and deeply spiritual. "
            "A perfect addition to any curated gallery wall or sacred space.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Elegant home decor · Spiritual art · Bedroom · Gallery wall · Gift for her\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["baroque angel","elegant angel art","spiritual wall art","angel print","printable wall art","instant download","digital download","classical art","spiritual home decor","gallery wall","bedroom decor","gift for her","divine art","angelic print","celestial wall art"],
        "price": 6.99,
    },
    {
        "image": "8_Ethereal Angel with Graceful Typography.jpg",
        "title": "Ethereal Angel Print with Typography | Spiritual Wall Art Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "An ethereal angel in graceful form, paired with flowing divine typography. "
            "Soft, luminous, and deeply moving — a perfect blend of art and sacred words.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Spiritual home decor · Bedroom wall art · Gallery wall · Meditation space · Gift for her\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["ethereal angel","angel typography","spiritual wall art","angel print","printable wall art","instant download","digital download","meditation decor","spiritual gift","gallery wall","bedroom art","boho wall art","divine art","angelic print","celestial art"],
        "price": 6.99,
    },
    {
        "image": "9_Luxurious Baroque Angel Poster.jpg",
        "title": "Luxurious Baroque Angel Poster | Divine Spiritual Wall Art Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "A luxurious baroque angel rendered with opulent detail and divine radiance. "
            "Rich, commanding, and deeply spiritual — this print demands attention.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Luxury home decor · Spiritual art · Living room statement · Gallery wall · Housewarming\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["baroque angel poster","luxurious angel","spiritual wall art","divine art","printable wall art","instant download","digital download","luxury decor","gallery wall","spiritual home decor","baroque decor","housewarming gift","angel print","celestial art","angelic wall art"],
        "price": 6.99,
    },
    {
        "image": "10_Warrior Archangel Michael with Shield and Sword.jpg",
        "title": "Archangel Michael Shield and Sword Print | Divine Warrior Spiritual Art Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "Archangel Michael wielding his sacred shield and flaming sword. "
            "The ultimate protector — powerful, fearless, and divinely armed. "
            "For those who need a guardian on their walls.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Spiritual protection art · Men's decor · Office wall art · Gallery wall · Spiritual gift\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["archangel michael","shield and sword","warrior angel","divine protection","spiritual wall art","printable wall art","instant download","digital download","angel warrior","catholic art","spiritual gift","archangel print","protection art","gallery wall","celestial art"],
        "price": 6.99,
    },
    {
        "image": "11_Dynamic Angel Poster with Ascendant Typography.jpg",
        "title": "Ascendant Angel Poster | Dynamic Spiritual Typography Print Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "A dynamic angel in full ascent, paired with powerful typography. "
            "Movement, energy, and divine ascension captured in a single bold print. "
            "For the walls that need to inspire.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Motivational wall art · Spiritual decor · Office · Gallery wall · Inspirational gift\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["ascendant angel","dynamic angel poster","spiritual typography","motivational wall art","printable wall art","instant download","digital download","angel art","inspirational print","gallery wall","spiritual home decor","divine ascension","angel poster","celestial art","spiritual gift"],
        "price": 6.99,
    },
    {
        "image": "12_Poster - Experience the divine protection and guidance of your guardian angel today..jpg",
        "title": "Guardian Angel Protection Print | Divine Guidance Spiritual Wall Art Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            '"Experience the divine protection and guidance of your guardian angel today."\n\n'
            "A powerful reminder that you are never alone — your guardian angel walks with you. "
            "Comforting, spiritual, and beautifully designed.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Spiritual home decor · Bedroom · Nursery · Grief gift · Spiritual encouragement gift\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["guardian angel print","divine protection","angel guidance","spiritual wall art","printable wall art","instant download","digital download","angel poster","comfort gift","spiritual gift","bedroom decor","nursery art","gallery wall","protection art","celestial art"],
        "price": 6.99,
    },
    {
        "image": "14_Soaring Angel Wings with Ethereal Glow.jpg",
        "title": "Soaring Angel Wings Print | Ethereal Glow Spiritual Wall Art Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "Majestic angel wings in full soar, radiating an ethereal golden glow. "
            "Breathtaking, luminous, and full of divine energy. "
            "A statement piece that transforms any room.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Spiritual home decor · Living room · Bedroom · Gallery wall · Housewarming gift\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["soaring angel wings","ethereal glow","spiritual wall art","angel wings print","printable wall art","instant download","digital download","divine light","celestial art","gallery wall","spiritual home decor","housewarming gift","angel art","luminous print","boho wall art"],
        "price": 6.99,
    },
    {
        "image": "15_Serene Angel Poster with Typography.jpg",
        "title": "Serene Angel Poster | Spiritual Typography Print Instant Digital Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "A serene, peaceful angel paired with graceful spiritual typography. "
            "Calm, centered, and deeply comforting — perfect for spaces that need peace.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Peaceful home decor · Meditation room · Bedroom · Gallery wall · Gift for her\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["serene angel","peaceful angel print","spiritual typography","spiritual wall art","printable wall art","instant download","digital download","meditation decor","bedroom art","gallery wall","gift for her","angel poster","calm decor","celestial art","angelic print"],
        "price": 6.99,
    },
    {
        "image": "17_Dark Armored Archangel with Ethereal Flames.jpg",
        "title": "Dark Armored Archangel Ethereal Flames Print | Spiritual Wall Art Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "A dark, armored archangel wreathed in ethereal flames — raw divine power made visible. "
            "Bold, intense, and commanding. For walls that need serious energy.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Dark home decor · Men's wall art · Office · Gaming room · Spiritual protection art\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["dark archangel","armored angel","ethereal flames","spiritual wall art","bold angel print","printable wall art","instant download","digital download","dark decor","men's wall art","protection art","archangel print","celestial art","gallery wall","spiritual gift"],
        "price": 6.99,
    },
    {
        "image": "18_Bold Angel Wings Graphic with 'RISE'.jpg",
        "title": "Bold RISE Angel Wings Graphic Print | Motivational Spiritual Wall Art Instant Download",
        "description": (
            "✨ INSTANT DIGITAL DOWNLOAD — no waiting, no shipping.\n\n"
            "Bold angel wings with the powerful word RISE — a declaration of ascension. "
            "Graphic, modern, and deeply motivational. "
            "For walls that push you higher every single day.\n\n"
            "── WHAT YOU GET ──\n"
            "• High-resolution JPG + PDF files\n"
            "• Sizes included: 5×7, 8×10, 11×14, 16×20, 18×24, 24×36\n"
            "• Print at home, Walgreens, Costco, FedEx — no quality loss\n\n"
            "── HOW IT WORKS ──\n"
            "1. Purchase → instant download link emailed to you\n"
            "2. Open files → choose your size\n"
            "3. Print same day\n\n"
            "── PERFECT FOR ──\n"
            "Motivational wall art · Office · Gym · Bedroom · Gallery wall · Inspirational gift\n\n"
            "© J2DAO Digital Art — personal use only."
        ),
        "tags": ["RISE angel wings","bold angel print","motivational wall art","angel wings graphic","printable wall art","instant download","digital download","inspirational print","gym wall art","office decor","gallery wall","spiritual gift","modern angel art","ascension print","celestial art"],
        "price": 6.99,
    },
]

# ── SHARED LISTING FIELDS ──────────────────────────────────────────────────────
SHARED_FIELDS = {
    "quantity": 999,
    "who_made": "i_did",
    "when_made": "made_to_order",
    "taxonomy_id": 2078,          # Art & Collectibles > Prints > Digital Prints
    "type": "download",
    "is_digital": True,
    "file_data": "",              # placeholder — upload files via listing_file endpoint
    "state": "draft",             # create as draft first — review then activate
    "should_auto_renew": True,
}

# ── HELPERS ────────────────────────────────────────────────────────────────────
def create_listing(data: dict) -> dict:
    payload = {
        **SHARED_FIELDS,
        "title":       data["title"],
        "description": data["description"],
        "price":       data["price"],
        "tags":        [t for t in data["tags"] if len(t) <= 20][:13],  # Etsy: max 13 tags, max 20 chars each
    }
    r = requests.post(
        f"{BASE_URL}/shops/{SHOP_ID}/listings",
        headers=HEADERS,
        json=payload,
    )
    if not r.ok:
        print(f"  ❌ HTTP {r.status_code}: {r.text}")
        r.raise_for_status()
    return r.json()


def upload_image(listing_id: int, image_path: Path) -> dict:
    with open(image_path, "rb") as f:
        r = requests.post(
            f"{BASE_URL}/shops/{SHOP_ID}/listings/{listing_id}/images",
            headers={
                "x-api-key":     ETSY_API_KEY,
                "Authorization": f"Bearer {ETSY_ACCESS_TOKEN}",
                # no Content-Type — multipart handled by requests
            },
            files={"image": (image_path.name, f, "image/jpeg")},
            data={"rank": 1, "overwrite": True},
        )
    r.raise_for_status()
    return r.json()


# ── MAIN ───────────────────────────────────────────────────────────────────────
def main():
    if ETSY_API_KEY == "YOUR_API_KEY_HERE":
        print("❌ Set ETSY_API_KEY and ETSY_ACCESS_TOKEN before running.")
        print("   export ETSY_API_KEY=your_key")
        print("   export ETSY_ACCESS_TOKEN=your_token")
        return

    created = []

    for i, listing_data in enumerate(LISTINGS[9:], 10):  # resume from #10 (1-9 already created)
        image_path = IMAGES_DIR / listing_data["image"]

        if not image_path.exists():
            print(f"⚠️  [{i}/{len(LISTINGS)}] Image not found: {listing_data['image']} — skipping")
            continue

        print(f"\n[{i}/{len(LISTINGS)}] Creating: {listing_data['title'][:60]}...")

        # 1. Create the listing (draft)
        result = create_listing(listing_data)
        listing_id = result["listing_id"]
        print(f"  ✅ Listing created — ID: {listing_id}")

        # 2. Upload the image
        img_result = upload_image(listing_id, image_path)
        print(f"  🖼  Image uploaded — {img_result.get('listing_image_id','?')}")

        created.append({
            "listing_id": listing_id,
            "title": listing_data["title"],
            "image": listing_data["image"],
            "url": f"https://www.etsy.com/listing/{listing_id}/",
        })

        time.sleep(1)  # be polite to the API

    # Save results
    out_file = Path(__file__).parent / "divine_listings_created.json"
    with open(out_file, "w") as f:
        json.dump(created, f, indent=2)

    print(f"\n\n✅ Done! {len(created)} listings created as DRAFTS.")
    print(f"📄 Listing IDs saved to: {out_file}")
    print(f"\n🔗 Review and activate at:")
    print(f"   https://www.etsy.com/your/shops/J2DAO/tools/listings")
    print(f"\n⚡ After activation, update etsy-landing.html links with the real listing URLs.")


if __name__ == "__main__":
    main()
