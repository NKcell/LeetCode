class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        tmp = Counter(nums)
        index = 0
        for i in range(3):
            for _ in range(tmp[i]):
                nums[index] = i
                index+=1
    
    # 这相当于修改成特定字符，然后把这些特定字符再改为0，空间复杂度会减小
    def setZeroes(self, matrix):
        height = len(matrix)
        if(height ==0): return
        width = len(matrix[0])
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    for tmp in range(height):
                        if matrix[tmp][j] != 0:
                            matrix[tmp][j] = 'a'
                    for tmp in range(width):
                        if matrix[i][tmp] != 0: 
                            matrix[i][tmp] = 'a'

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0