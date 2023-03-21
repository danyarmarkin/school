def t():
    x = "7y23x5"
    y = "67x9y"

    d = "0123456789a"
    for i in d:
        for j in d:
            a = int(x.replace("x", i).replace("y", j), 25)
            b = int(y.replace("x", i).replace("y", j), 11)

            if (a + b) % 131 == 0:
                print((a + b) // 131)
                return


t()  # 552647
