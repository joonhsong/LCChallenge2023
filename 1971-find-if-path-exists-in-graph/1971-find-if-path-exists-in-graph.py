class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        con = defaultdict(set)
        for u,v in edges:
            con[u].add(v)
            con[v].add(u)
        
        vis = {source}
        stack = [source]
        while stack:
            v = stack.pop()
            if v == destination:
                return True
            for u in con[v]:
                if u not in vis:
                    vis.add(u)
                    stack.append(u)
        return False
        