import re

# Input File
myList = []
inFile = open("input/day02.txt")
for line in inFile:
    myList.append(line.replace("\n",""))

# When a password is split: vals[0] = min, vals[1] = max, vals[2] = character, vals[4] = password

part1Count = 0
part2Count = 0
for pwd in myList :
    vals = re.split("-| |:", pwd)
    
    # PART 1
    numChars = vals[4].count(vals[2])
    if numChars >= int(vals[0]) and numChars <= int(vals[1]) :
        part1Count +=1

    # PART 2
    firstPos  = vals[4][int(vals[0]) - 1] == vals[2]
    secondPos = vals[4][int(vals[1]) - 1] == vals[2]
    if firstPos != secondPos :
        part2Count +=1
            
print("PART1: There are: " + str(part1Count) + " corrupt passwords")
print("PART2: There are: " + str(part2Count) + " invalid passwords")