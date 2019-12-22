class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split(' ')
        res.reverse()
        s = ""
        res1 = list()
        for i in res:
            if i == "" or i == " ":
                continue
            res1.append(i)
        return " ".join(res1)

    def reverseWords1(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])

    def reverseWords2(self, s):
        word = ""
        words = ""
        s = s[::-1]
        for j, i in enumerate(s):
            if i != " " and word != "" and s[j-1] == " ":
                words += (word + " ")
                word = i
            elif i != " ":
                word = i + word
            else:
                continue
        words += word
        return(words)

a = Solution()
print(a.reverseWords1( "a good   example"))