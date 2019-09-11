class Solution:
    def sortArrayByParity(self, A):
        odd = list()
        for i, v in enumerate(A):
            if v%2 != 0:
                odd.append(i)
            else:
                if len(odd) != 0:
                    A[odd[0]], A[i] = v, A[odd[0]]
                    odd = odd[1:]
                    odd.append(i)
        return A

    # 这个想法挺容易懂得
    def sortArrayByParity1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        size = len(A)
        res = [None] * size
        start = 0
        end = size - 1
        for val in A:
            if val % 2 == 1:
                res[end] = val
                end = end -1
            else:
                res[start] = val
                start = start + 1
        return res
    
    # 很好的运用了sorted的方法，和值都为正数这一条件
    def sortArrayByParity2(self, A):
        return sorted(A, key=lambda x: x % 2)

        #return([i for i in A if i%2==0]+[i for i in A if i%2!=0])

        #return sorted(A, key=lambda x: x & 1) #beats 98% 这个与操作是很骚啊

a = Solution()
print(a.sortArrayByParity([1,2,3,4]))