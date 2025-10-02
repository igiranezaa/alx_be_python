class BankAccount:
    def __init__(self, initial_balance=0):
        # Ensure balance is stored as float
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        self.account_balance += float(amount)

    def withdraw(self, amount):
        if self.account_balance >= float(amount):
            self.account_balance -= float(amount)
            return True
        return False

    def display_balance(self):
        # Format with 2 decimal places
        print(f"Current Balance: ${self.account_balance:.2f}")
