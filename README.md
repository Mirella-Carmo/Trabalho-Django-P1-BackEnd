# Como executar o projeto com Docker

## 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta:

```bash
cd Trabalho-Django-P1-BackEnd
```

---

## 2. Crie o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta

DEBUG=True

DB_NAME=sgta
DB_USER=sgta_user
DB_PASSWORD=sgta_password
DB_HOST=db
DB_PORT=5432
```

---

## 3. Suba os containers

```bash
docker compose up -d
```

Esse comando irá:

* baixar a imagem da aplicação
* baixar a imagem do PostgreSQL
* criar os containers
* executar migrations automaticamente
* iniciar a API

---

## 4. Verifique se tudo está rodando

```bash
docker compose ps
```

Os containers devem aparecer com status:

```text
Up
Healthy
```

---

## 5. Criar usuário administrador

Execute:

```bash
docker compose exec web python manage.py createsuperuser
```

Preencha:

```text
Username:
Email:
Password:
```

---

## 6. Acessar aplicação

API:

```text
http://localhost:8000/pedidos/
```

Admin:

```text
http://localhost:8000/admin/
```

---

## 7. Comandos úteis

Ver logs:

```bash
docker compose logs -f
```

Parar containers:

```bash
docker compose down
```

Subir novamente:

```bash
docker compose up -d
```