class Solution:
    def decodeString(self, s: str) -> str:

        stack = list()

        for i in s:
            if i != ']':
                stack.append(i)
            else:
                tmpstr = ''
                while True:
                    tmp = stack.pop()
                    if tmp == '[':
                        break
                    else:
                        tmpstr = tmp + tmpstr

                tmpcount = ''
                while True:
                    if len(stack)!= 0:
                        tmp = stack.pop()
                        if tmp.isdigit():
                            tmpcount = tmp + tmpcount
                        else:
                            stack.append(tmp)
                            stack.append(int(tmpcount)*tmpstr)
                            break
                    else:
                        if tmpcount:
                            stack.append(int(tmpcount)*tmpstr)
                        else:
                            stack.append(tmpstr)
                        break
        
        return ''.join(stack)

    def decodeString1(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString

a = Solution()
print(a.decodeString("aaaaa"))


