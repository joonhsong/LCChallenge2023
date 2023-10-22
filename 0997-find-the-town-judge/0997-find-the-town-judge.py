class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
            mat = [0]*(n+1)
            for i,j in trust:
                mat[i] -= 1
                mat[j] += 1
            for i in range(1, n+1):
                if mat[i] == n-1:
                    return i
            return -1
        