class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowls={"a","e","i","o","u"}
        count=0
        res=0
        l=0
        for r in range(len(s)):
            if s[r].lower() in vowls:
                count+=1
            if r-l+1==k:
                res=max(res,count)
                if s[l].lower() in vowls:
                    count-=1
                l+=1
        return res
                
            
                
            
        