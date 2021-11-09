class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to your Bank!")
    def deposit(self):
        amount = float(input("Enter your Amount to deposit: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
    def withdraw(self):
        amount = float(input("Enter Amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdraw:", amount)
        else:
            print("\n Insufficent Balance!")
    def display(self):
        print("\n Net Available Balance = ", self.balance)

s = Bank_Account()

s.deposit()
s.withdraw()
s.display()



