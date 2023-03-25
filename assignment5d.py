class Account:
    def __init__(self,title=None, balance=0):
        self.title=title
        self.balance=balance

    def deposit(self):
        amount=float(input("Enter amount: "))
        self.amount=amount
        self.balance=self.balance+amount
        print("\nDeposited:",amount,"\nbalance:",self.balance)

    def withdrawal(self):
        amount1=float(input("Enter amount:"))
        self.amount1=amount1
        if self.balance>=amount1:
            self.balance=self.balance-amount1
            print("\nwithdrwed:",amount1,"\nbalance:",self.balance)
        else:
            print("\ninsufficient:")
    
    def getbalance(self):
        return self.balance
class Saving_account(Account):
    
    def __init__(self, title=None, balance=0,interestrate=0):
        self.interestrate=interestrate
        super().__init__(title, balance)
    
    def interestamount(self):
        self.interestamount=self.balance*self.interestrate/100
        print("interest amount:",self.interestamount)


a= Account("asish",2000)
b=Saving_account("asish",2000,5)
a.deposit()
a.withdrawal()
a.getbalance()
b.interestamount()