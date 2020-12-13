inFile = open("input/day11.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n",""))

maxRow = len(myList)
maxCol = len(myList[0])

print("~~ Part 1 ~~")
def countSurrounding(c, r, li):
    count = 0
    for ro in range(max(0,r-1), min(r+2, maxRow)):
        count += li[ro][max(0, c-1):min(maxCol, c+2)].count("#")
    if li[r][c] == "#":
        count -=1
    return count

finished = False
while(not finished):
    finished = True
    newList = []
    for r in range(maxRow):
        s = ""
        for c in range(maxCol):
            if myList[r][c] != ".":
                total = countSurrounding(c, r, myList)
                if total == 0:
                    s += ("#")
                elif total >= 4:
                    s += ("L")
                else:
                    s += (myList[r][c])
                finished = finished and s[c] == myList[r][c]
            else:
                s += (".")
        newList.append(s)
    myList = newList

# Count number of occupied seats
sum = 0
for v in myList:
    sum+= v.count("#")
print(sum)

print("~~ Part 2 ~~")

