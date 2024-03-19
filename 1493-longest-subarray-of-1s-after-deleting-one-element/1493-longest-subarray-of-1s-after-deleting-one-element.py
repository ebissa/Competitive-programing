class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        count=0
        max_size=0
        can_delete=True
        for r in range(len(nums)):
            while nums[r]!=1 and can_delete==False:
                if nums[l]==1:
                    count-=1
                elif nums[l]!=1:
                    can_delete=True
                l+=1
            if nums[r]==1:
                count+=1
                max_size=max(max_size,count)
            elif  nums[r]!=1 and can_delete==True:
                can_delete=False
                continue
            
        return max_size - 1 if can_delete else max_size



            

        