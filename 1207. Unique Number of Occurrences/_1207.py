class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        from collections import Counter
        tmp = Counter(arr)
        return len(tmp)==len(set([tmp[i] for i in tmp]))