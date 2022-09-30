class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(idx):
            arr[:idx+1] = arr[:idx+1][::-1]
            
        ans, largest = [], len(arr)
        while(largest > 0):
            if arr[largest - 1] == largest:    
                largest -= 1
                continue
            for i in range(largest):
                if arr[i] == largest:
                    flip(i)
                    ans.append(i + 1)
                    flip(largest - 1)
                    ans.append(largest)
                    largest -= 1
        return ans
