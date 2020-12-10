import re

inFile = open("input/day07.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n","").replace(".", "").replace(" bags", "").replace(" bag", ""))

print("===== PART 1 =====")
data = {}

# Enter data into dictionary
for entry in myList:
    values = re.split(" contain |, ", entry)
    if values[1] is not "no other bags":
        data[values[0].replace(" bags", "")] = []
        for x in range(1, len(values)):
            data[values[0]].append(values[x][2:])

toCheck = ["shiny gold"]
checked = []

# Check through all the bags that contain silver gold or contain a bag that contains silver gold etc.
while len(toCheck) > 0:
    for item in data:
        if toCheck[0] in data[item]:
            if item not in checked:
                toCheck.append(item)
                checked.append(item)
    print(toCheck)
    toCheck.pop(0)

print("Outer Bags: " + str(len(checked)))

    