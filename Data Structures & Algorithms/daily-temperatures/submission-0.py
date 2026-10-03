class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n 
        stack = []

        for i in range(n):
            if not stack or temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
            else: 
                while not stack or temperatures[stack[-1]] < temperatures[i]:
                    if not stack:
                        break 
                    temp = stack.pop()
                    result[temp] = i - temp 
                
                stack.append(i)
        
        return result
        