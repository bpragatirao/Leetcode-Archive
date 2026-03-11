class Solution:
    def findPath(self, grid):
        n = len(grid)
        res = []
        def maze(r,c,path,sub):
            if r==n-1 and c==n-1:
                res.append(path)
                return

            sub.add((r,c))
            D = [[1,0,"D"],[0,1,"R"],[-1,0,"U"],[0,-1,"L"]]
            for dr,dc,move in D:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in sub and grid[nr][nc]==1:
                    maze(nr,nc,path+move,sub)
            sub.remove((r,c))

        if grid[0][0]==1:
            maze(0,0,"",set())
        return res
