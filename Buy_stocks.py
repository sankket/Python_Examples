class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        maxprofit = 0
        
        for i in range(len(prices)-1):
            if prices[i+1]> prices[i]:
                
                maxprofit += prices[i+1] -  prices[i]
            
        return maxprofit

 #program to buy the stocks and make the big profit
