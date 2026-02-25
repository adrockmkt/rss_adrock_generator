# Gerador de RSS para Blog em Framer (Ad Rock)

Este projeto gera um feed RSS no formato XML a partir dos posts públicos do blog da Ad Rock, desenvolvido em Framer. Cada item inclui título, link, data de publicação, descrição e imagem. Ideal para distribuir atualizações automaticamente em plataformas que consomem RSS.

O projeto também integra o protocolo **IndexNow**, notificando automaticamente mecanismos compatíveis (como Bing) sempre que novos posts são publicados. O envio ocorre logo após a geração do RSS, com controle de duplicidade via SQLite para evitar reenvios desnecessários.

Agora, o projeto também redimensiona e publica as imagens do feed RSS. As imagens redimensionadas são salvas na pasta `images/` do projeto e servidas publicamente via Nginx em `/rss_images/`. No feed, o elemento `<media:content>` mantém a URL original da imagem, enquanto o `<enclosure>` aponta para a versão redimensionada, garantindo melhor desempenho e compatibilidade.

O envio para o IndexNow utiliza apenas os parâmetros `host`, `key` e `urlList`, conforme especificação oficial do protocolo. A chave é validada via arquivo público hospedado em `https://adrock.com.br/adrock-indexnow-2026.txt`, servido por Cloudflare Worker. O endpoint pode retornar status 200 (processado imediatamente) ou 202 (aceito para processamento assíncrono), ambos considerados sucesso.

## 📦 Pré-requisitos

- Python 3.10 ou superior
- Dependências listadas no arquivo `requirements.txt`
- Pillow (biblioteca para manipulação de imagens)

## ⚙️ Como usar

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script principal:

   ```bash
   python main.py
   ```

3. O script irá:

   - Fazer scraping dos posts do blog
   - Gerar o arquivo `output/adrock.xml`
   - Redimensionar e salvar imagens em `images/`
   - (Em produção) Copiar o RSS para `/var/www/mobiledelivery.com.br/rss/adrock.xml`
   - Enviar automaticamente as URLs novas para o IndexNow
   - Registrar logs de envio e evitar reenvios duplicados via SQLite (`indexnow/logs.db`)

> ⚠️ Observação: Em ambiente local, o caminho `/var/www/...` pode não existir. A cópia final do RSS é relevante apenas no servidor de produção.

## 🚀 Publicação

O RSS é publicado automaticamente em:

```
https://mobiledelivery.com.br/rss/adrock.xml
```

## 🔔 Integração com IndexNow

O projeto utiliza o endpoint oficial:

```
https://api.indexnow.org/indexnow
```

A chave de verificação é publicada diretamente no domínio principal (requisito do protocolo):

```
https://indexnow.adrock.com.br/adrock-indexnow-2026.txt
```

O envio é feito automaticamente após a geração do RSS, com registro em `indexnow/logs.db` para controle de duplicidade e auditoria de status HTTP.

Arquivos locais não versionados:

- `images/`
- `output/`
- `indexnow/logs.db`
- `indexnow/key.txt`

## ✅ Validação

Valide o feed gerado utilizando:

👉 https://validator.w3.org/feed/

## 💡 Futuro

- Exibir estatísticas de consumo do feed no painel Looker Studio.

---

<!-- English Version -->

# RSS Feed Generator for Framer Blog (Ad Rock)

This project generates an RSS feed in XML format from public posts of the Ad Rock blog, built with Framer. Each item includes title, link, publish date, description, and image. Ideal for automatically distributing updates on platforms that consume RSS.

The project also integrates **IndexNow**, automatically notifying compatible search engines whenever new posts are published. A local SQLite database prevents duplicate submissions.

The project now also resizes and publishes images in the RSS feed. Resized images are saved in the project's `images/` folder and served publicly via Nginx at `/rss_images/`. In the feed, the `<media:content>` element retains the original image URL, while the `<enclosure>` points to the resized version, ensuring better performance and compatibility.

IndexNow submission uses only the `host`, `key`, and `urlList` parameters, following the official protocol specification. The verification key is validated through a public file hosted at `https://adrock.com.br/adrock-indexnow-2026.txt`, served via Cloudflare Worker. The endpoint may return status 200 (processed immediately) or 202 (accepted for asynchronous processing), both considered successful.

## 📦 Requirements

- Python 3.10 or higher
- Dependencies listed in `requirements.txt`
- Pillow (image processing library)

## ⚙️ How to Use

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

3. The script will:

   - Scrape blog posts
   - Generate `output/adrock.xml`
   - Resize and store images in `images/`
   - (In production) Copy the RSS to `/var/www/mobiledelivery.com.br/rss/adrock.xml`
   - Automatically notify IndexNow about new URLs
   - Log submission attempts and prevent duplicate resubmissions via SQLite (`indexnow/logs.db`)

> ⚠️ Note: The `/var/www/...` path is only relevant in the production server environment.

## 🚀 Deployment

The RSS feed is automatically published to:

```
https://mobiledelivery.com.br/rss/adrock.xml
```

## 🔔 IndexNow Integration

The project uses the official endpoint:

```
https://api.indexnow.org/indexnow
```

The verification key is published directly under the main domain (protocol requirement):

```
https://indexnow.adrock.com.br/adrock-indexnow-2026.txt
```

URLs are automatically submitted after RSS generation, with logging stored in `indexnow/logs.db` to prevent duplicate submissions and to keep HTTP status records.

Non-versioned local files:

- `images/`
- `output/`
- `indexnow/logs.db`
- `indexnow/key.txt`

## ✅ Validation

Validate the generated feed using:

👉 https://validator.w3.org/feed/

## 💡 Future

- Show feed consumption statistics in Looker Studio.

---

## 🧾 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja o arquivo [CONTRIBUTING.md](./CONTRIBUTING.md) para instruções.

---

## 🧭 Código de Conduta

Este projeto segue o [Código de Conduta](./CODE_OF_CONDUCT.md) para garantir um ambiente colaborativo saudável.

---

## 🔐 Segurança

Se você encontrar alguma vulnerabilidade, consulte o arquivo [SECURITY.md](./SECURITY.md) para saber como reportar de forma segura.

---

## 🌍 English Info

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.  
To contribute, read the [CONTRIBUTING.md](./CONTRIBUTING.md) guide.  
Please follow our [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) for respectful collaboration.  
For security concerns, check [SECURITY.md](./SECURITY.md).

# Ad Rock RSS Generator (Framer Blog)

Gerador de feed RSS (XML 2.0) para o blog da Ad Rock desenvolvido em Framer, com:

- Scraping estruturado dos posts
- Extração robusta de metadados (title, description, og:image, date)
- Redimensionamento e publicação de imagens
- Integração automática com IndexNow
- Controle de duplicidade via SQLite
- Deploy automatizado em ambiente Linux (cron)

O projeto foi estruturado para produção, evitando fallbacks artificiais como “Sem título” ou imagens padrão.

---

## 🧱 Arquitetura

Framer (Blog)  
↓  
`framer_scraper.py` – coleta estruturada  
↓  
`rss_generator.py` – formatação XML + otimização de imagem  
↓  
Publicação via Nginx  
↓  
IndexNow submission  

Feed publicado em:

```
https://mobiledelivery.com.br/rss/adrock.xml
```

---

## 📦 Requisitos

- Python 3.10+
- Linux (produção)
- Dependências em `requirements.txt`

Principais libs:

- requests
- beautifulsoup4
- pillow
- python-dateutil

---

## ⚙️ Execução

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar:

```bash
python main.py
```

O script:

- Faz scraping do blog
- Gera `output/adrock.xml`
- Redimensiona imagens em `images/`
- Copia o RSS para o diretório público do servidor
- Envia URLs novas para o IndexNow
- Registra envios em `indexnow/logs.db`

---

## 🖼️ Tratamento de Imagens

- `<media:content>` mantém a URL original (Framer CDN)
- `<enclosure>` aponta para a versão redimensionada (600px)
- Nenhuma imagem fallback é utilizada
- Apenas `og:image` válido é aceito

Imagens são servidas via:

```
/rss_images/
```

---

## 🔔 IndexNow

Endpoint oficial utilizado:

```
https://api.indexnow.org/indexnow
```

Parâmetros enviados:

- host
- key
- urlList

Chave validada via arquivo público:

```
https://indexnow.adrock.com.br/adrock-indexnow-2026.txt
```

Controle de duplicidade realizado via SQLite:

```
indexnow/logs.db
```

Status 200 e 202 são tratados como sucesso.

---

## 🚀 Produção

Deploy recomendado:

Local:
```bash
git push
```

Servidor:
```bash
git pull
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Execução automática via cron (root):

```bash
0 7 * * * /home/adrock/rss_adrock_generator/rodar_rss.sh >> /home/adrock/rss_adrock_generator/rss.log 2>&1
```

---

## 📁 Arquivos não versionados

- images/
- output/
- indexnow/logs.db
- indexnow/key.txt
- venv/

---

## ✅ Validação

Validação oficial:

👉 https://validator.w3.org/feed/

---

## 📌 Observações Técnicas

- Posts sem título são ignorados
- Não existem fallbacks “Sem título” ou “Sem descrição”
- Não há imagem padrão
- Metadados seguem prioridade: og → meta → estrutura HTML
- Timeout aplicado em requisições externas
- Compatível com agregadores RSS e motores de busca

---

## 📜 Licença

MIT License  
Consulte o arquivo LICENSE.