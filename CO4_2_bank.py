class Bank_Account():
    def __init__(self):
        self.accountno = 109891071
        self.name = "Philip Antony"
        self.type ="Saving"
        self.balance = 0
        print("Welcome to bank.!")

    def deposit(self):
        amount = float(input("Enter the Amount to be Deposited :"))
        self.balance = self.balance + amount
    def withdraw(self):
        amount = float(input("Enter the Amount to be Withdraw :"))
        if self.balance>=amount:
            self.balance = self.balance - amount
        else:
            print("\ninsufficient Balance..!")

    def accountbalance(self):
        print("Account Owner :",self.name)
        print("Account no :",self.accountno)
        print("Account Type :",self.type)
        print("Net Balance :",self.balance)

obj = Bank_Account()
obj.deposit()
obj.withdraw()
obj.accountbalance()