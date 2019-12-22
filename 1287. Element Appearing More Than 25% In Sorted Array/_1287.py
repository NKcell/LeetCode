class Solution:
    def findSpecialInteger(self, arr) -> int:
        count = 1
        flag = len(arr)/4
        for i in range(1, len(arr)):
            if count>flag:
                return arr[i-1]
            if arr[i] == arr[i-1]:
                count+=1
            else:
                count=1
        return arr[-1]

    def findSpecialInteger1(self, arr):
        from collections import Counter
        return Counter(arr).most_common(1)[0][0]