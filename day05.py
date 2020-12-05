inFile = open("input/day05.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n",""))

print("===== PART 1 =====")

seats = []
biggest = 0

for entry in myList:
    maxR, maxC, minR, minC, row, col = 127, 7, 0, 0, 0, 0
    for x in range(7): # First 7 characters for row
        mid = (minR + maxR)/2
        if entry[0] == "F":
            row = maxR = mid
        else :
            row = minR = mid + 1
        entry = entry[1:]   
    for x in range(3): # Last 3 characters for column
        mid = (minC + maxC)/2
        if entry[0] == "L":
            col = maxC = mid
        else :
            col = minC = mid + 1
        entry = entry[1:]
    biggest = max(biggest, (row * 8 + col))
    seats.append(row*8+col)

print("biggest seat ID is: " + str(biggest))

print("===== PART 2 =====")
seats.sort()

for i in range(len(seats) - 2):
    if(seats[i+1] - seats[i] == 1):
        continue
    else:
        print("seat is: " + str(seats[i] + 1))
        break