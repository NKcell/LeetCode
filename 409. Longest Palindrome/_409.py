class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        myDict = Counter(s)
        flag = 0
        res = 0
        for i in myDict:
            if myDict[i]%2 == 0:
                res += myDict[i]
            else:
                if flag == 0:
                    flag += 1
                res += (myDict[i]-1)
        return res+flag

    #去重想集合
    def longestPalindrome1(self, s):
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)

    # 思想一样，更python
    def longestPalindrome2(self, s: str) -> int:
        from collections import Counter
        res, center, count = 0, False, Counter(list(s))
        for _, value in count.items():
            if not center and value % 2 == 1:
                center = True
            res += (value // 2) * 2

        return res if not center else res + 1
