import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]  
        heapq.heapify(max_heap)  
        while len(max_heap)>1:
            largest = heapq.heappop(max_heap)
            smallest = heapq.heappop(max_heap)
            if largest != smallest:
                heapq.heappush(max_heap, -(abs(largest) - abs(smallest)))
        if len(max_heap):
            return -(max_heap[0])
        else:
            return 0


        