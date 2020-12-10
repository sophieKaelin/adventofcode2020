inFile = open("input/day09.txt")
myList = []
invalidNum = 0
position = 0

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
        invalidNum = myList[i]
        position = i
        break

print("===== PART 2 =====")
lower, upper = 0, 0

for i in range(0, position-1):
    total = myList[i]
    for x in range(i+1, position):
        if total > invalidNum:
            break
        elif total == invalidNum:
            print("RANGE FOUND! -> " + str(i) + " : " + str(x))
            lower = i
            upper = x
            break
        total += myList[x]

shortList = myList[lower : upper]
print(min(shortList) + max(shortList))