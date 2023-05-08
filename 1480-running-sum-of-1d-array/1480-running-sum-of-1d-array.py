class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = []
        tmp = 0
        for i in nums:
            tmp += i
            rs.append(tmp)
        return rs