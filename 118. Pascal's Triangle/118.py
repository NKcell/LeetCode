from operator import add
class Solution:
    # 我的方法
    def generate(self, numRows: int):
        mylist = []
        for i in range(numRows):
            i += 1
            if i == 1:
                mylist.append([1])
                continue
            if i == 2:
                mylist.append([1,1])
                continue
            tmp = [1]
            # print(mylist)
            for j in range(i-2):
                tmp.append(mylist[i-2][j]+mylist[i-2][j+1])
            tmp.append(1)
            mylist.append(tmp)
        return mylist

    # 好方法
    def generate1(self, numRows):
        res = [[1]]
        for _ in range(1, numRows):
            map_ = map(add, [0] + res[-1], res[-1] + [0])
            res.append(list(map_))
        return res if numRows else []

i = Solution()
print(i.generate1(5))

"""
总结
1. 首先 range可以设置起始数字，我的方法中要自己去加1，不好   range(start, stop[, step])
2. 列表取最后一个，自己去计算长度了，不好，直接-1就OK了

别人的方法
首先思路上就很好，通过观察可以发现把上一个的值右移一位与自己相加就能得到结果
比如第三个值的上一个是[1,1] 就可以看作[1,1,0] + [0,1,1]
其次对方使用 _ 不用的参数就用这个不获取值
然后是map的使用，这里导入了add，也可以使用lambda lambda x, y: x+y
"""

