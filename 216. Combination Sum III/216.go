package leetcode

func combinationSum3(k int, n int) [][]int {
    res := make([][]int, 0)
	if k>9 || n/k > 9{
		return res
	}
	for i:=1; i<10; i++{
		tmp := make([]int, 0)
		tmp = append(tmp, i)
		mysum(k-1, n-i, i, &res, &tmp)
	}
	return res
}

func mysum(k int, n int, min int, res *[][]int, tmp *[]int){
	if k == 0 && n == 0{
		*res = append(*res, *tmp)
		return
	}
	if k == 0 || n<1{
		return
	}
	for i:=min+1; i<10; i++{
		tmp1 := make([]int, len(*tmp))
		copy(tmp1, *tmp)
		tmp1 = append(tmp1, i)
		mysum(k-1, n-i, i, res, &tmp1)
	}
}

func combinationSum3_1(k int, n int) [][]int {
    res, nums := make([][]int, 0), []int{1,2,3,4,5,6,7,8,9}
    solution(nums, n, k, 0, []int{}, &res)
    return res
}
/*
*times 还可以添加几个数
*pos 下一个将添加的元素下标,通过+1去重
*ans 当前一种解
*res 所有可能解
 */
func solution(nums []int, target int, times int, pos int, ans []int, res *[][]int) {   
    if times == 0 {
        if target == 0  {
            *res = append(*res, append([]int{}, ans...))
        }
        return
    }
    for i := pos; i < len(nums); i++ {
        if target- nums[i] >= 0 {
            solution(nums, target - nums[i], times - 1, i + 1, append(ans, nums[i]), res)
        } 
    }  
}