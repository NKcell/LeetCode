class Solution:
    def queensAttacktheKing(self, queens, king):
        res = list()
        tmp = king[0]
        while tmp>-1:
            if [tmp, king[1]] in queens:
                res.append([tmp, king[1]])
                break
            tmp-=1
        tmp = king[0]
        while tmp<8:
            if [tmp, king[1]] in queens:
                res.append([tmp, king[1]])
                break
            tmp+=1
        tmp = king[1]
        while tmp>-1:
            if [king[0], tmp] in queens:
                res.append([king[0], tmp])
                break
            tmp-=1
        tmp = king[1]
        while tmp<8:
            if [king[0], tmp] in queens:
                res.append([king[0], tmp])
                break
            tmp+=1
        x = king[0]
        y = king[1]
        while x<8 and y<8:
            if [x, y] in queens:
                res.append([x, y])
                break
            x += 1
            y += 1
        
        x = king[0]
        y = king[1]
        while x<8 and y>-1:
            if [x, y] in queens:
                res.append([x, y])
                break
            x += 1
            y -= 1

        x = king[0]
        y = king[1]
        while x>-1 and y<8:
            if [x, y] in queens:
                res.append([x, y])
                break
            x -= 1
            y += 1

        x = king[0]
        y = king[1]
        while x>-1 and y>-1:
            if [x, y] in queens:
                res.append([x, y])
                break
            x -= 1
            y -= 1

        return res

    def queensAttacktheKing1(self, queens, king):
        res = []
        queens = {(i, j) for i, j in queens}
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in range(1, 8):
                    x, y = king[0] + i * k, king[1] + j * k
                    if (x, y) in queens:
                        res.append([x, y])
                        break
        return res

a = Solution()
print(a.queensAttacktheKing( queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]))