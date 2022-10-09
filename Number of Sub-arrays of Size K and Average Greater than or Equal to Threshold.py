class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        j=0
        sums=sum(arr[j:k])
        if k!=0:
            for i in range(k-1,len(arr)):
                if j+k-1==i:
                    average=(sums)/k
                    j+=1
                    if average>=threshold:
                        count+=1
                if i!=len(arr)-1:
                    sums+=arr[i+1]-arr[j-1]

        return count
