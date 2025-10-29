class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary


    def calculate_salary(self):
        return self.base_salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())


class RegularEmployee(Employee):
    def __init__(self, name, base_salary, bonus, tax):
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.tax = tax

    def calculate_salary(self):
        total_salary = self.base_salary + self.bonus - self.tax
        return total_salary


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        # Base salary is not needed for contract employees
        super().__init__(name, base_salary=0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        total_salary = self.hourly_rate * self.hours_worked
        return total_salary



class Manager(Employee):
    def __init__(self, name, base_salary, bonus, allowance):
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.allowance = allowance

    def calculate_salary(self):
        total_salary = self.base_salary + self.bonus + self.allowance
        return total_salary


if __name__ == "__main__":
    # Creating different employee objects
    emp1 = RegularEmployee("Siddarth", 40000, 5000, 2000)
    emp2 = ContractEmployee("Mohan", 800, 100)
    emp3 = Manager("Madhu", 60000, 10000, 5000)

    # Displaying their salary details
    print("----- Regular Employee -----")
    emp1.display_details()

    print("\n----- Contract Employee -----")
    emp2.display_details()

    print("\n----- Manager -----")
    emp3.display_details()
