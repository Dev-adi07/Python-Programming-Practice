class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The vector is {self.x}x + {self.y}y")

class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


    def show(self):
        print(f"The vector is {self.x}x + {self.y}y + {self.z}z")

a = TwoDVector(3, 4)
b = ThreeDVector(1, 2, 3)
a.show()
b.show()