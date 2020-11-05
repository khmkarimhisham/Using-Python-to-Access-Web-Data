import json
from urllib.request import urlopen

url = input("Enter location: ")
print("Retrieving: " + url)
data = urlopen(url).read().decode()

sum = 0
count = 0

comments = json.loads(data)["comments"]
for comment in comments:
    count += 1
    sum += comment["count"]

print("Count: " + str(count))
print("Sum: " + str(sum))
