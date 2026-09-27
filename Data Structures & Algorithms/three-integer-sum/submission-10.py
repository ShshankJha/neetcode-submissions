class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if num == nums[i-1] and (i>0):
                continue 
            
            l, r = i+1, len(nums)-1
            while l < r: 
                threesum = num + nums[l] + nums[r]

                if threesum < 0: 
                    l += 1
                
                elif threesum > 0: 
                    r -= 1 
                
                else:
                    result.append([num, nums[l], nums[r]])
                    l+=1 
                    while (nums[l] == nums[l-1]) and (l < r):
                        l += 1
        
        return result 


        