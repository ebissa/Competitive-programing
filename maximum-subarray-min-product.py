class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack=[]
        res=0
        prefix=[0]
        for n in nums:
            prefix.append(prefix[-1]+n)
        for i,num in enumerate(nums):
            new_start=i
            while stack and stack[-1][1]>num:
                start,val=stack.pop()
                total=prefix[i]-prefix[start]
                res=max(res,val*total)
                new_start=start
            stack.append((new_start,num))
        for start,val in stack:
            total=prefix[len(nums)]-prefix[start]
            res=max(res,val*total)
        return res%(10**9+7)
