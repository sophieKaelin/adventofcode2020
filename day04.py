import re

# Input File
myList = []
inFile = open("input/day04.txt")

for line in inFile:
    line = line.replace("\n","")
    lines = line.split(" ")
    for l in lines:       
        myList.append(l)

print(myList)

print("======= PART 1 =======")

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
data = {"byr" : False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False}
valids = 0

for entry in myList:
    if entry == "":
        if all(value == 1 for value in data.values()):
            valids += 1
            data = dict.fromkeys(data, False)
    elif entry[0:3] == "cid":
        continue
    elif entry[0:3] in fields:
        data[entry[0:3]] = True

print(data)
# if all(value == 1 for value in data.values()):
#     valids += 1

print("There are " + str(valids) + " valid passports")

print("======= PART 2 =======")

data = {"byr" : False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False}
eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valids = 0

for entry in myList:
    # WHAT ABOUT THE LAST ENTRY
    if entry == "":
        if all(value == 1 for value in data.values()):
            valids += 1
        data = dict.fromkeys(data, False)
    else:
        val = entry[4:]
        if entry[0:3] == "cid":
            continue
        elif entry[0:3] == "byr":
            if int(val) >= 1920 and int(val) <= 2002:
                data["byr"] = True
        elif entry[0:3] == "iyr":
            if int(val) >= 2010 and int(val) <= 2020:
                data["iyr"] = True
        elif entry[0:3] == "eyr":
            if int(val) >= 2020 and int(val) <= 2030:
                data["eyr"] = True
        elif entry[0:3] == "hgt":
            if "cm" in val:
                val = val.replace("cm", "")
                if int(val) >= 150 and int(val) <= 193:
                    data["hgt"] = True
            elif "in" in val :
                val = val.replace("in", "")
                if int(val) >= 59 and int(val) <= 76:
                    data["hgt"] = True
        elif entry[0:3] == "hcl":
            if(re.match(r'#[0-9A-Fa-f]{6}', val)):
                data["hcl"] = True
        elif entry[0:3] == "ecl":
            if val in eyes:
                data["ecl"] = True
        elif entry[0:3] == "pid": 
            if re.match(r'^[0-9]{9}$', val):
                data["pid"] = True

if all(value == 1 for value in data.values()):
    valids += 1

print("There are " + str(valids) + " valid passports")