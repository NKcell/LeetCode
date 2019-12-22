class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if coordinates[0][1] == coordinates[1][1]:
            return len(set([i[1] for i in coordinates])) == 1
        else:
            
            rate = (coordinates[0][0]-coordinates[1][0])/(coordinates[0][1]-coordinates[1][1])
            for i in range(2, len(coordinates)):
                if (coordinates[0][1]-coordinates[i][1]) == 0:
                    return False
                if (coordinates[0][0]-coordinates[i][0])/(coordinates[0][1]-coordinates[i][1]) != rate:
                    return False
            return True

a = Solution()
print(a.checkStraightLine([[-9,4],[-10,-7],[11,4],[-13,-13],[-7,-1],[-8,-4],[-13,-3],[10,-14],[13,6],[-2,-4],[-6,5],[-5,-2],[-8,-10],[-10,10]]))