class Solution:
    def hIndex(self, citations) -> int:   
        citations.sort()
        for i in range(len(citations),0,-1):
            if self.getindex(citations, i):
                return i

        return 0

    def getindex(self, citations, i):
        lens = len(citations)
        l = 0
        r = lens-1
        while l<=r:
            if lens-l<i:
                return 0
            mid = (l + r)//2
            if i == citations[mid]:
                while mid!=0 and i == citations[mid-1]:
                    mid -= 1
                if mid == 0:
                    return 1
                return lens-mid>=i
            if i < citations[mid]:
                if mid == 0:
                    return 1
                elif i>citations[mid-1]:
                    return lens-mid>=i
                else:
                    r = mid-1
            if i > citations[mid]:
                if mid == lens-1:
                    return 0
                elif i<citations[mid+1]:
                    return lens-mid-1>=i
                else:
                    l = mid+1

    def hIndex1(self, citations):
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= (n-i):
                return n-i
        return 0

    def hIndex2(self, citations):
        n = len(citations)
        citeCount = [0] * (n+1)
        for c in citations:
            if c >= n:
                citeCount[n] += 1
            else:
                citeCount[c] += 1
        
        i = n-1
        while i >= 0:
            citeCount[i] += citeCount[i+1]
            if citeCount[i+1] >= i+1:
                return i+1
            i -= 1
        return 0

a = Solution()
print(a.hIndex([7,7,7,7,7,7,7]))