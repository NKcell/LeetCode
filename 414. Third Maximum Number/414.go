package main

import "fmt"

func main(){
	fmt.Println(thirdMax([]int{1}))
}

func thirdMax(nums []int) int {
	var num1,num2,num3,flag int
	flag = 0
	for _,value := range nums{
		if flag == 0{
			num1 = value
			flag = 1
		}else if flag == 1{
			if value != num1{
				if value > num1{
					num2 = value
				}else{
					num1, num2 = value, num1
				}
				flag = 2
			}
		}else if flag == 2{
			if value != num1 && value != num2{
				if value > num2{
					num3 = value
				}else if value < num1{
					num1, num2, num3 = value, num1, num2
				}else{
					num2, num3 = value, num2
				}
				flag = 3
			}
		}else{
			if value != num1 && value != num2 && value != num3{
				if value > num3{
					num1, num2, num3 = num2, num3, value
				}else if value > num2{
					num2, num1 = value, num2
				}else if value > num1{
					num1 = value
				}else{

				}
			} 
		}
	}
	if flag == 2{
		return num2
	}else{
		return num1
	}
}

/////////////////////////////////////////////////////////
// 这个的有点在于最小值的表示，int的最小值，
//其次用了一个map来进行判断值是否重复
func thirdMax2(nums []int) int {
    if len(nums) == 1{
        return nums[0]
    }
    min1, min2, min3 := -1 << 31, -1 << 31, -1 << 31
    p := make(map[int]bool)
    for _, i := range nums{
        _,ok := p[i]
        if ok{
			continue 
        }
        
        if i > min1 {
            min3 = min2
            min2 = min1
            min1 = i
        }else if i > min2{
            min3 = min2
            min2 = i
        }else if i > min3{
            min3 = i
        }
        
        p[i] = true
    }

    if len(p) < 3 {
        return min1
    }else{
		return min3   
    }
    
}