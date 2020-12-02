import re

print("\n========== INPUTING FILE ==========")

inFile = open("input/day03.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n",""))

print("========== PART 1 ==========")