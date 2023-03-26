class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        arr = [0] *(target+1)
        for n in nums:
            if n <= target:
                arr[n] = 1
        for i in range(target+1):
            for n in nums:
                if i - n > 0:
                    arr[i] += arr[i-n]
        ret = arr[-1]
        
        return ret
        