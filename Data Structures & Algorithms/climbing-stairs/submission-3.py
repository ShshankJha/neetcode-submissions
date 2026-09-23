class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 2: 
            return n  


        combination = [0]*(n+1)
        combination[1] = 1
        combination[2] = 2

        for i in range(3, n+1): 
            combination[i] = combination[i-1] + combination[i-2]
        
        return combination[n]