# From https://www.codesdope.com/practice/python-decide-ifelse/ level 1

#1

length = float(input("Enter the length of the rectangle \n"))
breadth = float(input("Enter the Breadth Of the Rectangle \n"))
if length == breadth:
    print("It's a Square")
elif length < 0 or breadth < 0 :
    print("Bad Input")
else :
    print("It's not a square.")

#2
a = float(input("Enter a Number \n"))
b = float(input("Enter a Number \n"))
if a > b:
    print(a)
else :
    print(b)

#3
quantity = int(input('Enter the Quantity Purchased \n'))
cost = quantity * 100
if quantity >= 1000:
    disc_cost = 0.1 * cost
    print(disc_cost)
else :
    print(cost)

#4
salary = int(input('Enter the Salary'))
year = int(input('Enter the no of years into service'))

if year > 5:
    bonus = salary * 0.5
    net_sal = salary + bonus
    print(net_sal)
else :
    print(Salary)