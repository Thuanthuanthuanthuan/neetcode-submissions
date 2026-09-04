class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            num_count[n] = num_count.get(n,0) + 1

        for n, c in num_count.items():
            buckets[c].append(n)

        solution_list = []

        for i in range(len(buckets) - 1,0,-1):
            for n in buckets[i]:
                solution_list.append(n)
                if len(solution_list) == k:
                    return solution_list


        