"""
374. Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""

def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    minnum = 1
    maxnum = n

    while True:
        flag = (minnum + maxnum) // 2
        temp = guess(flag)
        if temp == 1:
            minnum = flag + 1
        if temp == -1:
            maxnum = flag - 1
        if temp == 0:
            return flag


"""
low = 1
        high = n
        while low <= high:
            mid = (low + high)//2
            res =  guess(mid)
            if res == 0 :
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1
"""

# 考虑数据溢出 low + (low + high)//2 主要用别的语言时要考虑