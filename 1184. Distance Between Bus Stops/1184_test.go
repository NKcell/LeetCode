package leetcode

import "testing"

func TestDistanceBetweenBusStops(t *testing.T){
	type test struct{
		distance []int
		start int
		destination int
		want int
	}

	tests := map[string]test{
		"1":{[]int{1,2,3,4}, 0, 3, 4},
		"2":{[]int{1,2,3,4}, 0, 2, 3},
		"3":{[]int{1,2,3,4}, 0, 1, 1},
		"4":{[]int{7,10,1,12,11,14,5,0}, 7, 2, 17},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := distanceBetweenBusStops(tc.distance, tc.start, tc.destination)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkDistanceBetweenBusStops(b *testing.B){
	for i:=0; i<b.N; i++{
		distanceBetweenBusStops([]int{1,2,3,4}, 0, 3)
	}
}