from framer_scraper import get_blog_posts
from rss_generator import generate_rss
import os

if __name__ == "__main__":
    try:
        posts = get_blog_posts()
        if not posts:
            raise ValueError("Nenhum post foi encontrado no blog.")
        generate_rss(posts)
        rss_path = os.path.abspath("output/adrock.xml")
        print(f"✅ RSS gerado com sucesso: {rss_path}")
    except Exception as e:
        print(f"❌ Erro ao gerar RSS: {e}")