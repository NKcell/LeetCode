class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        import datetime
        startTime = datetime.datetime.strptime(date1, '%Y-%m-%d')
        endTime = datetime.datetime.strptime(date2, '%Y-%m-%d')
        return abs((startTime - endTime).days)
    
    def daysBetweenDates1(self, date1: str, date2: str) -> int:
        def day(y, m, d):
            yd = 365 * (y-1970)
            for i in range(1970, y):
                if i % 4 == 0:
                    yd += 1    
            
            month = [31,28,31,30,31,30,31,31,30,31,30,31]        
            md = sum(month[:m-1])
            if y % 4 == 0 and y != 2100 and m > 2:
                md += 1
            
            return yd + md + d
			
        y1 = int(date1[:4])
        m1 = int(date1[5:7])
        d1 = int(date1[8:])
		
        y2 = int(date2[:4])
        m2 = int(date2[5:7])
        d2 = int(date2[8:])
		
        days1 = day(y1, m1, d1)
        days2 = day(y2, m2, d2)
		
        return abs(days1-days2)