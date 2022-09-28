class Solution: 
    class Solution: 
    def select(self, arr, i):
        return arr[i]
    
    def selectionSort(self, arr,n):
        for i in range (n):
            min_index=i
            for j in range(i+1,n):
                if arr[min_index]>arr[j]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
        
