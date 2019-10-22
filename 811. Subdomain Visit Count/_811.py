class Solution:
    def subdomainVisits(self, cpdomains):
        myDict = {}
        for i in cpdomains:
            v, domain = i.split()
            v = int(v)
            tmp = ""
            for j in domain.split('.')[::-1]:
                tmp = j + tmp
                tmpv = myDict.get(tmp, 0)
                myDict[tmp] = tmpv+v
                tmp = "." + tmp
        return [str(myDict[i])+ " "+ i for i in myDict]

    def subdomainVisits1(self, cpdomains):
        import collections
        counter = collections.Counter()
        for cpdomain in cpdomains:
            count, *domains = cpdomain.replace(" ",".").split(".")
            for i in range(len(domains)):
                counter[".".join(domains[i:])] += int(count)
        return [" ".join((str(v), k)) for k, v in counter.items()]