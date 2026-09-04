class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # defaultdict to make as list 
        # key: group all anagrams tgt that fits
        # turn key into tuple and use that to append any s fitting into the map
        #return as a list, only return the value

        tracker = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1

            tracker[tuple(key)].append(s)

        return list(tracker.values())
        