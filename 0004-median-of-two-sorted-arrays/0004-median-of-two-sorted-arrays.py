class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1+nums2
        arr.sort()
        l=0
        r=len(arr)-1
        m=(l+r)//2
        if (r-l+1)%2==0:
            median=(arr[m]+arr[m+1])/2
        else:
            median=arr[m]
        return median

        