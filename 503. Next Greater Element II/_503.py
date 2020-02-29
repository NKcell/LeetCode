class Solution:
    def nextGreaterElements(self, nums):
        nums = nums*2
        stack = list()
        res = list()
        for i in nums[::-1]:
            while True:
                if len(stack)==0:
                    stack.append(i)
                    res.append(-1)
                    break
                else:
                    if stack[-1]>i:
                        res.append(stack[-1])
                        stack.append(i)
                        break
                    else:
                        stack.pop()
        res.reverse()
        return res[:len(nums)//2]

    def nextGreaterElements1(self, A):
        stack, res = [], [-1] * len(A)
        for i in range(len(A)) * 2:
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)
        return res