class Solution:
    def findDuplicate(self, paths):
        mydict = dict()
        for i in paths:
            tmp = i.split(" ")
            for filename in tmp[1:]:

                content = filename.split('(')
                path = tmp[0]+'/'+content[0]
                exist = mydict.get(content[1], None)
                if exist:
                    exist.append(path)
                    mydict[content[1]] = exist
                else:
                    mydict[content[1]] = [path]

        res = list()
        for i in mydict:
            if len(mydict[i])>1:
                res.append(mydict[i])

        return res

    def findDuplicate1(self, paths):
        import collections
        M = collections.defaultdict(list)
        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                name, _, content = file.partition('(')
                M[content[:-1]].append(root + '/' + name)
                
        return [x for x in M.values() if len(x) > 1]

a = Solution()
print(a.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
