class Solution:
    def frequencySort(self, s: str) -> str:
        mydict = {}
        for i in s:
            tmp = mydict.get(i, 0)
            mydict[i] = tmp+1
        
        res = ""
        for i,v in sorted(mydict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True):
            res += (i*v)

        return res

    def frequencySort1(self, str):
        import collections
        return "".join(char * times for char, times in collections.Counter(str).most_common())

a = Solution()
print(a.frequencySort("Aabb"))