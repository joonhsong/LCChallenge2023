class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        a = 1
        for i in nums:
            ret.append(a)
            a *= i
        a = 1
        for i in reversed(range(len(nums))):
            ret[i] *= a
            a *= nums[i]
            
        return ret