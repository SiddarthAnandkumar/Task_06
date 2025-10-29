class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance   # Private variable (Encapsulation)

    def depositmoney(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" Deposited amount ₹{amount}. New balance amount: ₹{self.__balance}")
        else:
            print(" Deposit amount must be positive.")

    def withdrawamount(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f" Withdrawn ₹{amount}. New balance: ₹{self.__balance}")
            else:
                print(" Insufficient balance.")
        else:
            print(" Withdrawal amount must be positive.")

    # Getter method to view balance
    def get_balance(self):
        return self.__balance


# Savings Account (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.25):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    # Calculate and return interest
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f" Interest earned: ₹{interest}")
        return interest


# Current Account (inherits from BankAccount)
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, min_balance=12000):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    # Override withdraw method
    def withdraw(self, amount):
        if amount > 0:
            if self.get_balance() - amount >= self.min_balance:
                super().withdraw(amount)
            else:
                print(f" Cannot withdraw ₹{amount}. Minimum balance ₹{self.min_balance} must be maintained.")
        else:
            print(" Withdrawal amount must be positive.")




savings = SavingsAccount(account_number="ICICI16782", balance=78000, interest_rate=0.27)
current = CurrentAccount(account_number="SBI3578", balance=10000, min_balance=7000)


print("\n- Savings Account Operations ---")
savings.depositmoney(7000)
savings.withdrawamount(4200)
savings.calculate_interest()
print(f"Final Savings Balance: ₹{savings.get_balance()}")

# Operations on Current Account
print("\n---  Current Account Operations ---")
current.depositmoney(4500)
current.withdrawamount(25000)
current.withdrawamount(17000)
print(f"Final Current Balance: ₹{current.get_balance()}")
