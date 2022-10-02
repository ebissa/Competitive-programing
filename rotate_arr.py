class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums: return
        n = len(nums)
        k %= n
        
        j = 1
        while (j*k) % n:
            j+=1
        
        for i in range(n//j):
            temp = nums[i]
            for x in range(j, 1, -1):
                nums[(i+k*x)%n] = nums[i+k*(x-1)%n]
            nums[i+k] = temp
