import math


class Solution:
    def countPrimes(self, n):
        notPrime = {}
        primeCount = 0

        for i in range(2, n):
            if i not in notPrime:
                primeCount += 1

                j = 2
                z = i*j
                while (z < n):
                    notPrime.add(z)
                    j += 1
                    z = i*j
