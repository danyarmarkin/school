f = open("text.txt", "r")  # open file
index = 0
maxIndex = 0
maxLength = 0
lines = f.readlines()  # get all lines from file f
for line in lines:  # find max-length line
    if len(line) > maxLength:
        maxLength = len(line)
        maxIndex = index
    index += 1
fout = open("output_1.txt", "w")  # create or open output file
del lines[maxIndex]  # delete max-length line
fout.writelines(lines)  # write lines to output file
fout.close()
