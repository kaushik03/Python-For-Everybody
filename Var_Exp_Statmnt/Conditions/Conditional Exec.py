5 == 5 # == for 'true' statement.
x = int(input('Enter a number \n'))
if x > 0:
    print('x is positive')
#Condition Exercise
#1
hours = float(input('Enter the no of Hours \n'))
pay = float(input('Hourly pay to the employee \n'))

if hours > 40:
    incr_pay = pay * 1.5
    gross_pay = incr_pay * hours
    print(gross_pay)
else:
    gross_pay = hours * pay
    print(gross_pay)
#3
try:
    hours = float(input('Enter the no of Hours \n'))
    pay = float(input('Hourly pay to the employee \n'))
    if hours > 40:
        incr_pay = pay * 1.5
        gross_pay = incr_pay * hours
        print(gross_pay)
    else:
        gross_pay = hours * pay
        print(gross_pay)
except:
    print('Please enter a numeric input')

#4
inp = input('Enter score: ')
try:
    score = float(inp)
except:
    score = -1

if score > 1.0 or score < 0.0:
    print('Bad score')
elif score > 0.9:
    print('A')
elif score > 0.8:
    print('B')
elif score > 0.7:
    print('C')
elif score > 0.6:
    print('D')
else:
    print('F')



