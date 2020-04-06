class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mydict = dict()
        res = list()

        for i in p:
            tmp = mydict.get(i, 0)
            mydict[i] = tmp-1

        for i in s[:len(p)]:
            tmp = mydict.get(i, None)
            if tmp != None:
                mydict[i] = tmp+1

        if not any(mydict.values()):
            res.append(0)

        for i in range(1, len(s)-len(p)+1):
            if mydict.get(s[i-1], None)!=None:
                mydict[s[i-1]] -= 1
            if mydict.get(s[i+len(p)-1], None)!=None:
                mydict[s[i+len(p)-1]] += 1

            if not any(mydict.values()):
                res.append(i)

        return res

    def findAnagrams1(self, s, p):
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0]*123, [0]*123
        for x in p:
            phash[ord(x)] += 1
        for x in s[:m-1]:
            shash[ord(x)] += 1
        for i in range(m-1, n):
            shash[ord(s[i])] += 1
            if i-m >= 0:
                shash[ord(s[i-m])] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res