#python file created
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        result = []
        for emp in self.employees:
            if emp.age == target_age:
                result.append(emp)
        return result

    def search_by_name(self, target_name):
        result = []
        for emp in self.employees:
            if emp.name == target_name:
                result.append(emp)
        return result

    def search_by_salary(self, operator, target_salary):
        result = []
        for emp in self.employees:
            if operator == '>' and emp.salary > target_salary:
                result.append(emp)
            elif operator == '<' and emp.salary < target_salary:
                result.append(emp)
            elif operator == '>=' and emp.salary >= target_salary:
                result.append(emp)
            elif operator == '<=' and emp.salary <= target_salary:
                result.append(emp)
        return result

def main():
    emp_table = EmployeeTable()

    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose search parameter:")
    print("1. Age\n2. Name\n3. Salary (>, <, <=, >=)")
    choice = int(input())

    if choice == 1:
        target_age = int(input("Enter age: "))
        result = emp_table.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter name: ")
        result = emp_table.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter operator (> < <= >=): ")
        target_salary = int(input("Enter salary: "))
        result = emp_table.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return

    if result:
        print("Search results:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found")

if __name__ == "__main__":
    main()
