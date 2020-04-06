class Solution:
    def sortByBits(self, arr):
        for i in range(len(arr)-1,0, -1):
            for j in range(0, i):
                if self.mysort(arr[j], arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def mysort(self,a, b):
        count1 = bin(a).count('1')
        count2 = bin(b).count('1')
        if count1 > count2:
            return True
        elif count1 < count2:
            return False
        else:
            return a>b

    def sortByBits1(self, A):
        return sorted(A, key=lambda a: [bin(a).count('1'), a])