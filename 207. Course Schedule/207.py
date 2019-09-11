"""
207
"""

"""
def canFinish(numCourses, prerequisites):

    not_root = []
    for i in prerequisites:
        not_root.append(i[0])

    root = []
    for i in range(numCourses):
        if i in not_root:
            pass
        else:
            root.append(i)

    if len(root) == 0:
        return False
    return huan(root, prerequisites)

def huan(root, prerequisites):
    for i in root:
        re = panduan(i,prerequisites,[i])
        if re == 1:
            return False

    return True

def panduan(root, prerequisites, old):
    new = []
    for i in prerequisites:
        if i[1] == root:
            new.append(i[0])

    for i in new:
        if i in old:
            return 1

    if len(new) != 0:
        for i in new:
            re = panduan(i, prerequisites, old+new)
            if re == 1:
                return 1

    return 0

print(canFinish(2, [[1,0],[2,0],[1,2]]))
"""


# 超时， 拓扑排序
"""
def canFinish(numCourses, prerequisites):
    nr = list(range(numCourses))
    return(hexin(nr, prerequisites))


def hexin(nr, prerequisites):
    while True:
        not_root = []
        for i in prerequisites:
            if i[1] in nr:
                not_root.append(i[0])

        root = []
        for i in nr:
            if i in not_root:
                pass
            else:
                root.append(i)
                nr.remove(i)

        if len(root) == 0 and len(nr) != 0:
            return False

        if len(root) == 0 and len(nr) == 0:
            return True
"""


# 利用入度和出度解决（核心也是拓扑排序，图论算法）
def canFinish(n, pres):
    rudu = []
    chudu = []
    for i in range(n):
        rudu.append(0)
    for i in range(n):
        chudu.append([])

    for i in pres:
        rudu[i[1]] += 1
        chudu[i[0]].append(i[1])

    dq = []
    for i in range(n):
        if rudu[i] == 0:
            dq.append(i)

    num = 0
    while dq:
        x = dq.pop(0)
        num += 1
        for i in chudu[x]:
            rudu[i] -= 1
            if rudu[i] == 0:
                dq.append(i)

    return num == n


print (canFinish(2,[[1,0],[0,1]]))