from functools import reduce
l = [111, 2, 54, 785, 766, 89, 56,67,98]

def greater(a, b):
    if (a>b):
        return a
    return b


print(reduce(greater, l))