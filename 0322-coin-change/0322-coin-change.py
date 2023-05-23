class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [amount+1]*(amount+1)
        a[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    a[i] = min(a[i], a[i-c]+1)
        if a[amount] == amount+1:
            return -1
        return a[amount]