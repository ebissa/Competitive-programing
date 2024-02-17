class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r=0,len(matrix[0])-1
        h,lo=0,len(matrix)-1
        step=0
        res=[]
        while l<=r and h<=lo:
            matcher=step%4
            if matcher==0:
                for i in range(l,r+1):
                    res.append(matrix[h][i])
                h+=1
            elif matcher==1:
                for i in range(h,lo+1):
                    res.append(matrix[i][r])
                r-=1
            elif matcher==2:
                for i in range(r,l-1,-1):
                    res.append(matrix[lo][i])
                lo-=1
            elif matcher==3:
                for i in range(lo,h-1,-1):
                    res.append(matrix[i][l])
                l+=1
            step+=1
        return res
                    
        