class Solution:
    def nextGreaterElement(self, num1, num2):
        res = list()
        stack = list()
        for i in num2[::-1]:
            while True:
                if not stack:
                    res.append(-1)
                    stack.append(i)
                    break
                else:
                    if i>stack[-1]:
                        stack.pop()
                    else:
                        res.append(stack[-1])
                        stack.append(i)
                        break
        
        res.reverse()
        res2 = list()
        for i in num1:
            res2.append(res[num2.index(i)])
        return res2

    def nextGreaterElement1(self, findNums, nums):
        st, d = [], {}
        for n in nums:
            while st and st[-1] < n:
                d[st.pop()] = n
            st.append(n)
        
        return [d.get(x, -1) for x in findNums]