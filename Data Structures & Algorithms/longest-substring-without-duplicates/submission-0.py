class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        string_set = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in string_set:
                string_set.remove(s[l])
                l += 1

            string_set.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length
            

        



        