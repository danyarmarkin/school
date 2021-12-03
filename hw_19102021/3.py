f = open("text.txt", "r")  # open file
fout = open("output_3.txt", "w")  # create or open output file
fout.writelines(f.readlines())  # write lines from file f to output file
fout.write("\nend")  # write "end" on new line to fout file
fout.close()
