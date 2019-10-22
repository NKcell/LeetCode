package leetcode

import(
	"math"
)

func numSquares(n int) int {
	mylist := []int{n}
	step := 0

	for{
		step ++
		tmpDict := make(map[int]int, 0)
		for len(mylist)>0{
			n := mylist[0]
			mylist = mylist[1:]
			n1 := int(math.Sqrt(float64(n)))+1
			for i:=1; i<n1; i++{
				cha := n - i*i
				if cha == 0{
					return step
				}
				tmpDict[cha] = 1
			}
		}
		for i := range tmpDict{
			mylist = append(mylist, i)
		}
	}
}