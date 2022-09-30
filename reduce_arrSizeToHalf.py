class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr=sorted(arr)
        count=[0]*(arr[-1]+1)
        for num in arr:
            count[num]+=1
        minimum_sets=0
        count=sorted(count)[::-1]
        for i in range(len(count)):
            if count[i]>=len(arr)/2:
                minimum_sets=1
                break
            elif count[i]<len(arr)/2:
                j=i+1
                while i< j < (len(count)):
                    if count[i]+count[j]>=len(arr)/2:
                        minimum_sets=j+1
                        j=len(count)
                    else:
                        count[i]+=count[j]
                        j+=1
                break
            else: 
                continue
        return minimum_sets
