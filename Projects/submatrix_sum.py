# number of submatrices that sum to target
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        ylen = len(matrix)
        xlen = len(matrix[0])
        out = 0
        res = defaultdict(int)

        for row in matrix:
            for col in range(1, xlen):
                row[col] += row[col - 1]

        for j in range(xlen):
            for k in range(j, xlen):
                res.clear()
                res[0] = 1
                csum = 0

                for i in range(ylen):
                    csum += matrix[i][k] - (matrix[i][j - 1] if j else 0)
                    out += res[csum - target]
                    res[csum] += 1
        return out

a = Solution()
print(a.numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))
