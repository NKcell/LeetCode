package leetcode

import "testing"

func TestCountCharacters(t *testing.T){
	type test struct{
		input1 []string
		input2 string
		want int
	}

	tests := map[string]test{
		"1":{[]string{"cat","bt","hat","tree"}, "atach", 6},
		"2":{[]string{"hello","world","leetcode"}, "welldonehoneyr", 10},
	}

	for name, tc := range tests{
		t.Run(name, func(t *testing.T){
			got := countCharacters(tc.input1, tc.input2)
			if got != tc.want{
				t.Errorf("Test Failed! want: %#v got: %#v", tc.want, got)
			}
		})
	}
}

func BenchmarkCountCharacters(b *testing.B){
	for i:=0; i<b.N; i++{
		countCharacters([]string{"cat","bt","hat","tree"}, "atach")
	}
}

func BenchmarkCountCharacters1(b *testing.B){
	for i:=0; i<b.N; i++{
		countCharacters1([]string{"cat","bt","hat","tree"}, "atach")
	}
}