# Notas

Sistema web para calcular notas de prova. Exemplo simples com Django e VueJS.

## Este projeto foi feito com:

* Python 3.8.2
* Django 2.2.12
* VueJS 2.6.11

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/notas.git
cd notas/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Rodando o frontend

Abra uma outra aba no terminal e vá para a pasta `frontend`.

Então digite

```
npm install
npm run serve
```

## Usando o PostgreSQL

Instalando o PostgreSQL no Linux.

```
sudo apt update
sudo apt --fix-broken install
sudo apt install -y postgresql-client postgresql
```

#### Criando um banco rapidamente

```
sudo su - postgres

psql

 CREATE ROLE myuser ENCRYPTED PASSWORD 'mypass' LOGIN;

CREATE DATABASE mydb OWNER myuser;

\q  # sair
```

Leia mais em https://gist.github.com/rg3915/f63d9a37ca6bd5c0c7ecd4a907bd681f

E https://github.com/juliano777/pgsql_fs2w/blob/master/postgresql_sql_basico.pdf

#### Editando o settings.py

```
# default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
# DATABASES = {
#     'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Antes de versionar seu código faça:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', 'localhost'),
        'PORT': '5432',
    }
}
```

Acrescente essas informações no arquivo `.env`.

```
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypass
DB_HOST=localhost  # ou postgres://oyijbrec:uyoitunrb@ec2-xx-xx-xx-xxx.compute-1.amazonaws.com:5432/gynfyuhiygnfybrvc
```


#### Instalando mais dependências

```
pip install psycopg2-binary
pip freeze > requirements.txt
```

#### Migrações

Por fim, rode o migrate novamente.

```
python manage.py migrate
```

Se quiser, crie um super usuário.

```
python manage.py createsuperuser --username="admin"
```