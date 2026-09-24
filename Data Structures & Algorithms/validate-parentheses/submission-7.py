class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        bracket = []
        count = 0

        for p in s: 
            if p == "(" or p == "{" or p == "[":
                bracket.append(p)
                count += 1
            else: 
                if count == 0: 
                    return False 
                
                temp = bracket.pop()
                
                if temp == "{" and p != "}":
                    return False
                
                elif temp == "(" and p != ")":
                    return False
                
                elif temp == "[" and p != "]":
                    return False 
                
                count -= 1 
            
        
        if count != 0: 
            return False 
        else: 
            return True






