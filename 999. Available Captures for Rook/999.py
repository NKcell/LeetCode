class Solution:
    def numRookCaptures(self, board) -> int:
        R_loc = self.getLoc(board)
        count = 0
        for i in range(R_loc[1]+1,8):
            if board[R_loc[0]][i] == "p":
                count += 1
                break
            if board[R_loc[0]][i] == "B":
                break
        
        for i in range(R_loc[1]-1,-1, -1):
            if board[R_loc[0]][i] == "p":
                count += 1
                break
            if board[R_loc[0]][i] == "B":
                break

        for i in range(R_loc[0]-1,-1, -1):
            if board[i][R_loc[1]] == "p":
                count += 1
                break
            if board[i][R_loc[1]] == "B":
                break

        for i in range(R_loc[0]+1, 8):
            if board[i][R_loc[1]] == "p":
                count+=1
                break
            if board[i][R_loc[1]] == "B":
                break

        return count

    def getLoc(self, board):
        for i, v in enumerate(board):
            for j, v2 in enumerate(v):
                if v2 == "R":
                    return [i, j]

a = Solution()
print(a.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".","B","B","B","B","B","."],[".","p","B","p","p","p","B","p"],[".","p","B","p","R","p","B","p"],[".","p","B","p","p","p","B","p"],[".",".","B","B","B","B","B","."],[".",".",".","p","p","p",".","."],[".",".",".",".",".",".",".","."]]))