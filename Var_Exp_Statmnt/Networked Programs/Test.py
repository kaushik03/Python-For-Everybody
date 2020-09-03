import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = "http://python-data.dr-chuck.net/comments_459547.xml"

print("Retrieving " + url)

xml = urllib.request.urlopen(url).read()
print("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print("Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print("Sum:" + str(accumulator))