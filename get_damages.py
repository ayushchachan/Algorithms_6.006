def get_damages(H):
    '''
    Input:  H | list of bricks per house from west to east
    Output: D | list of damage per house from west to east
    '''
    D = [1 for _ in H]

    H2 = [(H[i], i) for i in range(len(H))];

    merge_sort(H2, 0, len(H), D);
    return D;

def merge_sort(A, p = 0, r = None, D = []):
    # print("------------merge_sort called with A =", A, ", D =", D, "---------")
    if r == None:
        r = len(A);

    if (r - p > 1):
        
        q = (p + r) // 2 ;
        merge_sort(A, p, q, D);
        merge_sort(A, q, r, D);

        # Now merging two sorted lists
        i, j, L, R = 0, 0, A[p : q], A[q : r];
        
        while (p < r):
            if (j == len(R)) or (i < len(L) and L[i][0] <= R[j][0]):
                A[p] = L[i];
                D[L[i][1]] += + j;
                i = i + 1;
            else:
                A[p] = R[j];
                j = j + 1;
            p = p + 1;

    # print("------------merge_sort terminated with A =", A, ", D =", D, "---------")

H = [34, 57, 70, 19, 48, 2, 94, 7, 63, 75]

answer = get_damages(H);
print(answer)

