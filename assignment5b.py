class student:

    def setName(self):
        self.Name=input('Enter Name:')
    def getName(self):
        return self.Name
    
    def setRollnumber(self):
        self.Rollnumber=input('Enter roll number:')
    def getRollnumber(self):
        return self.Rollnumber
    
s1=student()
s1.setName()
s1.setRollnumber()
