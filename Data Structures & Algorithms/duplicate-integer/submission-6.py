class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seta = set()

        for num in nums: 
            if num in seta:
                return True 
            
            seta.add(num)
        
        return False 


        