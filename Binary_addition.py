class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        c = a + b
        return bin(c)[2:]
    
# binary addition of the two numbers.
# The slicing is used.
        
