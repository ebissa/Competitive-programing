class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        output=0
        j=0
        vowels={'a':'vowel','e':'vowel','i':'vowel','o':'vowel','u':'vowel',}
        for i in range(len(s)):
            if s[i]in vowels:
                count+=1
            if i==j+k-1:
                output=max(output,count)
                if s[j]in vowels:
                    count-=1
                j+=1
        return output
