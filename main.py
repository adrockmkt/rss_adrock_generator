from framer_scraper import get_blog_posts
from rss_generator import generate_rss
import os
from indexnow.sender import init_db, send_urls

if __name__ == "__main__":
    try:
        posts = get_blog_posts()
        if not posts:
            raise ValueError("Nenhum post foi encontrado no blog.")
        generate_rss(posts)
        # === IndexNow Integration (não interfere na geração do RSS) ===
        try:
            init_db()
            urls = [post.get("url") for post in posts if post.get("url")]
            if urls:
                print("URLs para IndexNow:", urls)
                send_urls(urls)
        except Exception as indexnow_error:
            print(f"⚠️ Erro ao enviar para IndexNow: {indexnow_error}")
        rss_output_path = "/var/www/mobiledelivery.com.br/rss/"
        if os.path.exists(rss_output_path):
            os.system("cp output/adrock.xml /var/www/mobiledelivery.com.br/rss/adrock.xml")
            print("📦 RSS copiado para o diretório do servidor.")
        else:
            print("ℹ️ Ambiente local detectado. Cópia para /var/www ignorada.")
        rss_path = "/var/www/mobiledelivery.com.br/rss/adrock.xml"
        print(f"✅ RSS gerado com sucesso e disponível em: https://mobiledelivery.com.br/rss/adrock.xml")
    except Exception as e:
        print(f"❌ Erro ao gerar RSS: {e}")