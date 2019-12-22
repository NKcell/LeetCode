class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed)<len(name) or name[0] != typed[0]:
            return False

        pre = 0
        namelist = list()
        for i in range(len(name)-1):
            if name[i]!= name[i+1]:
                namelist.append(name[pre:i+1])
                pre = i+1
        pre = 0
        typedlist = list()
        for i in range(len(typed)-1):
            if typed[i]!= typed[i+1]:
                typedlist.append(typed[pre:i+1])
                pre = i+1

        if len(namelist) != len(typedlist):
            return False

        for i in range(len(namelist)):
            if len(typedlist[i])<len(namelist[i]) or typedlist[i][0] != namelist[i][0]:
                return False

        return True

    def isLongPressedName1(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)

a = Solution()
print(a.isLongPressedName(name = "laiden", typed = "laiden"))