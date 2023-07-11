class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        if n == 1:
            return 1
        c1, c2 = 1, 1
        for i in range(1, n):
            d1 = int(s[i])
            d2 = int(s[i-1] + s[i])
            c = 0
            if d1 > 0:
                c += c2
            if d2 >= 10 and d2 <= 26:
                c += c1
            c1 = c2
            c2 = c
        return c2