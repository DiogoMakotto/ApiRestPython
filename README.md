# API REST Python com Selenium

Esta é uma aplicação simples em Python utilizando Flask para criar uma API RESTful que se integra a um banco de dados MySQL e também oferece funcionalidade de automação de navegação web com Selenium.

## Requisitos

- Python 3.x
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- mysqlclient
- Selenium
- ChromeDriver (automagicamente instalado pelo WebDriver Manager)

## Instalação

1. Clone o repositório:

```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
```

2.Crie e ative um ambiente virtual (opcional, mas recomendado):
  
```bash
    python -m venv venv
        # No Windows
    venv\Scripts\activate
        # No Linux/Mac
    source venv/bin/activate
```

3.Instale as dependências:

```bash
    pip install -r requirements.txt
```

## Endpoints

### Usuários

#### `GET /user/<int:user_id>`

Obtém informações de um usuário pelo ID.

#### `POST /user`

Cria um novo usuário. Envie dados JSON no corpo da requisição com campos `name` e `email`.

Exemplo de requisição:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```
# ApiRestPython
