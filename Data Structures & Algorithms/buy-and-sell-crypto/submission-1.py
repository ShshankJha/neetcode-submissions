class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        dp[0] = 0
        minprice = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            
            dp[i] = prices[i] - minprice

        
        return max(dp)

