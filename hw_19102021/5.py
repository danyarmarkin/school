def aAmount(line):  # function to get amount of "a" in line
    count = 0
    for i in line:
        if i == "a":
            count += 1
    return count


f = open("text.txt", "r")  # open file
lines = f.readlines()  # get all lines from file f
maxIndex = 0
index = 0
maxA = 0
for line in lines:  # find max-a-amount line
    if aAmount(line) > maxA:
        maxIndex = index
        maxA = aAmount(line)
    index += 1
print(lines[maxIndex])  # print max-a-amount line
