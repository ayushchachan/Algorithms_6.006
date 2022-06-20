
def get_intervals(segment_list):
    point_set = set()
    start_map, end_map = {}, {}

    for a, b in segment_list:
        point_set.add(a)
        point_set.add(b)

        if a in start_map:
            start_map[a] += 1
        else:
            start_map[a] = 1

        if b in end_map:
            end_map[b] += 1
        else:
            end_map[b] = 1

    all_points = sorted(list(point_set))
    # print("all_points =", all_points)
    # print("start_map = ", start_map)
    # print("end_map =", end_map)
    answer = []

    i_start_map = all_points[0]
    i_end_map = None
    val = start_map[i_start_map]

    for j in range(1, len(all_points)):
        p = all_points[j]
        i_end_map = p

        if val != 0:
            answer.append((i_start_map, i_end_map, val))

        i_start_map = i_end_map

        if p in start_map:
            val += start_map[p]

        if p in end_map:
            val -= end_map[p]
    print("intervals = ", answer)
    return answer


def binary_search2(x, intervals):
    print("binary search for ", x)
    p, r = 0, len(intervals)

    while p < r:
        q = (p + r) // 2

        s, e, v = intervals[q]
        if s <= x <= e:
            print("found at index", q)

            if x == s and q > 0:
                return intervals[q - 1][2] + v

            if x == e and q < len(intervals) - 1:
                return intervals[q + 1][2] + v

            return v

        elif x < s:
            r = q
        else:
            p = q + 1
    return 0


def intersect_segments(segment_list, point_list):
    I = get_intervals(segment_list)

    answer_list = []

    for p in point_list:
        j = binary_search2(p, I)

        answer_list.append(j)

    print(" ".join(list(map(str, answer_list))))


s, p = list(map(int, input().split()))

segments = []


for i in range(s):
    segments.append(tuple(map(int, input().split())))

points = list(map(int, input().split()))

intersect_segments(segments, points)
