package leetcode

func sortColors(nums []int)  {
	tmp := make(map[int]int, 3)
	for _, v := range nums{
		tmp[v]++
	}

	index := 0
	for i:=0; i<3; i++{
		for j:=0; j<tmp[i];j++{
			nums[index] = i
			index ++
		}
	}
}