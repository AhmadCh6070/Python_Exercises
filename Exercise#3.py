#Task 1
print("Task#1")
Zander = float(input("Enter Zandar Size(cm): "))
if Zander >= 42:
    print(f"Good Job!\nYou Caught The Fish at {Zander:.2f}cm, So you can Keep it!")
else:
    print(f"Since You were {42-Zander:.2f}cm away from the Zander Size Limit, You Must Release it Back into the Lake")
print()

#Task 2
print("Task#2")
LUX = "Upper-deck cabin with a balcony."
A = "Above the car deck, equipped with a window."
B = "Windowless cabin above the car deck."
C = "Windowless cabin below the car deck."
Cabin = (input("Enter Cabin Class(LUX,A,B,C): ")).lower()
if Cabin == "lux":
    print(f"LUX : {LUX}")
elif Cabin == "a":
    print(f"A : {A}")
elif Cabin == "b":
    print(f"B : {B}")
elif Cabin == "c":
    print(f"C : {C}")
else:
    print("Invalid cabin class")
print()

#Task 3
print("Task#3")
gender = input("Enter your Gender(Male or Female): ").lower()
hemo = int(input("Enter your Hemoglobin Value(g/l): "))
if gender  == "male":
    if hemo<117:
        print(f"Hemoglobin of {hemo}(g/l) is low for a {gender}")
    elif (hemo>=117) and (hemo<=155):
        print(f"Hemoglobin of {hemo}(g/l) is normal for a {gender}")
    elif hemo>155:
        print(f"Hemoglobin of {hemo}(g/l) is high for a {gender}")
elif gender == "female":
    if hemo<134:
        print(f"Hemoglobin of {hemo}(g/l) is low for a {gender}")
    elif (hemo>=134) and (hemo<=167):
        print(f"Hemoglobin of {hemo}(g/l) is normal for a {gender}")
    elif hemo>167:
        print(f"Hemoglobin of {hemo}(g/l) is high for a {gender}")
else:
    print("Invalid Input")
print()

#Task 4
print("Task#4")
Year = int(input("Enter Year: "))
if (Year%4 == 0) and (Year%100 != 0):
    if (Year%400 == 0):
        print(f"The Year {Year} is a Leap Year")
elif (Year%400 == 0) and (Year%100 == 0):
    print(f"The {Year} is a leap year")
else:
    print(f"The Year {Year} is not a leap year")


