class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        pre = 0
        flag = 0
        res = list()
        for i,v in enumerate(S):
            if v == '(':
                flag += 1
            else:
                flag -= 1
            
            if flag == 0:
                res.append(S[pre+1:i])
                pre = i+1

        return ''.join(res)

    def removeOuterParentheses1(self, S):
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)

a = Solution()
print(a.removeOuterParentheses("()()"))