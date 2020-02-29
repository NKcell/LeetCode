class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        while n>=0:
            count += 1
            n -= count 
            
        return count-1

    def arrangeCoins1(self, n):
        start = 1
        end = n
        while end >= start:
            mid = (start+end)//2
            total = mid*(mid+1)//2
            if total == n:
                return mid
            elif total<n:
                start = mid + 1
            else:
                end = mid - 1
        return end