f = open("testfile.txt", "w")
# f.read()

f.write("I have entered some text into this file \n let's see if this works")
f.close()
f = open("testfile.txt", "r")
print(f.read())