# Записи учнів в секції

Сучасний **Django-сайт** для управління учнями та їх записами в різні клуби.
Проєкт демонструє чисту архітектуру, адаптивний дизайн та ефекти **Glassmorphism** з анімованим градієнтом.

---

## Особливості

- Додавання, редагування та видалення учнів
- Створення записів учнів у клуби
- Ефект матового скла (**Glassmorphism**)
- Авторизація користувачів (логін + реєстрація)

---

## 🛠 Технології

- **Backend:** [Django 6.0](https://www.djangoproject.com/)
- **Frontend:** HTML, CSS
- **Database:** SQLite3 (локально)
- **Deployment:** [Render.com](https://render.com/)
- **Стилі:** Glassmorphism + сучасний градієнт

---

## Локальний запуск

1. Клонуй репозиторій:

```bash
git clone https://github.com/Tetiana5Buria/python_project.git
cd python_project
Створи та активуй віртуальне середовище:
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Встанови залежності:
pip install -r requirements.txt
Виконай міграції:
python manage.py migrate
Створи суперюзера для доступу до адмін-панелі:
python manage.py createsuperuser
Запусти локальний сервер:
python manage.py runserver
Відкрий у браузері: http://127.0.0.1:8000/

Адмінка доступна за http://127.0.0.1:8000/admin
```
