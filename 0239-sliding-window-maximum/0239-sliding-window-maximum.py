class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        w = deque()
        ret = []
        for i, num in enumerate(nums):
            while w and w[0] < i - k + 1:
                w.popleft()

            while w and nums[w[-1]] < num:
                w.pop()

            w.append(i)

            if i >= k - 1:
                ret.append(nums[w[0]])

        return ret
        