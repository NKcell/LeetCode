class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        myDict = Counter(s)
        for i, v in enumerate(s):
            if myDict[v] == 1:
                return i
        return -1

    # 这就是以前说过的在有限已知的元素（比如这里的小写字母）可以使用列表
    def firstUniqChar1(self, s):
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1