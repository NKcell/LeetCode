class Solution:
    def longestWord(self, words) -> str:
        words.sort(key = lambda i:len(i)) 
        mylen = 1

        tmp = {}
        end = 0
        for i,v in enumerate(words):
            if len(v) == mylen:
                tmp[v] = 1
                end = i
        words = words[end+1:]
        end =0
        mylen += 1

        while len(words) != 0:
            tmp1 ={}
            for i,v in enumerate(words):
                if len(v) == mylen:
                    dictv = tmp.get(v[:mylen-1], 0)
                    if dictv != 0:
                        tmp1[v] = 1
                    end = i
            if len(tmp1) == 0:
                break
            else:
                tmp = tmp1
                words = words[end+1:]
                end =0
                mylen += 1

        res = [i for i in tmp]
        res.sort()
        return res[0]


    def longestWord1(self, words):
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

    # 这个思路还是一样，但写的更python
    def longestWord2(self, words):
        valid = set([""])
        for word in sorted(words, key=lambda x: len(x)):
            if word[:-1] in valid:
                valid.add(word)
        return max(sorted(valid), key=lambda x: len(x))

a = Solution()
print(a.longestWord( ["a", "banana", "app", "appl", "ap", "apply", "apple"]))