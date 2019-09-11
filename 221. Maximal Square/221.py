"""
221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if len(matrix) == 0:
        return 0

    lengthl = len(matrix)
    lengthr = len(matrix[0])
    max_len = 0

    for i in range(lengthl-max_len):
        for j in range(lengthr-max_len):
            if matrix[i][j] == "1":
                while True:
                    flag = judge(matrix,i,j,max_len)
                    if flag == 1:
                        max_len = max_len+1
                    else:
                        break
    return max_len**2

def judge(matrix,i,j,max_len):
    lengthl = len(matrix)
    lengthr = len(matrix[0])

    for m in range(max_len+1):
        for n in range(max_len+1):
            if i+m > lengthl -1 or j+n > lengthr -1 or matrix[i+m][j+n] == "0":
                return 0
    return 1

print(maximalSquare([["1"]]))


"""
二维dp
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix: return 0
        m , n = len(matrix), len(matrix[0])
        dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
        
        res = max(max(row) for row in dp)
        return res ** 2
"""

"""
class Solution(object):
    def maximalSquare(self, matrix):
        if (not matrix) or (not matrix[0]):
            return 0
        n = len(matrix)
        m = len(matrix[0])
        widths = [0] * n
        k = 0
        for j in xrange(0, m):
            max_continous_k = 0
            continous_k = 0
            for i in xrange(0, n):
                if matrix[i][j] == '1':
                    widths[i] += 1
                else:
                    widths[i] = 0
                if widths[i] > k:
                    continous_k += 1
                    max_continous_k = max(continous_k, max_continous_k)
                else:
                    continous_k = 0
            if max_continous_k > k:
                k += 1
        return k * k
"""

"""
def maximalSquare(self, matrix):
    dp, maxArea = [[0 for _1_ in range(len(matrix[0]))] for ___ in range(len(matrix))], 0
    for i in xrange(0, len(matrix)):
        for j in xrange(0, len(matrix[0])):
            if i == 0 or j == 0:
                dp[i][j] = int(matrix[i][j])
            elif int(matrix[i][j]) == 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            maxArea = max(maxArea, dp[i][j])
    return maxArea*maxArea
We define dp[i][j] the maximal ending at position (i, j). Thus, current state (dp[i][j])depends on left (dp[i][j - 1]), up (dp[i - 1][j]), and left-up's (dp[i - 1][j - 1]) states. The current state equals to the minimum of these three states plus matrix[i][j] because any smaller value will lead to a smaller square (holes in somewhere). I use maxArea to track the maximal square. When matrix[i][j] == '0', the maximal square ending at position (i, j) is obviously 0.

Recurrence relation:

For matrix[i][j] == 1, dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + int(matrix[i][j]).

For matrix[i][j] == 0, dp[i][j] = 0
"""