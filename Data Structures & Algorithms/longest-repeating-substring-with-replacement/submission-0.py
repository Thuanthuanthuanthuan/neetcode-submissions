class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0

        l = 0
        max_freq = 0

        for r in range(len(s)):
            # 1. scan using r and get counts
            count[s[r]] = count.get(s[r], 0) + 1

            #2. get max freq 
            max_freq = max(max_freq, count[s[r]])

            #3, check to see if we have enough k replacements
            # if not, shrink from left most
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            # update window size
            res = max(res, r-l + 1)

        return res
        