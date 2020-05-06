package main

import(
	"strconv"
	"fmt"
)

func getPermutation(n int, k int) string {
	res := ""
	tmp := make([]string, n)
	for i:=1; i<=n; i++{
		tmp[i-1] = strconv.Itoa(i)
	}
	k -- 

	for (n != 0){
		n --
		beichu := jie(n)
		index := k/beichu
		k = k%beichu
		res += tmp[index]

		newtmp := make([]string, 0, len(tmp)-1)
		newtmp = append(newtmp, tmp[:index]...)
		newtmp = append(newtmp, tmp[index+1:]...)
		tmp = newtmp
	}
	
	return res
}

func jie(n int)int{
	res := 1
	for(n != 0){
		res *= n
		n --
	}
	return res
}

func main(){
	fmt.Println(getPermutation(3, 2))
}