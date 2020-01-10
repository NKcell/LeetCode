class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(B)==len(A) and B in 2*A:
            return True
        return False

    def rotateString1(self, A, B):        
        return len(A) == len(B) and B in A + A