class Solution(object):
    def findKthLargest(self, nums, k):
        arr = []
        for i in nums:
            if(len(arr)>=k):
                heapq.heappushpop(arr, i)
            else:
                heapq.heappush(arr,i)
        return heapq.heappop(arr)
