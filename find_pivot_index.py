class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum=[nums[0]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[i-1])
        for j in range(1,len(prefix_sum)):
            if  (j-1 ==0 and prefix_sum[-1]-prefix_sum[j-1]==0): 
                return 0
        
            elif prefix_sum[-1]-prefix_sum[j]==prefix_sum[j-1]:
                return j
        else:
            if (len(nums)==1 and nums[0]==0):
                return 0
            else:
                return -1

