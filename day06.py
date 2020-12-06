inFile = open("input/day06.txt")
myList = []

for line in inFile:
    myList.append(line.replace("\n",""))
myList.append("")

print("===== PART 1 =====")

charCount = [] 
Sum = 0

for entry in myList:
    if entry == "": # if at the end of a series, count how many letters.
        Sum += len(charCount)
        charCount = []
    else :
        for ch in entry:
            if ch in charCount:
                continue
            else:
                charCount.append(ch)

print(Sum)

print("===== PART 2 =====")

answerLists = [] 
Sum = 0
flag = True
count = 0

for entry in myList:
    if entry == "":
        for ch in answerLists[0]: # Check if characters from first item are in all other items in group
            for item in answerLists:
                if ch not in item:
                    flag = False # Indicates the loop was broken because character is not present in all entries
                    break
            if flag == True: # Checks whether loop was broken or completed. Completed means a character was found in each entry.
                count += 1
            else:
                flag = True
        Sum += count
        answerLists = []
        count = 0
    else : # add answers to the answer list until there is a line break
        answerLists.append(entry)

print(Sum)