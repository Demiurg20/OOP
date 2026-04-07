from employee import Employee
from employee_dao import EmployeeDAO


def main():
    dao = EmployeeDAO()

    # CREATE
    emp = Employee(name="John Doe", position="Developer", salary=5000, hire_date="2024-01-01")
    emp2 = Employee(name="Jane Smith", position="Designer", salary=4500, hire_date="2024-02-01")
    dao.insert(emp)
    dao.insert(emp2)


    # READ by ID
    employees = dao.get_all()
    employee = employees[-1]  # последний добавленный
    print("\nGet by ID:")
    print(employee)

    # READ ALL
    print("\nAll Employees:")
    employees = dao.get_all()
    for e in employees:
        print(e)

    # UPDATE
    if employee:
        employee.name = "John Updated"
        employee.salary = 6000
        dao.update(employee)

    # DELETE
    dao.delete(1)


if __name__ == "__main__":
    main()