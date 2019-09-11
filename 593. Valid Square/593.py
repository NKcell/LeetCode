"""
593. Valid Square
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""


def validSquare(p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    point = [p1,p2,p3,p4]
    length = []
    for i in range(3):
        for j in range(i+1,4):
            length.append((point[i][0]-point[j][0])**2 + (point[i][1]-point[j][1])**2)

    if len(set(length)) == 2 and (length.count(length[0]) == 2 or length.count(length[0]) == 4):
        return True
    return False

print (validSquare([0,0], [1,1], [1,0], [0,1]))