def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,3,56,56984,456974,231054,45,6954]

f = list(filter(divisible5, a))
print(f)