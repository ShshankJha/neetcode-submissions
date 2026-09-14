class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for item in strs: 
            temp = str(sorted(item))

            if temp in words: 
                words[temp].append(item)

            else: 
                words[temp] = [item]

        results = []
        for key, value in words.items():
            results.append(value)
        
        return results 



        

        