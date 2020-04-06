class Solution:
    def findMinDifference(self, timePoints) -> int:
        timelist = list()
        for i in timePoints:
            h,m = i.split(':')
            timelist.append(int(h)*60+int(m))

        timelist.sort()
        minvalue = timelist[1]-timelist[0]
        for i in range(2, len(timelist)):    
            minvalue = min(timelist[i]-timelist[i-1], minvalue)

        return min(minvalue, 24*60+timelist[0]-timelist[-1])

    def findMinDifference1(self, timePoints):
        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        t.append(t[0] + 1440)
        return min(b - a for a, b in zip(t, t[1:]))