package  main

import "fmt"

func main(){
	fmt.Println(fib(2))
}

func fib(N int) int {
	a := 0
	b := 1
	if N==0{
		return a
	}
	if N==1{
		return b
	}
	for i:=1;i<N;i++{
		a, b = b, a+b
	}
	return b
}