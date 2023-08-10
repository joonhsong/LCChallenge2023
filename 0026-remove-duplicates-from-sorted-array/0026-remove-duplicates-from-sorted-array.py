class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        tmp = -101
        tn = []
        for i in nums:
            if i != tmp:
                cnt += 1
                tmp = i
                tn.append(i)
        for j in range(len(tn)):
            nums[j] = tn[j]
        return cnt