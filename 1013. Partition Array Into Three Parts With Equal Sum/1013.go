package leetcode

func canThreePartsEqualSum(A []int) bool {
	var sumvalue int
    for _, v := range A{
		sumvalue += v
	}

	if sumvalue%3 != 0{
		return false
	}

	partvalue := sumvalue/3

	flag := 0
	tmpvalue := 0
	tmpindex := 0
	for i, v := range A{
		tmpvalue += v
		if tmpvalue == partvalue{
			flag ++
			tmpvalue = 0
			tmpindex = i
		}
		if flag == 2 && tmpindex != len(A)-1{
			return true
		}
	}
	return false
}