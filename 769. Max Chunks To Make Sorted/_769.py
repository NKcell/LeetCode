class Solution:
    def maxChunksToSorted(self, arr) -> int:
        index = 0
        count = 0
        while index<len(arr):
            tmp = max(arr[index: arr[index]+1])
            if arr[index] == tmp:
                count+=1
                index = arr[index]+1
            else:
                arr[index] = tmp

        return count

    def maxChunksToSorted1(self, arr):
        curMax, res = -1, 0
        for i, v in enumerate(arr):
            curMax = max(curMax, v)
            res += curMax == i
        return res

    def maxChunksToSorted2(self, A):
        return reduce(lambda (m, res), (i, v): (max(m, v), res + (max(m, v) == i)), enumerate(A), (-1, 0))[1]