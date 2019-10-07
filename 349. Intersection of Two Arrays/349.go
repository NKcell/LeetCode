package leetcode

func intersection(nums1 []int, nums2 []int) []int {
	mydict := make(map[int]int, 0)
	res := make([]int, 0)
	for _, v := range nums1{
		if _, ok := mydict[v]; !ok{
			mydict[v] = 1
		}
	}
	// 上面这样写更好
	// for i:=0;i<len(nums1);i++{
    //     mydict[nums1[i]]=1
    // }

	for _, v := range nums2{
		if dictv, ok := mydict[v]; ok&&dictv == 1{
			res = append(res, v)
			mydict[v] = 0
		}
	}
	return res
}