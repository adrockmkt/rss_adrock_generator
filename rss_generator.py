from datetime import datetime, timezone
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import os
from email.utils import format_datetime
import requests
from PIL import Image
from io import BytesIO

def generate_rss(posts):
    """
    Gera o feed RSS com base na lista de posts extraída do blog da Ad Rock.
    Cada item inclui título, link, data de publicação e descrição extraída do meta description da página.
    """
    rss = Element("rss", version="2.0", attrib={
        "xmlns:media": "http://search.yahoo.com/mrss/",
        "xmlns:atom": "http://www.w3.org/2005/Atom"
    })
    channel = SubElement(rss, "channel")

    SubElement(channel, "atom:link", {
        "href": "https://mobiledelivery.com.br/rss/adrock.xml",
        "rel": "self",
        "type": "application/rss+xml"
    })

    SubElement(channel, "title").text = "Ad Rock Blog"
    SubElement(channel, "link").text = "https://adrock.com.br/blog"
    SubElement(channel, "description").text = "Novidades, projetos e conteúdo técnico sobre marketing digital, SEO e IA."
    SubElement(channel, "language").text = "pt-br"

    os.makedirs("images", exist_ok=True)

    for post in posts[:20]:  # Limita a 20 itens no feed
        item = SubElement(channel, "item")
        SubElement(item, "title").text = post["title"]
        SubElement(item, "link").text = post["url"]
        pub_date_obj = datetime.strptime(post["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        SubElement(item, "pubDate").text = format_datetime(pub_date_obj)
        description = post.get("description")
        SubElement(item, "description").text = description if description and description.strip() else "Sem descrição"
        clean_image = post["image"].split("?")[0]
        SubElement(item, "media:content", url=clean_image, medium="image")

        # baixar e redimensionar a imagem
        resp = requests.get(clean_image)
        if resp.status_code == 200:
            img = Image.open(BytesIO(resp.content))
            max_width = 600
            w_percent = max_width / float(img.size[0])
            h_size = int(float(img.size[1]) * float(w_percent))
            img = img.resize((max_width, h_size))
            local_filename = os.path.basename(clean_image)
            local_path = os.path.join("images", local_filename)
            img.save(local_path, format="PNG", optimize=True)
            enclosure_url = f"https://mobiledelivery.com.br/rss_images/{local_filename}"
            mime = "image/png"
        else:
            enclosure_url = clean_image
            mime = "image/png"

        SubElement(item, "enclosure", url=enclosure_url, type=mime)

    xml_str = minidom.parseString(tostring(rss)).toprettyxml(indent="  ")
    os.makedirs("output", exist_ok=True)
    with open("output/adrock.xml", "w", encoding="utf-8") as f:
        f.write(xml_str)