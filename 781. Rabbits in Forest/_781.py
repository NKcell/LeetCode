class Solution:
    def numRabbits(self, answers) -> int:
        import collections
        import math
        res = collections.Counter(answers)
        count = 0
        for i in res:
            count +=  math.ceil(res[i]/(i+1))*(i+1)
        return count