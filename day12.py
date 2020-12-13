inFile = open("input/day12.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n",""))
print(myList)

print("===== PART 1 =====")

curDeg = 90
curDir = "E"
degs = {"N": 0, "E": 0, "S": 0, "W": 0}

def getDeg(deg):
    if(deg == 0):
        return "N"
    elif(deg == 90):
        return "E"
    elif(deg == 180):
        return "S"
    else:
        return "W"

for instruction in myList:
    i = instruction[0]
    mv = int(instruction[1:])
    if(i == "F"):
        degs[curDir] += mv
    elif(i in degs):
        degs[i] += mv
    elif(i == "L"):
        curDeg = (curDeg - mv) % 360
        curDir = getDeg(curDeg)
    elif(i == "R"):
        curDeg = (curDeg + mv) % 360
        curDir = getDeg(curDeg)

print(abs(degs["N"] - degs["S"]) + abs(degs["E"] - degs["W"]))

print("===== PART 2 =====")

curWay = [10, 1]
curDeg = [90, 0]
curDir = ["E", "N"]
degs = {"N": 0, "E": 0, "S": 0, "W": 0}

def getOpp(l):
    if(l == "S"):
        return "N"
    elif(l == "W"):
        return "E"
    elif(l == "N"):
        return "S"
    else:
        return "W"

for instruction in myList:
    i = instruction[0]
    mv = int(instruction[1:])
    if(i == "F"):
        degs[curDir[0]] += curWay[0] * mv
        degs[curDir[1]] += curWay[1] * mv
    elif(i == "L"):
        curDeg = [(i - mv)%360 for i in curDeg] 
        curDir[0] = getDeg(curDeg[0])
        curDir[1] = getDeg(curDeg[1])
    elif(i == "R"):
        curDeg = [(i + mv)%360 for i in curDeg] 
        curDir[0] = getDeg(curDeg[0])
        curDir[1] = getDeg(curDeg[1])
    elif(i in curDir):
        curWay[curDir.index(i)] += mv
    else:
        curWay[curDir.index(getOpp(i))] -= mv

print(abs(degs["N"] - degs["S"]) + abs(degs["E"] - degs["W"]))

