class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        window = set()
        start, end = 0, 0

        while end < len(s):
            if s[end] not in window:
                window.add(s[end])
                end += 1
            else:
                window.remove(s[start])
                start += 1
            max_length = max(max_length, end - start)

        return max_length