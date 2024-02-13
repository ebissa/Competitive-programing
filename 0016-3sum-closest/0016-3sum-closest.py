class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res= sum(nums[:3])
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                sums=nums[i]+nums[l]+nums[r]
                diff=abs(sums-target)
                if diff<abs(res-target):
                    res=sums
                if sums<target:
                    l+=1
                else:
                    r-=1

        return res
                