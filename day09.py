inFile = open("input/day09.txt")
myList = []

for line in inFile:
    myList.append(int(line.replace("\n","")))

print("===== PART 1 =====")

def addTwo(li, addsTo):
    for x in range(len(li) - 1):
        if(x > addsTo):
            continue
        for y in range(x+1, len(li)):
            if li[x] + li[y] == addsTo:
                return True
    return False

for i in range(25, len(myList)):
    if not addTwo(myList[i-25:i], myList[i]):
        print(myList[i])
        break

print("===== PART 2 =====")