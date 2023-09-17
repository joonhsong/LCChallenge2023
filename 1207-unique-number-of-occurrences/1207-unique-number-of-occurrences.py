class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        u = {}
        for i in arr:
            if i not in u:
                u[i] = 1
            else:
                u[i] += 1
        if len(set(u.values())) == len(set(arr)):
            return True
        return False