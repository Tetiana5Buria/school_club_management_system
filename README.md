🎓 Student & Club Management

This project was created for learning Django 6+.
It is a simple but practical web application for managing students and their enrollments in clubs.

The project includes 3 main apps:

Students — manage student data
Clubs — manage clubs
Enrollments — connect students with clubs
🇬🇧 English
📌 Description

A basic Django project with authentication and multi-user support.
Each user works only with their own data.

⚙️ Features
User registration & login
Create / update / delete students
Create clubs
Enroll students into clubs
Data isolation per user
Validation (unique student ID)
🇺🇦 Українська
📌 Опис

Навчальний Django-проєкт з авторизацією та підтримкою кількох користувачів.
Кожен користувач працює тільки зі своїми даними.

⚙️ Функціонал
Реєстрація та логін
Додавання / редагування / видалення учнів
Створення гуртків
Запис учнів у гуртки
Ізоляція даних
Валідація (унікальний ІПН)
🛠 Tech Stack
Python 3.14
Django 6.x
SQLite3
📦 Installation
git clone https://github.com/Tetiana5Buria/python_project.git
cd python_project

# create virtual environment

python -m venv venv

# activate

venv\Scripts\activate # Windows

# source venv/bin/activate # Mac/Linux

# install dependencies

pip install -r requirements.txt
🚀 Run project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

Admin panel:
http://127.0.0.1:8000/admin

🔐 Demo (optional)

If deployed:

site: https://school-club-management-system.onrender.com

```

```
