class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_s = {}
        str_t = {}

        for letter in s: 
            if letter in str_s:
                str_s[letter] += 1
            else: 
                str_s[letter] = 1
        
        for letter in t: 
            if letter in str_t:
                str_t[letter] += 1
            else: 
                str_t[letter] = 1
        
        return str_s == str_t
        