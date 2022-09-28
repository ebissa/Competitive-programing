class Solution:
    def sortSentence(self, s: str) -> str:
        sentence=s.split(' ')
        words=[None]*len(sentence)
        for word in sentence:
            words[int(word[-1])-1]=word[:-1]
        return ' '.join(words)
        
