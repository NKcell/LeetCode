class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = list()
        for i in S:
            self.pushele(i, res)

        an = 0
        tmp = 1
        print(res)
        for i in res:
            if i == '(':
                tmp*=2
            elif i == ')':
                continue
            else:
                tmp*=int(i)
                an += tmp
                tmp = 1
        return an
        

    def pushele(self, i, res):
        if i == '(':
            res.append(i)
        elif i == ')':
            if res[-1] == '(':
                res.pop()
                self.pushele('1', res)
            else:
                res.append(i)
        else:
            if len(res) == 0:
                res.append(i)
            else:
                if res[-1] == '(' or res[-1] == ')':
                    res.append(i)
                else:
                    res.append(int(res.pop())+int(i))


a = Solution()
print(a.scoreOfParentheses("(()(()))"))