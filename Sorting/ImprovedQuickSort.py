import random


def Quick_Sort(A):
    if len(A) <= 1:
        return A

    q = random.randint(0, len(A) - 1)
    x = A[q]

    left = []
    mid = []
    right = []

    for n in A:
        if n < x:
            left.append(n)
        elif n > x:
            right.append(n)
        else:
            mid.append(x)

    left_sorted = Quick_Sort(left)
    right_sorted = Quick_Sort(right)

    return left_sorted + mid + right_sorted


n = int(input())
a = list(map(int, input().split()))
S = Quick_Sort(a);


print(" ".join(map(str, S)))