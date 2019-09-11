class Solution:
    def numSmallerByFrequency(self, queries, words):
        for i in range(len(queries)):
            queries[i] = self.countFrequency(queries[i])

        for i in range(len(words)):
            words[i] = self.countFrequency(words[i])

        words.sort(reverse = True)

        relist = list()
        for i in queries:
            count = 0
            for j in words:
                if j > i:
                    count+=1
                else:
                    break
            relist.append(count)
        
        return relist

    def countFrequency(self, word: str) -> int:
        mylist = [0]*26
        for i in word:
            mylist[ord(i)-97] += 1

        for i in mylist:
            if i != 0:
                return i

    # 写的很简洁很干练啊...
    def solutionOne(self, queries, words):
        w_counts = sorted([w.count(min(w)) for w in words])
        q_counts = [q.count(min(q)) for q in queries]
        return [sum( q_count < w_count for w_count in w_counts) for q_count in q_counts]


a = Solution()
print(a.numSmallerByFrequency(["bbb","cc"], ["a","aa","aaa","aaaa"]))