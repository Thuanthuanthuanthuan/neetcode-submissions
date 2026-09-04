class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            seen[n] = seen.get(n,0) + 1
        
        for n, c in seen.items():
            buckets[c].append(n)

        
        res = []
        for i in range(len(buckets) - 1,0, -1):
            for n in buckets[i]:
                res.append(n)

                if len(res) == k:
                    return res

        