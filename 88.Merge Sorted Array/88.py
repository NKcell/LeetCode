def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """

    num = nums1[0:m] + nums2[0:n]
    num = sorted(num)

    if len(nums1) > len(nums2):
        for i in range(n+m):
            nums1[i] = num[i]
        print (nums1)
    else:
        for i in range(m+n):
            nums2[i] = num[i]

        print (sorted(nums2))


merge([0], 0, [1], 1)