class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        score=0
        i=0
        j=len(tokens)-1
        while i<=j:
            if tokens[i]<=power:
                score+=1
                power-=tokens[i]
                i+=1
            else:
                if j-i>0 and score>0:
                    score-=1
                    power+=tokens[j]
                    j-=1
                else:
                     break
    
        return score
        
