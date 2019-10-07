package leetcode

func rob(nums []int) int {
	if len(nums) == 0{
		return 0
	}
	first := 0
	second := nums[0]
	for i:=1; i<len(nums); i++{
		if first + nums[i] > second{
			first, second = second, first+nums[i] 
		}else{
			first = second
		}
	}
	return second
}