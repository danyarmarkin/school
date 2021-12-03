p = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

fp = dict()
for i in range(int(input())):
    f, *per = input().split()
    fp[f] = set(per)

for i in range(int(input())):
    a, f = input().split()
    if p[a] in fp[f]:
        print('OK')
    else:
        print('Access denied')
