import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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

        from datetime import datetime

        title = title_tag.text.strip() if title_tag else "Sem título"
        pub_date_raw = date_tag.get("datetime") if date_tag else ""
        if isinstance(pub_date_raw, str) and pub_date_raw.strip():
            pub_date = pub_date_raw.strip()
        else:
            pub_date = datetime.utcnow().isoformat()
        content = content_tag.decode_contents() if content_tag else ""

        short_desc_tag = post_soup.select_one('[data-framer-name="Short description"] p')
        description = short_desc_tag.get_text(strip=True) if short_desc_tag else "Sem descrição"

        # tenta pegar a imagem principal
        img_tag = post_soup.select_one("img[src*='/blog/imagens/']")
        if img_tag and img_tag.get("src"):
            image_url = urljoin(BASE_URL, img_tag["src"])
        else:
            image_url = f"{BASE_URL}/blog/imagens/{url.split('/')[-1]}.jpg"

        posts.append({
            "title": title,
            "url": url,
            "date": pub_date,
            "description": description,
            "image": image_url
        })

    return posts