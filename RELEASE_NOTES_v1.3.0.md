

# RSS Ad Rock Generator – Release Notes v1.3.0

Release date: 2026-02-25

---

## Overview

Version 1.3.0 focuses on metadata accuracy, RSS integrity, parser stability, and production hardening.

This release eliminates incorrect fallback values, fixes duplicated images, and improves scraping reliability for Framer-based pages.

---

## Major Improvements

### 1. Metadata Handling Refactor

- Removed artificial fallback values such as "Sem título" and "Sem descrição"
- Implemented strict metadata extraction priority:
  - Title → og:title → twitter:title → <h1>
  - Description → Framer short description → meta[name="description"]
  - Image → og:image only
- Posts without valid titles are now ignored

Result:
- No more invalid RSS entries
- Deterministic metadata generation

---

### 2. Image Validation & Stability

- Eliminated repeated placeholder images
- Enforced og:image-only strategy
- Improved image processing validation
- Maintained original CDN image in media:content
- Local optimized image used only for enclosure

Result:
- Correct image mapping per post
- No duplicated image artifacts

---

### 3. Parser Hardening

- Added lxml parser
- Forced BeautifulSoup to use "lxml"
- Increased scraping reliability for Framer HTML structure

Updated dependency list:
- requests
- beautifulsoup4
- lxml
- pillow
- python-dateutil

Result:
- More robust DOM parsing
- Reduced metadata extraction inconsistencies

---

### 4. IndexNow Stability

- Confirmed idempotent behavior via SQLite logs.db
- Status 200 and 202 treated as successful submission
- Prevented duplicate submissions

Result:
- Clean incremental URL submission
- No redundant API calls

---

### 5. Documentation Upgrade

Added or fully revised:

- ARCHITECTURE.md
- DEPLOYMENT.md
- requirements.txt stabilization

Result:
- Production-grade documentation
- Clear operational standards

---

## Production Validation

Validated on:

- Ubuntu 22.04 LTS
- Python 3.10
- Nginx

Feed validation:
https://validator.w3.org/feed/

Production RSS:
https://mobiledelivery.com.br/rss/adrock.xml

---

## Breaking Changes

None.

Metadata logic is stricter but backward compatible.

---

## Known Limitations

- Full re-scrape on every execution (incremental scraping not yet implemented)
- No ETag or Last-Modified header handling

---

## Next Planned Improvements (v1.4.x)

- Incremental scraping support
- Image hash deduplication
- JSON Feed support
- Optional Docker deployment
- systemd service option

---

This version marks the transition of the RSS Ad Rock Generator from utility script to structured production service.