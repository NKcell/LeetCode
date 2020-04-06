package leetcode

func minDeletionSize(A []string) int {
	count := 0
	for i:=0; i<len(A[0]); i++{
		for j:=1; j<len(A); j++{
			if A[j-1][i] > A[j][i]{
				count ++
				break
			}
		}
	}
	return count
}