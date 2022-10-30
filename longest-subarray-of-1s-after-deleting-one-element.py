class Solution(object):
    def longestSubarray(self, nums):
        delnum=1
        maximum,l=0,0
        maximum,l=0,0
        for i in range(len(nums)):
            delnum-=(1-nums[i])
            if delnum<0:
                delnum+=1-nums[l]
                l+=1
            maximum=max(maximum,(i-l))
        return maximum
