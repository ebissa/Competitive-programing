class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        t_count = Counter(t)
        required = len(t_count)

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in t_count and window_counts[character] == t_count[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in t_count and window_counts[character] < t_count[character]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

            
            