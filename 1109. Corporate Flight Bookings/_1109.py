class Solution:
    def corpFlightBookings(self, bookings, n: int) :
        res = [0]*(n+1)
        for item in bookings:
            res[item[0]-1] += item[2]
            res[item[1]] -= item[2]
        for i in range(1,n):
            res[i] += res[i-1] 
        return res[:-1]
