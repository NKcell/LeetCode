class Solution:
    def relativeSortArray(self, arr1, arr2):
        from collections import OrderedDict
        mydict = OrderedDict()
        arr1.sort()
        for i in arr1:
            v = mydict.get(i, 0)
            mydict[i] = v+1
        
        loc = 0
        for i in arr2:
            count = mydict[i]
            while count>0:
                arr1[loc] = i
                count -= 1
                loc += 1
            mydict[i] = 0

        for i in mydict:
            count = mydict[i]
            while count>0:
                arr1[loc] = i
                count -= 1
                loc += 1
            mydict[i] = 0
        return arr1

    # 这个对sorted函数用的挺好的
    # key返回一个元组，两个值来进行比较，也是第一次见到这种操作
    def relativeSortArray1(self, arr1, arr2):
        def custom_sort(val):
            try:
                index = arr2.index(val)
                return (0, index)
            except ValueError:
                return (1, val)
        return sorted(arr1, key=custom_sort)

    # 这个用了很多自带的函数
    def relativeSortArray2(self, arr1, arr2):
        res = []
        for i in arr2:
            res = res + [i] * arr1.count(i)
        return res + sorted(filter(lambda x: arr2.count(x) == 0, arr1))

a = Solution()
print(a.relativeSortArray([28,6,22,8,44,17],[22,28,8,6]))