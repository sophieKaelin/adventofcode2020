import re

inFile = open("input/day07.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n","").replace(".", "").replace(" bags", "").replace(" bag", ""))

print("===== PART 1 =====")
data1 = {}
data2 = {}

# Enter data into dictionary
for entry in myList:
    values = re.split(" contain |, ", entry)
    if values[1] != "no other":
        data1[values[0].replace(" bags", "")] = []
        data2[values[0].replace(" bags", "")] = []
        for x in range(1, len(values)):
            data1[values[0]].append(values[x][2:])
            data2[values[0]].append([values[x][0], values[x][2:]])

toCheck = ["shiny gold"]
checked = []

# Check through all the bags that contain silver gold or contain a bag that contains silver gold etc.
while len(toCheck) > 0:
    for item in data1:
        if toCheck[0] in data1[item]:
            if item not in checked:
                toCheck.append(item)
                checked.append(item)
    toCheck.pop(0)

print("Outer Bags: " + str(len(checked)))

print("===== PART 2 =====")

# DFS (sort of) starting from "shiny gold"
def nextBag(toCheck, data):
    total = 1
    if toCheck not in data: # Empty Bag isn't in the dictionary, end of bag sequence
        return total
    else :
        for bags in data[toCheck]: # Check each bag within the current bag, then check that bag, then ...
            total += int(bags[0]) * nextBag(bags[1], data)
        return total

print("The shiny gold bag contains " + str(nextBag("shiny gold", data2)) + " bags (including itself)")