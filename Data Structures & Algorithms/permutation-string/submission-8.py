class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # length check

        if len(s1) > len(s2):
            return False

        # build 2 frequency maps
        s1Count, s2Count = {}, {}

        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1

        left = 0
        for right in range(len(s2)):
            s2Count[s2[right]] = s2Count.get(s2[right], 0) + 1

            # make sure window size is kept at length s1
            if (right - left + 1) > len(s1):
                s2Count[s2[left]] -= 1

                if s2Count[s2[left]] == 0:
                    del s2Count[s2[left]]

                left += 1

            if s1Count == s2Count:
                return True

        return False




        