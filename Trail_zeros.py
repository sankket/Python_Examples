class Solution:
    def trailingZeroes(self, num: int) -> int:
        counter = 0
        while num >= 5:
            num = num // 5
            counter += num
        return counter
            
        
