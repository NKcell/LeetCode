class Solution:
    def twoSum(self, numbers, target: int):
        for i in range(len(numbers)-1,0,-1):
            for j in range(len(numbers[:i])):
                if numbers[i]+numbers[j]>target:
                    break
                if numbers[i]+numbers[j] == target:
                    return [j+1,i+1]

    def twoSum1(self, numbers, target):
        pre = 0
        fin = len(numbers)-1
        while True:
            if numbers[pre]+numbers[fin]<target:
                pre+=1
            elif numbers[pre]+numbers[fin]>target:
                fin-=1
            else:
                return [pre+1, fin+1]
    
    # dictionary           
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
    
    # binary search        
    def twoSum3(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1


a = Solution()
print(a.twoSum1([-1,0],-1))