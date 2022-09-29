class Solution:
    def mergeSort(self,arr,points):
        if len(arr) > 1:

            mid = len(arr)//2
            midp=len(arr)//2

            L = arr[:mid]
            LP=points[:midp]

            R = arr[mid:]
            RP=points[mid:]

            self.mergeSort(L,LP)

            self.mergeSort(R,RP)

            i = j = k = 0


            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    points[k]=LP[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    points[k]=RP[j]
                    j += 1
                k += 1

        
            while i < len(L):
                arr[k] = L[i]
                points[k]=LP[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                points[k]=RP[j]
                j += 1
                k += 1
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        for point in points:
            distance=((point[0])**2+(point[1])**2)**0.5
            distances.append(distance)
        self.mergeSort(distances,points)
        return points[:k]
        
