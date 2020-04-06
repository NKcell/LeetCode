package leetcode

func intToRoman(num int) string {
	res := ""

	symbol := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
	value := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}

	i := 0

	for (true){
		if num == 0{
			return res
		}
		tmp := num/value[i]
		for j:=0; j<tmp; j++{
			res += symbol[i]
		}

		num = num%value[i]
		i ++
	}
	return res
}