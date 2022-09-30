class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        temp=[]
        output=[None]*len(l)
        for i in range(len(l)):
            for j in range(l[i],r[i]+1):
                temp.append(nums[j])
            temp=sorted(temp)
            for k in range(len(temp)-2): 
                if len(temp)>2 and temp[k+1]-temp[k]==temp[k+2]-temp[k+1]:
                    output[i]=True
                else:
                    output[i]=False
                    break
            if len(temp)==2:
                    output[i]=True
        
            temp=[]
                        
                
        return output
