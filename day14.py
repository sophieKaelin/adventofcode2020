import re
inFile = open("input/day14.txt")
myList = []
changes = {}

# Input the memory changes
for line in inFile:
    myList.append(line.replace("\n",""))
    
print("~~ PART 1 ~~")
vals = {}

for num in myList:
    if "mask" in num:
        changes={}
        # Input mask and determine which bits change
        mask = num[7:].replace("\n","")
        for i in range(len(mask)):
            if mask[i] != "X":
                changes[36-i] = mask[i]
    else:
        items = re.split(" |] ", num)
        idx = items[0][4:]
        binNum = list('{0:036b}'.format(int(items[2])))
        for e in changes:
            binNum[36-e] = changes[e]
        vals[idx] = int("".join(binNum), 2)

total = 0
for nums in vals:
    total += vals[nums]
print(total)

print("~~ PART 2 ~~")

