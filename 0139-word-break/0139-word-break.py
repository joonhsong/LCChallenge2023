class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ls = len(s)
        d = [False]*(ls+1)
        d[0] = True
        for i in range(1, ls+1):
            for w in wordDict:
                if len(w) > i:
                    continue
                if s[i-len(w):i] == w and d[i-len(w)]:
                    d[i] = d[i-len(w)]
                    break
                    
        return d[len(s)]
        