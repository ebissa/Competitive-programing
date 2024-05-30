class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subArray=0
            curr=0
            for n in nums:
                curr+=n
                if curr>largest:
                    subArray+=1
                    curr=n
            subArray+=1
            return subArray<=k
        l,r=max(nums),sum(nums)
        res=r
        while l<=r:
            mid=l+(r-l)//2
            if canSplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
            
        