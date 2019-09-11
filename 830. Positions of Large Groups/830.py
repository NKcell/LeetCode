class Solution:
    def largeGroupPositions(self, S: str):
        pre = 0
        length = 0
        mylist = list()
        for i in range(len(S)):
            if S[i] == S[pre]:
                length += 1
            else:
                if length > 2:
                    mylist.append([pre,i-1])
                pre = i
                length = 1
        if length > 2:
                    mylist.append([pre,len(S)-1])
        return mylist

    def largeGroupPositions1(self, S):
        i, j, N = 0, 0, len(S)
        res = []
        while i < N:
            while j < N and S[j] == S[i]: j += 1
            if j - i >= 3: res.append((i, j - 1))
            i = j
        return res

a = Solution()
print(a.largeGroupPositions("aaa"))