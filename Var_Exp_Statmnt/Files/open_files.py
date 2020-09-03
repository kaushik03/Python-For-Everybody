fhand = open("mbox.txt")
count=0
for line in fhand:
    count = count+1
print("Total number of lines: " , count)
for line in fhand:
    if line.startswith("au"):
        print(line)


