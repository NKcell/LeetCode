class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        flag = True
        for value in bits[:-1]:
            if value == 1:
                if flag == False:
                    flag = True
                else:
                    flag = False
            else:
                flag = True
        return flag

a = Solution()
print(a.isOneBitCharacter([1, 1, 0]))
