class Solution:
    # 没加set超时，加了set后就ok...
    def fairCandySwap(self, A, B):
        avg = (sum(A) + sum(B))/2
        dvalue = sum(A)-avg
        B = set(B)
        for i in set(A):
            if (i - dvalue) in B:
                return [i, int(i-dvalue)]

    def fairCandySwap1(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = (sum(A) - sum(B)) // 2
        A = list(map(lambda a: a - n, A))
        b = (list(set(A) & set(B)))[0]
        return [b + n, b]


a = Solution()
print(a.fairCandySwap([1,2,5],[2,4]))