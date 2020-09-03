import re

book = open("mbox.txt")
count = 0
for line in book:
    line = line.rstrip()
    if re.search("From: " , line):
        print(line)

