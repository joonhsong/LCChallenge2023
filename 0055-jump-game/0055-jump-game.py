class Solution:
    def canJump(self, nums: List[int]) -> bool:
        e = 0
        for i, v in enumerate(nums):
            if e < i:
                return False
            e = max(e, v+i)
        return True