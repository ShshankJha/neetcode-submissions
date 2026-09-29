class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0]*len(cost)
        memo[0] = cost[0]
        memo[1] = cost[1]

        for i in range(2, len(memo)):
            memo[i] = min(cost[i]+memo[i-1], cost[i]+memo[i-2])
        
        return min(memo[-1], memo[-2])
        