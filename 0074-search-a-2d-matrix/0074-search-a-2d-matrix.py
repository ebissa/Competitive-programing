class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u=0
        d=len(matrix)-1
        while u<=d:
            half=(d+u)//2
            l=0
            r=len(matrix[half])-1
            if matrix[half][l]<=target<=matrix[half][r]:
                while l<=r:
                    m=(l+r)//2
                    if matrix[half][m]>target:
                        r=m-1
                    elif matrix[half][m]<target:
                        l=m+1
                    else:
                        return True
        
            if matrix[half][r]<target:
                u=half+1
            else:
                d=half-1
        return False
