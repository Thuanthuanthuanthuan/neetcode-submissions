class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1

        for num, cnt in count.items():
            bucket[cnt].append(num)

        solution = []
        for i in range(len(bucket) -1,0,-1):
            for num in bucket[i]:
                solution.append(num)
                
                if len(solution) == k:
                    return solution