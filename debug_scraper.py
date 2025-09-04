import requests
from bs4 import BeautifulSoup

url = "https://adrock.com.br/blog"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("👀 Verificando estrutura de títulos:")
for tag in soup.find_all(["h1", "h2", "h3", "a", "time"]):
    print(f"{tag.name}: {tag.text.strip()} | href={tag.get('href')} | datetime={tag.get('datetime')}")

print("\n🔍 Buscando containers com possíveis títulos de posts (exibindo HTML bruto):\n")
print("➡️ Buscando links com seletor: a.framer-bGNrD")
for a in soup.select("a.framer-bGNrD"):
    print(f"Título (limpo): {a.get_text(strip=True)}")
    print(f"Link: {a.get('href')}")
    print("-" * 60)

# Novo bloco para inspecionar descrições curtas nos cards
print("➡️ Buscando descrições curtas (Short Description) nos cards:")
for card in soup.select("a.framer-bGNrD"):
    desc_tag = card.find("p")
    if desc_tag:
        print(f"Descrição curta: {desc_tag.get_text(strip=True)}")
    else:
        print("❌ Nenhuma descrição encontrada nesse card")
for container in soup.find_all(["article", "section", "div"]):
    if container.find("h2") and container.find("a"):
        print(container.prettify())
        print("=" * 80)

print("\n🧩 Análise detalhada dos containers dos cards (HTML simplificado):\n")
for card in soup.select("a.framer-bGNrD"):
    print("=" * 80)
    print(card.prettify())
    print("=" * 80)