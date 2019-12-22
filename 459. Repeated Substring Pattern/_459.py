class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2,0,-1):
            if len(s)%i == 0 and s[:i]*(len(s)//i) == s:
                return True
        
        return False
    
    def repeatedSubstringPattern1(self, str):
        if not str:
            return False
            
        ss = (str + str)[1:-1]
        return ss.find(str) != -1

        # 和上面一样，但这个更python
        # ss = (str*2)[1:-1]
        # return str in ss

a = Solution()
print(a.repeatedSubstringPattern("aa"))