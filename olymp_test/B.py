def ask(n):
    sign = n >= 0
    ans = ""
    s = abs(n)
    z = False

    if n == 0:
        return "0"

    while s != 1:
        r = s % 3
        if (s + 1) % 3 == 0:
            s += 1
            z = True
        if z:
            z = False
            if sign:
                ans = "$" + ans
            else:
                ans = "1" + ans
        elif r == 1:
            if sign:
                ans = "1" + ans
            else:
                ans = "$" + ans
        else:
            ans = "0" + ans
        s //= 3


    if sign:
        ans = "1" + ans
    else:
        ans = "$" + ans
    return ans


n = int(input())
print(ask(n))