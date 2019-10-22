class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        res  = [intervals[0]]
        for i in intervals:
            if res[-1][-1]<i[0]:
                res.append(i)
            else:
                res[-1] = [res[-1][0], max(res[-1][-1], i[-1])]
        return res

    def merge1(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out