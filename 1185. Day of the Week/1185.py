class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        from datetime import date
        weeklist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        a = date(year, month, day)
        return weeklist[a.weekday()]

a = Solution()
print(a.dayOfTheWeek(13,9,2019))