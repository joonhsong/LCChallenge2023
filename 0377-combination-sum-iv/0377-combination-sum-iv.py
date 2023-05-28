class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = [0] * (target+1)
        d[0] = 1
        
        for i in range(target):
            for n in nums:
                if n + i <= target:
                    d[i+n] += d[i]
        return d[target]