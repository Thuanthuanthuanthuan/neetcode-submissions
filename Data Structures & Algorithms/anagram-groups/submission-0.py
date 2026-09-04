class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = defaultdict(list) #hashmap for keys, initalizes them as empty list if key is absent

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            group[tuple(count)].append(s)

        return list(group.values())


        