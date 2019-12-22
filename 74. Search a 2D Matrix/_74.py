class Solution:
    def searchMatrix(self, matrix , target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False
        start, end, flag, mindex = 0, len(matrix)-1, 0, 0
        while start<=end:
            mid = (start+end)//2
            if matrix[mid][0]>target:
                end = mid-1
            elif matrix[mid][-1]<target:
                start = mid+1
            else:
                flag = 1
                mindex = mid
                break
        
        if flag == 0:
            return False

        start, end = 0, len(matrix[0])-1
        while start<=end:
            mid = (start+end)//2
            if matrix[mindex][mid]>target:
                end = mid-1
            elif matrix[mindex][mid]<target:
                start = mid+1
            else:
                flag = 0
                break

        if flag == 1:
            return False
        return True

    
    # 确实没必要像上面那样分成两个循环，看成一个整体来做就好了
    # 毕竟整体是递增的
    def searchMatrix1(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

    # 这里第一次见到bisect，算是在有序列表中插入，查找都很有用的一个模块吧
    # 里面有插入和查找的方法（左插右插都行）
    def searchMatrix2(self, matrix, target):
        import bisect
        i = bisect.bisect(matrix, [target])
        if i < len(matrix) and matrix[i][0] == target:
            return True
        row = matrix[i-1]
        j = bisect.bisect_left(row, target)
        return j < len(row) and row[j] == target