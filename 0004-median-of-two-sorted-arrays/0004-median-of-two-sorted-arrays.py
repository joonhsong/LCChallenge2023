class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 == 1:
            return nums[len(nums)//2]
        n = len(nums)//2
        m = len(nums)//2-1
        r = (nums[m]+nums[n])/2
        return r
        