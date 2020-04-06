class Solution:
    def rankTeams(self, votes) -> str:
        myDict = dict()
        for i in votes:
            for index, value in enumerate(i):
                tmp = myDict.get(value, 0)
                if tmp == 0:
                    tmpList = [0]*len(i)+[value]
                    tmpList[index] -= 1
                    myDict[value] = tmpList
                else:
                    tmp[index] -= 1
                    myDict[value] = tmp

        return ''.join(sorted(votes[0], key = myDict.get))