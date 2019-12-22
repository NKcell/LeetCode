class Solution:
    def toLowerCase(self, st: str) -> str:
        return st.lower()

    def toLowerCase1(self, str): 
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)