class Solution:
    def replaceWords(self, mydict, sentence: str) -> str:
        sentence = sentence.split(" ")
        res = list()
        for i in sentence:
            tmp = list()
            flag = 0
            for j in mydict:
                if i.startswith(j):
                    tmp.append(j)
                    flag = 1
            if flag != 0:
                tmp.sort(key = lambda i:len(i))
                res.append(tmp[0])
            else:
                res.append(i)
        return ' '.join(res) 

    def replaceWords1(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))