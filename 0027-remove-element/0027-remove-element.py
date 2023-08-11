class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ret = 0
        tmp = []
        for i in nums:
            if i != val:
                ret += 1
                tmp.append(i)
        for j in range(len(tmp)):
            nums[j] = tmp[j]
        return ret
            