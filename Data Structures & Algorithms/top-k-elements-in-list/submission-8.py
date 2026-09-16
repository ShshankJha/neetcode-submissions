class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        
        results = []
        x = k
        while x != 0: 
            maxvalue = max(dic.values())

            for key, value in dic.items():
                if dic[key] == maxvalue:
                    results.append(key)
                    del dic[key]
                    break 
            
            x -= 1 
        
        return results 



        
        