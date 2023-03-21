i = 103

while i < 10e9:
    s = [j for j in str(i)]
    if s == sorted(s) and len(s) == len(set(s)):
        print(i, i // 103)
    i += 103
