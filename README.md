# Gerador de RSS para Blog em Framer (Ad Rock)

Este projeto gera um feed RSS no formato XML a partir dos posts públicos do blog da Ad Rock, desenvolvido em Framer. Cada item inclui título, link, data de publicação, descrição e imagem. Ideal para distribuir atualizações automaticamente em plataformas que consomem RSS.

## 📦 Pré-requisitos

- Python 3.10 ou superior
- Dependências listadas no arquivo `requirements.txt`

## ⚙️ Como usar

1. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script principal:

   ```bash
   python main.py
   ```

3. O arquivo RSS será gerado em:

   ```
   output/adrock.xml
   ```

## 🚀 Publicação

Após a geração, copie o arquivo `adrock.xml` para o servidor em:

```
https://mobiledelivery.com.br/rss/adrock.xml
```

## ✅ Validação

Valide o feed gerado utilizando:

👉 https://validator.w3.org/feed/

## 💡 Futuro (opcional)

- Automatizar a execução do script com um cron job no servidor.
- Exibir estatísticas de consumo do feed no painel Looker Studio.
- Enviar atualizações automaticamente para plataformas de distribuição (LinkedIn, Email, etc).

---

<!-- English Version -->

# RSS Feed Generator for Framer Blog (Ad Rock)

This project generates an RSS feed in XML format from public posts of the Ad Rock blog, built with Framer. Each item includes title, link, publish date, description, and image. Ideal for automatically distributing updates on platforms that consume RSS.

## 📦 Requirements

- Python 3.10 or higher
- Dependencies listed in `requirements.txt`

## ⚙️ How to Use

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

3. The RSS file will be generated at:

   ```
   output/adrock.xml
   ```

## 🚀 Deployment

After generation, copy the `adrock.xml` file to the server at:

```
https://mobiledelivery.com.br/rss/adrock.xml
```

## ✅ Validation

Validate the generated feed using:

👉 https://validator.w3.org/feed/


## 💡 Future (optional)

- Automate the script execution with a cron job on the server.
- Show feed consumption statistics in Looker Studio.
- Automatically distribute updates to platforms (LinkedIn, Email, etc).

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
