class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        res = 0
        for i in range(1, len(points)):
            res += max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))
        return res

    def minTimeToVisitAllPoints1(self, p) -> int:
        return sum(max(abs(p[i][0] - p[i - 1][0]), abs(p[i][1] - p[i - 1][1])) for i in range(1, len(p)))

    def minTimeToVisitAllPoints2(self, points) -> int:
        return sum(max(abs(cur[0] - prev[0]), abs(cur[1] - prev[1])) for cur, prev in zip(points, points[1 :]))

    def minTimeToVisitAllPoints3(self, points) -> int:
        return sum(max(abs(c - p) for c, p in zip(cur, prev)) for cur, prev in zip(points, points[1 :]))