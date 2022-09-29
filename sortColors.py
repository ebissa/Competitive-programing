class Solution:
    def sortColors(self, nums: List[int]) -> None:
        temp=self.bubleSort(nums)
        nums=temp
    def bubleSort(self,customList):
        for i in range(len(customList)-1):
            for j in range(len(customList)-1-i):
                if customList[j]>customList[j+1]:
                    customList[j],customList[j+1]=customList[j+1],customList[j]
