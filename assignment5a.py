class calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        return self.x+self.y
    
    def subtract(self):
        return self.x-self.y
    
    def multiply(self):
        return self.x*self.y
    
    def divide(self):
        return self.x/self.y

x=int(input("enter first number"))
y=int(input("enter second number"))
obj =calculator(x,y)
while True:
    def menu():
        x=('1.add\n2.sub\n3.muliti\n4.divide')
        print(x)
    menu()
    option = int(input('select any one: '))
    if option==1:
        print("result:",obj.add())
    elif option==2:
        print("result:",obj.subtract())
    elif option==3:
        print("result:",obj.multiply())
    elif option==4:
        print("result:",obj.divide())
        break
print()