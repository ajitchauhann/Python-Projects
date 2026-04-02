class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount


atm = ATM(1000)
atm.deposit(500)
atm.withdraw(300)
print(atm.check_balance())

class Employee:
    def salary(self):
        pass

class FullTime(Employee):
    def salary(self):
        return 50000

class PartTime(Employee):
    def salary(self):
        return 20000

employees = [FullTime(), PartTime()]

for emp in employees:
    print(emp.salary())


    class Cart:
     def __init__(self):
        self.items = []

    def add_item(self, price):
        self.items.append(price)

    def total(self):
        return sum(self.items)


cart = Cart()
cart.add_item(100)
cart.add_item(200)

print(cart.total())






