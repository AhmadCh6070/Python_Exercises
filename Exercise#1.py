#Task 1
print("Task#1")
name = input("Enter Your Name: ")
year = int(input("Enter A Year: "))
print(f"{name} is a valiant knight, born in the year {year}.\nOne morning {name} woke up to an awful racket: a dragon was approaching the village. \nOnly {name} could save the village's residents.")

#Task 2
print("Task#2")
days = int(input("Enter Number Of Days: "))
print(f"Seconds in that many Days: {days*24*3600}")

#Task 3
print("Task#3")
Cafe = float(input("Enter days at Cafe: "))
Lunch = float(input("Enter Typical Lunch Cost: "))
Gro = float(input("Enter Cost of Groceries: "))
print(f"\nAverage Food Expenditure:\nDaily:{(Cafe*Lunch+Gro)/7:.2f}\nWeekly:{Cafe*Lunch+Gro:.2f}")