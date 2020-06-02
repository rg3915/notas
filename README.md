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