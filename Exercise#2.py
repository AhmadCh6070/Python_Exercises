#Task 1
print("Task#1")
name = input("Enter your Name: ")
print(f"Hello, {name}!")
print()

#Task 2
print("Task#2")
import math
R = float(input("Enter Radius Of Circle: "))
print(f"{R**2*math.pi:.3f} is the Area of Circle")
print()

#Task 3
print("Task#3")
L = float(input("Enter Length of Rectangle: "))
W = float(input("Enter Width of Rectangle: "))
print(f"Perimeter of Rectangle: {2*L+2*W:.2f} \nArea of Rectangle: {L*W:.2f}")
print()

#Task 4
print("Task#4")
F = int(input("Enter First Number:"))
S = int(input("Enter Second Number:"))
T = int(input("Enter Third Number:"))
print(f"Sum Of Numbers: {F+S+T} \nProduct of Numbers: {F*S*T} \nAverage of Numbers: {(F+S+T)//3} ")
print()

#Task 5
print("Task#5")
Talents = float(input("Enter Talents(leiviskä):\n"))
print()
Pounds = float(input("Enter Pounds(naula):\n"))
print()
Lots = float(input("Enter Lots(luoti):\n"))
print()
Total = ((((Talents*20)+Pounds)*32)+Lots)*13.3
KG = int(Total//1000)
G = Total-KG*1000
print(f"The Weight in Modern Units:\n{KG} Kilograms and {G:.2f}grams")
print()

#Task 6
print("Task#6")
import random
One_R,Two_R,Three_R = random.randint(0,9),random.randint(0,9),random.randint(0,9)
print(f"Three Digit Code Between 0 and 9: {One_R,Two_R,Three_R}\n")

Four_R,Five_R,Six_R,Seven_R = random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)
print(f"Three Digit Code Between 0 and 9: {Four_R,Five_R,Six_R,Seven_R}")


