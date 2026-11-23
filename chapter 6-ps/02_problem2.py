marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))
marks4 = int(input("Enter marks 4: "))
marks5 = int(input("Enter marks 5: "))

#check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3 + marks4 + marks5))/500

if(total_percentage>=60 and marks1>=51 and marks2>=67 and marks3>=51 and marks4>=68 and marks5>=57):
    print("You are pass: ", total_percentage)

else:
    print("You failed, try again next year:", total_percentage)