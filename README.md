# Basic Authentication API

## 1. Account List and Registration

### Endpoint: `/users/`

- **Request Type**: GET
- **Request Params**: None
- **Permissions**: Only Staff
- **Description**: List of all users

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
