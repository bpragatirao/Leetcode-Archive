class Solution:
    def graphColoring(self, edges, m, n):
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        colors = [0] * n
        def possible(node, c):
            for j in adj[node]:
                if colors[j] == c:
                    return False
            return True

        def solve(node):
            if node == n:
                return True
            for c in range(1, m + 1):
                if possible(node, c):
                    colors[node] = c
                    if solve(node + 1):
                        return True
                    colors[node] = 0
            return False
        return solve(0)
