class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
    
        stops = 0
        curr = startFuel
        
        for location, fuel in stations:
            while curr < location:
                if not pq:
                    return -1
                
                curr += -heapq.heappop(pq)
                
                stops += 1
            
            heapq.heappush(pq, -fuel)
        
        while curr < target:
            if not pq:
                return -1
            
            curr += -heapq.heappop(pq)
            
            stops += 1
        
        return stops