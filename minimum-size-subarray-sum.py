class Solution(object):
    def minSubArrayLen(self, target, nums):
        PreSum = [0]
        left = 0
        res = float('inf')
        for right in range(len(nums)):
            PreSum += [(PreSum[-1] + nums[right])]
            while PreSum[right+1] - PreSum[left] >= target:
                res = min(res, right - left + 1)
                left += 1
        return 0 if res == float('inf') else res
            
