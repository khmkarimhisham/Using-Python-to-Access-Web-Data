import xml.etree.ElementTree as ET
import ssl
from urllib.request import urlopen

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

data = urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
 
tree = ET.fromstring(data)
count = 0
sum = 0
counts = tree.findall('.//count')
for i in counts:
    count += 1
    sum += int(i.text)

print("Count: " + str(count))
print("Sum: " + str(sum))