class work:
    def __init__(self, name, income, penalty):
        self.name = name
        self.income = income
        self.penalty = penalty

    def calculate_payment(self):
        total_salary = self.income - self.penalty
        # Вивід залишаємо англійською для універсальності
        print(f"Employee {self.name} earned {self.income} and received {self.penalty} in internal penalties. Total: {total_salary}")

# Створюємо об'єкти з англійськими назвами змінних
employee1 = work("Andrii", 31999, 1200)
employee2 = work("Vova", 31900, 1100)
employee3 = work("Vlad", 33999, 0)

employee1.calculate_payment()
employee2.calculate_payment()
employee3.calculate_payment()
