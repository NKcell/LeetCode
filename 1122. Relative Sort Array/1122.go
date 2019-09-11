package leetcode

import "sort"

func relativeSortArray(arr1 []int, arr2 []int) []int {
	sort.Ints(arr1)
	mymap := make(map[int]int, len(arr1))
	for _,v := range arr1{
		mapv, ok := mymap[v]
		if !ok{
			mymap[v] = 1
		}else{
			mymap[v] = mapv + 1
		}
	}

	myslice := make([]int, len(arr1))
	var loc int
	for _,v := range arr2{
		mapv, _ := mymap[v]
		for mapv > 0{
			myslice[loc] = v
			mapv --
			loc ++
		}
		mymap[v] = 0
	}

	for _,v := range arr1{
		mapv, _ := mymap[v]
		for mapv > 0{
			myslice[loc] = v
			mapv --
			loc ++
		}
		mymap[v] = 0
	}

	return myslice
}

// 上面那个测试内存调用4次，这个只有一次，有点谜啊
// 这个用数组的方式来代替字典，也见过几次，感觉这个的效果貌似比字典好些
func relativeSortArray1(A, B []int) []int {
	count := [1001]int{}
	for _, a := range A {
		count[a]++
	}

	res := make([]int, 0, len(A))
	for _, b := range B {
		for count[b] > 0 {
			res = append(res, b)
			count[b]--
		}
	}
	for i := 0; i < 1001; i++ {
		for count[i] > 0 {
			res = append(res, i)
			count[i]--
		}
	}

	return res
}