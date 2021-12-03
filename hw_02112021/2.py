p = list(map(int, input().split()))
a = set()
for i in p:
    if i in a:
        print("YES")
    else:
        print("NO")
        a.add(i)
