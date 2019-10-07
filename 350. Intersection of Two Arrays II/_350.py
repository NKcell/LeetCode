class Solution:
    def intersect(self, nums1, nums2):
        from collections import Counter
        res = list()
        mydict = Counter(nums1)
        for i in nums2:
            if mydict[i]:
                res.append(i)
                mydict[i]-=1
        return res

    # 这种双指针的思路，对于两个有序的列表是有不错的效果的
    def intersect1(self, nums1, nums2):
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []
        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break
        return res