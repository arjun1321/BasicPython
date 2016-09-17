import re

# print(dir(re))

string = "The night was cold and dark"
m = re.search("night", string)
print(m)

start = m.start()
end = m.end()

print(string[start:end])