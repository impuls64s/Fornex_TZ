# Basic Authentication API
## Установка

Чтобы установить и запустить проект, выполните следующие команды:

1. Клонируйте репозиторий:
    ```sh
    git clone git@github.com:impuls64s/Fornex_TZ.git
    ```

2. Перейдите в директорию проекта:
    ```sh
    cd Fornex_TZ
    ```

3. Создайте виртуальное окружение:
    ```sh
    python3 -m venv .venv
    ```

4. Активируйте виртуальное окружение:
    ```sh
    source .venv/bin/activate
    ```

5. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

6. Создайте миграции для базы данных:
    ```sh
    python manage.py makemigrations
    ```

7. Примените миграции:
    ```sh
    python manage.py migrate
    ```

8. Создайте суперпользователя:
    ```sh
    python manage.py createsuperuser
    ```

9. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

## 1. Account List and Registration

### Endpoint: `/users/`

- **Request Type**: GET
- **Request Params**: None
- **Permissions**: Only Staff
- **Description**: List of all users
- **Non-mandatory params** : is_verified, username

---

- **Request Type**: POST
- **Request Params**:
    ```json
    {
      "username": "",
      "first_name": "",
      "last_name": "",
      "email": "",
      "password": "",
      "password2": ""
    }
    ```
- **Permissions**: Any User
- **Description**: New user registration

## 2. CRUD Account

### Endpoint: `/users/<id>/`

- **Request Type**: GET
- **Request Params**: None
- **Permissions**: Only Staff
- **Description**: Detailed user information

---

- **Request Type**: PATCH
- **Request Params**: Only required fields.
- **Permissions**: Only Staff
- **Description**: User data change. Only a verified user can change the "balance". Field "username" cannot be edited.

---

- **Request Type**: DELETE
- **Request Params**: ...
- **Permissions**: Only Staff
- **Description**: Delete user

### Account model example
```json
{
    "id": 2,
    "password": "pbkdf2_sha256$720000$5kb07YyyQMwdmsCG7dDNvu$h1JsZSR7aMg1NbZdzyAY/Mo0kGpAkjVZVI9MH5cogto=",
    "last_login": null,
    "is_superuser": false,
    "username": "imp64",
    "first_name": "Oleg",
    "last_name": "Dev",
    "email": "impuls_64@mail.ru",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2024-07-17T22:23:51.457152Z",
    "country": "",
    "city": "",
    "balance": 0.0,
    "is_verified": false,
    "groups": [],
    "user_permissions": []
}
```
