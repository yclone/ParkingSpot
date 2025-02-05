# Sistema de Gerenciamento de Estacionamento

## Descrição
Sistema desenvolvido para gerenciar vagas de estacionamento em condomínios, permitindo o controle de veículos, moradores e suas respectivas vagas.

## Funcionalidades

### Usuários
- Cadastro de usuários
- Autenticação (login/logout)
- Atualização de dados do usuário
- Visualização de perfil

### Estacionamento
- Cadastro de vagas
- Associação de veículos a vagas
- Vinculação com apartamentos e blocos
- Controle de placas de veículos

## Tecnologias Utilizadas
- Python
- Flask (Framework Web)
- SQLAlchemy (ORM)
- Flask-SQLAlchemy
- Werkzeug (Segurança)

## Estrutura do Projeto
```
app/
├── src/
│   ├── models/
│   │   ├── user.py         # Modelo de usuário
│   │   └── parking.py      # Modelo de vagas de estacionamento
│   ├── routes/
│   │   └── user_routes.py  # Rotas para gerenciamento de usuários
│   └── services/
│       └── parking_service.py  # Serviços de estacionamento
```

## Configuração

### Pré-requisitos
- Python 3.x
- pip (gerenciador de pacotes Python)

### Instalação
1. Clone o repositório
```bash
git clone [url-do-repositorio]
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente
```bash
export FLASK_APP=app
export FLASK_ENV=development
```

### Execução
```bash
flask run
```

## APIs Disponíveis

### Usuários
- `POST /register_user` - Cadastro de novo usuário
- `POST /login` - Autenticação de usuário
- `GET /users` - Lista todos os usuários
- `GET /user/<id>` - Obtém dados de um usuário específico
- `PUT /user/<id>` - Atualiza dados do usuário
- `POST /logout` - Finaliza sessão do usuário

### Estacionamento
- Cadastro de vaga de estacionamento (via serviço)

## Segurança
- Senhas criptografadas usando Werkzeug
- Sessões de usuário
- Validações de dados

## Manutenção
Inclui script de limpeza (`cleanup.py`) para remover arquivos temporários e caches.

## Autor
Vinicius Marra Santos

## Licença
Free