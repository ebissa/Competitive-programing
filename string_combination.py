class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        times = 1
        
        while r < len(chars):
            if r + 1 != len(chars) and chars[r] == chars[r+1]:
                r += 1
                times += 1 
            else:
                chars[l] = chars[r]
                l += 1
                if times != 1:
                    for c in str(times):
                        chars[l] = c
                        l += 1
                r += 1
                times = 1
        
        return l
