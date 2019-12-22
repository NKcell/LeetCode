class Solution:
    # 自己的dfs最终超时
    def exist(self, board, word: str) -> bool:
        if not word:
            return True
        if not board or len(board[0]) == 0:
            return False

        start = list()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    start.append([i,j])

        res = list()
        for i in start:
            indexs = set()
            indexs.add(str(i[0])+'-'+str(i[1]))

            self.myfunc(indexs, i ,res, board, word[1:])
        return sum(res)>0
    
    def myfunc(self, indexs, index, res, board, word):
        from copy import deepcopy
        if sum(res)>0:
            return
        if len(word)==0:
            res.append(1)
            return
        
        if index[0]>0:
            if board[index[0]-1][index[1]] == word[0]:
                tmp = deepcopy(indexs)
                tmp.add(str(index[0]-1)+'-'+str(index[1]))
                if len(tmp) == len(indexs):
                    pass
                else:
                    self.myfunc(tmp, [index[0]-1, index[1]] ,res, board, word[1:])

        if index[1]>0:
            if board[index[0]][index[1]-1] == word[0]:
                tmp = deepcopy(indexs)
                tmp.add(str(index[0])+'-'+str(index[1]-1))
                if len(tmp) == len(indexs):
                    pass
                else:
                    self.myfunc(tmp, [index[0], index[1]-1] ,res, board, word[1:])

        if index[0]<len(board)-1:
            if board[index[0]+1][index[1]] == word[0]:
                tmp = deepcopy(indexs)
                tmp.add(str(index[0]+1)+'-'+str(index[1]))
                if len(tmp) == len(indexs):
                    pass
                else:
                    self.myfunc(tmp, [index[0]+1, index[1]] ,res, board, word[1:])

        if index[1]<len(board[0])-1:
            if board[index[0]][index[1]+1] == word[0]:
                tmp = deepcopy(indexs)
                tmp.add(str(index[0])+'-'+str(index[1]+1))
                if len(tmp) == len(indexs):
                    pass
                else:
                    self.myfunc(tmp, [index[0], index[1]+1] ,res, board, word[1:])

    # 整体dfs的思路是没有变的，单别人在很多地方优化的很好，内存开销小很多
    def exist1(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


a = Solution()
print(a.exist(board =[["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","b"]], word = "aaaaaaaaaaaaaaaaaaaa"))