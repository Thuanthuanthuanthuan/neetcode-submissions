class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # precheck
        if len(s1) > len(s2):
            return False

        #build freq maps
        s1Count, s2Count = {}, {}

        #fill s1Count
        for char in s1:
            s1Count[char] = s1Count.get(char, 0) + 1

        # starts the sliding window w s2
        l = 0
        for r in range(len(s2)):
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1

            #check if length condition is met 
            if (r - l + 1) > len(s1):
                s2Count[s2[l]] -= 1

                # when s[l] == 0 ?
                if (s2Count[s2[l]] == 0):
                    del s2Count[s2[l]]

                l += 1

            # check to see if the two maps match
            if s1Count == s2Count:
                return True

        return False
        