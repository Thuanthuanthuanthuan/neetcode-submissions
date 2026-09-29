class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # ana = same char + num of char
        # precheck length if len(s) is same as len(t)
        # since fixed sized, use a fixed array of 26 placeholders
        #convert char -> index n increment counts
        # if ana, then it balances out (+, -)
        #check for result

        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True

        