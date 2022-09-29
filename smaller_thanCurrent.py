class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[]
        for num in nums:
            count=0
            for i in range(len(nums)):
                if nums[i]<num:
                    count+=1
            arr.append(count)
                
        return arr
