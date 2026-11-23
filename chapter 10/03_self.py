class Employee:
    language = "python" # This is a class attribute
    salary = 4500000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    
    @staticmethod
    def greet():
        print("Good morning")


Shreya = Employee()
#Shreya.language = "JavaScript" # This is an instance attribute
Shreya.greet()
Shreya.getInfo()
#Employee.getInfo(Shreya)