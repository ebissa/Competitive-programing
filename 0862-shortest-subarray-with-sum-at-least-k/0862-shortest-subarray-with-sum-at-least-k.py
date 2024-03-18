class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        min_length = float('inf')
        dq = deque()
        for i in range(len(prefix_sum)):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        return min_length if min_length != float('inf') else -1