# Validação de Pedidos

Projeto em **Python** para validação automática de pedidos atrasados, com envio de **notificação por e-mail ao setor de transporte**.

## 📌 Descrição

Este projeto realiza a leitura de pedidos a partir de um banco de dados, identifica quais estão fora do prazo e envia automaticamente um e-mail de alerta para o transporte responsável.  
O objetivo é **automatizar o controle de atrasos**, reduzindo falhas manuais e melhorando a comunicação entre áreas.

## 🚀 Funcionalidades

- Conexão com banco de dados de pedidos
- Identificação de pedidos atrasados
- Envio automático de e-mails de notificação
- Código simples e fácil de adaptar para outros cenários

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas padrão do Python
- Biblioteca para envio de e-mail (`smtplib`, `email`)
- Banco de dados (ex.: SQLite ou similar)

## 📂 Estrutura do Projeto

validacao-de-pedidos/
```bash
│── database/ # Arquivos ou scripts relacionados ao banco de dados
│── project/ # Código principal do projeto
│ └── main.py # Script principal
│── .gitignore
│── README.md
│── requirements.txt
```


## ⚙️ Pré-requisitos

- Python 3 instalado
- Acesso ao banco de dados utilizado
- Credenciais de e-mail para envio das notificações

## ▶️ Como Executar
1. Clone o Repositório
```bash
   git clone https://github.com/guimalicki/validacao-de-pedidos.git
   cd validacao-de-pedidos
```
2. (Opcional) Crie um ambiente virtual:
```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows
```
3. Instale as dependências:
```bash
   pip install -r requirements.txt
```
4. Configure as credenciais de banco de dados e e-mail no código.
5. Execute o projeto:
```bash
   python project/main.py
```

## 📬 Envio de E-mail

- Para o envio de e-mails, configure corretamente:

- Servidor SMTP

- Porta

- Usuário e senha

- Destinatários do alerta

### ⚠️ Recomenda-se usar variáveis de ambiente para proteger informações sensíveis.

## 🧪 Testes

Sugestões de testes:

- Validação da leitura do banco de dados

- Testes da lógica de atraso

- Mock do envio de e-mail

## 🤝 Contribuição

Contribuições são bem-vindas!

- Faça um fork do projeto

- Crie uma branch (git checkout -b feature/nova-feature)

- Commit (git commit -m "Descrição da alteração")

- Push (git push origin feature/nova-feature)

- Abra um Pull Request

## 📄 Licença

Este projeto ainda não possui licença definida.
Sinta-se livre para adicionar uma (MIT, GPL, etc.).

## 👤 Autor

Desenvolvido por **Guilherme Malicki Barbosa**


🔗 https://github.com/guimalicki

