class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, num in enumerate(nums): 
            dif = target - num
            if dif in numbers: 
                return [numbers[dif], i]
            
            numbers[num] = i