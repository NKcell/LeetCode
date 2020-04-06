class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        start = nums[0]
        last = nums[0]
        res = list()
        for i in nums[1:]:
            if i == last+1:
                last = i
            else:
                if last == start:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(last))
                start = i
                last = i

        if last == start:
            res.append(str(start))
        else:
            res.append(str(start)+'->'+str(last))

        return res

    def summaryRanges1(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]