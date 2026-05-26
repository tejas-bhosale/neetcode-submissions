from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])

        q = deque()
        fresh = 0 
        def addroom(r,c):
            nonlocal fresh
            if r<0 or r>=row or c <0 or c>=col or grid[r][c] == 0 or grid[r][c] ==2:
                return
            q.append([r,c])
            grid[r][c] = 2
            fresh-=1

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r,c])
                    
                elif grid[r][c] == 1:
                    fresh+=1
        
        time = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)
            if q:
                time += 1
        
        return time if fresh ==0 else -1


        