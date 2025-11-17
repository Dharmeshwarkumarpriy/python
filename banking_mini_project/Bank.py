class Bank:
    def __init__(self,account_holder,initial_balance=0.0):
        self.account_holder=account_holder
        self.balance=initial_balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposited{amount:.2f} new balance is {self.balance:.2f}")
        else:
            print("invalid deposit amount")

    def withdraw(self,amount):
        if amount>0 and amount <=self.balance:
            self.balance-=amount
            print(f"withdrawn {0.2} new balance is {self.balance:2f}")
        else:
            print("invalid withdrawal amount or insufficient balance")

    def print_statement(self):
        print("account statement--")
        print(f"account holder: {self.account_holder}")
        print(f"curent balance: {self.balance:2f}")

    def saving(self):
        print(f"curent saving balance is {self.balance:.2f}")

my_account=Bank(1000.0)
my_account.deposit(500.0)
my_account.print_statement()
