op = {1: 0}

op_from = {1: 1}


def min_operation_to_reach(n):

    for x in range(1, n + 1):
        if x not in op:

            op_1 = op[x - 1]

            if x % 2 == 0:
                op_2 = op[x/2]
            else:
                op_2 = float('inf')

            if x % 3 == 0:
                op_3 = op[x/3]
            else:
                op_3 = float('inf')

            if op_1 == min(op_1, op_2, op_3):
                op[x] = 1 + op_1
                op_from[x] = x - 1

            if op_2 == min(op_1, op_2, op_3):
                op[x] = 1 + op_2
                op_from[x] = x//2

            if op_3 == min(op_1, op_2, op_3):
                op[x] = 1 + op_3
                op_from[x] = x//3

    y = n
    track_back = []
    while y != 1:
        track_back.append(y)
        y = op_from[y]
    track_back.append(1)
    return op[n], track_back


N = int(input())
min_op = min_operation_to_reach(N)
print(min_op[0])
for j in reversed(min_op[1]):
    print(j, end=" ")
