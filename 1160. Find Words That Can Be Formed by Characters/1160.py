class Solution:
    def countCharacters(self, words, chars: str) -> int:
        mydict = {}
        for i in chars:
            v = mydict.get(i, 0)
            mydict[i] = v+1

        count = 0

        for i in words:
            flag =0
            for j in set(i):
                v = mydict.get(j, 0)
                if i.count(j)>v:
                    flag = 1
                    break
            if flag == 0:
                count += len(i)
        
        return count

    # 用列表替换字典的尝试，效果一般
    def countCharacters1(self, words, chars: str) -> int:
        mylist = []
        for i in range(97, 123):
            mylist.append(chars.count(chr(i)))
        count = 0
        for i in words:
            for j in set(i):
                flag = 0
                if i.count(j) > mylist[ord(j)-97]:
                    flag = 1
                    break 
            if flag == 0:
                count += len(i)
        return count

    # 这个我主要觉得all用的好，这样相对与我的代码少用了一个变量去控制
    def countCharacters2(self, words, chars: str) -> int:
        from collections import Counter
        ans=0
        char_c=Counter(chars)
        for word in words:
            t_cs=Counter(word)
            if all(t_cs[t_c]<=char_c[t_c] for t_c in t_cs):
                ans+=len(word)
        return ans

    # 这个思路比较简洁吧
    def countCharacters3(self, words, chars: str) -> int:
        res = 0
        for i in range(len(words)):
            boole = True
            a = list(chars)
            b = words[i]
            for j in range(len(b)):
                if b[j] in a:
                    a.remove(b[j])
                else:
                    boole = False
                    break
            if boole:
                res += len(b)
        return res

a = Solution()
print(a.countCharacters1(["hello","world","leetcode"], "welldonehoneyr"))