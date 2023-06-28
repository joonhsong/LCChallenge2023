class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0]
        for i in range(1, n+1):
            ret.append(ret[i >> 1] + i % 2)
        return ret
            
        