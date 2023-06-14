class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        minpri = float('inf')
        for p in prices:
            minpri = min(minpri, p)
            prof = max(prof, p - minpri)
        return prof
        