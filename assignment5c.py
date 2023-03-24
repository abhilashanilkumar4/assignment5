class Account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
    def Details(self):
        print("Name:",self.title,'\n'"balance:",self.balance)

class Savings_account():
    
    def __init__(self,interestrate):
        self.inerestrate=interestrate
    def interest(self):
        print('intrest:',self.inerestrate)

A=Account('Ashish',5000)
B=Savings_account(5)
A.Details()
B.interest()

