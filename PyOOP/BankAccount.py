class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance =balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self,amount):
        self.balance-=amount
        print("withdraw  amount is " ,self.balance)
    def deposit(self,amount):
        self.balance-=amount
        print("deposit  amount is ", self.balance)
a1=BankAccount("Daya",200)
a1.display()
a1.withdraw(100)
a1.deposit(200)