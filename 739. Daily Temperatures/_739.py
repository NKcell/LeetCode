class Solution:
    def dailyTemperatures(self, T) :
        res = [0]*len(T)
        mydict = dict()

        for i in range(len(T)-1, -1, -1):
            tmp = 30001
            for j in range(T[i]+1, 101):
                if j in mydict:
                    tmp = min(tmp, mydict[j]-i)
            if tmp != 30001:
                res[i] = tmp
            mydict[T[i]] = i

        return res

    # 这个用栈的思想简直太棒了
    def dailyTemperatures1(self, T):
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans

    def dailyTemperatures2(self, T):
        n = len(T)
        res = [0] * n
        for i in range(n - 2, -1, -1):
            k = i + 1
            while T[i] >= T[k] and res[k] > 0:
                k += res[k]
            if T[k] > T[i]:
                res[i] = k - i
        return res

a = Solution()
print(a.dailyTemperatures1([73, 74, 75, 71, 69, 72, 76, 73]))
