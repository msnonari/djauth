# Django Auth Project

This project is a Django-based authentication system designed for learning and rapid prototyping. It provides essential user management features including registration, login, logout, dashboard, and profile update. The project uses SQLite for the database and Bootstrap for the frontend, making it easy to set up and customize for your own needs.

## Features

- User registration with validation
- Login and logout
- Dashboard (protected view)
- Profile update
- Django messages for feedback
- Superuser access to Django admin

## Project Structure

```
djauth/
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   └── update_profile.html
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── djauth/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── .gitignore
```

## Setup Instructions

1. **Clone the repository**

   ```sh
   git clone https://github.com/msnonari/djauth.git
   cd djauth
   ```

2. **Create and activate a virtual environment**

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```sh
   pip install django
   ```

4. **Apply migrations**

   ```sh
   python manage.py migrate
   ```

5. **Run the development server**

   ```sh
   python manage.py runserver
   ```

6. **Access the app**
   - Home: [http://localhost:8000/](http://localhost:8000/)
   - Login: [http://localhost:8000/login/](http://localhost:8000/login/)
   - Register: [http://localhost:8000/register](http://localhost:8000/register)
   - Dashboard: [http://localhost:8000/dashboard/](http://localhost:8000/dashboard/)
   - Update Profile: [http://localhost:8000/update_profile](http://localhost:8000/update_profile)

## Django Admin

- Access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **Default superuser credentials:**
  - Username: `admin`
  - Password: `djauth123`

## Notes

- All sensitive files and folders (e.g., `.env`, `db.sqlite3`, `__pycache__`, etc.) are excluded from version control via `.gitignore`.
- You can create your own superuser with:
  ```sh
  python manage.py createsuperuser
  ```

## License

This project is licensed under the MIT License.
