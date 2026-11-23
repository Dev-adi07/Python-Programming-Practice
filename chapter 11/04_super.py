class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 10


class programmer(Employee):
    def __init__(self):
        print("Constructor of programmer")
    b = 20

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of manager")
    c = 30


#o = Employee()
#print(o.a)  # prints the a attribute

#o = programmer()
#print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)
