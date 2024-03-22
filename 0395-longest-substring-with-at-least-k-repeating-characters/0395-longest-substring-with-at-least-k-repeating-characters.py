class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_length = 0
        for t in range(1, len(set(s)) + 1):
            start = 0
            freq = [0] * 26
            unique, at_least_k = 0, 0
            for end in range(len(s)):
                if freq[ord(s[end]) - ord('a')] == 0:
                    unique += 1
                freq[ord(s[end]) - ord('a')] += 1
                if freq[ord(s[end]) - ord('a')] == k:
                    at_least_k += 1
                while unique > t:
                    if freq[ord(s[start]) - ord('a')] == k:
                        at_least_k -= 1
                    freq[ord(s[start]) - ord('a')] -= 1
                    if freq[ord(s[start]) - ord('a')] == 0:
                        unique -= 1
                    start += 1
                if unique == at_least_k:
                    max_length = max(max_length, end - start + 1)
        return max_length
                
            
        