package leetcode
import(
	"strconv"
)

func summaryRanges(nums []int) []string {
    if len(nums) == 0{
		return []string{}
	}
	
	start := nums[0]
	last := nums[0]
	res := make([]string, 0, 1)

	for i:=1; i<len(nums); i++{
		if nums[i] == last+1{
			last = nums[i]
		}else{
			if start == last{
				res = append(res, strconv.Itoa(start))
			}else{
				res = append(res, strconv.Itoa(start)+"->"+strconv.Itoa(last))
			}
			start = nums[i]
			last = nums[i]
		}
	}
	if start == last{
		res = append(res, strconv.Itoa(start))
	}else{
		res = append(res, strconv.Itoa(start)+"->"+strconv.Itoa(last))
	}
	return res
}