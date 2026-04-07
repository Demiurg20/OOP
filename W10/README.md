# Employee Database (SQLite CRUD Application)

## 📌 About the Project

This project is a simple Python application that manages employee data using a SQLite database.

The program allows you to:
- Add new employees
- View employee information
- Update employee data
- Delete employees

This project demonstrates basic database operations (CRUD) and Object-Oriented Programming (OOP).

---

## 🧱 Project Structure
Employee-Database/
│
├── employee.py
├── employee_dao.py
├── main.py
├── employee_db.db
├── README.md
└── screenshots/Employee-Database/
│
├── employee.py
├── employee_dao.py
├── main.py
├── employee_db.db
├── README.md
└── screenshots/

---

## 🧠 Classes Used

### 1. Employee Class

This class represents an employee.

Attributes:
- id
- name
- position
- salary
- hire_date

It is used to store employee data.

---

### 2. EmployeeDAO Class

This class handles all database operations.

Main methods:
- insert(employee) → adds a new employee
- get_by_id(id) → gets employee by ID
- get_all() → gets all employees
- update(employee) → updates employee data
- delete(id) → deletes employee

---

## 💾 Database

The application uses SQLite.

# Database name:

employee_db.db

# table name:

employee


Columns:
- id (primary key)
- name
- position
- salary
- hire_date

---

## ▶ How to Run

1. Make sure Python 3 is installed

2. Run the program:

# python main.py


3. The database file will be created automatically.

---

## 📊 Sample Output

Example:

Employee inserted.

Get by ID:
ID: 1, Name: John Doe, Position: Developer, Salary: 5000, Hire Date: 2024-01-01

All Employees:
ID: 1, Name: John Doe, Position: Developer, Salary: 5000, Hire Date: 2024-01-01

Employee updated.
Employee deleted.


---

## 📸 Screenshots

Screenshots are included in the `screenshots` folder:

- Table structure in SQLite
- Program output in console

---

## 👤 Author

Islambek Asylbekov