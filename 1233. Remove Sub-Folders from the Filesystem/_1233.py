class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = lambda i:len(i))
        res = set()
        for item in folder:
            flag = 1
            for i,v in enumerate(item):
                if v == '/' and item[:i] in res:
                    flag = 0
                    break
            if flag:
                res.add(item)

        return list(res)