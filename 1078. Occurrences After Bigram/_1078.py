class Solution:
    def findOcurrences(self, text: str, first: str, second: str) :
        mylist = text.split(" ")
        res = list()
        for i in range(len(mylist)-2):
            if mylist[i] == first and mylist[i+1] == second:
                res.append(mylist[i+2])

        return res

    def findOcurrences1(self, t: str, f: str, s: str):
        return [c for a, b, c in zip(t.split(), t.split()[1:], t.split()[2:]) if a == f and b == s]