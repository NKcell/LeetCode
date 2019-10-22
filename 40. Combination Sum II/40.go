package leetcode

import(
	"sort"
)

func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	res := make([][]int, 0)
	tmp := make([]int, 0)
	findNum(candidates, target, &res, tmp)
	return res
}

func findNum(nums []int, target int, res *[][]int, tmp []int) {
	for i, v := range nums{
		if i != 0 && v == nums[i-1]{
			continue
		}
		if v > target{
			return
		}else if v == target{
			// tmp1 := make([]int, 0, len(tmp)+1)
			// tmp1 = append(tmp1, tmp...)
			// tmp1 = append(tmp1, v)
			*res = append(*res, append(tmp, v))
			return
		}else{
			// tmp1 := make([]int, 0, len(tmp)+1)
			// tmp1 = append(tmp1, tmp...)
			// tmp1 = append(tmp1, v)
			findNum(nums[i+1:], target-v, res, append(tmp, v))
		}
	}
}

func combinationSum2_1(candidates []int, target int) [][]int {
    sort.Ints(candidates)
    result := make([][]int, 0)
    combinationSum2Helper(candidates, target, []int{}, &result)
    return result
}

func combinationSum2Helper(candidates []int, target int, current []int, result *[][]int) {
	if target <= 0 || len(candidates) == 0 {
		return
	}
	for i, v := range candidates {
        if v >= target {
            if v == target {
                *result = append(*result, append(current, v))
            }
            break
        } else if i != 0 && (i == len(candidates)-1 || candidates[i] != candidates[i+1]) {
            combinationSum2Helper(candidates[:i], target-v, append(current, v), result)
        }
	}
	return
}