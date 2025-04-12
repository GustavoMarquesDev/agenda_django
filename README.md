# 📇 Lista de Contatos - Projeto Django

Este é um projeto de exemplo utilizando o framework **Django** para criação de uma aplicação web simples de gerenciamento de contatos. Através do painel administrativo nativo do Django, você pode cadastrar, editar, visualizar e excluir contatos com facilidade.

O projeto é ideal para fins educacionais, prática com o Django ou como base para projetos mais complexos.

## 🚀 Funcionalidades

- Autenticação via admin do Django  
- CRUD completo de contatos  
- Geração automática de contatos aleatórios para testes  
- Interface administrativa pronta para uso  
- Organização por categorias (opcional)

## 📦 Tecnologias Utilizadas

- Python 3.8+  
- Django 5.x  
- SQLite (banco de dados padrão)  
- Faker (para geração de dados fictícios)

📌 Requisitos

Python 3.8 ou superior
Django 5.x

## 🛠️ Como Executar o Projeto

Clone o repositório e entre no diretório do projeto:

```bash
git clone https://github.com/GustavoMarquesDev/agenda_django.git
cd agenda_django
```
### Crie um ambiente virtual 

- python -m venv venv
- source venv/bin/activate  # Linux/macOS ou
- venv\Scripts\activate  # Windows

### Instale as dependencias
-pip install -r requirements.txt

### Crie as migrações
-python manage.py migrate

### Crie seu superusuario
python manage.py createsuperuser

### *** Opcional: Para criar 1000 contatos utilizando o script ****
python utils/create_contacts.py

### Por fim inicialize o servidor com:
-python manage.py runserver




