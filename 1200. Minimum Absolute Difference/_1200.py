class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        absolute = float("inf")
        for i in range(len(arr)-1):
            absolute = min(absolute, arr[i+1]-arr[i])
            if absolute == 1:
                break

        relist = []
        for i in range(len(arr)-1):
            if arr[i+1] == arr[i]+absolute:
                relist.append([arr[i], arr[i+1]])
        return relist

    # 很python的代码
    def minimumAbsDifference1(self, arr):
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]  

