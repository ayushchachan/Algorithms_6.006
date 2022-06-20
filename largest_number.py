import math
def prblm(A):
    salary = ""
    numberdict = partitiondict(A)
    l = list(numberdict.keys())[::2]
    l = sorted(l, reverse=True)
    for no in l:
        pseudodic = pseudodict(numberdict, no)

        for i in (sorted(pseudodic[1], reverse=True)):
            salary += pseudodic[0][i]
    return salary


def partitiondict(A):
    l = {}
    for no in A:
        try:
            l[str(no)[0]].append(str(no))
            if (no > l["maxl" + str(no)[0]]):
                l["maxl" + str(no)[0]] = int(math.log10(no)) + 1
        except:
            l[str(no)[0]] = [str(no)]
            l["maxl" + str(no)[0]] = int(math.log10(no)) + 1

    return l


def pseudodict(dic, value):
    d = {}
    li = []
    l = dic[value]
    lengthmax = dic["maxl" + value]
    for no in l:
        d[int(pseudonumber(no, lengthmax))] = no
        li.append(int(pseudonumber(no, lengthmax)))

    return (d, li)


def pseudonumber(value, max):
    no = value[0]
    while (len(value) < max):
        value += no
    return value


print(prblm([1,2,3,4,5,6,7,8,9,890,203,97,901,702,406]))