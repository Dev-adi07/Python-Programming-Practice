# Basic class
class Employee:
    name = "Shreya"
    language = "python"
    salary = 4500000

Shreya = Employee()
print(Shreya.name, Shreya.language)
# output = shreya python



# Class Abstractions
class Employee:
    language = "python"
    salary = 4500000

Shreya = Employee()
print(Shreya.language, Shreya.salary)

Shreya = Employee()
print(Shreya.salary, Shreya.language)
#output = python 4500000
          #450000 Python



class Employee:
    language = "python" # This is a class attribute
    salary = 4500000

Shreya = Employee()
Shreya.name = "shreya" # This is an instance attribute
print(Shreya.name, Shreya.language, Shreya.salary)

Shreya = Employee()
Shreya.name = "shreya adi ko RoKo please"
print(Shreya.name, Shreya.salary, Shreya.language)

# here name is instance attribute and salary and language are attributes as they directly to the class