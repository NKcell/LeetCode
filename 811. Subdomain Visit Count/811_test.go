package leetcode

import(
	"testing"
)

func BenchmarkSubdomainVisits(b *testing.B){
	for i:=0; i<b.N; i++{
		subdomainVisits([]string{"9001 discuss.leetcode.com"})
	}
}

func BenchmarkSubdomainVisits1(b *testing.B){
	for i:=0; i<b.N; i++{
		subdomainVisits1([]string{"9001 discuss.leetcode.com"})
	}
}