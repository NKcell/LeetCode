package leetcode

func minimumSwap(s1 string, s2 string) int {
	res := make([]rune, 0)
	for i,v := range s1{
		if v != rune(s2[i]){
			res = append(res, v)
		}
	}

	if len(res)%2 != 0{
		return -1
	}

	x := 0
	y := 0
	for _, v:= range res{
		if v == 'x'{
			x++
		}else{
			y++
		}
	}

	if x%2 != 0{
		return x/2+y/2+2
	}
	return x/2+y/2
}

func minimumSwap1(s1 string, s2 string) int {
	x := 0
	y := 0
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			if s1[i] == 'x' {
				x++
			} else {
				y++
			}
		}
	}
	// totalDiff MUST BE even
	totalDiff := x + y
	if totalDiff%2 == 1 {
		return -1
	}
	diffPair := totalDiff/2
	oneStepDiffPair := x/2 + y/2
	twoStepDiffPair := diffPair - oneStepDiffPair
	return oneStepDiffPair + 2*twoStepDiffPair
}