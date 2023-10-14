#Task 1
print("Task#1")

import random
def Rice_roll():
    roll = random.randint(1,6)
    print(f"You rolled a {roll}")
    return roll
while True:
    Roll = Rice_roll()
    if Roll == 6:
        break

print("You got a 6 so the program ended.")
print()

#Task 2
print("Task#2")
def High_Roll(L):
    high_roll = random.randint(1, L)
    print(f"You rolled a {high_roll}")
    return high_roll
L = int(input("Enter The Highest Roll on the Dice: "))

rolled = High_Roll(L)

while True:
    if rolled == L:
        break
    else:
        rolled = High_Roll(L)

print(f"You got a {L} so the program ended.")
print()

#Task 3
print("Task#3")

def Conversation(gallon):
    liter = gallon * 4.546092
    return liter

while True:
    gallon = float(input("Enter volume of Gas in gallons: "))
    if gallon < 0:
        print("Program Ended due to Entering Negative Value.")
        break
    else:
        convert = Conversation(gallon)
        print(f"{gallon} gallons is equal to {convert:.3f} liters.")

print()

#Task 4
print("Task#4")

def Sum(list_int):
    all = sum(list_int)
    return all
y = []
while True:
    x = input("Enter Number to the List: ")
    if x.isdigit():
        x = int(x)
        y.append(x)
    else:
        break
print()
print(f"The list was {y}")
print(f"The sum of the List was {Sum(y)}")
print()

#Task 5
print("Task#5")

def Cut_List(lis):
    cut_out = []
    for i in lis:
        if i%2 == 0:
            cut_out.append(i)
    return cut_out
uncut_list = []
while True:
    original_list = input("Enter Number to the List: ")
    if original_list.isdigit():
        original_list = int(original_list)
        uncut_list.append(original_list)
    else:
        break

print(f"The Original list was {uncut_list}")
print(f"The Even Numbers in the the List were {Cut_List(uncut_list)}")
print()

#Task 6
print("Task#6")

import math
def Unit_Price(D,P):
    R = D/100
    sqrmeter = ((P)/(math.pi*(R**2)))
    return sqrmeter
Diameter = float(input("Enter Diameter of First Pizza(in m): "))
Price = float(input("Enter Price of First Pizza(in €): "))

unit_per_sqrmeter_1= Unit_Price(Diameter, Price)
print(f"The Unit Price of the First Pizza per Square meter is {unit_per_sqrmeter_1: .2f}€/square meter")
print()

Diameter_2 = float(input("Enter Diameter of Second Pizza(in cm): "))
Price_2 = float(input("Enter Price of Second Pizza(in €): "))

unit_per_sqrmeter_2= Unit_Price(Diameter_2, Price_2)
print(f"The Unit Price of the Second Pizza per Square meter is {unit_per_sqrmeter_2: .2f}€/square meter")
print()

if unit_per_sqrmeter_1 == unit_per_sqrmeter_2:
    print("Both Pizza have same Unit Price Per Square Meter.")
elif unit_per_sqrmeter_1 < unit_per_sqrmeter_2:
    print("The First Pizza has the better Unit Price Per Square Meter.")
else:
    print("The Second Pizza has the better Unit Price Per Square Meter.")