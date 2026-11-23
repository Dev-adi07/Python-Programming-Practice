from matplotlib.pylab import rint


class Programmer :
    company = "Microsoft"
    def __init__(self, name, salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("shreya", 450000, 800013)
print(p.name, p.salary, p.pin, p.company)