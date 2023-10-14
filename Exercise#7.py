#Task 1
print("Task#1")
M = int(input("Enter Number of the Month: "))
Seasons = ("Spring", "Summer", "Autumn", "Winter")
if M >= 3 and M <= 5:
    print(f"The Season is {Seasons[0]}")
elif M >= 6 and M <= 8:
    print(f"The Season is {Seasons[1]}")
elif M >= 9 and M <= 11:
    print(f"The Season is {Seasons[2]}")
elif M == 1 or M == 2 or M == 12:
    print(f"The Season is {Seasons[3]}")
else:
    print("The Month Entered Does Not Exist")
print()

#Task 2
print("Task#2")
list_n = set()
while True:
    Name = str(input("Enter Name: "))
    if Name != "":
        if Name in list_n:
            print(f"{Name} already exists in the List.")
            print()
        else:
            list_n.add(Name)
            print(f"{Name} has been added to The list")
            print()
    else:
        print()
        print("Here are all the names entered into the set:")
        for i  in list_n:
            print(i)
        break
print()

#Task 3
print(("Task#3"))
print()

def Options():
    print("1. Enter A New Airport.")
    print("2. Fetch Airport Information.")
    print("3. Quit")
    print()

Airports = {}

while True:
    Options()
    Command = input("Enter The Number For The Command: ")
    if Command == "1":
        Air_Name = input("Enter Name Of Airport(No Need To Write Airport At End): ").title()
        Air_Name += " Airport"
        Air_Code = input("Enter ICAO Code Of Airport: ").upper()
        print()
        Airports[Air_Code] = Air_Name
        print(f"{Air_Name} with ICAO Code {Air_Code} Has been added")
        print()
    elif Command == "2":
        Fetch_Code = input("Enter ICAO Code Of Airport To Fetch Name: ").upper()
        print()
        if Fetch_Code in Airports:
            print(f"The Name Of Airport with ICAO Code {Fetch_Code} is {Airports[Fetch_Code]}")
            print()
        else:
            print(f"No Airport With ICAO Code {Fetch_Code} exists.")
            print()
    elif Command == "3":
        print("You Have Decided To Exit The Program, Goodbye!")
        break


