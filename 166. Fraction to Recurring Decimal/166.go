package  leetcode

import(
	"strings"
	"strconv"
)

func fractionToDecimal(numerator int, denominator int) string {
	res := make([]string, 0, 1)

	if numerator*denominator<0{
		res = append(res, "-")
	}

	if numerator<0{
		numerator = -numerator
	}
	if denominator<0{
		denominator = -denominator
	}

	if numerator<denominator{
		res = append(res, "0")
	}

	for numerator>=denominator{
		mod := numerator%denominator
		res = append(res, strconv.Itoa(numerator/denominator))
		numerator = mod
	}
	
	if numerator == 0{
		return strings.Join(res, "")
	}
	res = append(res, ".")
	numerator *= 10
	
	myDict := make(map[int]int, 1)
	myDict[numerator] = len(res)

	for numerator != 0{
		mod := numerator%denominator
		res = append(res, strconv.Itoa(numerator/denominator))
		numerator = mod*10
		v,ok := myDict[numerator]
		if !ok{
			myDict[numerator] = len(res)
		}else{
			tmp := make([]string, len(res[v:]), len(res[v:]))
			copy(tmp, res[v:]) // 这里的拷贝必须要长度一样...
			res = append(res[:v],"(")
			res = append(res, tmp...)
			res = append(res, ")")
			return strings.Join(res, "")
		}
	}
	return strings.Join(res, "")
}