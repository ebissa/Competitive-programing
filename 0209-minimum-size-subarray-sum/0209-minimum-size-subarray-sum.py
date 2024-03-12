class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        l=0
        res=len(nums)
        current=0
        for r in range(len(nums)):
            current+=nums[r]
            while current>=target:
                res=min(res,r-l+1)
                current-=nums[l]
                l+=1
        return res
    
                