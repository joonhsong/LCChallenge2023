class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        a = [1]*(len(nums))

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and a[i] < a[j] + 1:
                    a[i] = a[j] + 1
        
        return max(a)
            
            
        
        
        