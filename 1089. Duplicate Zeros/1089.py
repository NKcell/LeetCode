class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        tmp = list()
        for i,v in enumerate(arr):
            if v==0:
                tmp.append(0)
                tmp.append(0)
            else:
                tmp.append(v)

            arr[i] = tmp[i]
                

a = Solution()
arr = [1,2,3]
a.duplicateZeros(arr)
print(arr)