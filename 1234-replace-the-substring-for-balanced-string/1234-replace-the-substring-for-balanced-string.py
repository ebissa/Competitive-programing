class Solution:
    def balancedString(self, s: str) -> int:
        l=len(s)
        d={}
        a=0
        for i in 'QWER':
            d[i]=max(s.count(i)-int(l/4),0)
        a=d['Q']+d['W']+d['E']+d['R']
        if a<=1:
            return a
        
        i=0
        ans=float('inf')
        for j in range(l):
            d[s[j]]-=1
            while d['Q']<=0 and d['W']<=0 and d['E']<=0 and d['R']<=0 and i<j:
                d[s[i]]+=1
                ans=min(ans,j-i+1)
                i+=1
        return ans
        
            
            