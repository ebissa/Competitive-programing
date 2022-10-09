class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j=0
        output=0
        max_delete=1
        for i in range(len(nums)):
            if nums[i]==0:
                max_delete-=1
            while max_delete<0:
                if nums[j]==0:
                    max_delete+=1
                j+=1
            output=max(output,i-j)
        return output
