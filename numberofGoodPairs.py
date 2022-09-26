import array as ar
class Solution:
    def numIdenticalPairs(self, nums):
        output=0
        for i in range(len(nums)):
            for j in  range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    output+=1
        return output
