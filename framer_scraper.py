import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime, timezone

BASE_URL = "https://adrock.com.br"

def get_blog_posts():
    response = requests.get(f"{BASE_URL}/blog")
    response.encoding = 'utf-8'  # força utf-8
    soup = BeautifulSoup(response.text, "html.parser")

    seen = set()
    post_links = []

    for a_tag in soup.select("a.framer-bGNrD[href*='/blog/']"):
        href = a_tag["href"]
        title_element = a_tag.select_one(".framer-jha8re p")
        if title_element and href != "/blog" and href not in seen:
            full_url = urljoin(BASE_URL, href)
            seen.add(href)
            post_links.append(full_url)
            print(f"🔗 Post encontrado: {full_url}")

    posts = []

    for url in post_links:
        post_resp = requests.get(url)
        post_resp.encoding = 'utf-8'  # força utf-8
        post_soup = BeautifulSoup(post_resp.text, "html.parser")

        title_tag = post_soup.find("h1")
        date_tag = post_soup.find("time")
        content_tag = (
            post_soup.find("article")
            or post_soup.select_one("main > div")
            or post_soup.find("main")
            or post_soup.find("div")
        )

        from email.utils import format_datetime
        from dateutil import parser as date_parser

        title = title_tag.text.strip() if title_tag else "Sem título"
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
        description = short_desc_tag.get_text(strip=True) if short_desc_tag else "Sem descrição"

        og_image_tag = post_soup.find("meta", property="og:image")
        if og_image_tag and og_image_tag.get("content"):
            image_url = og_image_tag["content"]
        else:
            # fallback: primeira imagem do conteúdo do artigo
            img_tag = post_soup.select_one("article img")
            if img_tag and img_tag.get("src"):
                image_url = img_tag["src"]
            else:
                image_url = ""

        posts.append({
            "title": title,
            "url": url,
            "date": pub_date,
            "description": description,
            "image": image_url
        })

    return posts