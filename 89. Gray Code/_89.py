class Solution:
    def grayCode(self, n: int):
        # nums = list(range(0, 2**n))
        # myDict = {}
        # for i in nums:
        #     tmp = myDict.get((bin(i).count('1')), 0)
        #     if tmp == 0:
        #         myDict[(bin(i).count('1'))] = [i]
        #     else:
        #         tmp.append(i)

        # print(myDict)
        # now = 0
        # min = 0
        # res = list()
        # for _ in range(len(nums)):
        #     tmp = myDict[now]

        #     tmpnum = tmp.pop()
        #     res.append(tmpnum)
        #     myDict[now] = tmp

        #     if len(tmp) == 0 and now == min:
        #         min += 1
        #         now += 1
        #         continue

        #     if min < now:
        #         now -= 1
        #     else:
        #         now += 1

        # return res
        res = [0]
        for i in range(0, n):
            res += [j+len(res) for j in res[::-1]]
        return res




a = Solution()
print(a.grayCode(1))