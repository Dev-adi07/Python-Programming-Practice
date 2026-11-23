class Employee:
    language = "python" # This is a class attribute
    salary = 4500000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good morning")


Shreya = Employee("Shreya", 4500000, "JavaScript")
#shreya.name = "Shreya"
Shreya.name = "shreya"
print(Shreya.name, Shreya.salary)
#Shreya = Employee()