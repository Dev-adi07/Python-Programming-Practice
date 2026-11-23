class Employee:
    a = 10

class programmer(Employee):
    b = 20

class manager(programmer):
    c = 30


o = Employee()
print(o.a)  # prints the a attribute
# print(o.b) # shows and error as there is no b attribute in Employee class

o = programmer()
print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)


