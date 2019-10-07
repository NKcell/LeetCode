package leetcode

import(
	"sort"
)

func combinationSum(candidates []int, target int) [][]int {
	res := make([][]int, 0)
	sort.Ints(candidates)
	dfs(candidates, target, &res, []int{})
	return res
}

func dfs(candidates []int, target int, res *[][]int, tmp []int){
	if target<0{
		return
	}
	if target == 0{
		*res = append(*res, tmp)
		return
	}
	for i, v := range(candidates){
		if v>target{
			return
		}
		tmp1 := make([]int, 0, len(tmp))
		tmp1 = append(tmp1, tmp...)
		tmp1 = append(tmp1, v)
		dfs(candidates[i:], target-v, res, tmp1)
	}
}

func combinationSum1(candidates []int, target int) [][]int {//最简单的想法，直接回溯剪枝
    sort.Ints(candidates)//排个序就能节省大量的去重过程
    var results [][]int
    var result []int
    var sum int
    find(candidates,target,&result,&results,sum)
    return results
}

func find(candidates []int,target int,result *[]int,results *[][]int,sum int){
    for i:=0;i<len(candidates);i++{
        if sum+candidates[i]<target{//继续往下找
            *result=append(*result,candidates[i])
            find(candidates[i:],target,result,results,sum+candidates[i])
            *result=(*result)[:len(*result)-1]
        }else{//找到或者已经超出，结束这个分支
            if sum+candidates[i]==target{//找到
                *result=append(*result,candidates[i])
                var cc []int
                for _,v:=range *result{//不能直接用从*result切出来的，因为那是地址引用
                    cc=append(cc,v)
                }
                *results=append(*results,cc)
                *result=(*result)[:len(*result)-1]//让*result回溯之前返回原样
            }
            continue//这个分支结束了
        }
    }
}