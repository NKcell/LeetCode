package leetcode

func judgeCircle(moves string) bool {
	a := 0
	b := 0
    for _, v := range moves{
		if v == 'L'{
			a ++
		}else if v == 'R'{
			a --
		}else if v == 'U'{
			b ++
		}else{
			b --
		}
	}
	if a == 0 && b==0{
		return true
	}
	return false
}