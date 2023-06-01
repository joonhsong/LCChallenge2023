class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        d = [0] * n
        d[0] = nums[0]
        d[1] = nums[1]
        for i in range(2, n):
            if i > 2:
                d[i] = nums[i] + max(d[i-2], d[i-3])
            else:
                d[i] = nums[i] + d[i-2]
        return max(d[-1], d[-2])
        