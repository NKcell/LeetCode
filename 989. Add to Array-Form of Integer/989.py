class Solution:
    def addToArrayForm(self, A, K: int) :
        Alen = len(A)-1
        flag = 0
        while True:
            if K == 0 and flag == 0:
                break
            tmp = K%10
            K = K//10
            if Alen>-1:
                if A[Alen]+tmp+flag>=10:
                    A[Alen] = (A[Alen]+tmp+flag)%10
                    flag = 1
                else:
                    A[Alen] = (A[Alen]+tmp+flag)%10
                    flag =0
                Alen -= 1
            else:
                if tmp + flag >= 10: 
                    A = [(tmp+flag)%10] + A
                    flag = 1
                else:
                    A = [(tmp+flag)%10] + A
                    flag = 0
        return A

    # pythonic的做法
    def addToArrayForm1(self, A, k):
        return (list(str(int(''.join(map(str, A))) + k)))

a = Solution()
print(a.addToArrayForm([7], 993))