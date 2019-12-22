class Solution:
    def tictactoe(self, moves) -> str:
        if len(moves)<5:
            return "Pending"
        
        res = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(0, len(moves), 2):
            res[moves[i][0]][moves[i][1]] = 1
        
        for i in range(1, len(moves), 2):
            res[moves[i][0]][moves[i][1]] = -1

        for i in range(3):
            if res[0][i]+res[1][i]+res[2][i] == 3 or res[i][0]+res[i][1]+res[i][2] == 3:
                return "A"
            if res[0][i]+res[1][i]+res[2][i] == -3 or res[i][0]+res[i][1]+res[i][2] == -3:
                return "B"

        if res[0][0]+res[1][1]+res[2][2] == 3 or res[2][0]+res[1][1]+res[0][2] == 3:
            return "A"
        if res[0][0]+res[1][1]+res[2][2] == -3 or res[2][0]+res[1][1]+res[0][2] == -3:
            return "B"

        if len(moves) == 9:
            return "Draw"
        return "Pending"

    def tictactoe1(self, moves) -> str:
        row, col = [[0] * 3 for _ in range(2)], [[0] * 3 for _ in range(2)]
        d1, d2, id = [0] * 2, [0] * 2, 0
        for r, c in moves:
            row[id][r] += 1
            col[id][c] += 1
            d1[id] += r == c
            d2[id] += r + c == 2
            if 3 in (row[id][r], col[id][c], d1[id], d2[id]):
                return 'AB'[id]
            id ^= 1
        return 'Draw' if len(moves) == 9 else 'Pending'

    def tictactoe2(self, moves) -> str:
        A=[0]*8
        B=[0]*8
        for i in range(len(moves)):
            r,c=moves[i]
            player = A if i%2==0 else B
            player[r] += 1
            player[c+3] += 1
            if r==c:
                player[6] += 1
            if r==2-c:
                player[7] += 1
        for i in range(8):
            if A[i]==3:
                return "A"
            if B[i]==3:
                return "B"
        
        return "Draw" if len(moves) == 9 else "Pending"

a = Solution()
print(a.tictactoe(moves = [[0,0],[1,1]]))