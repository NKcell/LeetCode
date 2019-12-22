class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start<end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                return self.lala(s, start+1, end) or self.lala(s, start, end-1)
        return True


    def lala(self, s:str, start:int, end:int) -> bool:
        while start<end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        
        return True

    def validPalindrome1(self, s):
        i = 0
        while i < len(s) / 2 and s[i] == s[-(i + 1)]: i += 1
        s = s[i:len(s) - i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]