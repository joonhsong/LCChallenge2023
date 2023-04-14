class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ret = []
        lef = 0
        rig = len(numbers)-1
        
        while lef != rig:
            if numbers[lef]+numbers[rig] == target:
                ret.append(lef+1)
                ret.append(rig+1)
                break
            if numbers[lef]+numbers[rig] > target:
                rig -= 1
            else:
                lef += 1
        return ret
                