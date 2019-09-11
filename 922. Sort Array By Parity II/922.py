class Solution:
    def sortArrayByParityII(self, A) :
        odd = list()
        even = list()
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        relist = list()
        for i in range(len(A)):
            if i%2==0:
                relist.append(even.pop())
            else:
                relist.append(odd.pop())
        return relist

    def sortArrayByParityII1(self, a):
        i = 0 # pointer for even misplaced
        j = 1 # pointer for odd misplaced
        sz = len(a)
        
        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens

        while i < sz and j < sz:
            if a[i] % 2 == 0:
                i += 2
            elif a[j] % 2 == 1:
                j += 2
            else:
                # a[i] % 2 == 1 AND a[j] % 2 == 0
                a[i],a[j] = a[j],a[i]
                i += 2
                j += 2

        return a

    # 和我的方法想法一样，但列表生成式用的很好
    def sortArrayByParityII2(self, A):
        even, odd = [a for a in A if not a % 2], [a for a in A if a % 2]
        return [even.pop() if not i % 2 else odd.pop() for i in range(len(A))]

a = Solution()
print(a.sortArrayByParityII([4,2,5,7]))