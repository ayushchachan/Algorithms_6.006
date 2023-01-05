#  implementation of various sorting algorithms

import random


def merge_sort(A, p=0, r=None):
    if r is None:
        r = len(A)

    if (r - p > 1):

        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q, r)

        # Now merging two sorted lists
        i, j, L, R = 0, 0, A[p: q], A[q: r]



        while (p < r):
            if (j == len(R)) or (i < len(L) and L[i] <= R[j]):
                A[p] = L[i]
                i = i + 1
            else:
                A[p] = R[j]
                j = j + 1
            p = p + 1


l = [random.randint(1, 30) for i in range(30)]
print("l =", l)

merge_sort(l)
print(l)
