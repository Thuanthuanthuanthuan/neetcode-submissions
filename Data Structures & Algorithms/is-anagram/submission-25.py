class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #precheck: r they the same length

        if len(s) != len(t):
            return False

        # its only lowercase letters, we can use a frequency list
        count = [0] * 26
        # if anagram, cancelling each other out
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for value in count:
            if value != 0:
                return False
        return True


        

        
        

        