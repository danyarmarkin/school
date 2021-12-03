f = open("text.txt", "r")  # open file
fout = open("output_2.txt", "w")  # create or open output file
ind = 1
for line in f.readlines():
    if ind % 2 == 0:
        fout.write(line)  # write line to fout file
    ind += 1
f.close()
