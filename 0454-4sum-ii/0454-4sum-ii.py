class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        result = 0
        sumMap1 = {}  
        sumMap2 = {}  

        for i in range(n):
            for j in range(n):
                sum1 = nums1[i] + nums2[j]
                sum2 = nums3[i] + nums4[j]
                sumMap1[sum1] = sumMap1.get(sum1, 0) + 1
                sumMap2[sum2] = sumMap2.get(sum2, 0) + 1

        for num1, count1 in sumMap1.items():
            complement = -1 * num1
            if complement in sumMap2:
                result += count1 * sumMap2[complement]

        return result