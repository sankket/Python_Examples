class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        return 0 if not s else len(s.strip().split(" ")[-1])
 


#Split method is used here.
