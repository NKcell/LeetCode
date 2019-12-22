class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        count = 0
        while count*k<len(s):
            if (count+1)*k<len(s):
                self.myreverse(s,k*count,(count+1)*k)
            else:
                self.myreverse(s,k*count,len(s))
            count+=2
        return ''.join(s)

    def myreverse(self, s: list, start: int, end: int):
        for i in range(0, (end-start)//2):
            s[start+i],s[end-i-1] = s[end-i-1],s[start+i]

    def reverseStr1(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)

    def reverseStr2(self, s, k):
        slist = list(s)
        for i in range(0, len(s), 2*k):
            #slist[i:i+k] = reversed(slist[i:i+k])
            l=i;r=min(i+k-1, len(s)-1)
            while l<r:
                slist[l],slist[r]=slist[r],slist[l]
                l+=1;r-=1
        return "".join(slist)

    def reverseStr3(self, s, k):
        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k) if s else ""

a = Solution()
print(a.reverseStr1("abcdefg", k = 3))