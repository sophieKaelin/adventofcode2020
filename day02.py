import re

print("\n========== INPUTING FILE ==========")

inFile = open("input/day02.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n",""))

print("========== PART 1 ==========")

# When a password is split:
# vals[0] = min, vals[1] = max, vals[2] = character, vals[4] = password

count1 = 0
count2 = 0
for pwd in myList :
    vals = re.split("-| |:", pwd)
    
    # PART 1
    numChars = vals[4].count(vals[2])
    if numChars >= int(vals[0]) and numChars <= int(vals[1]) :
        count1 +=1

    # PART 2
    firstPos  = vals[4][int(vals[0]) - 1] == vals[2]
    secondPos = vals[4][int(vals[1]) - 1] == vals[2]
    if firstPos != secondPos :
        count2 +=1
            
print("PART1: There are: " + str(count1) + " corrupt passwords")
print("PART2: There are: " + str(count2) + " invalid passwords")