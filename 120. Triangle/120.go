package leetcode

func minimumTotal(triangle [][]int) int {
    for i,v := range triangle{
		if i==0{
			continue
		}

		for index, value := range v{
			if index == 0{
				v[0] = value+triangle[i-1][0]
			}else if index == len(v)-1{
				v[len(v)-1] = value+triangle[i-1][len(v)-2]
			}else{
				min := 0
				if triangle[i-1][index]>triangle[i-1][index-1]{
					min = triangle[i-1][index-1]
				}else{
					min = triangle[i-1][index]
				}
				v[index] = value+min
			}
		}
	}

	min := triangle[len(triangle)-1][0]
	for _,v := range triangle[len(triangle)-1]{
		if min>v{
			min = v
		}
	}
	return min
}