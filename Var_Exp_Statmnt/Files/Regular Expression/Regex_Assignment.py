import re
text = open('regex_sum_840658.txt')
nums = []

for line in text:
    line = line.rstrip()
    regex = re.findall("([0-9]+)", line)
    if len(regex) < 1:
        continue

    for i in range(len(regex)):
        num = float(regex[i])
        nums.append(num)

print(sum(nums))