import re

f = open("Week 2 - file.txt", "r")
arr = re.findall('[0-9]+', f.read())
sum = 0

for i in arr:
    sum = sum + int(i) 

print(sum)