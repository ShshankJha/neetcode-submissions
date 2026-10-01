class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        k = len(s1)
        valid = Counter(s1) 
        temp = Counter(s2[:k])

        left = 0

        for right in range(k,len(s2)):
            if temp == valid: 
                return True 
            
            else: 
                left += 1
                temp = Counter(s2[left:right+1])

        
        return temp == valid 

        