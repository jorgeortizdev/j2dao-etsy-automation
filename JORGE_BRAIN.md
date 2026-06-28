# Jorge's Second Brain
**Last updated:** 2026-06-27
*This file is Claude's persistent memory. Update it at the end of each session.*

---

## Who Jorge Is

**Full name:** Jorge Ortiz Marin
**Location:** Rockville, MD area
**Email:** jorgeortiz3333@gmail.com
**Phone:** (202) 660-2909
**Languages:** Bilingual — English / Spanish

**Current situation:**
- Day job: Data Entry Librarian (current, keeping while building side income)
- Previous role: IT Project Manager (contract ended — hence the job search)
- Building J2DAO Etsy/Shopify store + automation agency as primary growth path
- Money is tight right now — always ask before recommending paid tools, subscriptions, or anything that costs money

**Background:**
- 15+ years IT project management (cybersecurity, construction, retail)
- National A.C.E. Award recipient (top 2% regionally) at Camden Property Trust
- Currently at Intertek as IT PM (Cybersecurity) and CloudFactory as AI Data Analyst
- No raw Python coding — uses AI-assisted vibe coding with Claude
- No Jira on resume (removed by request)
- Agile/Scrum listed as "AI-Assisted Agile/Scrum"

---

## Active Projects

### 1. J2DAO Etsy/Shopify Store
- **75 Etsy active + 1 bundle = 76 total** ✅ (76 Shopify active)
  - All 5 sections complete: Terracotta 15 / Navy 15 / Blush 15 / Black 15 / Sage 15
  - Section IDs: terracotta=59114387, navy=59097500, blush=59097502, black=59114389, sage=59114391
- Platforms: Etsy (primary) + Shopify (r7ugfc-ur.myshopify.com, $1/mo until Sept 20 2026)
- Agency site: https://j2dao-automation.netlify.app
- Project files: `~/Documents/etsy-agent/`
- Full context: load the `j2dao-automation` skill
- Command Center dashboard: localhost:5001 (includes Health Report at /health)

**Make.com Automation (Free plan — 2/2 scenarios used):**
- Scenario 1: J2DAO Wall Art Daily Promoter (ID: 5476264) — posts wall art photo to Instagram every 24h, ACTIVE ✅
- Scenario 2: J2DAO AI Guide Reel Poster (ID: 5476373) — posts English + Spanish Reels on demand, INACTIVE (run manually)
- Facebook connection ID: 9575888 | Instagram account ID: 17841406779430027

**Pending:**
- TikTok app review submitted ✅ (2026-06-23) — awaiting review
- Reddit Make connection — deleted old broken scenario; slot freed

### 2. J2DAO Automation Agency
- Sells automation builds to Etsy/Shopify sellers
- Packages: Starter $997 / Growth $2,497 / Enterprise $4,997
- Files in `~/Documents/etsy-agent/agency/`
- No clients yet (launched June 2026)

### 4. Local AI Setup Guide (NEW — launched June 2026)
- Product: "Your Own AI: The Beginner's Complete Guide to Running AI Privately on Your Computer"
- Platform: Gumroad — daoist67.gumroad.com/l/your-own-ai-guide
- Price: $47
- Gumroad account: J2DAO.store@gmail.com — login via EMAIL/PASSWORD only (NOT Google OAuth — that creates a separate empty account). Username: daoist67
- PDF file: `~/Documents/Claude's Projects/Your_Own_AI_Setup_Guide.pdf` (13 pages)
- Listing copy: `~/Documents/Claude's Projects/Gumroad_Listing_Copy.md` (English + Spanish/bilingual)
- Service tiers upsell: $47 guide / $197 done-with-you / $397 done-for-you
- Inspired by Instagram video from @michellescomputer (local AI on Raspberry Pi)
- Target markets: General beginners (English) + Hispanic community (bilingual)

**HeyGen Videos (DONE ✅):**
- English Reel: df44db5e-5301-4950-9876-2424c2b38009 — posted to Instagram ✅
- Spanish Reel: 7950b656-890e-4a83-867d-68da9d4320e2 — posted to Instagram ✅
- Both posted via Make Scenario 2 (J2DAO AI Guide Reel Poster)
- Instagram bio updated: Gumroad link + store links added ✅

**Pending:** (done — cover image uploaded ✅ 2026-06-24)

### 3. Job Search
- Goal: AI-oriented IT role to "job stack" alongside Data Entry Librarian job
- Priority: Remote first → Hybrid → In-person
- Salary target: ~$115K for IT PM roles; $7,500/mo for AI automation roles
- Resume: `~/Documents/Claude's Projects/Jorge_Ortiz_Resume.html` (HTML, print-to-PDF)
- Word resume: `~/Documents/Claude's Projects/Jorge_Ortiz_Resume_AI.docx`
- All cover letters: `~/Documents/Claude's Projects/Jorge_Ortiz_All_Cover_Letters.docx`

**Applications (as of 2026-06-22):**
- ✅ C-4 Analytics — AI Automation Specialist (applied)
- ✅ Pavago — AI Automation Specialist (applied, $7,500/mo)
- ⏳ McKesson — Sr. IT Project Manager M&A (listed Irving TX, confirm if remote)
- ❌ ODNI — IT Project Manager (not remote, skipped)
- ❌ Omnisolve INC — posting expired, skipped

---

## Decisions & Preferences

| Decision | Detail |
|---|---|
| No auto-spending | Always ask before anything that costs money |
| Remote-first jobs | Remote → Hybrid → In-person priority order |
| Python framing | "AI-Assisted Python Scripting" — not raw Python |
| Agile/Scrum framing | "AI-Assisted Agile/Scrum" |
| No Jira on resume | Removed from skills AND experience bullets |
| Resume print tip | Chrome → Cmd+P → uncheck "Headers and footers" → Save as PDF |
| Job salary | $115K for IT PM; $7,500/mo for AI automation roles |
| Cover letter style | 4 body paragraphs, navy header, tailored per company |
| Skill approach | Build skills as both a .skill file + human-readable markdown |
| Chat focus | Business only — Etsy, Shopify, Gumroad, agency, new business ideas |
| Brain protocol | Read JORGE_BRAIN.md at start of every session; save updates at end |

---

## Skills & Files Built

| Skill/File | What it is | Location |
|---|---|---|
| `j2dao-automation` skill | Full J2DAO store + agency context | Installed |
| `jorge-brain` skill | This second brain | Installed |
| `Jorge_Ortiz_Resume.html` | Two-column HTML resume (print to PDF) | Claude's Projects |
| `Jorge_Ortiz_Resume_AI.docx` | Word resume | Claude's Projects |
| `Jorge_Ortiz_All_Cover_Letters.docx` | 6 tailored cover letters | Claude's Projects |
| `seo_optimizer.py` | Audits + rewrites titles/tags for all active Etsy listings via Claude + Etsy API. Uses PATCH, tags truncated to 20 chars each. | etsy-agent/ |
| `retry_failed_seo.py` | Retries listings that seo_optimizer.py failed to update (reads seo_report.json) | Claude's Projects/ |
| `audit_colors.py` | Downloads all listing thumbnails, samples pixel colors, flags wrong-color duplicates | etsy-agent/ |
| `fix_wrong_colors.py` | Re-generates + re-uploads correct color images for a hardcoded list of listings | etsy-agent/ |
| `organize_sections.py` | Creates 5 Etsy color sections, assigns all listings (dry run or --apply) | etsy-agent/ |
| `fix_sections.py` | Patches 8 specific listing section assignments that text detection got wrong | etsy-agent/ |
| `activate_new_listings.py` | Activates 15 sage/blush/black drafts for 5 new quotes, fixes titles | etsy-agent/ |
| `activate_navy_new.py` | Activates 5 navy drafts for 5 new quotes, fixes titles (DO NOT delete) | etsy-agent/ |
| `list_drafts.py` | Lists all draft listings in the shop | etsy-agent/ |
| `debug_drafts.py` | Fetches specific listing IDs and shows all required fields + state | etsy-agent/ |
| `build_resume.js` | Script that generates the .docx resume | Claude's Projects |
| `build_cover_letters.js` | Script that generates all cover letters | Claude's Projects |
| `Your_Own_AI_Setup_Guide.pdf` | 13-page local AI setup guide (for sale on Gumroad) | Claude's Projects |
| `Gumroad_Listing_Copy.md` | English + Spanish listing copy, captions, Reel scripts | Claude's Projects |

---

## Session Log

### 2026-06-28 (Divine Collection Etsy + Shopify fix + deploy prep)

**Shopify collections fixed ✅**
- Root cause: products had `inventoryPolicy: DENY` with 0 inventory AND were not published to Online Store channel
- Fixed via `productVariantsBulkUpdate` (set all to `CONTINUE`) + `publishablePublish` for all 50 products
- Online Store Publication ID: `gid://shopify/Publication/165938856051`
- All 5 color collections now show products on storefront ✅
- Fixed collection descriptions showing raw `<p>` tags via `collectionUpdate` with `descriptionHtml` field

**Divine Collection — All 18 designs now live on Etsy ✅**
- Discovered only 5 of 18 divine designs had Etsy listings; 13 were missing
- Created 15 new divine listings via Etsy API (`create_divine_listings.py`) — all as drafts
- Uploaded digital files to all 15 listings (`upload_digital_files.py`)
- Published all 15 → Etsy shop now at 96 total listings (81 + 15 divine)
- New listing IDs 4529197197–4529213398 (see `divine_listings_created.json`)

**Scripts built this session:**
- `create_divine_listings.py` — creates all 15 divine Etsy listings with images + metadata
- `upload_digital_files.py` — attaches digital download files to listings
- `etsy_get_token.py` — OAuth2 PKCE flow to get fresh Etsy access tokens

**Etsy API auth (confirmed working):**
- `ETSY_API_KEY` = `keystring:shared_secret` (combined with colon)
- `ETSY_ACCESS_TOKEN` = OAuth2 Bearer token (expires in 3600s)
- Shop ID: 45562671 | App: j2s-shop-agent (Personal Access, active)
- Banned app: j2dao-shop-manager — do NOT use

**Deploy script ready:**
- `deploy-to-netlify.sh` in Claude's Projects — copies HTML + images to agency folder, deploys to Netlify
- Sites: j2dao-automation.netlify.app/etsy + /shopify

**Pending:**
- Run `bash deploy-to-netlify.sh` to publish both landing pages
- Push new scripts to GitHub (j2dao-etsy-automation repo)
- Add landing page URLs to Etsy shop bio and Shopify store
- Add traffic analytics section to Command Center dashboard
- Always keep GitHub updated with major new scripts going forward

### 2026-06-27 (Pinterest + SEO optimizer session)

**Divine Collection Pinterest — DONE ✅**
- All 18 Divine Collection pins published to new "Divine Collection" Pinterest board
- Board created fresh; all pins link to https://www.etsy.com/shop/J2DAO
- Images from: `~/Documents/Claude's Projects/divine_collection/jpeg_export/`
- Pins 1–15 done in prior session; Pins 16–18 completed this session ✅

**SEO Optimizer — All 81 listings updated ✅**
- Ran `seo_optimizer.py` — 67/81 updated on first pass; 14 failed
- Root cause of 14 failures: script was using `requests.put` instead of `requests.patch` (fixed), AND tags were not being truncated to Etsy's 20-char limit per tag
- Fixed via `retry_failed_seo.py` (saved to `~/Documents/Claude's Projects/retry_failed_seo.py`)
- Also fixed `seo_optimizer.py` directly: `payload["tags"] = [t[:20] for t in tags[:13]]`
- All 81 listings now SEO-optimized ✅
- Average SEO score: 6.8/10 (baseline before optimization)
- Token refresh flow documented: `POST https://api.etsy.com/v3/public/oauth/token` with `grant_type=refresh_token`, `client_id=ETSY_KEYSTRING`, `refresh_token=ETSY_REFRESH_TOKEN`

**Key Etsy API notes (learned this session):**
- Update endpoint: `PATCH` (not PUT) to `/application/shops/{shop_id}/listings/{listing_id}`
- Tags: max 13 tags, each max 20 characters
- Auth header: `x-api-key: keystring:shared_secret`, `Authorization: Bearer {access_token}`
- Access token expires in 3600s — refresh with ETSY_REFRESH_TOKEN when expired

### 2026-06-25 (late night — Make.com Daily Promoter fix)
- Fixed J2DAO Wall Art Daily Promoter (scenario 5476264) — both data store modules (10 and 20) had lost their data store references, counter formula was missing
- Module 10: re-selected J2DAO Wall Art Rotation data store, key = "rotation" ✅
- Module 20: re-selected data store, added counter formula `{{(10.counter + 1) % 5}}` (mod not recognized in UI, % operator works) ✅
- All 3 modules green — scenario running daily again ✅
- Confirmed: Facebook group auto-posting via Make.com is NOT possible (Meta API blocks posting to groups you don't own) — outreach must be done manually
- Pending: post Facebook group outreach copy (Version 3) manually in 3–5 Etsy seller groups

### 2026-06-25 (evening — Divine Collection published + Agency outreach + HeyGen video)

**Divine Collection — DONE ✅**
- All 18 design PNGs converted to high-quality JPEGs (95%, 2–5MB each) for Etsy compatibility
- JPEG exports: `~/Documents/Claude's Projects/divine_collection/jpeg_export/`
- Uploaded design photos to all 5 draft listings via Chrome MCP, split by design theme:
  - Elévate (4 files: 1,2,11,14), Tu Ángel Te Cuida (4 files: 5,7,8,9), Blessed & Elevated (2 files: 13,15), RISE (4 files: 4,6,16,18), Warrior Archangel Michael (4 files: 3,10,12,17)
- All 5 listings published and LIVE on Etsy ✅
- Listing IDs: Elévate=4527671434, Tu Ángel=4527661327, Blessed=4527665284, RISE=4527655295, Warrior=4527660022
- Note: Etsy's new listing editor doesn't show a digital file upload section inline — files were uploaded as listing photos only. Digital download file upload may need separate handling.

**Agency Outreach — IN PROGRESS**
- HeyGen English outreach video composed (project: 08ab946e-6fba-4a58-ba91-b6170c77b48a)
- Video rendered — render ID: 7c56b47f-a7d2-4685-9e85-8a52339e1e35
- Spanish version blocked (monthly HeyGen credit used) — script saved for July
- Spanish script: `~/Documents/Claude's Projects/agency_outreach/heygen_script_spanish.md`
- Facebook group post copy (4 versions, English): `~/Documents/Claude's Projects/agency_outreach/facebook_post_copy_english.md`
- Recommended: post Version 3 (educational "3 things to automate") first in new groups, then Version 1 (story) a week later
- No Reddit outreach (rejected before) — Facebook groups only
- Jorge is not comfortable on camera — using HeyGen AI voice animation style (no real person)

**Pending:**
- Download HeyGen English video and post to Etsy seller Facebook groups
- Render Spanish video in July (HeyGen credits reset monthly)
- Post English Facebook outreach copy in 3–5 Etsy seller groups

### 2026-06-25 (full day session — SEO audit + mockups + API reapplication)
- Make.com Facebook connection reauthorized ✅ — Instagram Wall Art Promoter running again
- Etsy SEO audit complete: titles/tags are fine (all 13 used). Root issue = PHOTOS. Every listing has only 1 photo, Etsy penalizes this in search ranking
- Created 2 navy blue no-text frame mockup images in Canva (designs saved: DAHNnyAoimo, DAHNnwwukOo)
- Mockup upload script written: `~/Documents/Claude's Projects/etsy_mockups/upload_navy_mockups.py`
- Etsy API still blocked — old app was DENIED/banned. Re-applied for new API app today (Jun 25, ~8pm)
  - New app name: "J2DAO Shop Manager", use case: personal shop management only, Website: r7ugfc-ur.myshopify.com
  - Awaiting Etsy approval (1–3 business days) — once approved, run upload_navy_mockups.py to bulk-add mockups
- Manually uploaded 2 mockups to "Do The Work Navy Blue" listing ✅ as proof of concept
- While waiting for API: mockups ready, script ready — just need the approved key
- Pending: Generate mockup sets for terracotta, blush, sage, black color themes (same workflow)
- j2dao-marketing skill created and installed ✅ — CMO-level marketing expert for J2DAO

### 2026-06-22 (morning session)
- Rebuilt resume from uploaded PDF → HTML (two-column, navy sidebar) + Word .docx + Pages
- Reframed Jorge as "AI Automation Specialist" — J2DAO added as founder experience
- Found and applied to C-4 Analytics (AI Automation Specialist) and Pavago (AI Automation Specialist)
- Answered C-4 Analytics custom questions (6 questions, salary $115K)
- Answered Pavago custom questions (3 questions, salary $7,500/mo)
- Searched for ODNI, McKesson, Omnisolve — ODNI not remote, Omnisolve expired
- Built J2DAO Automation skill (.skill file, installed)
- Built Jorge's Second Brain (this file + jorge-brain skill)

### 2026-06-22 (evening session — Cowork setup + new product launch)
- Set up Cowork: installed Small Business + Marketing plugins, connected Canva + HeyGen connectors
- Connected Claude's Projects folder as workspace
- Identified new business idea: Local AI Setup Guide (inspired by @michellescomputer Instagram Reel)
- Built 13-page PDF guide "Your Own AI" using reportlab — covers Mac, Windows, Raspberry Pi
- Created Gumroad account (J2DAO.store@gmail.com) and published product at $47
- Gumroad URL: daoist67.gumroad.com/l/your-own-ai-guide
- Wrote full English + bilingual Spanish listing copy, Instagram captions, DM templates, Reel scripts
- Kicked off two HeyGen Reel videos (English + Spanish) — still rendering, pick up tonight
- Next: Review HeyGen videos → render MP4s → post to Instagram → add link to bio

### 2026-06-23 (job applications session)
- This conversation is now dedicated to job applications only — agency/business stays in separate chat
- Applied (in progress) to **Triple Whale** — Social Media Specialist role
  - Answered B2B SaaS social media question using J2DAO Automation as the company
  - Framed audience as Shopify/Etsy sellers, channels as Instagram + bilingual expansion
  - Highlighted HeyGen Reels, Make.com automation pipeline, Gumroad product launch
- Triple Whale context: e-commerce analytics SaaS for Shopify brands — Jorge's Shopify experience is a strong fit

### 2026-06-23 (late night session — TikTok submission)
- TikTok app review submitted ✅ — in review, awaiting TikTok approval (1–7 business days)
- Added TikTok meta verification tag to agency site index.html
- Deployed agency site via Netlify MCP (site ID: 69d10228-919d-48d9-9016-fc0023089dde)
- Created J2DAO Sandbox (ID: 7654738384037218311) with Content Posting API + video.publish
- Demo video recorded and compressed to mp4 (J2DAO_TikTok_Demo_small.mp4 in Claude's Projects)
- Submission reason: initial submission for Content Posting API + video.publish scope

### 2026-06-24 (late night — Shopify sync complete + niche expansion discussion)
- Ran 4 batch pipeline commands locally to create 20 missing Shopify products (5 new quotes × blush/black/sage/navy)
- All 20 created as drafts, then activated via Shopify MCP — 20/20 success ✅
- Fixed "Do The Work" blush title (came through as "Title" — corrected to proper name)
- Shopify now at 76 active products — fully synced with Etsy (15 quotes × 5 colors + 1 bundle) ✅
- Discussed niche expansion: current motivational print niche is slow/crowded
- Top expansion opportunities identified: nursery prints, kitchen prints, Spanish-language prints (biggest edge — bilingual + underserved), faith/scripture prints
- Spanish prints are the top recommendation — genuine competitive moat, almost no competition at quality level
- Next step: pick one niche, run a 5-quote test batch through existing pipeline

### 2026-06-24 (late night — SEO fix + health check upgrade)
- **Root cause identified:** `seo_optimizer.py` stripped color keywords from titles → downstream scripts defaulted to terracotta → 17 listings got wrong images
- **Fixed `seo_optimizer.py`:** added `protect_color()` function + updated Claude prompt to treat color labels as protected tokens. Double-layered: prompt instructs preservation AND code re-injects if Claude drops it
- **Upgraded `health_check.py`:** added 3 new shop-level checks that run after per-listing scan:
  1. Draft alert — flags if any draft listings exist (should always be 0)
  2. Section count check — each color must have exactly 15 listings
  3. Variant coverage — every known quote × every color must be present
- `health_check.py` now has `KNOWN_QUOTES` list — update it when adding new quote batches
- All 5 navy listings assigned to Navy Blue Prints section via `assign_navy_sections.py` (bypassed Etsy indexing lag by patching section_id directly by listing ID)

### 2026-06-24 (evening — Etsy image fix + section organization)
- Root cause found: `fix_listing_images_v2.py` defaulted to terracotta when SEO optimizer stripped color keywords from titles+descriptions, causing 17/55 listings to get wrong-color images
- Built `audit_colors.py` — downloads all listing thumbnails, samples pixel colors, flags duplicate (quote+color) pairs
- Audit revealed 32 terracotta (should be 15), 8 quotes with duplicate terracotta listings
- Built `fix_wrong_colors.py` — regenerated + re-uploaded correct color images for 17 listings ✅
- Re-authorized Etsy OAuth with `shops_w` scope (was missing — needed for section creation)
- Built `organize_sections.py` — created 5 color sections, assigned all 55 listings ✅
- 8 listings still mis-assigned (text detection reads "Terracotta" in old title/description, overrides correct image)
- Built `fix_sections.py` — patches those 8 listing section assignments directly via API
- **Still to run:** `fix_sections.py`, then sage/blush/black batches for 5 new quotes (--skip 10), then `organize_sections.py --apply`
- Tools built this session: `audit_colors.py`, `fix_wrong_colors.py`, `organize_sections.py`, `fix_sections.py`

### 2026-06-24 (late night — Divine Collection Etsy listings)
- Created all 5 Divine Collection digital download listings on Etsy via browser automation (tabId 1441164821)
- Each listing: 2–4 preview photos, title, full description, 13 tags, $6.99 price, 999 qty, Digital files, "With an AI generator" ✅
- Listings: 1) You Are Protected (warrior angel) 2) RISE Up (wings+halo) 3) Blessed & Elevated (celestial) 4) Tu Ángel Te Cuida (baroque) 5) Elévate (fine line wings)
- All 5 saved as drafts ✅ — Jorge must manually upload full-res PNG files (too large for automation) then publish

### 2026-06-27 (GitHub portfolio build — job applications session)
- Changed GitHub username from `jorgeortiz3333-crypto` → `jorgeortizdev` ✅
- Built full GitHub portfolio at **github.com/jorgeortizdev** with 5 repos:
  1. `jorgeortizdev` (profile README) — bilingual bio, skills table, featured projects, Gumroad link, contact
  2. `j2dao-etsy-automation` — Etsy listing automation, SEO pipeline, Make.com integration (Python 3.11 / Etsy API / Shopify API)
  3. `ai-setup-guide-generator` — Python/ReportLab PDF generator, links to Gumroad ($47 guide at daoist67.gumroad.com/l/your-own-ai-guide)
  4. `social-media-automation` — HeyGen → Make.com → Instagram Reels / TikTok / YouTube Shorts pipeline
  5. `resume-cover-letter-builder` — Ollama-powered ATS resume tailoring, bilingual support, batch mode
- All repos public with professional READMEs ✅
- Portfolio is job-application ready — showcases automation, AI, e-commerce, and bilingual skills
- Preview photos location: `~/Documents/Claude's Projects/etsy_previews/` (warrior_1-4.jpg, rise_1-4.jpg, blessed_1-4.jpg, baroque_1-4.jpg, divine_1-2.jpg)
- Etsy API still "Pending Personal Approval" — etsy_upload.py will automate this once approved

### 2026-06-24 (Gumroad + Wall Art rotation session)
- Gumroad login clarified: J2DAO.store@gmail.com via EMAIL/PASSWORD only (not Google OAuth). Username: daoist67
- Created Gumroad cover image (1280x720px) — dark navy, laptop/terminal visual, cyan accents, Gumroad URL in footer
- Uploaded cover image to daoist67.gumroad.com/l/your-own-ai-guide ✅
- Fixed Wall Art Daily Promoter (Make Scenario 5476264) to rotate all 5 listings instead of repeating "Do The Work"
- Created Make Data Store (ID: 111295) + Data Structure (ID: 409695) "J2DAO Wall Art Rotation" — stores counter 0–4
- Counter seeded at 1 (next post: Stay Soft → Embrace The Process → Show Up Daily → Protect Your Peace → Do The Work → repeat)
- Rotation uses switch() + mod() functions — 100% free, no Make paid plan needed

### 2026-06-23 (full day session — Make automation + HeyGen Reels)
- Finalized 5 new quote listings: Do The Work, Stay Soft, Embrace The Process, Show Up Daily, Protect Your Peace
- Fixed Shopify 20MP image error (resized to ≤2000px in print_creator.py) — all 5 images uploaded
- Fixed Stay Soft SEO tags (was 10/13, now 13/13)
- Activated all 5 Etsy listings + all 5 Shopify products — store now at 55 Etsy / 56 Shopify active
- Added Health Report page to Command Center (localhost:5001/health + /run-health)
- Built Make Scenario 1: J2DAO Wall Art Daily Promoter — posts wall art photo to Instagram every 24h, ACTIVE ✅
- "Do The Work" first post went live on Instagram successfully ✅
- Both HeyGen Reels confirmed rendered (English + Spanish)
- Built Make Scenario 2: J2DAO AI Guide Reel Poster — ran once, posted both Reels to Instagram ✅
- Updated Instagram bio with Gumroad link (daoist67.gumroad.com/l/your-own-ai-guide) + store links ✅
- Set chat focus to business only; brain read/save protocol established
- Pending: TikTok app review submission, Gumroad cover image

### 2026-06-22 (late night session — social media automation setup)
- Researched full social media automation pipeline: HeyGen → Make → Instagram/Facebook/YouTube/TikTok
- Confirmed Make has native modules: "Publish a Reel" (Facebook), "Create a Reel Post" (Instagram Business), YouTube upload
- TikTok: semi-auto only (video goes to inbox, one tap to publish) — no cost workaround
- Created Meta Business Suite account (J2DAO Automation) — business_id: 1547136876784093
- Created J2DAO Automation Facebook Page (page_id: 61591447642707)
- Connected Instagram j2_da_o to the Facebook Page and Meta Business Suite ✅
- Opened Make scenario editor and confirmed "Publish a Reel" module exists under Facebook Pages
- **Pick up here next session:**
  1. Click "Publish a Reel" in Make Facebook Pages module to start scenario
  2. Connect Facebook Pages account to Make (OAuth)
  3. Add Instagram Business module + connect
  4. Add HeyGen "Watch New Videos" trigger as the start of the scenario
  5. Wire: HeyGen finish → post to Facebook Reel + Instagram Reel + YouTube Short simultaneously
  6. Test with a sample video, then activate

## Future App Project Ideas (added 2026-06-25)

Priority order for development — validate demand before building anything.

| # | Idea | Edge | First Step |
|---|------|------|------------|
| 1 | Bilingual ops tool for Latino-owned small businesses | Bilingual moat, massive underserved market (construction, cleaning, landscaping) | Talk to 10 Latino small business owners |
| 2 | AI immigration timeline tracker | High emotional need, almost no good affordable tooling | Research existing tools, find the gap |
| 3 | Etsy/Shopify seller AI assistant ⭐ **START HERE** | Jorge IS the customer, knows pain points cold, audience reachable via Reddit/FB groups | Build lightweight beta on existing J2DAO pipeline |
| 4 | Trades contractor copilot | Voice-first, job site context, small contractors ignored by enterprise software | Survey local contractors |
| 5 | Faith community ops tool | Loyal word-of-mouth communities, massive volunteer coordination need, zero good tools | Find 1-2 church admins to interview |

**Rule:** Sell before you build. Get 3 people to commit to paying before writing a line of app code.

---

## Master To-Do List

### 🟢 Recently Completed
- [x] TikTok app review submitted ✅ (2026-06-23) — awaiting review (1–7 business days)
- [x] Gumroad cover image created + uploaded ✅ (2026-06-24) — dark tech theme, laptop terminal visual, Gumroad URL in footer
- [x] Wall Art Daily Promoter rotation fixed ✅ (2026-06-24) — now rotates all 5 listings using Make Data Store counter (free)
- [x] Shopify fully synced to Etsy ✅ (2026-06-24 late night) — 20 missing products (5 new quotes × blush/black/sage/navy) created + activated. Shopify now at 76 active products matching Etsy
- [x] All 5 Divine Collection Etsy listings created as drafts ✅ (2026-06-24) — via browser automation

### 🟡 Up Next
- [ ] Upload actual full-res PNG digital download files (17–31 MB) to each Divine Collection listing's "Digital files" section (must be done manually — above file size limit for automation)
- [ ] Publish all 5 Divine Collection drafts on Etsy after files are uploaded
- [ ] Add 2 retry Shopify products (Poster Experience Divine Protection + Majestic Baroque) to Divine Collection manually
- [ ] Pick niche expansion target (Spanish prints recommended) and run 5-quote test batch
- [ ] Fix ~4 Etsy listings with stale "Terracotta" in title but correct non-terracotta image (cosmetic)
- [ ] Gumroad dashboard integration — add sales/revenue data to Command Center
- [ ] Agency: start outreach to first potential clients
- [ ] Etsy API pending personal approval — once resolved, etsy_upload.py handles future listings automatically

---

## Command Center Dashboard — Recovery Guide

**URL:** http://localhost:5001
**File:** `~/Documents/etsy-agent/dashboard_server.py`
**launchd service:** `com.j2dao.dashboard`

### If localhost:5001 won't connect:
1. Check if service is running: `launchctl list | grep j2dao`
   - If `com.j2dao.dashboard` shows `-` in first column = not running (crashed)
   - Exit code 78 = config/startup error
2. Start manually: `python3 ~/Documents/etsy-agent/dashboard_server.py`
3. If "command not found: python" → use `python3` (installed at `/Library/Frameworks/Python.framework/Versions/3.14/bin/python3`)
4. Dashboard will come up at localhost:5001 — keep Terminal window open while using it

### What the dashboard shows:
- Top bar: Etsy live count, total views, favorites, revenue, orders, prints made, QA passed, variants total
- Quick links: Etsy Shop, Shopify Admin, Gumroad, Health Report, Refresh
- Left panel: Pipeline steps (1-6) + Color variant progress bars
- Main area: All quotes × color status grid (Etsy ✓5 / Shopify ✓5 per quote)
- 7-Day Views chart (top right)

---

## How to Update This File

At the end of each session, add a new entry under **Session Log** with:
- Date
- What was built or decided
- Any new pending items
- Any preference changes

Keep entries concise — one line per item.
