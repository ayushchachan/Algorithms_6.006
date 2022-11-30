

class Solution:
    def numSquares(self, n):
        result = [i for i in range(n + 1)]
        
        i = 0
        i_square = i*i
        while i_square < n + 1:
            result[i_square] = 1
            i += 1
            i_square = i*i

        
        for i in range(2, n + 1):
            if result[i] != 1:
                for k in range(1, (i//2) + 1):
                    val1 = result[k]
                    val2 = result[i - k]
                    if val1 + val2 < result[i]:
                        result[i] = val1 + val2
        # print(result)
        return result[i]


n = 100
result = Solution().numSquares(n)

