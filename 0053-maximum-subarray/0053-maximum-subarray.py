class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = 0
        msum = float('-inf')
        
        for n in nums:
            tmp = tmp + n
            if tmp > msum:
                msum = tmp
            if tmp < 0:
                tmp = 0
                
        return msum
        
        