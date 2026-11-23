with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if(content2== content2):
    print("Yes these files are identical")

else:
    print("No these files are not identical")