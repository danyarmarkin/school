spisok=(filter(lambda x: x>=1600 and x<=1800,list(map(int,input().split()))))
print(spisok)
print(*spisok)
#print(list(filter(lambda line: len(line)==1,
print(list(map(lambda t: list(filter(lambda x: x>t,spisok)),spisok)))