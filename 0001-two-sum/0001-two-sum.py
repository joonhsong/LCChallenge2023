class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        out = []
        for i, j in enumerate(nums):
            if j in d:
                out.append(d[j])
                out.append(i)
            else:
                d[target-j] = i
        return out
                
            
        