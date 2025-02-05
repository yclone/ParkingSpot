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


## Configuração e Execução Local

### Ambiente Virtual
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto:

1. Criar ambiente virtual:
```bash
# Windows
python -m venv venv

# Linux/MacOS
python3 -m venv venv
```

2. Ativar ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/MacOS
source venv/bin/activate
```

### Instalação
1. Clone o repositório
```bash
git clone [url-do-repositorio]
cd [nome-do-diretorio]
```

2. Ative o ambiente virtual (conforme instruções acima)

3. Instale as dependências
```bash
pip install -r requirements.txt
```

### Execução Local
1. Inicialize o banco de dados:
```bash
# Navegar ate a pasta app do projeto
cd ../TR-AI/app
```

2. Execute o servidor de desenvolvimento:
```bash
python src/app.py
```

O aplicativo estará disponível em `http://localhost:5000`

### Testes

1. Instalação das dependências de teste:
```bash
pip install pytest pytest-cov
```

2. Executar todos os testes:
```bash
pytest
```

3. Executar testes com cobertura:
```bash
pytest --cov=src tests/
```

4. Para ver o relatório de cobertura detalhado:
```bash
pytest --cov=src tests/ --cov-report=html
```
O relatório será gerado na pasta `htmlcov/`

### Desativando o Ambiente Virtual
Quando terminar de trabalhar no projeto:
```bash
deactivate
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