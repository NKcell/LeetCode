"""
278. First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    fir = 1
    fin = n

    while True:
        mid = (fir+fin)//2
        flag = isBadVersion(mid)

        if flag:
            flag2 = isBadVersion(mid-1)
            if mid!=1 and not flag2:
                return mid
            if mid == 1:
                return 1
            if flag2:
                fin = mid

        else:
            fir  = mid + 1

"""
def firstBadVersion(self, n):
        if n == 1:
            return 1
        low = 1
        high = n+1
        guess = int((high+low)/2)
        while high > low:
            if isBadVersion(guess) == True:
                if isBadVersion(guess-1) == False:
                    return guess
                else:
                    high = guess
                    guess = int((high + low)/2)
            else:
                low = guess
                guess = int((high+low)/2)
        return False
"""