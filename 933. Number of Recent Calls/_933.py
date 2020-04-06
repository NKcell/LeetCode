class RecentCounter:

    def __init__(self):
        self.res = list()
        
    def ping(self, t: int) -> int:
        flag = len(self.res)
        while flag > 0:
            if t-self.res[flag-1]>3000:
                self.res.pop()
                flag -= 1
            else:
                break

        self.res = [t] + self.res
        return len(self.res)
    
    # def __init__(self):
    #     self.dq = collections.deque()

    # def ping(self, t: int) -> int:
    #     self.dq.append(t)
    #     while self.dq[0] < t - 3000:
    #         self.dq.popleft()
    #     return len(self.dq)