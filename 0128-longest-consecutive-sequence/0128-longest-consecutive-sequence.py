class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numss = set(nums)
        long = 0
        
        for i in nums:
            if i-1 not in numss:
                leng = 0
                while(i+leng in numss):
                    leng += 1
                long = max(leng, long)
        return long
        
            
            
            
        