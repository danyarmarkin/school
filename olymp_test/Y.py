n, m = map(int, input().split())
island = [[i for i in input()] for _ in range(n)]
graph = [[False] * (m * n + 1) for _ in range(m * n + 1)]
graph_sum = [0] * (m * n + 1)

k = 0

for ni, i in enumerate(island):
    for mi, j in enumerate(i):
        if j == "N":
            ind = 1
            while island[ni - ind][mi] == "." and ni >= ind:
                ind += 1
            if ni - ind == -1:
                graph[k][-1] = True
            else:
                graph[k][mi + (ni - ind) * m] = True
                ind += 1
            graph_sum[k] += 1
            while ni >= ind:
                if island[ni - ind][mi] != ".":
                    graph[k][mi + (ni - ind) * m] = True
                    graph_sum[k] += 1
                ind += 1

        elif j == "W":
            ind = 1
            while island[ni][mi - ind] == "." and mi >= ind:
                ind += 1
            if mi - ind == -1:
                graph[k][-1] = True
            else:
                graph[k][k - ind] = True
                ind += 1
            graph_sum[k] += 1
            while mi >= ind:
                if island[ni][mi - ind] != ".":
                    graph[k][k - ind] = True
                    graph_sum[k] += 1
                ind += 1

        elif j == "S":
            ind = 1
            while island[(ni + ind) % n][mi] == "." and n - ni > ind:
                ind += 1
            if ni + ind >= n:
                graph[k][-1] = True
            else:
                graph[k][mi + (ni + ind) * m] = True
                ind += 1
            graph_sum[k] += 1
            while n - ni > ind:
                if island[(ni + ind) % n][mi] != ".":
                    graph[k][mi + (ni + ind) * m] = True
                    graph_sum[k] += 1
                ind += 1

        elif j == "E":
            ind = 1
            while island[ni][(mi + ind) % m] == "." and m - mi > ind:
                ind += 1
            graph[k][k + ind] = True
            ind += 1
            graph_sum[k] += 1
            while m - mi > ind:
                if island[ni][(mi + ind) % m] != ".":
                    graph[k][k + ind] = True
                    graph_sum[k] += 1
                ind += 1
        k += 1

for i in graph:
    print(*[int(j) for j in i])
print(graph_sum)


def amount(gs, v):
    if v == len(gs):
        s = 0
        for i in range(len(gs)):
            if graph[i][-1] > 0:
                s += amount(gs, i)
        return s
    gs[v] -= 1
    if gs[v] == 0:
        s = 1
        for i in range(len(gs)):
            if graph[i][v] > 0:
                s += amount(gs, i)
        return s
    return 0


print(amount(graph_sum, len(graph_sum)))
