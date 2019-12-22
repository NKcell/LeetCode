class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = list()
        for i in s:
            if 'z'>=i>='a' or 'Z'>=i>='A' or '9'>=i>='0':
                res.append(i.upper())

        print(res)
        l,r = 0, len(res)-1
        while l<r:
            if res[l] != res[r]:
                return False
            l+=1
            r-=1
        return True
    
    # 很好，我喜欢
    def isPalindrome1(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]

    # 这个和我go用的方法就类似了
    def isPalindrome2(self, s):
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True

a = Solution()
print(a.isPalindrome("0P"))