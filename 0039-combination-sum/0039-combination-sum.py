class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def dfs(candidates, start, path):
            if sum(path) > target or start >= len(candidates):
                return
            if sum(path) == target:
                ret.append(path)
                return
            dfs(candidates, start, path+[candidates[start]])
            dfs(candidates, start+1, path)
        
        dfs(candidates, 0, [])
        return ret
        