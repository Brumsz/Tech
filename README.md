# 🔐 Tech — Autenticação com OAuth 2.0

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![OAuth](https://img.shields.io/badge/OAuth-2.0-EB5424)

Projeto Django que demonstra autenticação social com **GitHub** usando **django-allauth**. A página inicial permite fazer login com a conta do GitHub, e uma área de membros fica disponível apenas para usuários autenticados.

> 🧪 Projeto de demonstração, criado para mostrar a integração de login social via OAuth 2.0. A área de membros tem conteúdo ilustrativo.

## ✨ Funcionalidades

- Login e cadastro com conta do GitHub (OAuth 2.0)
- Área de membros protegida por login
- Logout
- Interface em português (pt-BR) e fuso horário de São Paulo

## 🛠️ Tecnologias

- Python · Django · django-allauth · HTML · CSS

## 📁 Estrutura do projeto

```
Tech/
├── setup/            # Configurações do projeto (settings, urls)
├── tech/             # App principal (views e urls das páginas)
├── templates/
│   ├── index.html    # Página inicial com login pelo GitHub
│   ├── members.html  # Área de membros
│   └── static/       # CSS e imagens
├── config.py         # Lê as credenciais do OAuth do arquivo .env
└── requirements.txt
```

## 🚀 Como instalar e rodar

**1. Clone o repositório**
```bash
git clone https://github.com/Brumsz/Tech.git
cd Tech
```

**2. Crie um OAuth App no GitHub**

Acesse **Settings → Developer settings → OAuth Apps → New OAuth App** e preencha:

- **Homepage URL:** `http://localhost:8000`
- **Authorization callback URL:** `http://localhost:8000/accounts/github/login/callback/`

Copie o **Client ID** e gere um **Client Secret**.

**3. Crie o arquivo `.env` na raiz do projeto**
```env
CLIENT_ID=seu_client_id
SECRET=seu_client_secret
```

**4. Crie e ative um ambiente virtual**
```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

**5. Instale as dependências**
```bash
pip install -r requirements.txt
```

**6. Aplique as migrações**
```bash
python manage.py migrate
```

**7. Configure o site no Django Admin**

Crie um superusuário, rode o servidor e acesse `http://localhost:8000/admin`. Em **Sites**, edite o site padrão para o domínio `localhost:8000`. Esse passo é necessário para o allauth gerar o callback corretamente.

```bash
python manage.py createsuperuser
python manage.py runserver
```

**8. Teste**

Acesse `http://localhost:8000`, clique em **GitHub** e autorize a aplicação. Após o login, você será redirecionado para a área de membros.

---

Desenvolvido por [João](https://github.com/Brumsz)
