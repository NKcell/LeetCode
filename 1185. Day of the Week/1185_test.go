package leetcode

import(
	"testing"
)

func TestDayOfTheWeek(t *testing.T){
	type test struct{
		day, month, year int
		want string
	}

	tests := map[string]test{
		"1": test{31, 8, 2019, "Saturday"},
		"2": test{18, 7, 1999, "Sunday"},
		"3": test{15, 8, 1993, "Sunday"},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := dayOfTheWeek(tc.day, tc.month, tc.year)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkDayOfTheWeek(b *testing.B){
	for i:=0; i<b.N; i++{
		dayOfTheWeek(31, 8, 2019)
	}
}