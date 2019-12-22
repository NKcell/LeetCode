package leetcode

func exist(board [][]byte, word string) bool {
	if len(word) == 0{
		return true
	}
    if len(board) == 0 || len(board[0])==0{
		return false
	}

	for i:=0; i<len(board); i++{
		for j:=0; j<len(board[0]); j++{
			tmp := dfs(board, i, j, word)
			if tmp{
				return true
			}
		}
	}
	return false
}

func dfs(board [][]byte, i,j int, word string)bool{
	if len(word) == 0{
		return true
	}
	if i<0 || j<0 || i>=len(board) || j>=len(board[0]) || board[i][j] != word[0]{
		return false
	}

	tmp := board[i][j]
	board[i][j] = '#'

	res := dfs(board, i, j+1, word[1:])||dfs(board, i, j-1, word[1:])||dfs(board, i+1, j, word[1:])||dfs(board, i-1, j, word[1:])
	board[i][j] = tmp
	return res
}