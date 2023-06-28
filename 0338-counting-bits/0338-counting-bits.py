class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        for i in range(n+1):
            binar = bin(i)
            c = binar.count('1')
            ret.append(c)
        return ret
            
        