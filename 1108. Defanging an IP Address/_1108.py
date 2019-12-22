class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))

    def defangIPaddr1(self, address: str) -> str:
        return address.replace('.', '[.]')