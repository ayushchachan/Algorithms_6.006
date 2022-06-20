# filename = "test/inversions.txt"

# int_list = []

# fileReader = open(filename)

# l = fileReader.readline()
# while l != "":
#     l = l.strip()
#     int_list.append(int(l))
#     l = fileReader.readline()


def countInversions(A, p=0, r=None):
    if r is None:
        r = len(A)

    if (r - p <= 1):
        return 0

    q = (p + r) // 2
    a = countInversions(A, p, q)
    b = countInversions(A, q, r)

    # Now merging two sorted lists
    i, j, L, R = 0, 0, A[p: q], A[q: r]

    count = 0

    while (p < r):
        if (i == len(L)) or (j < len(R) and R[j] < L[i]):
            A[p] = R[j]
            count += len(L) - i
            j = j + 1
        else:
            A[p] = L[i]
            i = i + 1
        p = p + 1

    return a + b + count


n = int(input())
a = list(map(int, input().split()))
x = countInversions(a)
print(x)
