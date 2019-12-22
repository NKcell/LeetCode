class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        import collections
        tmp = collections.Counter(text)
        return min(tmp['b'], tmp['a'], tmp['l']//2, tmp['o']//2)


a = Solution()
print(a.maxNumberOfBalloons("loonbalxballpoon"))