package leetcode

func canJump(nums []int) bool {
	numsLen := len(nums)-1
	startIndex := 0
	endIndex := nums[0]
	for{
		if endIndex>=numsLen{
			return true
		}
		bigvalue := -1
		for i:=startIndex; i<endIndex+1; i++{
			tmp := nums[i] + i
			if tmp>numsLen{
				return true
			}
			if tmp>bigvalue{
				bigvalue = tmp
			}
		}
		startIndex = endIndex
		endIndex = bigvalue
		if endIndex<=startIndex{
			return false
		}
	}
}

func canJump1(nums []int) bool{
	numsLen := len(nums)-1
	for i:=numsLen; i>=0; i--{
		if nums[i] + i >= numsLen{
			numsLen = i
		}
	}
	return numsLen == 0
}