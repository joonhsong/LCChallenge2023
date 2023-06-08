class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = nums[0]
        mxp = nums[0]
        mnp = nums[0]
        
        for i in range(1, len(nums)):
            tmp = max(nums[i], mxp*nums[i], mnp*nums[i])
            mnp = min(nums[i], mxp*nums[i], mnp*nums[i])
            mxp = tmp
            ret = max(mxp, ret)
        
        return ret