M = {1: 1, 2: 2, 3: 1, 4: 1}


def min_denomination(n):
    for i in range(1, n + 1):
        if i not in M:
            M[i] = 1 + min(M[i - 1], M[i - 3], M[i - 4])

    return M[n]


N = int(input())

print(min_denomination(N))
