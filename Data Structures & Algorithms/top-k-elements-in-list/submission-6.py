class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        bucket_freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n,0) + 1

        for n, c in count.items():
            bucket_freq[c].append(n)

        solution = []
        for i in range(len(bucket_freq) - 1, 0, -1):
            for n in bucket_freq[i]:
                solution.append(n)
                if len(solution) == k:
                    return solution
        