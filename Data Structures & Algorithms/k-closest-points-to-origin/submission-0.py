import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for x,y in points:
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            res.append([dist,x,y])
        
        heapq.heapify(res)
        ans = []
        while k>0:
            dist, x, y = heapq.heappop(res)
            ans.append([x, y])
            k -= 1
        return ans
        



        