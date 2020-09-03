#1
a = "Umbrella"
for i in a:
        if i == "e":
            print("e not exist ")
#2
a = "This is Orange juice"
for i in a.split():
    if i == "Orange":
        print("True")


#3
fhand = open("../Strings/mbox.txt")
count = 0
for line in fhand:
    count = count + 1
print("No of Lines " , count)