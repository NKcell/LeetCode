package leetcode

func removeDuplicates(nums []int) int {
    if len(nums) == 0{
		return 0
	}

	i := 0
	fin := nums[len(nums)-1]
	flag := 0
	pre := nums[0]
	for i < len(nums){
		if nums[i] == pre{
			flag ++
		}else if nums[i] < pre{
			return i
		}else{
			flag = 1
		}

		pre = nums[i]


		if flag<3{
			i++
		}else{
			if nums[i] == fin{
				return i
			}
			for j:=i; j<len(nums)-1; j++{
				if nums[j]<=nums[j+1]{
					nums[j],nums[j+1] = nums[j+1],nums[j]
				}else{
					break
				}
			}
		}
	}
	return i
}