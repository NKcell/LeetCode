"""
447
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""

def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    import collections

    res = 0
    for p0 in points:
        distmap = collections.defaultdict(int)
        for p1 in points:
            dist = (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2
            distmap[dist] += 1
        for p in distmap:
            res += distmap[p] * (distmap[p] - 1)

    return res

print (numberOfBoomerangs([[0,0],[1,0],[2,0]]))


# 超时代码
"""
        if len(points) < 3:
            return 0

        bian = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                bian.append([[points[i],points[j]],(((points[i][0]- points[j][0])**2 + (points[i][1]- points[j][1])**2)**0.5)])

        num = 0
        for i in range(len(bian)):
            for j in range(i+1,len(bian)):
                if bian[i][0][0] == bian[j][0][1] or bian[i][0][0] == bian[j][0][0] or bian[i][0][1] == bian[j][0][1] or bian[i][0][1] == bian[j][0][0]:
                    if bian[i][1] == bian[j][1]:
                        num += 2

        return num
"""

# 优秀代码，思想和第一个代码是一样的
"""
        S=0
        for i in range(len(points)):
            s=0
            D=dict()
            for j in range(len(points)):
                d=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                if d in D and d!=0:
                    D[d]+=1
                else:
                    D[d]=1
            for a in D.values():
                s+=a*(a-1)
            S+=s
        return S
        
        
        
        Very straight forward solution. 3 ways to make it more concise:

No need to iterate on index
    for p in points:
Use default return value for dict. Below one line can reach the same goal as your 4 lines
    D[d] = D.get(d, 0) + 1
Local sum in the loop is unnecessary
"""