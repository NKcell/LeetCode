class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        mydict = {}
        bull = 0
        cows = 0

        for i in secret:
            v = mydict.get(i, 0)
            mydict[i] = v+1

        for i in guess:
            v = mydict.get(i, 0)
            if v != 0:
                cows+=1
                mydict[i] = v-1
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                cows -= 1
                bull += 1

        return str(bull)+'A'+str(cows)+'B'

    # 这个用库的方式还是要多学习，特别是collections这个库
    def getHint1(self, secret: str, guess: str) -> str:
        from collections import Counter
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return '%sA%sB' % (a, sum((s & g).values()) - a)