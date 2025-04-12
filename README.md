Iniciar o projeto Django

```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

```
Opcional: Criar 1000 contatos aleatórios para popular o projeto

python utils/create_contacts.py
```

Configurar o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

```
