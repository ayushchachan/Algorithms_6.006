
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def gcd1(a, b):
    if a % b == 0:
        return b
    return gcd1(a, a % b)

import random

n1 = random.randint(1, 1000)
n2 = random.randint(1, 1000)
print((n1, n2))
print(gcd(n1, n2))
print(gcd1(n1, n2))
