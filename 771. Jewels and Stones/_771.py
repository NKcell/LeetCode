class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        for i in S:
            if i in J:
                res += 1
        return res

    def numJewelsInStones1(self, J, S):
        return sum(map(J.count, S))
    
    def numJewelsInStones2(self, J, S):
        return sum(map(S.count, J)) 

    def numJewelsInStones3(self, J, S):             
        return sum(s in J for s in S)
        #  return sum([i in J for i in S])