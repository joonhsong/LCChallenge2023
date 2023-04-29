class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas = []
        for i in range(1, numRows+1):
            tmp = i*[1]
            pas.append(tmp)
        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    continue
                pas[i][j] = pas[i-1][j-1]+pas[i-1][j]
        return pas
        