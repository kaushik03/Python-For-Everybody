def overtime(hours, pay):
    if hours > 40:
        pay = pay * 1.5
    else :
        pay = pay


hours = int(input('Enter the Hours \n'))
pay = float(input('Hourly Pay \n'))
x = overtime(hours, pay)
print(x)