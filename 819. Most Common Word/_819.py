class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        import collections
        paragraph = paragraph.replace(',',' ').replace(';',' ').replace('!', ' ').replace('\'', ' ').replace('?', ' ').replace('.', ' ')
        print(paragraph)
        res = paragraph.split(' ')
        for i in range(len(res)):
            res[i] = res[i].lower()
        resdict = collections.Counter(res)
        print(resdict)
        for k in sorted(resdict,key=resdict.__getitem__,reverse=True):
            if k == " " or k == "":
                continue
            if k in banned:
                continue
            return k

a = Solution()
print(a.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))