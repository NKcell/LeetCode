class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res1 = list()
        for i in S:
            if i!='#':
                res1.append(i)
            elif len(res1)==0:
                continue
            else:
                res1.pop()
        
        res2 = list()
        for i in T:
            if i!='#':
                res2.append(i)
            elif len(res2)==0:
                continue
            else:
                res2.pop()

        return res1==res2