# Gerador de RSS para Blog em Framer (Ad Rock)

Este projeto gera um feed RSS no formato XML a partir dos posts públicos do blog da Ad Rock, desenvolvido em Framer. Cada item inclui título, link, data de publicação, descrição e imagem. Ideal para distribuir atualizações automaticamente em plataformas que consomem RSS.

Agora, o projeto também redimensiona e publica as imagens do feed RSS. As imagens redimensionadas são salvas na pasta `images/` do projeto e servidas publicamente via Nginx em `/rss_images/`. No feed, o elemento `<media:content>` mantém a URL original da imagem, enquanto o `<enclosure>` aponta para a versão redimensionada, garantindo melhor desempenho e compatibilidade.

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

3. O arquivo RSS será gerado automaticamente em:

   ```
   /var/www/mobiledelivery.com.br/rss/adrock.xml
   ```

   Além disso, as imagens redimensionadas serão salvas na pasta `images/` do projeto e disponibilizadas publicamente via Nginx em `/rss_images/`.

## 🚀 Publicação

O RSS é publicado automaticamente em:

```
https://mobiledelivery.com.br/rss/adrock.xml
```

## ✅ Validação

Valide o feed gerado utilizando:

👉 https://validator.w3.org/feed/

## 💡 Futuro

- Exibir estatísticas de consumo do feed no painel Looker Studio.

---

<!-- English Version -->

# RSS Feed Generator for Framer Blog (Ad Rock)

This project generates an RSS feed in XML format from public posts of the Ad Rock blog, built with Framer. Each item includes title, link, publish date, description, and image. Ideal for automatically distributing updates on platforms that consume RSS.

The project now also resizes and publishes images in the RSS feed. Resized images are saved in the project's `images/` folder and served publicly via Nginx at `/rss_images/`. In the feed, the `<media:content>` element retains the original image URL, while the `<enclosure>` points to the resized version, ensuring better performance and compatibility.

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

3. The RSS file will be automatically generated at:

   ```
   /var/www/mobiledelivery.com.br/rss/adrock.xml
   ```

   Additionally, resized images will be saved in the project's `images/` folder and made publicly available via Nginx at `/rss_images/`.

## 🚀 Deployment

The RSS feed is automatically published to:

```
https://mobiledelivery.com.br/rss/adrock.xml
```

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
