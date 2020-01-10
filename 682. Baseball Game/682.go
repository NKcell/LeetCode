package leetcode

import(
	"strconv"
)

func calPoints(ops []string) int {
    res := make([]int, 2)
	for _, v := range ops{
		if v == "D"{
			res = append(res, res[len(res)-1]*2) 
		}else if v == "+"{
			res = append(res, res[len(res)-1]+res[len(res)-2])
		}else if v == "C"{
			if len(res)>2{
				res = res[:len(res)-1]
			}
		}else{
			tmp, _ := strconv.Atoi(v)
			res = append(res, tmp)
		}
	}

	sum := 0
	for _,v := range res{
		sum += v
	}
	return sum
}