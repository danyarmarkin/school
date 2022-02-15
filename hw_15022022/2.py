print(max([sum(list(map(int, i.replace('\n', '').split()))) / 3 for i in open("output.txt", "r").readlines()]))
