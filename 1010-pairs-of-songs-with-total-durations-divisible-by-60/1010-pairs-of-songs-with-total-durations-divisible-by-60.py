class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mc = [0] * 60
        ans = 0
        
        for t in time:
            opt = (60-(t%60))%60
            ans += mc[opt]
            mc[t%60] += 1
        
        return ans
        
        
        