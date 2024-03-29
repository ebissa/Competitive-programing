class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res=0
        values=set()
        res=0
        count=0
        l=0
        for r in range(len(nums)):
            if nums[r] not in values:
                values.add(nums[r])
                count+=nums[r]
            elif nums[r] in values:
                while nums[l]!=nums[r]:
                    values.remove(nums[l])
                    count-=nums[l]
                    l+=1
                l+=1
            res=max(res,count)

        return res
                
        