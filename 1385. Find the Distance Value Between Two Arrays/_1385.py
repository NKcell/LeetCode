class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in arr1:
            flag = 1
            for j in arr2:
                if abs(i-j)<=d:
                    flag = 0
                    break
            if flag:
                count += 1

        return count

    def findTheDistanceValue1(self, A, B, d):
        return sum(all(abs(a - b) > d for b in B) for a in A)

    def findTheDistanceValue2(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
            
        def is_valid(val):
            l, r = 0, len(arr2)
            while l < r:
                mid = (l + r) // 2
                if abs(arr2[mid] - val) <= d:
                    return False
                elif arr2[mid] > val:
                    r = mid
                else:
                    l = mid + 1
            return True

        return sum(is_valid(x) for x in arr1)
