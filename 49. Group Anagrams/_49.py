class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = dict()

        for i in strs:
            tmp = ''.join(sorted(list(i)))
            tmplist = mydict.get(tmp, None)
            if not tmplist:
                mydict[tmp] = [i]
            else:
                tmplist.append(i)
                mydict[tmp] = tmplist

        return mydict.values()

    def anagrams(self, strs):
        import collections
        count = collections.Counter([tuple(sorted(s)) for s in strs])
        return filter(lambda x: count[tuple(sorted(x))]>1, strs)

    def groupAnagrams1(self, strs):
        hashmap = {}
        for st in strs:
            key = ''.join(sorted(st))
            if key not in hashmap:
                hashmap[key] = [st]
            else:
                hashmap[key] += [st]
        return hashmap.values()