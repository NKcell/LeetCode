class Solution:
    def getRow(self, rowIndex: int):
        mylist = [1]
        for i in range(2,rowIndex+1):
            if i%2 == 1:
                mylist = self.mid(mylist)
            else:
                lastvalue = mylist[-1]*2
                mylist = self.mid(mylist)
                mylist.append(lastvalue)

        if rowIndex%2 == 1:
            tmp = mylist[:]
            tmp.reverse()
        else:
            tmp = mylist[:-1]
            tmp.reverse()

        try:
            return mylist+tmp
        except:
            return mylist
    
    def mid(self, mylist):
        tmp = mylist[:]
        for i in range(len(mylist)-1):
            tmp[i+1] = mylist[i] + mylist[i+1]
        return tmp

#####################################################################################
    
    # 好方法
    def getRow1(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

test = Solution()
print(test.getRow1(1))

"""
1.python 列表的复制 a = b[:]这样才能复制操作a不会影响b
2.再强调range(start, stop)，start开始数值（能取到），stop结束数值（取不到）

好方法可以看到，用的方法还是和118那道题一样，比如算[1,1]下面一个，就相当于[0,1,1]与[1,1,0]相加
这里好方法中用到了zip方法和列表生成式

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
我们可以使用 list() 转换来输出列表。    元素个数与最短的列表一致
与 zip 相反，zip(*) 可理解为解压

自己真的是莫名把题做复杂了
"""