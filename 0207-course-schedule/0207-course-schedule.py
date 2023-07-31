class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for x in range(numCourses)]
        for i in prerequisites:
            g[i[1]].append(i[0])
        vis = [0] * numCourses
        path = [0] * numCourses
        def dfs(node, vis, path, g):
            vis[node] = 1
            path[node] = 1
            for i in g[node]:
                if vis[i] == 0:
                    if dfs(i, vis, path, g):
                        return True
                elif path[i] == 1:
                    return True
            path[node] = 0
            return False
        for i in range(numCourses):
            if vis[i] == 0:
                if dfs(i, vis, path, g):
                    return False
        return True
        