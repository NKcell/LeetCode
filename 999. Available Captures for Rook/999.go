package main

import (
	"fmt"
)

func main(){
	fmt.Println(numRookCaptures([][]byte{{'.','.','.','.','.','.','.','.'},{'.','.','.','p','.','.','.','.'},{'.','.','.','p','.','.','.','.'},{'p','p','.','R','.','p','B','.'},{'.','.','.','.','.','.','.','.'},{'.','.','.','B','.','.','.','.'},{'.','.','.','p','.','.','.','.'},{'.','.','.','.','.','.','.','.'}}))
}

func numRookCaptures(board [][]byte) int {
	rLoc := getLoc(board)
	var count int

	for i:=rLoc[0]+1; i<8; i++{
		if board[i][rLoc[1]] == 'p'{
			count ++
			break
		}
		if board[i][rLoc[1]] == 'B'{
			break
		}
	}

	for i:=rLoc[0]-1; i>-1; i--{
		if board[i][rLoc[1]] == 'p'{
			count ++
			break
		}
		if board[i][rLoc[1]] == 'B'{
			break
		}
	}

	for i:=rLoc[1]+1; i<8; i++{
		if board[rLoc[0]][i] == 'p'{
			count ++
			break
		}
		if board[rLoc[0]][i] == 'B'{
			break
		}
	}

	for i:=rLoc[1]-1; i>-1; i--{
		if board[rLoc[0]][i] == 'p'{
			count ++
			break
		}
		if board[rLoc[0]][i] == 'B'{
			break
		}
	}
	
	return count
}

func getLoc(board [][]byte) []int{
	for i, v := range board{
		for j, v2 := range v{
			if v2 == 'R'{
				return []int{i, j}
			}
		}
	}
	return []int{}
}