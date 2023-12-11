class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r=len(numbers)-1
        l=0
        res=[]
        for l in range(len(numbers)):
            while (numbers[l]+numbers[r])>target and r>l:
                r-=1
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            

        