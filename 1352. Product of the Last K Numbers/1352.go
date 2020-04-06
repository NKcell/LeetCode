package leetcode

type ProductOfNumbers struct {
    myList []int
}


func Constructor() ProductOfNumbers {
    return ProductOfNumbers{
		myList: []int{1},
	}
}


func (this *ProductOfNumbers) Add(num int)  {
    if num == 0{
		this.myList = []int{1}
	}else{
		this.myList = append(this.myList, this.myList[len(this.myList)-1]*num)
	}
}


func (this *ProductOfNumbers) GetProduct(k int) int {
    if k>=len(this.myList){
		return 0
	}else{
		return this.myList[len(this.myList)-1]/this.myList[len(this.myList)-k-1]
	}
}