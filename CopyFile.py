ufn = input("Enter your file name: ")
ufn += ".txt"
file1 = open(ufn, "r")
file2 = open("copiedfile.txt", "w")
file2.write(file1.read())
file1.close()
file2.close()
file2 = open("copiedfile.txt", "r")
print(file2.read())
