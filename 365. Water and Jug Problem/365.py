"""
365. Water and Jug Problem

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
"""

# 后面想了很久才发现是求最大公约数解决，但总感觉还有问题
def canMeasureWater(x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        da = max(x, y)
        xi = min(x, y)

        if xi == 0:
            if da == 0:
                return da == z
            else:
                return z % da == 0

        a = x
        b = y

        flag = a%b
        while flag:
            a,b = b, a%b
            flag = b

        if z % a == 0 and z <= x+y:
            return True
        else:
            return False


print (canMeasureWater(2,6,5))



"""
class Solution(object):
    def canMeasureWater(self, x, y, z):
        # Explanation: 
        # Key idea is that z litres is measurable using jugs of size x and y only if , z is a linear combination of x and y.
        # Reasoning for key idea : 
        # basically only options we have to solve the issue is - either pour water of amount x or y (which is positive multiplication constant on x or y) or a choice of emptying x or y (which is negative multiplication constant on x or y). hence for z to be measurable by x and y, z has to be 
z = sx+ly (where s and l are integer constants, we dont need to know s and l to solve our problem :))
        # So, in positive case where, z = kx + ly where k and l are constants, z is measurable. 
        # Now, if g is gcd of x and y, then z = kag + lbg where a and b are constants 
        # So, z = (ka+lb)g -> which suggests z must be divisible by g in order for z to be measurable by x and y. 
        # AND 
        # x + y must be equal or greater than z, otherwise we can fill up x and y both, but still they will sum up less than z. Hence, z won't be measurable if x + y < z
        # using that logic, we can say answer is:
        # return true if z % gcd(x, y) == 0 and x + y >= z
        
        def gcd(x, y):
            #Using Euclid's algorithm - https://en.wikipedia.org/wiki/Greatest_common_divisor
            if x < y : 
                x, y = y, x
            while x != y and y != 0 :
                remainder = x % y 
                x = y
                y = remainder
            return x
        
        g = gcd(x,y)
        #print("gcd: ", g)
        if g == 0:
            return z == 0
        
        return (x+y) >= z and z % g == 0 
				```
"""





