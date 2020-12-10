import re
import copy
inFile = open("input/day08.txt")
myList = []

for line in inFile:
    myList.append(re.split("- | +", line.replace("\n","")))

print("===== PART 1 =====")

accu = 0
visited = []
potentialErrors = []
pos = 0

while pos not in visited:
    visited.append(pos)
    if(myList[pos][0] != "acc"):
        potentialErrors.append(pos)
    inc = int(myList[pos][1])
    if(myList[pos][0] == "jmp"):
        pos += inc
    elif(myList[pos][0] == "acc"):
        accu += inc
        pos += 1
    else:
        pos += 1

print("Current Accu is: " + str(accu))

print("===== PART 2 =====")

for errorPos in potentialErrors:
    copied = copy.deepcopy(myList)
    accu = 0
    visited = []
    pos = 0

    if myList[errorPos][0] == "jmp":
        copied[errorPos][0] = "nop"
    else :
        copied[errorPos][0] = "jmp"
    while pos not in visited and pos < len(myList):
        visited.append(pos)
        inc = int(myList[pos][1])
        if(copied[pos][0] == "jmp"):
            pos += inc
        elif(copied[pos][0] == "acc"):
            accu += inc
            pos += 1
        else:
            pos += 1
    if pos >= len(myList):
        print("Program Ended, Accu is: " + str(accu))
        break