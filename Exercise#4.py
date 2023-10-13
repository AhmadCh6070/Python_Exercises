#Task 1
print("Task#1")
counter = 1
print("Numbers divisible by 3:",end="")
while counter <= 1000:
    if counter%3 == 0:
        print(f" {counter},",end="")
    counter += 1
print()
print()

#Task 2
print("Task#2")
M = 0
while M >= 0:
    M = float(input("Enter Inches: "))
    if M < 0:
        print("Program has Ended Due to Entering Negative Number.")
        break
    if M > 0:
        print(f"{M} inches is equal to ",end="")
        M = M * 2.54
        print(f"{M:.3f} in centimeters")
        print()
print()

#Task 3
print(("Task#3"))
Number = input("Enter Number:")
List_Numbers=[]
Update_List=[]
if Number != "":
    while Number != "":
        List_Numbers.append(Number)
        Number = input("Enter Number:")
    for i in List_Numbers:
        Update_List.append(int(i))
    print()
    print(f"Max Number: {max(Update_List)}")
    print(f"Min Number: {min(Update_List)}")
else:
    print("Empty Input So no Max and Min Number")
print()

#Task 4
import random

print("Task#4")
Final = random.randint(1,10)
User = int(input("Enter Your Guess: "))
if User != Final:
    while True:
        if User > Final:
            print("Your Guess was Too High, Try Again")
            User = int(input("Enter Your Guess: "))

        elif User < Final:
            print("Your Guess was  Too Low, Try Again")
            User = int(input("Enter Your Guess: "))

        elif User == Final:
            print(f"Your Guess was Right! The Number was {User}")
            break

else:
    print(f"Congratulations! You Guessed Correctly on the First Try! The Number Was {User}")
print()

#Task 5
print("Task#5")
Login = ["python","rules"]
U_Name = input("Please Enter Your Username: ")
Pass = input("Please Enter Your Password: ")
print()
attempt = 0
if (U_Name != Login[0]) or (Pass != Login[1]):
    while attempt < 5:
        print("Login Details are Wrong, Try Again.")
        U_Name = input("Please Enter Your Username: ")
        Pass = input("Please Enter Your Password: ")
        print()
        attempt += 1
        if (U_Name == Login[0]) or (Pass == Login[1]):
            break
    if attempt < 5:
        print("Welcome")
    else:
        print("Access Denied")
else:
    print("Welcome")
print()

#Task 6
print("Task#6")
U_Points = int(input("Enter Number of points to be generated: "))
Points_in_Circle = 0
for t in range(U_Points):
    x = random.uniform(-1,1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        Points_in_Circle += 1

print(f"Out of {U_Points}, only {Points_in_Circle} points landed in circle")