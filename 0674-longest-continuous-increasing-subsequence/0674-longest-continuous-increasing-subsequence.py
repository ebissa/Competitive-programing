class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l=0
        count=1
        res=1
        for r in range(1,len(nums)):
            if nums[r]>nums[r-1]:
                count+=1
            else:
                l=r
                count=1
            res=max(res,count)
        return res
            
        