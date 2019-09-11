class Solution:
    def majorityElement(self, nums) -> int:
        mymap = {}
        flag = len(nums)//2
        for i in nums:
            tmp = mymap.get(i, 0)+1
            if tmp > flag:
                return i
            mymap[i] = tmp

##########################################
    # 这个想法很棒啊，一个排序，然后我们要的元素数量超过一半，取中间的数就一定是那个数了
    def majorityElement1(self, nums) -> int:
        return sorted(nums)[len(nums)//2]

test = Solution()
print(test.majorityElement1([2,2,1,1,1,2,2]))

"""
dict: get(,)第二个参数可以设默认值
"""