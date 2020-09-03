#8
Classes_held = int(input("Enter the Number of classes held: \n"))
Classes_attended = int(input("Enter the Number of classes attended: \n"))
Attendance = (Classes_attended/Classes_held)*100
print("Your Attendance is ", Attendance)
if Attendance >= 75.0:
    print("You're allowed to take the exam")
else:
    print("Your are kicked out of the class")

#1 Level 2
Year = int(input("Enter the year to check: \n"))
if (Year%4) == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")