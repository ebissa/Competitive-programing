   class Solution(object):
    def lastStoneWeight(self, stones):
        heap = list()
        
        for stone in stones:
            heapq.heappush(heap, (-stone, stone))
        
        while len(heap) > 1:
            y = heapq.heappop(heap)[1]
            x = heapq.heappop(heap)[1]
            if x != y:
                heapq.heappush(heap, (-(y-x), y-x))
        
        return heap[0][1] if heap else 0
       
