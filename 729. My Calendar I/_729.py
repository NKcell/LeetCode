class MyCalendar:

    def __init__(self):
        self.booked = list()

    def book(self, start: int, end: int) -> bool:
        for s,e in self.booked:
            if start<e and end>s:
                return False
        self.booked.append((start, end))
        return True
            

class MyCalendar1:
    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        import bisect
        index = bisect.bisect(self.ends, start)
        if index == len(self.ends) or end<=self.starts[index]:
            self.starts.insert(index, start)
            self.ends.insert(index, end)
            return True
        return False