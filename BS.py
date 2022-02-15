from random import randint


def binarySearch(arr, l, r, x, k):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid, k
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x, k + 1)
        else:
            return binarySearch(arr, mid + 1, r, x, k + 1)
    return -1, k


a = sorted([randint(0, 10 ** 5) for _ in range(10 ** 7)])
# print(sorted(a))
s = randint(0, 10 ** 7 - 1)
print(s, a[s])
print(binarySearch(a, 0, len(a) - 1, a[s], 1))
