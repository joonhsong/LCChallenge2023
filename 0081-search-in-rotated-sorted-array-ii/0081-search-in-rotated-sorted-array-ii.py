class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # for i in nums:
        #     if i == target:
        #         return True
        # return False
        
        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False