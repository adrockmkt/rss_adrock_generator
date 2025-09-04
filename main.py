from framer_scraper import get_blog_posts
from rss_generator import generate_rss
import os

if __name__ == "__main__":
    try:
        posts = get_blog_posts()
        if not posts:
            raise ValueError("Nenhum post foi encontrado no blog.")
        generate_rss(posts)
        os.system("cp output/adrock.xml /var/www/mobiledelivery.com.br/rss/adrock.xml")
        rss_path = "/var/www/mobiledelivery.com.br/rss/adrock.xml"
        print(f"✅ RSS gerado com sucesso e disponível em: https://mobiledelivery.com.br/rss/adrock.xml")
    except Exception as e:
        print(f"❌ Erro ao gerar RSS: {e}")