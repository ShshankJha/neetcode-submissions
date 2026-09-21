class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0

        seta = set(nums)
        start = []
        for num in seta: 
            if (num-1) in seta: 
                continue 
            else: 
                start.append(num)

        longeststreak = 1

        for number in start:
            tempnum = number
            temp = 1

            while (tempnum + 1) in seta: 
                temp += 1
                tempnum += 1 


            longeststreak = max(longeststreak, temp)


        return longeststreak 
            







        