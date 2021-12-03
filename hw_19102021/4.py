f = open("text.txt", "r")  # open file
fout = open("output_4.txt", "w")  # create or open output file
for line in f.readlines():
    if "procedure" in line:
        fout.write(line)  # write line to fout file
fout.close()
