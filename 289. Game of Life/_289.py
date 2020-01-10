class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        res = [0]*(len(board)*len(board[0]))

        for i in range(len(board)):
            for j in range(len(board[0])):
                count = self.getcount(i, j, board)
                if (count == 2 and board[i][j] == 1) or count==3:
                    res[i*len(board[0])+j] = 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = res[i*len(board[0])+j]


        
    def getcount(self, i, j, board):
        count = 0
        if i>0:
            count += board[i-1][j]
            if j>0:
                count+=board[i-1][j-1]
            if j<len(board[0])-1:
                count += board[i-1][j+1]

        if i<len(board)-1:
            count += board[i+1][j]
            if j>0:
                count+=board[i+1][j-1]
            if j<len(board[0])-1:
                count += board[i+1][j+1]

        if j>0:
                count+=board[i][j-1]
        if j<len(board[0])-1:
            count += board[i][j+1]
        return count

    def gameOfLife1(self, board):
        if not board or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                count = 0
                for a in range(max(0, i - 1), min(i + 2, m)):
                    for b in range(max(0, j - 1), min(j + 2, n)):
                        if (a, b) != (i, j) and 1 <= board[a][b] <= 2:
                            count += 1
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1

a = Solution()
l = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
a.gameOfLife(l)
print(l)