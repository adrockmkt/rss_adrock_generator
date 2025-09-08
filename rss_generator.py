from datetime import datetime, timezone
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import os
from email.utils import format_datetime

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

    xml_str = minidom.parseString(tostring(rss)).toprettyxml(indent="  ")
    os.makedirs("output", exist_ok=True)
    with open("output/adrock.xml", "w", encoding="utf-8") as f:
        f.write(xml_str)