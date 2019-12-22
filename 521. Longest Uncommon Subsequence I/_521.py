# 这道题的难点在理解题意吧，感觉理解对了都不相信是这样理解...
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:
            return -1
        return max(len(a),len(b))

    def findLUSlength1(self, a, b):
        return -1 if a==b else max(len(a), len(b))