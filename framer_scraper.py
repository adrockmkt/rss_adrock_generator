import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime, timezone

BASE_URL = "https://adrock.com.br"

def get_blog_posts():
    response = requests.get(f"{BASE_URL}/blog", timeout=10, headers={"User-Agent": "Mozilla/5.0"})
    response.encoding = 'utf-8'  # força utf-8
    soup = BeautifulSoup(response.text, "lxml")

    seen = set()
    post_links = []

    for a_tag in soup.select("a[href*='/blog/']"):
        href = a_tag["href"]
        title_element = a_tag.select_one(".framer-jha8re p")
        if title_element and href != "/blog" and href not in seen:
            full_url = urljoin(BASE_URL, href)
            seen.add(href)
            post_links.append(full_url)
            print(f"🔗 Post encontrado: {full_url}")

    posts = []

    for url in post_links:
        post_resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        post_resp.encoding = 'utf-8'  # força utf-8
        post_soup = BeautifulSoup(post_resp.text, "lxml")

        def extract_title(soup):
            og = soup.find("meta", property="og:title")
            if og and og.get("content"):
                return og["content"].strip()

            tw = soup.find("meta", attrs={"name": "twitter:title"})
            if tw and tw.get("content"):
                return tw["content"].strip()

            if soup.title and soup.title.string:
                return soup.title.string.strip()

            h1 = soup.find("h1")
            if h1 and h1.text:
                return h1.text.strip()

            return None


        def extract_image(soup):
            og = soup.find("meta", property="og:image")
            if og and og.get("content") and "framerusercontent" in og["content"]:
                return og["content"].strip()

            return None

        title = extract_title(post_soup)

        # Validação robusta de título (evita posts quebrados do Framer)
        if (
            not title
            or len(title.strip()) < 10
            or title.strip().lower() in ["ad rock blog", "blog", ""]
        ):
            print(f"⚠️ Post ignorado (título inválido): {url}")
            continue

        # Normaliza o título para evitar espaços estranhos
        title = " ".join(title.split())
        # Remove prefixo padrão do Framer (quando vem do <title>)
        title = title.replace("Ad Rock Digital Mkt - Blog - ", "")
        title = title.replace("Ad Rock Digital Mkt - Blog", "")
        title = title.strip()

        date_tag = post_soup.find("time")
        content_tag = (
            post_soup.find("article")
            or post_soup.select_one("main > div")
            or post_soup.find("main")
            or post_soup.find("div")
        )

        from email.utils import format_datetime
        from dateutil import parser as date_parser

        pub_date_raw = date_tag.get("datetime") if date_tag else ""
        if isinstance(pub_date_raw, str) and pub_date_raw.strip():
            try:
                parsed_date = date_parser.parse(pub_date_raw.strip())
                pub_date = parsed_date.strftime("%Y-%m-%d")
            except Exception as e:
                print(f"Erro ao analisar data: {e}")
                pub_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        else:
            pub_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        content = content_tag.decode_contents() if content_tag else ""

        short_desc_tag = post_soup.select_one('[data-framer-name="Short description"] p')
        if short_desc_tag and short_desc_tag.get_text(strip=True):
            description = short_desc_tag.get_text(strip=True)
        else:
            # fallback: meta description
            meta_desc = post_soup.find("meta", attrs={"name": "description"})
            if meta_desc and meta_desc.get("content"):
                description = meta_desc["content"].strip()
            else:
                description = ""

        image_url = extract_image(post_soup)
        if not image_url:
            print(f"⚠️ Post ignorado (sem imagem válida): {url}")
            continue

        posts.append({
            "title": title,
            "url": url,
            "date": pub_date,
            "description": description,
            "image": image_url
        })

    return posts