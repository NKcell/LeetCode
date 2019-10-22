class Solution:
    def uncommonFromSentences(self, A: str, B: str) :
        s = A + " " + B
        s = s.split()
        return [i for i in s if s.count(i) < 2]

    def uncommonFromSentences1(self, A, B):
        import collections
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]
