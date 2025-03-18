# Main file
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("--- Employee Details ---")
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")

class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, department, basic_salary, bonus):
        super().__init__(employee_id, name, department)
        self.basic_salary = basic_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus

    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self.basic_salary:.2f}")
        print(f"Bonus: ${self.bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")

class ContractEmployee(Employee):
    def __init__(self, employee_id, name, department, hourly_rate, hours_worked):
        super().__init__(employee_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self.hourly_rate:.2f}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")

class Intern(Employee):
    def __init__(self, employee_id, name, department, stipend):
        super().__init__(employee_id, name, department)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self.stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")

employee1 = PermanentEmployee("P001", "Arthur Morgan", "IT", 50000, 3000)
employee2 = ContractEmployee("C300", "Abigail Roberts", "Marketing", 70, 400)
employee3 = Intern("I431", "John Marston", "Finance", 2300)

employee1.display_details()
print()
employee2.display_details()
print()
employee3.display_details()
