from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,col = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        def addroom(r,c):
            if r<0 or r>=rows or c <0 or c>=col or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            queue.append([r,c])

        for r in range(rows):
            for c in range(col):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    queue.append([r,c])
        
        distance = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = distance
                addroom(r+1,c)
                addroom(r-1,c)
                addroom(r,c+1)
                addroom(r,c-1)
            distance+=1

        