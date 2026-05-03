class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row,col = len(grid),len(grid[0])
        visited = set()

        def dfs(r,c):
            if ((r,c) in visited or r>=row or c>= col or r<0 or c<0 or grid[r][c] == 0):
                return 0
            visited.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))


        area = 0
        for r in range(row):
            for c in range(col):
                area  = max(area,dfs(r,c))
        return area