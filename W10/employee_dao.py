import sqlite3
from employee import Employee


class EmployeeDAO:

    def __init__(self):
        self.conn = sqlite3.connect("employee_db.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            position TEXT,
            salary REAL,
            hire_date TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert(self, employee: Employee):
        query = "INSERT INTO employee (name, position, salary, hire_date) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()
        print("Employee inserted.")

    def get_by_id(self, id: int):
        cursor = self.conn.execute("SELECT * FROM employee WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            return Employee(*row)
        return None

    def get_all(self):
        cursor = self.conn.execute("SELECT * FROM employee")
        return [Employee(*row) for row in cursor]

    def update(self, employee: Employee):
        query = """
        UPDATE employee
        SET name=?, position=?, salary=?, hire_date=?
        WHERE id=?
        """
        self.conn.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()
        print("Employee updated.")

    def delete(self, id: int):
        self.conn.execute("DELETE FROM employee WHERE id=?", (id,))
        self.conn.commit()
        print("Employee deleted.")