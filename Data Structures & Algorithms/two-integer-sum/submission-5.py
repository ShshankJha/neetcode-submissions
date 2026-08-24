class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #value : index
        for i, n in enumerate(nums):
            req = target - n
            if req in prevMap:
                return [prevMap[req], i]
            prevMap[n] = i 
