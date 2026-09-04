class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        tracker = {}
        buckets = [[] for i in range(len(nums) + 1)]

        #counting

        for num in nums:
            tracker[num] = tracker.get(num,0) + 1

        # populate

        for num, cnt in tracker.items():
            buckets[cnt].append(num)

        
        # result list
        res = []

        # go to last bucketks
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                
                if len(res) == k:
                    return res
        