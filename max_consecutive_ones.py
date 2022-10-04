class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maximum,l=0,0
        for i in range(len(nums)):
            k-=(1-nums[i])
            if k<0:
                k+=1-nums[l]
                l+=1
            maximum=max(maximum,(i-l+1))
        return maximum
