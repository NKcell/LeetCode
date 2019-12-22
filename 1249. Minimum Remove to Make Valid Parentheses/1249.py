class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = list()
        right = list()

        for i, v in enumerate(s):
            if v == '(':
                left.append(i)
            elif v == ')':
                if left:
                    left.pop()
                else:
                    right.append(i)

        res = right+left
        res.sort(reverse=True)

        ns = ""
        for i, v in enumerate(s):
            if res and i == res[-1]:
                res.pop()
                continue
            ns += v

        return ns

    def minRemoveToMakeValid1(self, s: str) -> str:
        status_dict = {}
        stack = []
        # keep indexe's status in status_dict. If a parenthesis is valid
        # mark it as True else False. use stack to check it's validity
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append(idx)
            elif ch == ")" and len(stack) > 0:
                    status_dict[idx] = True
                    status_dict[stack[-1]] = True
                    stack.pop()
        res = []
        for idx, ch in enumerate(s):
            if ch == "(" or ch == ")":
                if idx in status_dict: # only append the parenthesis which are valid
                    res.append(ch)
            else:
                res.append(ch)
        return "".join(res)

a = Solution()
print(a.minRemoveToMakeValid("(a(b(c)d)"))        