import copy
import itertools

class Solution:
    def imageSmoother(self, M):
        import copy
        re_value = copy.deepcopy(M)
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                count = 0
                tmp = 0
                for a in range(i-1, i+2):
                    for b in range(j-1, j+2):    
                        if a>=0 and a<len(M) and b>=0 and b<len(M[0]):
                            tmp += M[a][b]
                            count += 1
                re_value[i][j] = tmp // count

        return re_value

    ##################################################
    #这个列表表达式用的很帅气
    def imageSmoother1(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        x_len = len(M)
        y_len = len(M[0]) if x_len else 0
        res = copy.deepcopy(M)
        for x in range(x_len):
            for y in range(y_len):
                neighbors = [
                    M[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < x_len and 0 <= _y < y_len
                ]
                res[x][y] = sum(neighbors) // len(neighbors)

    ###################################################
    # 这个列表表达式涉及的很巧妙，itertools.product用的很好，然后这里直接新生成了一个列表没用深拷贝，我看说测试比深拷贝快
    def imageSmoother2(self, M):
        R,C=len(M),len(M[0])
        M2=[[0]*C for i in range(R)]
        for i in range(R):
            for j in range(C):
                temp=[M[i+x][j+y] for x,y in list(itertools.product([-1,0,1],[-1,0,1])) if 0<=i+x<R and 0<=j+y<C ]
                M2[i][j]=(sum(temp)//len(temp))
        return M2

a = Solution()
print(a.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))

"""
首先还是列表拷贝的问题
使用 a[:], list(a), a*1, copy.copy(a)四种方式复制列表结果都可以得到一个新的列表，
但是如果列表中含有列表，所有b, c, d, e四个新列表的子列表都是指引到同一个对象上。
只有使用copy.deepcopy(a)方法得到的新列表f才是包括子列表在内的完全复制。

这里就是涉及到深拷贝和浅拷贝


"""