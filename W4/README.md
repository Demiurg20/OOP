# User Management System

## 📌 About the Project

This project is an object-oriented Python application for managing user records

It demonstrates:
- Instance variables and methods
- Class attributes and class methods
- Static methods
- Dictionary-based storage
- Unit testing
- UML design

The system allows creating users, storing them, updating information, and validating user data such as passwords and emails

---

## 🧱 Project Structure


W4/
│
├── README.md
├── test_user_service.py
├── test_user_util.py
├── test_user.py
├── user_service.py
├── user_util.py
├── user.py
├── W4.drawio.png


---

## 👤 User Class

Represents a single user.

Attributes:
- user_id
- name
- surname
- email
- password
- birthday

Methods:
- get_details()
- get_age()

---

## 🗂 UserService Class

Manages all users using a class-level dictionary.

Class attribute:
- users (dictionary)

Class methods:
- add_user()
- find_user()
- delete_user()
- update_user()
- get_number()

Relationship:
UserService manages multiple User objects.

---

## 🛠 UserUtil Class

Provides utility functions using static methods.

Methods:
- generate_user_id()
- generate_password()
- is_strong_password()
- generate_email()
- validate_email()

UserService uses UserUtil for generating and validating user data.

---

## ▶ How to Run

To run tests:

```python -m unittest```

To run a single test file:

```python test_user.py```

---

## 🧪 Sample Run

Generated ID: 241234567
Generated password: Abc!12345
Email: john.doe@test.com

User added successfully.
Total users: 1



---

## 📊 UML Diagram

The UML diagram is included as:

W4.drawio.png

It shows:
- Three classes (User, UserService, UserUtil)
- One-to-many relationship (1 -------- * between UserService and User)
- Dependency relationship (UserService uses UserUtil)

---

## 👨‍💻 Author

Islambek Asylbekov