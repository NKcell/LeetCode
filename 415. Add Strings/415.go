package leetcode

import(
	"strconv"
	"strings"
)

func addStrings(num1 string, num2 string) string {
	n1 := strings.Split(num1, "")
	n2 := strings.Split(num2, "")

	n1 = myreverse(n1)
	n2 = myreverse(n2)

	var n12 bool
	var minLen int
	var maxLen int
	if len(n1)<len(n2){
		minLen = len(n1)
		maxLen = len(n2)
		n12 = true
	}else{
		minLen = len(n2)
		maxLen = len(n1)
		n12 = false
	}

	ans := make([]string, maxLen)
	var flag int
	flag = 0

	for i:=0; i<minLen; i++{
		n1int, _ := strconv.Atoi(n1[i])
		n2int, _ := strconv.Atoi(n2[i])

		tmp := n1int+n2int+flag
		flag = tmp/10
		ans[i] = strconv.Itoa(tmp%10)
	}

	if n12{
		for i:=minLen; i<maxLen; i++{
			n2int, _ := strconv.Atoi(n2[i])
			tmp := n2int+flag
			flag = tmp/10
			ans[i] = strconv.Itoa(tmp%10)
		}
	}else{
		for i:=minLen; i<maxLen; i++{
			n1int, _ := strconv.Atoi(n1[i])
			tmp := n1int+flag
			flag = tmp/10
			ans[i] = strconv.Itoa(tmp%10)
		}
	}

	ans = myreverse(ans)

	if flag == 0{
		return strings.Join(ans, "")
	}
	return "1"+strings.Join(ans, "")
	
}

func myreverse(s []string) []string {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
    return s
}


// 这里主要要注意byte的加减法是怎么用
func addStrings1(num1 string, num2 string) string {
	len1 := len(num1)
	len2 := len(num2)
	size := 0
	if len1 > len2 {
		size = len1
	} else {
		size = len2
	}
	result := make([]byte, size+1)
	isMemorized := false
	for i := size - 1; i >= 0; i-- {
		len1--
		len2--
		sum := getValue(num1, len1)
		sum += getValue(num2, len2)
		key := i + 1
		if isMemorized {
			sum++
			isMemorized = false
		}

		if sum <= 9 {
			result[key] = '0' + sum
		} else {
			result[key] = '0' + sum - 10
			isMemorized = true
		}
	}
	if isMemorized {
		result[0] = '1'
		return string(result)
	}
	return string(result[1:])
}

func getValue(str string, index int) byte {
	if index >= 0 {
		return str[index] - '0'
	}
	return 0
}