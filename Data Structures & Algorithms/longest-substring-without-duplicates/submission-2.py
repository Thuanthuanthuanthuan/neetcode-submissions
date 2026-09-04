class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_length = 0
        string_tracker = set()
        l = 0

        for r in range(len(s)):
            while s[r] in string_tracker:
                string_tracker.remove(s[l])
                l += 1
            string_tracker.add(s[r])

            longest_length = max(longest_length, r - l + 1)

        return longest_length

        