class Solution:
    def stringMatching(self, words):
        tmp = ' '.join(words)

        res = [i for i in words if tmp.count(i)>=2]

        return res

a = Solution()
print(a.stringMatching(words = ["blue","green","bu"]))