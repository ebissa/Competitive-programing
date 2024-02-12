class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        double=[]
        for i in range(len(nums)):
            double.append([nums[i],i])
        sortedNums=sorted(double,key=lambda x:x[0])
        
        l=0
        r=len(nums)-1
        while l<r:
            if sortedNums[l][0]+sortedNums[r][0]<target:
                l+=1
            elif sortedNums[l][0]+sortedNums[r][0]>target:
                r-=1
            elif sortedNums[l][0]+sortedNums[r][0]==target:
                return [sortedNums[l][1],sortedNums[r][1]]

        