package leetcode

import(
	"testing"
)

func BenchmarkNumJewelsInStones(b *testing.B){
	for i:=0; i<b.N; i++{
		numJewelsInStones("aA", "aAAbbbb")
	}
}

func BenchmarkNumJewelsInStones1(b *testing.B){
	for i:=0; i<b.N; i++{
		numJewelsInStones1("aA", "aAAbbbb")
	}
}