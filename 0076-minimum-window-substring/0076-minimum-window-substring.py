class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        countS = {}
        min_substring = [0, len(s)]
        l = 0
        matched = 0

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] = countS.get(s[r], 0) + 1
                if countS[s[r]] == countT[s[r]]:
                    matched += 1

            while matched == len(countT):
                if min_substring[1] - min_substring[0] > r - l:
                    min_substring = [l, r]

                if s[l] in countS:
                    countS[s[l]] -= 1
                    if countS[s[l]] < countT[s[l]]:
                        matched -= 1
                l += 1

        if min_substring[1] == len(s):
            return ""

        return s[min_substring[0]: min_substring[1] + 1]
                



