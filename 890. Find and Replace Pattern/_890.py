class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        res = list()
        for i in words:
            tmpDict1 = {}
            tmpDict2 = {}
            flag = 0
            for index,value in enumerate(i):

                tmp1 = tmpDict1.get(value, None)
                tmp2 = tmpDict2.get(pattern[index], None)
                if not tmp1 and not tmp2:
                    tmpDict1[value] = pattern[index]
                    tmpDict2[pattern[index]] = value
                elif not tmp1 and tmp2:
                    flag = 1
                    break
                elif tmp1 and not tmp2:
                    flag = 1
                    break
                else:
                    if tmp1 != pattern[index] or tmp2 != value:
                        flag = 1
                        break
            
            if flag == 0:
                res.append(i)

        return res

    def findAndReplacePattern1(self, words, p):
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]
        return [w for w in words if F(w) == F(p)]