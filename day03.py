import re

print("\n========== INPUTING FILE ==========")

inFile = open("input/day03.txt")
myList = []
rows = 0

for line in inFile:
    rows +=1
    myList.append(line.replace("\n",""))

cols = len(myList[0])
print("ROWS: " + str(rows))
print("COLS: " + str(cols))

print("========== PART 1 ==========")

curRow = 0
curCol = 0
numTrees = 0

while (curRow != rows):
    if(myList[curRow][curCol] == "#"):
        numTrees += 1
    curRow+=1
    curCol = (curCol + 3) % cols


print("You have hit " + str(numTrees) + " trees")

print("========== PART 2 ==========")

threeOne = numTrees
oneOne = 0
fiveOne = 0
sevenOne = 0
oneTwo = 0

combos = [[1, 1, 0], [5, 1, 0], [7, 1, 0], [1, 2, 0]]

for i in range(4):
    curRow = 0
    curCol = 0
    numTrees = 0

    while (curRow < rows):
        if(myList[curRow][curCol] == "#"):
            numTrees += 1
        curRow+=combos[i][1]
        curCol = (curCol + combos[i][0]) % cols
    combos[i][2] = numTrees

print("Multiplication is: " + str(combos[0][2] * combos[1][2] * combos[2][2] * combos[3][2] * threeOne))