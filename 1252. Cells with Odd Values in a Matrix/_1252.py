class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        col = [0]*n
        row = [0]*m
        for i in indices:
            col[i[0]] += 1
            row[i[1]] += 1

        res = 0
        for i in range(n):
            for j in range(m):
                if (col[i]+row[j])%2 == 1:
                    res += 1
        return res

    def oddCells1(self, n: int, m: int, indices) -> int:
        odd_rows, odd_cols = [False] * n, [False] * m
        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
        return sum(ro ^ cl for ro in odd_rows for cl in odd_cols)

a = Solution()
print(a.oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))