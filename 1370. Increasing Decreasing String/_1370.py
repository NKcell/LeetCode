class Solution:
    def sortString(self, s: str) -> str:
        res = ""
        myList = list(s)
        myList.sort(reverse = True)
        while True:
            if len(myList) == 0:
                break
            tmplist = list()
            pre = 'A'
            while myList:
                tmp = myList.pop()
                if tmp == pre:
                    tmplist.append(tmp)
                else:
                    res += tmp
                    pre = tmp
            myList = tmplist
        return res
    
    def sortString1(self, s: str) -> str:
        import collections
        cnt, ans, asc = collections.Counter(s), [], True
        while cnt:                                                                  # if Counter not empty.
            for c in sorted(cnt.keys()) if asc else reversed(sorted(cnt.keys())):   # traverse keys in ascending/descending order.
                ans.append(c)                                                       # append the key.
                cnt[c] -= 1                                                         # decrease the count.
                if cnt[c] == 0:                                                     # if the count reaches to 0.
                    del cnt[c]                                                      # remove the key from the Counter.
            asc = not asc                                                           # change the direction, same as asc ^= True.
        return ''.join(ans)

    def sortString2(self, s: str) -> str:
        import collections
        import string
        cnt, ans, asc  = collections.Counter(s), [], True
        while len(ans) < len(s):                                # if not finish.
            for i in range(26):                                 # traverse lower case letters.
                c = string.ascii_lowercase[i if asc else ~i]    # in ascending/descending order.
                if cnt[c] > 0:                                  # if the count > 0.
                    ans.append(c)                               # append the character.
                    cnt[c] -= 1                                 # decrease the count.
            asc = not asc                                       # change direction.
        return ''.join(ans)