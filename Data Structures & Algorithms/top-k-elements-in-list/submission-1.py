import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            d[num] = 1+d.get(num,0)
        
        heap=[]
        heapq.heapify(heap)
        for num in d.keys():
            heapq.heappush(heap, (d[num],num))
            if len(heap) >k:
                heapq.heappop(heap)
        
        res=[]
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res

        