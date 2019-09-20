package leetcode

import(
	"sort"
)

func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	res := make([][]int, 0)
	numLen := len(nums)
	for i:=0; i<numLen-3; i++{
		if i>0 && nums[i] == nums[i-1]{
			continue
		}
		// 下面的两个判断在大量测试下还是很有效的，单看只有一个测试例子的压力测试是没有什么区别，甚至更差
		if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target {
			break
		}
		if nums[i]+nums[numLen-1]+nums[numLen-2]+nums[numLen-2] < target {
			continue
		}
		for j:=i+1; j<numLen-2; j++{
			if j>i+1 && nums[j] == nums[j-1]{
				continue
			}
			l, r := j+1, numLen-1
			for l<r{
				v := nums[i] + nums[j] + nums[l] +nums[r]
				if v>target{
					r--
					for l<r && nums[r] == nums[r+1]{
						r--
					}
				}else if v<target{
					l++
					for l<r && nums[l] == nums[l-1]{
						l++
					}
				}else{
					res = append(res, []int{nums[i], nums[j], nums[l], nums[r]})
					r--
					for l<r && nums[r] == nums[r+1]{
						r--
					}
					l++
					for l<r && nums[l] == nums[l-1]{
						l++
					}
				}
			}
		}
	}
	return res
}

// 递归的方法实现任意位数和求目标
func find(nums []int, target int, N int, result []int, results [][]int)[][]int{
	numsLen := len(nums)
	sort.Ints(nums)
	if N<2 || numsLen<N || nums[0]*N>target || nums[numsLen-1]*N<target{
		return results
	}
	if N == 2{
		l, r := 0, numsLen-1
		for l<r{
			v := nums[l] + nums[r]
			if v == target{
				results = append(results, append(result, nums[l], nums[r]))
				l ++
				r --
				for l<r && nums[l] == nums[l-1]{
					l++
				}
				for l<r && nums[r] == nums[r+1]{
					r--
				}
			}else if v > target{
				r--
				for l<r && nums[r] == nums[r+1]{
					r--
				}
			}else{
				l++
				for l<r && nums[l] == nums[l-1]{
					l++
				}
			}
		}
	}else{
		for i:=0; i<numsLen-N+1; i++{
			if i>0 && nums[i] == nums[i-1]{
				continue
			}
			tmp := append(result, nums[i])
			results = find(nums[i+1:], target-nums[i],N-1,tmp,results)
		}
	}
	return results
}

func fourSum1(nums []int, target int) [][]int {
	var result []int
	var results [][]int
	return find(nums, target, 4, result, results)
}