class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res,lmax,rmax=0,0,0
        if r<2:
            return res
        while l<r:
            if height[l]<height[r]:
                lmax=max(lmax,height[l])
                res+=lmax-height[l]
                l+=1
            else:
                rmax=max(rmax,height[r])
                res+=rmax-height[r]
                r-=1
        return res


    
            
            