package leetcode

func intersect(nums1 []int, nums2 []int) []int {
	myDict := make(map[int]int, 0)
	res := make([]int, 0)
	for _, v := range nums1{
		if _, ok := myDict[v]; ok{
			myDict[v]++
		}else{
			myDict[v]=1
		}
	}

	// map取不到值时，用的是默认值，比如这里的int就默认是0了，所以下面的写法更简洁
	// for _, n := range nums1 {
	// 	myDict[n]++
	// }

	for _, v := range nums2{
		if dictv, ok := myDict[v]; ok&&dictv!=0{
			myDict[v]--
			res = append(res, v)
		}
	}
	return res
}