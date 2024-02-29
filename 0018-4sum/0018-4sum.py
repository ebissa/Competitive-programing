class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()

        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                left, right = b + 1, n - 1
                while left < right:
                    curr_sum = nums[a] + nums[b] + nums[left] + nums[right]
                    if curr_sum == target:
                        ans.add((nums[a], nums[b], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1

        return list(ans)
            
