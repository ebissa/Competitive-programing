class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        list=[]
        i=0
        while i <(len(nums)/2):
                pair_sum=nums[i]+nums[-(i+1)]
                list.append(pair_sum)
                i+=1
        return max(list)
                
