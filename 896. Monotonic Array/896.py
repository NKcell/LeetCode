class Solution:
    def isMonotonic(self, A) -> bool:
        flag = 0
        pre = A[0]
        for i in A:
            if i>pre:
                if flag == -1:
                    return False
                pre = i
                flag = 1
            elif  i<pre:
                if flag == 1:
                    return False
                pre = i
                flag = -1
            else:
                pre = i
        return True
    

a = Solution()
print(a.isMonotonic([1,1,1]))