class Solution:
    def filterRestaurants(self, restaurants, veganFriendly: int, maxPrice: int, maxDistance: int):
        from operator import itemgetter
        res = list()
        for i in restaurants:
            if veganFriendly:
                if i[2] and i[3]<=maxPrice and i[4]<=maxDistance:
                    res.append([i[0], i[1]])
            else:
                if i[3]<=maxPrice and i[4]<=maxDistance:
                    res.append([i[0], i[1]])

        res.sort(key=itemgetter(1,0), reverse=True)

        return [x[0] for x in res]


a = Solution()
print(a.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3))