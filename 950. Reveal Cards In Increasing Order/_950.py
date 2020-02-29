class Solution:
    def deckRevealedIncreasing(self, deck):
        res = [0]*len(deck)

        deck.sort()
        flag = 1
        count = 0
        while True:
            for index, value in enumerate(res):
                if count>=len(deck):
                    return res
                if value != 0:
                    continue
                flag = (flag+1)%2
                if flag:    
                    continue
                else:
                    res[index] = deck[count]
                    count+=1

    def deckRevealedIncreasing1(self, deck):
        d = []
        for x in sorted(deck)[::-1]:
            d = [x] + d[-1:] + d[:-1]
        return d