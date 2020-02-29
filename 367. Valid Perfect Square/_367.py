class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        while start<=end:
            mid = (start+end)//2
            tmp = mid**2
            if tmp == num:
                return True
            if tmp > num :
                end = mid-1
            else:
                start = mid+1

        return False