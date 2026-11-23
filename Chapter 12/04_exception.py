try:
    a = int(input("Enter a number: "))
    print(a)


except ValueError as v:
    print("Shreya")
    print(v)

except Exception as e:
    print(e)

print("Thank You")