
# Q: Create Account class with 2 attributes - balance & account no.
# create methods for debit, credit & printing the balance. 

class Account:
    def __init__(self, bal, acc):
        self.balance = bal  # instance attribute for balance
        self.account_no = acc  # instance attribute for account number

    # debit method to withdraw amount from balance
    def debit(self, amount):
        self.balance -= amount  # deduct amount from balance
        print("Rs", amount, "was debited")
        print("Current balance is Rs", self.get_balance())

     # credit method to add amount to balance
    def credit(self, amount):
        self.balance += amount  # add amount to balance
        print("Rs", amount, "was credited")
        print("Current balance is Rs", self.get_balance())

    # method to print the current balance
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
print(acc1.balance)  # Output: 10000
print(acc1.account_no)  # Output: 12345
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)

# Other then lecture:-------------------------------------------------------

# Method 2:
class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no  # instance attribute for account number
        self.balance = balance  # instance attribute for balance

    def debit(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # deduct amount from balance
            print(f"Debited {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def credit(self, amount):
        if amount > 0:
            self.balance += amount  # add amount to balance
            print(f"Credited {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount.")

    def print_balance(self):
        print(f"Account No: {self.account_no}, Balance: {self.balance}")

# Usage:
account = Account("123456789", 1000)  # creating an account with initial balance of 1000
account.print_balance()  # Output: Account No: 123456789, Balance: 1000
account.debit(200)  # Output: Debited 200. New balance: 800
account.credit(500)  # Output: Credited 500. New balance: 1300