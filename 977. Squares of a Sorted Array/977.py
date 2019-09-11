class Solution:
    def sortedSquares(self, A):
        return sorted([i**2 for i in A])

    def sortedSquares1(self, A):
        answer = [0] * len(A)
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer

a = Solution()
print(a.sortedSquares( [-4,-1,0,3,10]))