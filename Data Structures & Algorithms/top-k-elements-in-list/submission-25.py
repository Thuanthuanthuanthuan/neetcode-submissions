class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for i in range(len(nums) + 1)]
        count = {}

        #get count
        for num in nums:
            count[num] = count.get(num, 0) + 1

        #fill buckets
        for num, cnt in count.items():
            buckets[cnt].append(num)

        
        res = []
        #retrieve from buckets
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)

            if len(res) == k:
                return res

        