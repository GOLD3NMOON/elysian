# Elysian - Discord Application

[Elysian banner](https://i.imgur.com/oT5YfKP.jpg)

## 📜 Sobre

**Elysian** é um aplicativo para o Discord, projetado para atuar como um personagem em uma comunidade na [plataforma Discord](). Ele oferece uma estrutura modular que facilita a expansão com novos comandos e listeners, sendo ideal para personalizações.

## 🚀 Funcionalidades

- **Modularidade**: Estrutura organizada para adicionar comandos e eventos facilmente.
- **Configuração Simples**: Utiliza variáveis de ambiente e arquivos `.env` para simplificar a configuração.
- **Personalizável**: Perfeito para adicionar funcionalidades específicas ao seu servidor.

## 🛠️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/GOLD3NMOON/elysian.git
   cd elysian
   ```

2. (Opcional) Crie um ambiente virtual Python:
   - [Tutorial: Criando um Ambiente Virtual no Python](https://cienciaprogramada.com.br/2020/08/ambiente-virtual-projeto-python/)

   ```bash
   python3 -m venv .venv
   ```
   Substitua `.venv` pelo nome que preferir para o ambiente virtual.

3. Ative o ambiente virtual:
   - [Tutorial: Ativando Ambientes Virtuais em Diferentes Sistemas](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)

   ```bash
   source .venv/bin/activate  # Para Linux/Mac
   .venv\Scripts\activate     # Para Windows
   ```

   **Nota**: Use o nome que você definiu no passo anterior.

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure o arquivo `.env` com o token do seu aplicativo do Discord:
   ```
   APP_TOKEN=seu-token-aqui
   ```

6. Inicie o aplicativo:
   ```bash
   python3 main.py
   ```

## 📂 Estrutura do Projeto

```plaintext
elysian/
├── src/
│   ├── app/
│   │   ├── events/             # Listeners do aplicativo
│   │   ├── commands/           # Comandos do aplicativo
│   ├── settings/               # Configurações e constantes
│   ├── core/                   # Lógica principal e arquivos essenciais
├── .env                        # Variáveis de ambiente
├── main.py                     # Arquivo principal do aplicativo
└── README.md                   # Documentação
```

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar *pull requests* ou abrir *issues* com sugestões de melhorias.

---

Feito com ❤️ por [gold3nmoon](https://github.com/gold3nmoon)
