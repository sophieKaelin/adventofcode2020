import math
import os

print("\n========== INPUTING FILE ==========")

inFile = open("input/day01.txt")
output = 0
myList = []

for line in inFile:
    output += 1
    temp = int(line.replace("\n",""))
    myList.append(temp)

print("Number of Items: " + str(output))
print("List: " + str(myList) + "\n")

print("========== PART 1 ==========")

for x in myList:
    for y in myList:
        if x + y == 2020:
            print('Found Pair: ')
            print(str(x)+' * '+str(y)+' = '+str(x*y)+"\n")
            

print("\n========== PART 2 ==========")

for x in myList:
    for y in myList:
        for z in myList:
            if x + y + z == 2020:
                print('Found Trio: ')
                print(str(x)+' * '+str(y)+' * '+str(z)+' = '+str(x*y*z)+"\n")