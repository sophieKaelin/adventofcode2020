import re
inFile = open("input/day08.txt")
myList = []

for line in inFile:
    myList.append(re.split("- | +", line.replace("\n","")))

print("===== PART 1 =====")

accu = 0
visited = []
pos = 0

while pos not in visited:
    visited.append(pos)
    inc = int(myList[pos][1])

    if(myList[pos][0] == "jmp"):
        pos += inc
    elif(myList[pos][0] == "acc"):
        accu += inc
        pos += 1
    else:
        pos += 1

print("Current Accu is: " + str(accu))