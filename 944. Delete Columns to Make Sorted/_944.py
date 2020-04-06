class Solution:
    def minDeletionSize(self, A) -> int:
        count = 0
        for i in range(len(A[0])):
            for j in range(1,len(A)):
                if A[j-1][i]>A[j][i]:
                    count+=1
                    break

        return count

a = Solution()
print(a.minDeletionSize(["cba","daf","ghi"]))
