class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        storage = set()
        left = 0 
        best = 0

        for right, letter in enumerate(s):
            while letter in storage: 
                storage.remove(s[left])
                left += 1
            
            storage.add(letter)
            best = max(best, (right-left)+1)

        return best 

        

        