class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for c in s:                  # ✅ iterate over string
            countS[c] = countS.get(c, 0) + 1

        for c in t:                  # ✅ iterate over string
            countT[c] = countT.get(c, 0) + 1

        return countS == countT

