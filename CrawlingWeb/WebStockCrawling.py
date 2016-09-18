import re
import urllib.request

url = "https://www.google.com/finance?q="

stock = input("Enter your stock")
url = url + stock
data = urllib.request.urlopen(url).read()

print(data)

data1 = data.decode("utf-8")

m = re.search('meta itemprop="price"', data1)
start = m.start()
end = start + 50
newString = data1[start:end]

print(newString)

m = re.search('content="', newString)
start = m.end()
newString1 = newString[start:]

m = re.search("/", newString1)
start = 0
end = m.end() - 3
final = newString1[0:end]
print("The value of " + stock + "is " + final)