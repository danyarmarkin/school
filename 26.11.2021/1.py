def is_open(s):
    if s == "(" or s == "[" or s == "{":
        return True
    return False


def rev(s):
    if s == "}":
        return "{"
    if s == ")":
        return "("
    if s == "]":
        return "["


stack = []
s = str(input())
l = len(s)
if l == 0:
    print("yes")
for i in range(l):
    if is_open(s[i]):
        stack.append(s[i])
    else:
        if len(stack) == 0:
            print("no")
            break
        if stack[-1] == rev(s[i]):
            stack.pop()
        else:
            print("no")
            break

    if i == l - 1:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")