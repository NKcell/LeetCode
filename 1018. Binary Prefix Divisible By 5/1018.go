package  leetcode

// 这个方法python能用，但go不行，后面数值过大会超过int的范围，int64也是不够的
// func prefixesDivBy5(A []int) []bool {
// 	tmp := 0
// 	relist := make([]bool,0,len(A))
// 	for _, v := range A{
// 		tmp = (tmp<<1) + v
// 		if tmp%5 == 0{
// 			relist = append(relist, true)
// 		}else{
// 			relist = append(relist, false)
// 		}
// 	}
// 	return relist
// }

func prefixesDivBy5(A []int) []bool {
	tmp := 0
	relist := make([]bool,0,len(A))
	for _, v := range A{
		tmp = ((tmp<<1) + v)%5
		if tmp == 0{
			relist = append(relist, true)
		}else{
			relist = append(relist, false)
		}
	}
	return relist
}

// 这个利用了默认值为false，减少了操作
func prefixesDivBy5_1(A []int) []bool {
    num, answer := 0, make([]bool, len(A))
    for i := 0; i < len(A); i++ {
        num = (num * 2 + A[i]) % 5 //prevent overflow
        if num == 0 {
            answer[i] = true
        }
    }
    
    return answer
}