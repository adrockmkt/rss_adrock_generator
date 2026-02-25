# RSS Ad Rock Generator – Architecture Documentation

## 1. Overview

The RSS Ad Rock Generator is a production-grade Python service responsible for generating a valid RSS 2.0 feed from a Framer-based blog.

It performs:

- Structured scraping of blog posts
- Metadata extraction (title, description, og:image, date)
- Image optimization and local publishing
- Incremental IndexNow submission
- SQLite-based duplication control
- Scheduled execution via cron

---

## 2. High-Level Architecture

Framer Blog (adrock.com.br/blog)
        ↓
framer_scraper.py
        ↓
rss_generator.py
        ↓
Local image processing (Pillow)
        ↓
XML generation (RSS 2.0)
        ↓
Public directory (Nginx)
        ↓
IndexNow API

---

## 3. Components

### 3.1 framer_scraper.py

Responsible for:

- Fetching blog listing
- Iterating over post URLs
- Extracting structured metadata

Metadata priority order:

Title:
1. og:title
2. twitter:title
3. <h1>

Description:
1. Short description block (Framer component)
2. meta[name="description"]

Image:
1. og:image only

No artificial fallback values are allowed.
Posts without a valid title are ignored downstream.

---

### 3.2 rss_generator.py

Responsible for:

- Formatting XML using ElementTree
- Generating valid RSS 2.0 structure
- Injecting media:content and enclosure tags
- Handling pubDate formatting (RFC 2822)
- Resizing images to 600px width
- Publishing optimized images

Image logic:

- media:content → original CDN image
- enclosure → optimized local PNG
- No placeholder image is ever used

---

### 3.3 main.py

Entry point that orchestrates:

1. Scraping
2. RSS generation
3. File publishing
4. IndexNow submission

---

### 3.4 IndexNow Module

Located under:

indexnow/

Features:

- Deduplication via SQLite (logs.db)
- Submission to https://api.indexnow.org/indexnow
- Status 200 and 202 treated as success
- Idempotent behavior

---

## 4. Data Flow

1. Fetch blog listing
2. Extract post URLs
3. Visit each post
4. Extract structured metadata
5. Build RSS XML tree
6. Optimize and save images
7. Publish XML to public directory
8. Submit new URLs to IndexNow

---

## 5. Storage

Temporary:
- images/
- output/

Persistent:
- indexnow/logs.db

Non-versioned directories are ignored via .gitignore.

---

## 6. Execution Model

### Manual

python main.py

### Automated (Production)

Cron (root):

0 7 * * * /home/adrock/rss_adrock_generator/rodar_rss.sh >> /home/adrock/rss_adrock_generator/rss.log 2>&1

---

## 7. Environment

Production:
- Ubuntu 22.04 LTS
- Python 3.10
- Nginx

Dependencies:
- requests
- beautifulsoup4 (lxml parser)
- lxml
- pillow
- python-dateutil

---

## 8. Reliability Considerations

- Timeout on external HTTP requests
- Try/except around image processing
- No silent fallback metadata
- Controlled dependency versions
- Deterministic RSS generation

---

## 9. Validation

Feed validation:
https://validator.w3.org/feed/

Manual inspection:
https://mobiledelivery.com.br/rss/adrock.xml

---

## 10. Versioning Strategy

Tags follow semantic versioning:

v1.x.x

Major changes include:
- Metadata logic
- Image processing
- IndexNow behavior
- XML structure changes

---

## 11. Future Improvements

- Incremental scraping (only new posts)
- ETag / Last-Modified support
- Image hash deduplication
- Optional JSON Feed support
- Dockerized deployment

---

This document defines the technical foundation of the RSS Ad Rock Generator and must be updated whenever architectural changes occur.
