"""
649. Dota2 Senate
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right:
A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory:
If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and make the decision about the change in the game.
Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.

Example 1:
Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
And the second senator can't exercise any rights any more since his right has been banned.
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:
Input: "RDD"
Output: "Dire"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And the third senator comes from Dire and he can ban the first senator's right in the round 1.
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
"""


# 成功被接受，打败0%
def predictPartyVictory(senate):
    """
    :type senate: str
    :rtype: str
    """
    senate = list(senate)

    while True:
        temp = []
        while len(senate) != 0:
            temp.append(senate[0])

            if senate[0] == 'R':
                try:
                    senate = senate[1:]
                except:
                    try:
                        temp.remove('D')
                        break
                    except:
                        return "Radiant"
                try:
                    senate.remove('D')
                    continue
                except:
                    try:
                        temp.remove('D')
                        continue
                    except:
                        return "Radiant"

            if senate[0] == 'D':
                try:
                    senate = senate[1:]
                except:
                    try:
                        temp.remove('R')
                        break
                    except:
                        return "Dire"
                try:
                    senate.remove('R')
                    continue
                except:
                    try:
                        temp.remove('R')
                        continue
                    except:
                        return "Dire"

            if senate is None:
                break

        senate = temp

print( predictPartyVictory("R"))

"""
Simulate the process. We don't have to resolve bans until later - we can just let them "float".

We have people = [int, int] representing how many people are in the queue, and bans = [int, int] representing how many "floating" bans there are. When we meet a person, if there is a floating ban waiting for them, then they are banned and we skip them. Eventually, the queue will just have one type of person, which is when we break.

def predictPartyVictory(self, senate):
    A = collections.deque()
    people = [0, 0]
    bans = [0, 0]

    for person in senate:
        x = person == 'R'
        people[x] += 1
        A.append(x)

    while all(people):
        x = A.popleft()
        people[x] -= 1
        if bans[x]:
            bans[x] -= 1
        else:
            bans[x^1] += 1
            A.append(x)
            people[x] += 1

    return "Radiant" if people[1] else "Dire"
"""

"""
My python code beats 100%. Any improvement suggestions are welcome

class Solution(object):
    def predictPartyVictory(self, senate):
        
        global nex, cr, cd, r, d
        cur = []
        nex = []
        cr = cd = 0
        r = d = 0
        
        def helper(c):
            global nex, cr, cd, r, d
            if c == 'R':
                if cd > 0:
                     cd -= 1
                else:
                    cr += 1
                    nex.append('R')
                    r += 1
            else:
                if cr > 0:
                    cr -= 1
                else:
                    cd += 1
                    nex.append('D')
                    d += 1
        
        for c in senate:
            helper(c)
        
        while r <= 2 * d and d <= 2 * r:
            cur[:] = nex[:]
            del nex[:]
            r = d = 0
            for c in cur:
                helper(c)

        if r > 2 * d:
            return "Radiant"
        if d > 2 * r:
            return "Dire"
"""

"""
class Solution:
    def predictPartyVictory(self, senate):
        ban_r = ban_d = 0
        while True:
            new = []
            r_cnt = d_cnt = 0
            for s in senate:
                if s == 'R': 
                    r_cnt += 1
                    if ban_r: 
                        ban_r -= 1
                    else: 
                        ban_d += 1
                        d_cnt -= 1
                        new.append(s)
                elif s == 'D':
                    d_cnt += 1
                    if ban_d: 
                        ban_d -= 1
                    else: 
                        ban_r += 1
                        r_cnt -= 1
                        new.append(s)
            if d_cnt < 0 < r_cnt:
                return "Radiant"
            elif r_cnt < 0 < d_cnt:
                return "Dire"
            senate = new
"""