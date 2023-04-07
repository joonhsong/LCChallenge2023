class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        ss = re.sub(r'[\W_]+|[\s]+','',lower)
        l = 0
        r = len(ss) - 1
        while l <= r:
            if ss[l] != ss[r]:
                return False
            l += 1
            r -= 1
        return True
        