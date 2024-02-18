class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=1
        canAdd=True
        while r <n:
            if nums[l]==nums[r]:
                if canAdd:
                    l+=1
                    nums[l]=nums[r]
                    canAdd=False
            elif nums[l]!=nums[r]:
                l+=1
                canAdd=True
                nums[l]=nums[r]
            r+=1
        return l+1

