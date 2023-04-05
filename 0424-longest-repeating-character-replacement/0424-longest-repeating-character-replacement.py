class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        coun = {}
        maxc = 0
        longest = 0
        while r < len(s):
            coun[s[r]] = coun.get(s[r], 0) + 1
            maxc = max(maxc, coun[s[r]])
            if r - l + 1 - maxc > k:
                coun[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        return longest 
        