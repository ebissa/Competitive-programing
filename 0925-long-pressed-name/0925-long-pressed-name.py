class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l=0
        r=0
        while l<=len(name) and r<len(typed):
            if l<len(name) and typed[r]==name[l]:
                l+=1
                r+=1
            elif typed[r]==name[l-1] and l!=0:
                r+=1
            else:
                return False
        return r==len(typed) and l==len(name)
            
