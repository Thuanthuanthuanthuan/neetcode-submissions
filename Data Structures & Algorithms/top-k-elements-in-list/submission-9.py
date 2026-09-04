class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n,0) + 1

        for n, c in count.items():
            buckets[c].append(n)

        solution = []
        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]:
                solution.append(n)

                if len(solution) == k:
                    return solution 