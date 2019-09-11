package  leetcode

func distanceBetweenBusStops(distance []int, start int, destination int) int {
	if start > destination{
		destination, start = start, destination
	}

	var tmp1, tmp2 int
	for i:=start; i<destination; i++{
		tmp1 += distance[i]
	}

	for i:=0; i<start; i++{
		tmp2 += distance[i]
	}
	for i:=destination; i<len(distance); i++{
		tmp2 += distance[i]
	}

	if tmp1>tmp2{
		return tmp2
	}
	return tmp1
}