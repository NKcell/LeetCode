package leetcode

import(
	"reflect"
)

func queensAttacktheKing(queens [][]int, king []int) [][]int {
	x := king[0]
	y := king[1]
	res := make([][]int, 0)

	for x<8{
		if isexist(&queens, &[]int{x,y}){
			res = append(res, []int{x,y})
			break
		}
		x++
	}
	x = king[0]
	for x>-1{
		if isexist(&queens, &[]int{x,y}){
			res = append(res, []int{x,y})
			break
		}
		x--
	}
	x = king[0]
	for y<8{
		if isexist(&queens, &[]int{x,y}){
			res = append(res, []int{x,y})
			break
		}
		y ++
	}
	y = king[1]
	for y>-1{
		if isexist(&queens, &[]int{x,y}){
			res = append(res, []int{x,y})
			break
		}
		y--
	}
	y = king[1]

	for y>-1 && x>-1{
		if isexist(&queens, &[]int{x,y}){
			res = append(res, []int{x,y})
			break
		}
		y--
		x--
	}
	x = king[0]
	y = king[1]
	for y>-1 && x<8{
		if isexist(&queens, &[]int{x,y}){
			res = append(res, []int{x,y})
			break
		}
		y--
		x++
	}
	x = king[0]
	y = king[1]
	for y<8 && x>-1{
		if isexist(&queens, &[]int{x,y}){
			res = append(res, []int{x,y})
			break
		}
		y++
		x--
	}
	x = king[0]
	y = king[1]
	for y<8 && x<8{
		if isexist(&queens, &[]int{x,y}){
			res = append(res, []int{x,y})
			break
		}
		y++
		x++
	}
	return res
}

func isexist(a *[][]int, b *[]int) bool{
	for _, v := range *a{
		if reflect.DeepEqual(v, *b){
			return true
		}
	}
	return false
}