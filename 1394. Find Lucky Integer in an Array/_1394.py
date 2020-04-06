class Solution:
    def findLucky(self, arr) -> int:
        import collections
        myDict = collections.Counter(arr)

        for v in myDict.most_common():
            if v[0] == v[1]:
                return v[0]

        return -1




a = Solution()
print(a.findLucky([7,7,7,7,7,7,7]))