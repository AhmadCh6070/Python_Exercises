#Task 1
import random

print("Task#1")
Roll = int(input("Enter Number Times to roll dice: "))
roll_sum = []
for i in range(Roll):
    NO = random.randint(1,6)
    roll_sum.append(NO)
print(f"\nThe Dice was rolled {Roll} times, and their sum was {sum(roll_sum)}")
print()

#Task 2
print("Task#2")
List_of_no = []
while True:
    U_no = (input("Enter Number: "))
    if U_no != "":
        U_no = int(U_no)
        List_of_no.append(U_no)
    else:
        break
print()
List_of_no.sort(reverse=True)
print(f"The Five greatest numbers in descending number are: \n{List_of_no[:5]}")
print()

#Task 3
print("Task#3")
num = int(input("Enter Number: "))
prime = True
if num < 2:
    prime = False
for z in range(2,int(num**0.5+1)):
    if num%z == 0:
        prime = False
if prime:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")
print()

#Task 4
print("Task#4")
cities = []
for y in range(5):
    u_city = input("Enter Name of City: ")
    cities.append(u_city)

print()
print("Cities :")
for w in cities:
    print(f"{w}")