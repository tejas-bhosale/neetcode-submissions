class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        return self.traversal(grid,0,0,visit)

        
    
    def traversal(self,grid,r,c,visit):
        row, col = len(grid),len(grid[0])
        if (min(r, c) < 0 or r == row or c == col or (r, c) in visit or grid[r][c] == 1):
            return 0
        if r == row-1 and c==col-1:
            return 1
        visit.add((r,c))
        count = 0 
        count+=self.traversal(grid,r+1,c,visit)
        count+=self.traversal(grid,r-1,c,visit)
        count+=self.traversal(grid,r,c+1,visit)
        count+=self.traversal(grid,r,c-1,visit)
        visit.remove((r,c))
        return count
        