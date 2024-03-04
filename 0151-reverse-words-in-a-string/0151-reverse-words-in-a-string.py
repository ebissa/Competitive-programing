class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        word=''
        for char in s:
            if char!=' ':
                word+=char
            else:
                if word and word!=" ":
                    res.append(word)
                word=''
        if word and word!=" ":
            res.append(word)
        l=0
        r=len(res)-1
        while l<r:
            res[l],res[r]=res[r],res[l]
            l+=1
            r-=1
        return ' '.join(res)
            
        

        