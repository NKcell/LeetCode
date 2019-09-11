class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        length = len(flowerbed)
        flowerbed.append(0)
        prev = 0
        count = 0
        for i in range(length):
            if count == n:
                return True
            if flowerbed[i] == 1:
                prev = 1
                continue
            if flowerbed[i] == 0:
                if prev == 0:
                    if flowerbed[i+1] == 0:
                        count += 1
                        prev = 1
                        continue
                prev = 0

        if count == n:
                return True
        return False

###################################################################################
# 这个思路还是比我好很多，都想着去原列表首尾添0，但后面的判断，这个做法就好很多
def canPlaceFlowers1(self, flowerbed, n):
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        count = 0
        for f in flowerbed:
            if f == 0:
                count += 1
            else:
                count = 0
            if count == 3:
                n -= 1
                count = 1
            if n == 0:
                return True
        return False

a = Solution()
print(a.canPlaceFlowers([1,0,0,0,1], 2))
            
