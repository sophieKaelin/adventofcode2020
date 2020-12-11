import copy
inFile = open("input/day10.txt")
myList = [0]

for line in inFile:
    myList.append(int(line.replace("\n","")))
myList.sort()
print(myList)

print("===== PART 1 =====")
dif1, dif3 = 0, 1

for i in range(len(myList)-1):
    dif = myList[i+1] - myList[i]
    # print( str(myList[i+1]) + " - " + str(myList[i]) + " == " + str(myList[i+1] - myList[i]))
    if dif == 1:
        dif1 += 1
    else:
        dif3 += 1

print(dif1)
print(dif3)
print(dif1 * dif3)

print("===== PART 2 =====")

def part2(pos, li):
    # print("li: " + str(li))
    if len(li) < 3 or pos == len(li)-1:
        return 1
    if li[pos+1] - li[pos-1] <= 3: # Means you could keep or remove this item
        temp = copy.deepcopy(li)
        temp.pop(pos)
        return part2(pos, temp) + part2(pos+1, li)
    else:
        return part2(pos+1, li)
print(myList)
print(part2(1, myList))