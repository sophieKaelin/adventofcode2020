inFile = open("input/day03.txt")
myList = []
rows = 0

for line in inFile:
    rows +=1
    myList.append(line.replace("\n",""))

cols = len(myList[0])
print("ROWS: " + str(rows))
print("COLS: " + str(cols))

# combo = [column movement, row movement, totalTrees]
combos = [[1, 1, 0], [3, 1, 0], [5, 1, 0], [7, 1, 0], [1, 2, 0]]

for i in range(len(combos)):
    curRow = 0
    curCol = 0
    numTrees = 0

    while (curRow < rows):
        if(myList[curRow][curCol] == "#"):
            numTrees += 1
        curRow+=combos[i][1]
        curCol = (curCol + combos[i][0]) % cols
    combos[i][2] = numTrees
    print("You have hit " + str(combos[i][2]) + " trees")

print("Multiplication is: " + str(combos[0][2] * combos[1][2] * combos[2][2] * combos[3][2] * combos[4][2]))