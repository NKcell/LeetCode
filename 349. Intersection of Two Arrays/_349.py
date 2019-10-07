class Solution:
    def intersection(self, nums1, nums2):
        mydict = {}
        res = list()

        for i in nums1:
            mydict[i] = 1
        
        for i in nums2:
            v = mydict.get(i, 0)
            if v != 0:
                res.append(i)
                mydict[i] = 0

        return res

    # 去重要想到set
    def intersection1(self, nums1, nums2):
        return list(set(nums1) & set(nums2))