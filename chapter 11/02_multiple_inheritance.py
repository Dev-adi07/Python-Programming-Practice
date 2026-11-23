class Employee:
    company = "ICT"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")

class coder:
    language = "python"
    def printLanguage(self):
        print(f"out of all the language here is your language: {self.language}")



class programmer(Employee, coder):
    company = "ICT infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

        
a = Employee()
b = programmer()

b.show()
b.printLanguage()
b.showlanguage()