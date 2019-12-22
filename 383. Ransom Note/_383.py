class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        rc = Counter(ransomNote)
        mc = Counter(magazine)
        mc.subtract(rc)
        
        for _, v in mc.items():
            if v<0:
                return False
        return True

    def canConstruct1(self, ransomNote, magazine):
        import collections
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

a = Solution()
print(a.canConstruct("aa","aab"))