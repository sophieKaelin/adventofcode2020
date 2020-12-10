inFile = open("input/day09.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n",""))
myList.append("")

print(myList)
print("===== PART 1 =====")