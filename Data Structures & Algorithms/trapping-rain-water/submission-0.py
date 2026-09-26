class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        Left_max = 0
        Right_max = 0 
        area = 0

        while left < right: 
            if height[left] < height[right]:
                if height[left] >= Left_max: 
                    Left_max = height[left]
                else: 
                    area += Left_max - height[left]
                
                left +=1
            else: 
                if height[right] >= Right_max: 
                    Right_max = height[right]
                else: 
                    area += Right_max - height[right]
                
                right -= 1
            
        
        return area 


        






