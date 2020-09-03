n = 5
while n > 0:
    print(n)
    n = n-1
    print("blastoff")

#1

sum = 0
count = 0
avg = 0
while True:
    try:
        x = input("Enter a Number: ")
        if (x == "done"):
            break
        value = float(x)
        sum = value + sum
        count = count + 1
        avg = sum / count
    except:
        print("Invalid Input")
print(sum)
print(count)
print(avg)


