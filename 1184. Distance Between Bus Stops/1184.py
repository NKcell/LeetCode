class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        return min(sum(distance[start:destination]), (sum(distance[:start])+sum(distance[destination:])))

a = Solution()
print(a.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))