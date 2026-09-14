class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, n in enumerate(nums): 
            differnece = target - nums[i]
            if differnece in numbers: 
                return [numbers[differnece], i]
            numbers[n] = i 