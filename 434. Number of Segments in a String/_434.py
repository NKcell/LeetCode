class Solution:
    def countSegments(self, s: str) -> int:
        flag = False
        count = 0
        for i in s:
            if i != ' ' and not flag:
                count += 1
                flag = True
            if i == ' ':
                flag = False
        
        return count

    def countSegments1(self, s: str) -> int:
        return len(s.split())