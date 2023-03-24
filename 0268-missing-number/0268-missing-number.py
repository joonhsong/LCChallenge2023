class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        
        for n in nums:
            if n != count:
                return count            
            count += 1            
            
        return count