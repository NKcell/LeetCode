package leetcode

func corpFlightBookings(bookings [][]int, n int) []int {
	res := make([]int,  n+1)
	for i:=0; i<len(bookings); i++{
		res[bookings[i][0]-1] += bookings[i][2]
		res[bookings[i][1]] -= bookings[i][2] 
	}
	for i:=1; i<n; i++{
		res[i] += res[i-1]
	}
	return res[:n]
}