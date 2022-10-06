class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        total = 0
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in prefixSum:
                count += prefixSum[total-k]
            if total in prefixSum:
                prefixSum[total] += 1
            else:
                prefixSum[total] = 1
        return count
