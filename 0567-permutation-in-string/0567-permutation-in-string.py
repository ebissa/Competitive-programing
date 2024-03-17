from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length=len(s1)
        countS1=Counter(s1)
        l=0
        for r in range(len(s2)):
            while (r-l+1)==s1_length:
                if Counter(s2[l:r+1])==countS1:
                    return True
                l+=1
        return False

        
        