class Solution:
    def arrayRankTransform(self, arr):
        newarr = sorted(list(set(arr)))
        mydict = dict()
        for i,v in enumerate(newarr):
            mydict[v] = i+1
        
        for i,v in enumerate(arr):
            arr[i] = mydict[v]

        return arr

    def arrayRankTransform1(self, A):
        rank = {}
        for a in sorted(A):
            rank.setdefault(a, len(rank) + 1)
        return map(rank.get, A)