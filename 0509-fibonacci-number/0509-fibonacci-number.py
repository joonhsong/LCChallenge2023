class Solution:
    def fib(self, n: int) -> int:
        mem = []
        for i in range(n):
            mem.append(0)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if mem[n-1] != 0:
            return mem[n-1]
        mem[n-1] = self.fib(n-1)+self.fib(n-2)
        return mem[n-1]