# 📚 API de Reserva de Salas

Este repositório contém a **API de Reserva de Salas**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Reserva de Salas é um **microsserviço** que faz parte de um sistema maior de [Gerenciamento de Escola](https://github.com/viniciuscassapian/Projeto-Flask.git)
, sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ **Esta API depende de outra API de Gerenciamento Escolar (Projeto-Flask)**, que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se a **Turma** existe (`GET /turmas/<id>`)
- (Opcional) Se o **Aluno** existe (`GET /alunos/<id>`) – pode ser desativado se não usado.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (como banco de dados local)
- Requests (para consumo da API externa)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/reserva-salas.git](https://github.com/viniciuscassapian/Reserva-de-Sala.git
cd reserva-salas
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:5001`(necessário colocar "/reservas" após "http://localhost:5001" na barra de navegação)

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

- `GET /reservas` – Lista todas as reservas
- `POST /reservas` – Cria uma nova reserva
- `GET /reservas/<id>` – Detalha uma reserva
- `PUT /reservas/<id>` – Atualiza uma reserva
- `DELETE /reservas/<id>` – Remove uma reserva

### Exemplo de corpo JSON para criação:

```json
{
  "turma_id": 1,
  "sala": "101",
  "data": "2025-05-06T14:00:00"
}
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando em:

```
http://localhost:5000
```

E que os endpoints de `GET /turmas/<id>` (e opcionalmente `GET /alunos/<id>`) estejam funcionando corretamente para que a validação seja feita com sucesso.

---

## 📦 Estrutura do Projeto

```
Reserva-de-salas-flask/
├── controller/
│   └── reserva_controller.py     
├── instance/
│   └── reservas.db              
├── models/
│   └── reserva_model.py          
├── app.py                        
├── config.py                     
├── database.py                   
├── dockerfile                    
├── reserva_route.py              
└── readme.md                     

```

---

## 🛠️ Futuras Melhorias

🔐 Autenticação e Autorização
Implementar login de usuários e permissões para restringir quem pode criar, visualizar ou excluir reservas.

🕐 Validação de Conflitos de Horário
Impedir que duas reservas sejam feitas para a mesma sala no mesmo horário.

🗓️ Filtro por Data e Sala
Adicionar parâmetros de busca para consultar reservas por data ou sala.
---

## 🧑‍💻 Autores

Vinicius Cassapian
Beatriz Alves
Janaina Figueiredo
