def squared_distance(p, q):
    '''Returns the squared distance between points p and q'''
    (px, py), (qx, qy) = p, q
    return (px - qx)**2 + (py - qy)**2


def base_case(points):

    if len(points) == 2:
        p1, p2 = points
        return squared_distance(p1, p2)

    if len(points) == 3:
        p1, p2, p3 = points
        return min(squared_distance(p1, p2),
                squared_distance(p1, p3),
                squared_distance(p2, p3))
    raise Exception("invalid arguments")


def closest_pair_in_strip(delta, strip):
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[i][1] - strip[j][1])**2 >= delta:
                break
            delta = min(delta, squared_distance(strip[i], strip[j]))
    return delta


def closest_pair_sorted_x(points):
    if len(points) <= 3:
        return base_case(points)

    mid = len(points) // 2

    d1 = closest_pair_sorted_x(points[0: mid])
    d2 = closest_pair_sorted_x(points[mid: len(points)])

    d = min(d1, d2)

    mid_x = points[mid][0]

    strip = [p for p in points if (p[0] - mid_x)**2 < d]
    return min(d, closest_pair_in_strip(d, strip))


def closest_pair(points):
    '''
    Input:  points | tuple of at least 2 points of the form (x, y)
    Output: smallest squared distance between any pair of points
    '''
    sorted_by_x = sorted(points, key=lambda p: p[0])
    return closest_pair_sorted_x(sorted_by_x)


N = int(input("Enter no of points:"))

POINTS = []
for i in range(N):
    p = tuple(map(int, input().split(" ")))
    POINTS.append(p)

print(closest_pair(POINTS)**(0.5))
