class BankAccount:
    """Represents a single bank account."""
    def __init__(self, account_number, name, initial_balance=0):
        """Initializes a new bank account."""
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposits funds into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws funds from the account."""
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")

    def check_balance(self):
        """Prints the current account balance."""
        print(f"Account {self.account_number} balance for {self.name}: ${self.balance}.")

# Example Usage:
# 1. Create an account
account1 = BankAccount(account_number="12345", name="Alice Smith", initial_balance=100)
account1.check_balance()

# 2. Deposit funds
account1.deposit(50)

# 3. Withdraw funds
account1.withdraw(30)

# 4. Attempt to withdraw more than the balance
account1.withdraw(200)

# 5. Check the final balance
account1.check_balance()
