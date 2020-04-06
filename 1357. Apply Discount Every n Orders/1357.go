package leetcode

type Cashier struct {
	myMap map[int]int
	n int
	people int
	discount int
}


func Constructor(n int, discount int, products []int, prices []int) Cashier {
	myMap := make(map[int]int,len(products))
	for i:=0; i<len(products); i++{
		myMap[products[i]] = prices[i]
	}
    return Cashier{
		myMap: myMap,
		n: n,
		people: 0,
		discount: discount,
	}
}


func (this *Cashier) GetBill(product []int, amount []int) float64 {
	this.people ++
	sum := 0
	if(this.people == this.n){
		this.people = 0
		for i:=0; i<len(product); i++{
			price, _ := this.myMap[product[i]]
			sum += (price*amount[i])
		}
		return float64(sum)*(1-float64(this.discount)/100)
	}else{
		for i:=0; i<len(product); i++{
			price, _ := this.myMap[product[i]]
			sum += (price*amount[i])
		}
		return float64(sum)
	}
}