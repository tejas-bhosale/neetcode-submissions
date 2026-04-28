 
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        q = deque()
        visit=set()
        visit.add((0,0))
        q.append((0,0))
        length=0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r == row-1 and c == col-1:
                    return length
                
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    if min(dr+r,dc+c)<0 or r+dr ==row or c+dc == col or (dr+r,dc+c) in visit or grid[dr+r][dc+c] == 1:
                        continue
                    q.append((dr+r,dc+c))
                    visit.add((dr+r,dc+c))
            length+=1
        return -1



        