class Solution:
    def maxDistToClosest(self, seats) -> int:
        import math
        start = -1
        start1 = -1
        maxlength = 0
        for index, value in enumerate(seats):
            if value == 1 and start1 == -1:
                start1 = index
            if value == 1:
                maxlength = max(maxlength, math.ceil((index-start-1)/2))
                start = index
        return max(maxlength, max(len(seats)-start-1, start1))

    def maxDistToClosest1(self, seats):
        res, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last) / 2)
                last = i
        return max(res, n - last - 1)

    def maxDistToClosest2(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # left记载当前位置左边第一个1的位置
        # count进行0的计数
        # _max_distance维护最大距离返回值
        left, count, _max_distance = -1, 0, 1
        for i, x in enumerate(seats):
            if x == 0:
                count += 1
            else:
                if left < 0:
                    # 左边没有1最大距离就是count
                    distance = count
                else:
                    # 左边有1最大距离就是一半左右
                    # 奇数个0正好在中间
                    # 偶数个0要比一半小1
                    distance = count // 2 + count % 2
                # 重置左边第一个1的位置
                # 遇到1重新计数0的个数
                left, count = i, 0
                # 更新最大距离
                _max_distance = max(_max_distance, distance)
        # 末尾一连串0的情况也可能刷新最大距离
        return max(_max_distance, count)

a = Solution()
print(a.maxDistToClosest([0,0,0,0,1,0,0,0]))