class Animals:
    pass

class Pets(Animals):
    pass


class Dogs(Pets):

    @staticmethod
    def bark():
        print("Woof woof!")

d = Dogs()
d.bark()
