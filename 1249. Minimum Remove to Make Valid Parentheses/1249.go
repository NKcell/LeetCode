package leetcode

import(
	"sort"
)

func minRemoveToMakeValid(s string) string {
	right := make([]int, 0)
	r := 0
	left := make([]int, 0)

	for i,v := range s{
		if v == '('{
			if r>=len(right){
				right = append(right, i)
			}else{
				if r == 0{
					right[0] = i
				}else{
					right[r] = i
				}
			}
			r++
		}else if v == ')'{
			if r>0{
				r --
			}else{
				left = append(left, i)
			}
		}
	}

	res := make([]int, len(left))
	copy(res, left)
	for i:=0; i<r; i++{
		res = append(res, right[i])
	}
	
	sort.Ints(res)
	ns := ""
	count := 0
	for i,v := range s{
		if count<len(res) && res[count] == i{
			count++
			continue
		}
		ns += string(v)
	}
	return ns
}