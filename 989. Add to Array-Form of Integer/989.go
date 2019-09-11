package main

import(
	"fmt"
)

func main(){
	fmt.Println(addToArrayForm([]int{7}, 997))
}

func addToArrayForm(A []int, K int) []int {
	flag := 0
	Alen := len(A)-1
    for{
		if flag == 0 && K == 0{
			break
		}

		tmp := K%10
		K = K/10

		if Alen>-1{
			if A[Alen] + flag +tmp >= 10{
				A[Alen] = (A[Alen] + flag +tmp)%10
				flag = 1
			}else{
				A[Alen] = (A[Alen] + flag +tmp)
				flag = 0
			}
			Alen --
		}else{
			if flag +tmp >= 10{
				A = append([]int{(flag +tmp)%10}, A...)
				flag = 1
			}else{
				A = append([]int{(flag +tmp)}, A...)
				flag = 0
			}
		}
	}
	return A
}

func addToArrayForm1(A []int, K int) []int {
    var res []int      
    
    for i := len(A)-1; i >= 0; i-- {
        res = append(res,(A[i]+K)%10)
        K = (A[i]+K)/10
    }

    for K>0 {
		res=append(res,K%10)
		K /= 10		
    }
    
    for i := 0;i < len(res)/2;i++ {
        tmp := res[i]
        res[i] = res[len(res)-1-i]
        res[len(res)-1-i] = tmp
    }    
    return res        
}
