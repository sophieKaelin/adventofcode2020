inFile = open("input/day11.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n",""))

maxRow = len(myList)
maxCol = len(myList[0])

print("~~ Part 1 ~~")
# def countSurrounding(c, r, li):
#     count = 0
#     for ro in range(max(0,r-1), min(r+2, maxRow)):
#         count += li[ro][max(0, c-1):min(maxCol, c+2)].count("#")
#     if li[r][c] == "#":
#         count -=1
#     return count

# finished = False
# while(not finished):
#     finished = True
#     newList = []
#     for r in range(maxRow):
#         s = ""
#         for c in range(maxCol):
#             if myList[r][c] != ".":
#                 total = countSurrounding(c, r, myList)
#                 if total == 0:
#                     s += ("#")
#                 elif total >= 4:
#                     s += ("L")
#                 else:
#                     s += (myList[r][c])
#                 finished = finished and s[c] == myList[r][c]
#             else:
#                 s += (".")
#         newList.append(s)
#     myList = newList

# # Count number of occupied seats
# sum = 0
# for v in myList:
#     sum+= v.count("#")
# print(sum)

print("~~ Part 2 ~~")

def inRange(tc, tr):
    return tc in range(0, maxCol) and tr in range(0, maxRow)

def checkDir(tc,tr, mvC, mvR, li):
    while(inRange(tc, tr) and li[tr][tc] == "."):
        tc += mvC
        tr += mvR
    if(inRange(tc, tr) and li[tr][tc] == "#"):
        return 1
    return 0

def countVisuals(c, r, li):
    count = 0
    count += checkDir(c, r-1, 0, -1, li) #UP
    count += checkDir(c, r+1, 0, 1, li) #DOWN
    count += checkDir(c-1, r, -1, 0, li) #LEFT
    count += checkDir(c+1, r, 1, 0, li) #RIGHT
    count += checkDir(c-1, r-1, -1, -1, li) #UP/LEFT
    count += checkDir(c+1, r-1, 1, -1, li) #UP/RIGHT
    count += checkDir(c-1, r+1, -1, 1, li) #DOWN/LEFT
    count += checkDir(c+1, r+1, 1, 1, li) #DOWN/RIGHT
    return count

finished = False
while(not finished):
    finished = True
    newList = []
    for r in range(maxRow):
        s = ""
        for c in range(maxCol):
            if myList[r][c] != ".":
                total = countVisuals(c, r, myList)
                if total == 0:
                    s += ("#")
                elif total >= 5:
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

