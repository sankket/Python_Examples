class Solution:
    def romanToInt(self, s: str) -> int:
        sums=0
        count=None
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if d[s[i]]>=d[s[i+1]]:
                sums+=d[s[i]]
            else:
                sums+= -d[s[i]]
        sums+=d[s[len(s)-1]]
        return sums
