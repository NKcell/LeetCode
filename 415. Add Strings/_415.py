class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]

        ans = list()

        minlength = min(len(num1), len(num2))

        flag = 0
        for i in range(0, minlength):
            tmp = int(num1[i])+int(num2[i])+flag
            flag = tmp//10
            ans.append(str(tmp%10))

        if len(num2)<len(num1):
            for i in num1[minlength:]:
                tmp = int(i) + flag
                flag = tmp//10
                ans.append(str(tmp%10))
        else:
            for i in num2[minlength:]:
                tmp = int(i) + flag
                flag = tmp//10
                ans.append(str(tmp%10))

        if flag != 0:
            ans.append(str(flag))
        
        return ''.join(ans[::-1])

    # 我觉得这里pop用
    def addStrings1(self, num1, num2):
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop())-ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop())-ord('0') if len(num2) > 0 else 0
            
            temp = n1 + n2 + carry 
            res.append(temp % 10)
            carry = temp // 10
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]





