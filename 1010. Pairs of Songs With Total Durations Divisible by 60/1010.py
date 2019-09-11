class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        myDict = {}
        for i in time:
            v = myDict.get(i%60, 0)
            myDict[i%60] = v+1
        
        count = 0
        
        count += myDict.get(0, 0)*(myDict.get(0, 0)-1)//2
        count += myDict.get(30, 0)*(myDict.get(30, 0)-1)//2
        for i in range(1,30):
            count += myDict.get(i, 0)*myDict.get(60-i, 0)

        return count

    # 想法是类似的不过我用的是字典，这个用的是列表
    def numPairsDivisibleBy601(self, time):
        length = [0 for _ in range(60)]
        for t in time:
            length[t % 60] += 1

        ans = 0

        ans += length[0] * (length[0] - 1) // 2  # 0
        ans += length[30] * (length[30] - 1) // 2  # 30
        for idx in range(1, 30):
			# 1 to 29
            ans += length[idx] * length[60-idx]

        return ans

a = Solution()
print(a.numPairsDivisibleBy60([60,60,60]))