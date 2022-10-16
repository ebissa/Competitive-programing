class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        chars,countP = {},{}
        result=[]
        for char in p:
            countP[char]=1+ countP.get(char,0)
        for r in range(len(s)):
            if s[r]in countP:
                chars[s[r]]=1+ chars.get(s[r],0)
            if chars==countP:
                result.append(l)
            while r-l==len(p)-1:
                if s[l]in countP:
                    chars[s[l]]-=1
                l+=1
                

        return result
