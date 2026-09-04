class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = defaultdict(list)

        for s in strs:
            uniqueCode = [0] * 26
            for c in s:
                uniqueCode[ord(c) - ord('a')] += 1

            count[tuple(uniqueCode)].append(s)

        return list(count.values())