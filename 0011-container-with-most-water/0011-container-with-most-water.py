class Solution:
    def maxArea(self, height: List[int]) -> int:
        lef = 0
        rig = len(height) - 1
        maxa = 0
        while lef < rig:
            maxa = max(maxa, min(height[lef], height[rig]) * (rig - lef))
            if height[lef] < height[rig]:
                lef += 1
            else:
                rig -= 1
        return maxa