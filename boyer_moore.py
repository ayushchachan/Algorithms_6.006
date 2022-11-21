def findPattern(T, P):
    """
    Returns the lowest index at which substring pattern begins in text (or else -1).
    """
    n = len(T)
    m = len(P)
    if m == 0:
        return 0
    last = {}
    for c in T:
        last[c] = -1
    for i in range(len(P)):
        last[P[i]] = i
    
    i = m - 1
    while (i < n):
        j = m - 1
        while (j >= 0 and P[j] == T[i + j + 1 - m]):
            j = j - 1
        if j < 0:
            return i - m + 1
        else:
            c = T[i + j + 1 - m]
            k = last[c]
            if k == -1:
                i = i + m
            elif k < j:
                i = i + (j - k)
            else:
                i = i + 1
    return -1

T = "abacaabadcabacabaabb"
P = "abacab"

z = findPattern(T, P)
print(z)