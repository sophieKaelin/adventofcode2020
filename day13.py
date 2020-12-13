inFile = open("input/day13.txt")
start = inFile.readline()
start = int(start)
inp = ""

for line in inFile:
    inp = line.replace("\n","")
inpt = inp.replace(",x", "")
myList = inpt.split(",")
myList2 = inp.split(",")
myList = [int(i) for i in myList]

print(myList)

print("===== PART 1 =====")

found = False
cur = int(start)
id = 0
while(not found):
    for num in myList:
        if cur % num == 0:
            found = True
            id = num
            break
    cur+=1

print(id * (cur-1 - start))