class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count('L') == moves.count('R') and moves.count('D') == moves.count('U'):
            return True
        return False