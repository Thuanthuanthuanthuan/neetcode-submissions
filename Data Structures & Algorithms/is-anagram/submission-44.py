class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # length check
        # freq list size 26, get count of each s and one incrments , the other  qdecrments, if val of freq == 0, its true, otherwise false


        if len(s) != len(t):
            return False

        tracker = [0] * 26

        for i in range(len(s)):
            tracker[ord(s[i]) - ord('a')] += 1
            tracker[ord(t[i]) - ord('a')] -= 1

        for val in tracker:
            if val != 0:
                return False

        return True




        