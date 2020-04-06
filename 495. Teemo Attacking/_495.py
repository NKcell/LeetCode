class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        res = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i-1]+duration < timeSeries[i]:
                res += duration
            else:
                res += (timeSeries[i]-timeSeries[i-1])
        if len(timeSeries)>=1:
            res += duration
        return res

    def findPoisonedDuration1(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1,len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans

    def findPoisonedDuration2(self, s, d):
        return sum(min(d, b - a) for a, b in zip(s, s[1:] + [10e7]))