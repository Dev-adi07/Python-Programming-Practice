class Employee:
    company = "ICT"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


#class programmer:
#    company = "ICT infotech"
#    def show(self):
#        print(F"The name is {self.name} and the salary is {self.salary}")


#    def showlanguage(self):
#        print(f"The name is {self.name} and he is good with {self.language} language")

class programmer(Employee):
    company = "ICT infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

        
a = Employee()
b = programmer()

print(a.company, b.company)