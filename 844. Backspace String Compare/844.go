package leetcode

import(
	"reflect"
)

func backspaceCompare(S string, T string) bool {
    res1 := make([]rune, 0)
    for _,v := range S{
		if v != '#'{
			res1 = append(res1, v)
		}else if len(res1)==0{
			continue
		}else{
			res1 = res1[:len(res1)-1]
		}
	}

	res2 := make([]rune, 0)
    for _,v := range T{
		if v != '#'{
			res2 = append(res2, v)
		}else if len(res2)==0{
			continue
		}else{
			res2 = res2[:len(res2)-1]
		}
	}

	if (len(res1)==len(res2))&&(reflect.DeepEqual(res1, res2)){
		return true
	}
	return false
}