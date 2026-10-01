class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # length check
        if len(s1) > len(s2):
            return False

        # create frequency maps
        s1Count, s2Count = {}, {}

        #populate s1Count (target)
        for char in s1:
            s1Count[char] = s1Count.get(char, 0) + 1

        #start the sliding window (s2)
        left = 0
        for right in range(len(s2)):
            s2Count[s2[right]] = s2Count.get(s2[right], 0) + 1

            #check window size to s1
            if (right - left + 1) > len(s1):
                s2Count[s2[left]] -= 1

                # what happens when a char == 0?
                if (s2Count[s2[left]] == 0):
                    del s2Count[s2[left]]
                      #kicking a char = more left forward
                left += 1

            if s1Count == s2Count:
                return True

        return False

        