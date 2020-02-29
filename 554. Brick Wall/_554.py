class Solution:
    def leastBricks(self, wall) -> int:
        myDict = dict()
        for i in wall:
            tmp = 0
            for v in i[:-1]:
                tmp += v
                count = myDict.get(tmp, 0)
                count += 1
                myDict[tmp] = count

        if len(myDict) == 0:
            return len(wall)
        return len(wall) - max(myDict.values())

    def leastBricks1(self, wall):
        import collections
        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        # print len(wall), d
        return len(wall)-max(d.values()+[0])