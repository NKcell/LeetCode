def solution(words, maxWidth):
    length = 0
    tmplist = list()
    res = list()
    i = 0
    while i<len(words):
        length += len(words[i])
        if length<=maxWidth:
            tmplist.append(words[i])
            i+=1
            length += 1
        else:
            newlength = 0
            for j in tmplist:
                newlength += len(j)
            tmp = ""
            if len(tmplist) != 1:
                average = (maxWidth-newlength)//(len(tmplist)-1)
                mod = (maxWidth-newlength)%(len(tmplist)-1)
                for j in range(len(tmplist)):
                    if j != len(tmplist)-1:
                        if mod != 0:
                            tmp += (tmplist[j]+" "+" "*average)
                            mod -= 1
                        else:
                            tmp += (tmplist[j]+" "*average)
                    else:
                        tmp+=(tmplist[j])
            else:
                tmp = tmplist[0] + " "*(maxWidth-newlength)
            res.append(tmp)
            length=0
            tmplist = list()
    tmp = ""
    for i in range(len(tmplist)):
        if i != len(tmplist)-1:
            tmp += (tmplist[i]+" ")
        else:
            tmp+=tmplist[i]
    tmp += " "*(maxWidth-len(tmp))
    res.append(tmp)
    return res