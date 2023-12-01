class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        total, m, n = 0, len(mat), len(mat[0])
        for i in range(m):
            stack = [-1]
            mat[i].append(0)
            mat[i].append(-1)
            for j in range(n + 1):
                if i > 0 and mat[i][j] > 0: 
                    mat[i][j] += mat[i - 1][j]
                while stack and mat[i][stack[-1]] >= mat[i][j]:
                    height = mat[i][stack.pop()] - max(mat[i][j], mat[i][stack[-1]])
                    width = j - stack[-1] - 1
                    total += ((width * (width + 1)) // 2) * height
                stack.append(j)
        return total