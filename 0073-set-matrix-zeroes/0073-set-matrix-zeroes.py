class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        jset=set()
        iset=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    jset.add(j)
                    iset.add(i)
        for i in iset:
            matrix[i]=[0]*len(matrix[i])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j in jset:
                    matrix[i][j]=0