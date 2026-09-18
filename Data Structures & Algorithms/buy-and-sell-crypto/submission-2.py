class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        dp[0] = 0 
        minvalue = prices[0]

        for i in range(1,len(prices)):
            if prices[i] < minvalue:
                minvalue = prices[i]
            
            dp[i] = prices[i] - minvalue 

        return max(dp)





