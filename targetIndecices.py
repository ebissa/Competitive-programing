 def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indexes=[]
        for i in range(len(nums)):
            if nums[i]==target:
                indexes.append(i)
        return indexes
