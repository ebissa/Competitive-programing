class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                start=l
                end=r
                while nums[start]!=target:
                    start+=1
                while nums[end]!=target:
                    end-=1
                return [start,end] 
        return [-1,-1]
                
        