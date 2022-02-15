print((lambda a: (lambda x: len(a) - x if x % 2 != 0 else x)(len(list(filter(lambda x: x % 2 != 0, a)))))(list(map(int, input().split()))))
